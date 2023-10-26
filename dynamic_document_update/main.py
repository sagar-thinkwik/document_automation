import json

from database.database import MySQLDatabase
from docs_generator.update_doc_file import update_doc_file, convert_temp_file_to_proper_format
from dynamic_document_update.convertor.convertor import Convertor
from dynamic_document_update.convertor.table_field_mapper import table_filed_mapper, get_data


def add_data_to_database(file_data):
    """function read the data from json file and insert the data to database"""
    try:
        data = json.load(file_data)
        file.close()

        convertor = Convertor(data)
        convertor.set_question_and_answer()
        convertor.categorize_answers()
        question_and_answer = convertor.get_question_answer()

        # map data of question with database table fields
        final_output = table_filed_mapper(question_and_answer)
        db = MySQLDatabase()
        db.connect()
        db.add_data(final_output)
        db.disconnect()
    except Exception as e:
        print(e)
        print("Error in adding data to database")
        raise e


def get_doc_file():
    """function return those data which emails are pending to send"""
    try:
        db = MySQLDatabase()
        db.connect()

        # query = "SELECT * FROM workplace_wellness_member_intake_form"
        query = "SELECT * FROM workplace_wellness_member_intake_form WHERE is_sent = false"

        results = db.execute_query(query)
        files = []
        for result in results:
            output = get_data(result)
            temp_file = update_doc_file(output)
            files.append({"file_path": convert_temp_file_to_proper_format(temp_file, output),
                          "email": result[11],
                          "id": result[0]})
        db.disconnect()
        return files
    except Exception as e:
        print(e)
        print("Error in getting doc file")
        raise e


def update_is_sent(user_id: int):
    """function will get invoked once user mail is send to the user."""
    try:
        db = MySQLDatabase()
        db.connect()
        query = f"""UPDATE workplace_wellness_member_intake_form
                SET is_sent = true
                WHERE id = {user_id};"""
        db.execute_query(query)
        db.conn.commit()
    except Exception as e:
        print(e)
        print("Error in updating is_sent field")
        raise e


if __name__ == "__main__":
    file = open("sample_response.json")
    add_data_to_database(file)
