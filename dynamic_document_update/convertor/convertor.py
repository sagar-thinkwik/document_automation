import json


class Convertor:
    def __init__(self, data: dict):
        self.data = data
        self.number_type_data = []
        self.short_text_type_data = []
        self.email_type_data = []
        self.phone_type_data = []
        self.multiple_choice_type_data = []
        self.yes_no_type_data = []
        self.opinion_scale_type_data = []
        self.long_text_type_data = []
        self.dropdown_type_data = []
        self.question = None
        self.answer = None
        self.question_and_answer = {}

    def set_question_and_answer(self) -> None:
        """function set the question and its answer in different dictionaries"""
        self.question = self.data['form_response']['definition']['fields']
        self.answer = self.data['form_response']['answers']

    def categorize_answers(self) -> None:
        """function categories the answer based on its type"""
        for answer in self.answer:
            if answer['field']['type'] == 'number':
                self.number_type_data.append(answer)
            elif answer['field']['type'] == 'short_text':
                self.short_text_type_data.append(answer)
            elif answer['field']['type'] == 'email':
                self.email_type_data.append(answer)
            elif answer['field']['type'] == 'phone_number':
                self.phone_type_data.append(answer)
            elif answer['field']['type'] == 'multiple_choice':
                self.multiple_choice_type_data.append(answer)
            elif answer['field']['type'] == 'yes_no':
                self.yes_no_type_data.append(answer)
            elif answer['field']['type'] == 'opinion_scale':
                self.opinion_scale_type_data.append(answer)
            elif answer['field']['type'] == 'long_text':
                self.long_text_type_data.append(answer)
            elif answer['field']['type'] == 'dropdown':
                self.dropdown_type_data.append(answer)

    def get_question_answer(self):
        """this function create dictionary with its question and answer."""
        event_id = self.data["event_id"]
        form_response = self.data["form_response"]
        form_id = form_response["form_id"]
        landed_at = form_response["landed_at"]
        submitted_at = form_response["submitted_at"]
        self.question_and_answer.update({"event_id": event_id,
                                         "form_id": form_id,
                                         "landed_at": landed_at,
                                         "submitted_at": submitted_at})
        for question in self.question:
            id = question.get('id')
            type = question.get('type')
            title = question.get('title')
            answer = self.get_answer_from_question(question_id=id, question_type=type)
            self.question_and_answer[title] = answer

        return self.question_and_answer

    def get_answer_from_question(self, question_id, question_type):
        """function fetch and return the answer of given question"""
        if question_type == 'number':
            return self.fetch_answer(self.number_type_data, question_id, question_type)
        elif question_type == 'short_text':
            return self.fetch_answer(self.short_text_type_data, question_id, question_type)
        elif question_type == 'email':
            return self.fetch_answer(self.email_type_data, question_id, question_type)
        elif question_type == 'phone_number':
            return self.fetch_answer(self.phone_type_data, question_id, question_type)
        elif question_type == 'multiple_choice':
            return self.fetch_answer(self.multiple_choice_type_data, question_id, question_type)
        elif question_type == 'yes_no':
            return self.fetch_answer(self.yes_no_type_data, question_id, question_type)
        elif question_type == 'opinion_scale':
            return self.fetch_answer(self.opinion_scale_type_data, question_id, question_type)
        elif question_type == 'long_text':
            return self.fetch_answer(self.long_text_type_data, question_id, question_type)
        elif question_type == 'dropdown':
            return self.fetch_answer(self.dropdown_type_data, question_id, question_type)
        else:
            return None

    @staticmethod
    def fetch_answer(answers, id, question_type):
        """function return the answer of the given question"""
        try:
            for answer in answers:
                if id == answer['field']['id']:
                    if question_type == "short_text" or question_type == "long_text":
                        return answer['text']
                    elif question_type == "number" or question_type == "opinion_scale":
                        return answer['number']
                    elif question_type == "email":
                        return answer['email']
                    elif question_type == "phone_number":
                        return answer['phone_number']
                    elif question_type == "yes_no":
                        return answer['boolean']
                    elif question_type == "multiple_choice" or question_type == "dropdown":
                        if answer.get('choice'):
                            return answer['choice']['label']
                        else:
                            return answer['choices']['labels']
                    else:
                        pass
        except Exception as e:
            print(e)
