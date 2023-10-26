import mysql.connector
from decouple import config


class MySQLDatabase:
    def __init__(self):
        self.host = config('DB_HOST')
        self.user = config('DB_USER')
        self.password = config('DB_PASSWORD')
        self.database = config('DB_NAME')
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("MySQL connection is open.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def disconnect(self):
        if self.conn and self.conn.is_connected():
            self.conn.close()
            print("MySQL connection is closed.")

    def execute_query(self, query, data=None):
        """function will execute query and return the result"""
        if not self.conn or not self.conn.is_connected():
            print("Not connected to the database. Call connect() method first.")
            return
        cursor = self.conn.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        self.conn.commit()
        cursor.close()
        if not self.conn or not self.conn.is_connected():
            print("Not connected to the database. Call connect() method first.")
            return

        cursor = self.conn.cursor()
        if data:
            cursor.execute(query, data)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result

    def create_table_if_not_exists(self):
        """function will create new table is it doesn't exist"""
        create_table_query = """
            CREATE TABLE IF NOT EXISTS workplace_wellness_member_intake_form (
              id INT NOT NULL AUTO_INCREMENT,
              event_id VARCHAR(255) NOT NULL,
              form_id VARCHAR(255) NOT NULL,
              landed_at DATETIME NOT NULL,
              submitted_at DATETIME NOT NULL,
              first_name VARCHAR(255) NOT NULL,
              last_name VARCHAR(255) NOT NULL,
              company_name VARCHAR(255) NOT NULL,
              company_tenure INT NOT NULL,
              job_title VARCHAR(255) NOT NULL,
              location VARCHAR(255) NOT NULL,
              email VARCHAR(255) NOT NULL,
              phone_number VARCHAR(255) NOT NULL,
              sex VARCHAR(255) NOT NULL,
              pregnant BOOLEAN NOT NULL,
              perimenopausal BOOLEAN NOT NULL,
              postmenopausal BOOLEAN NOT NULL,
              age INT NOT NULL,
              height INT NOT NULL,
              weight INT NOT NULL,
              bmi FLOAT NOT NULL,
              lose_weight BOOLEAN NOT NULL,
              weight_loss_goal FLOAT NOT NULL,
              improve_body_composition BOOLEAN NOT NULL,
              energy_level VARCHAR(255) NOT NULL,
              stress_level VARCHAR(255) NOT NULL,
              sleep_duration FLOAT NOT NULL,
              go_chemical_free BOOLEAN NOT NULL,
              drink_caffeine BOOLEAN NOT NULL,
              cups_of_caffeine_per_day VARCHAR(255) NOT NULL,
              willing_to_be_caffeine_free BOOLEAN NOT NULL,
              willing_to_change_to_decaf BOOLEAN NOT NULL,
              alcohol_nights_per_week VARCHAR(255) NOT NULL,
              alcohol_free_nights_per_week VARCHAR(255) NOT NULL,
              cups_of_water_per_day VARCHAR(255) NOT NULL,
              avoid_processed_foods BOOLEAN NOT NULL,
              interested_in_nutrition_plan BOOLEAN NOT NULL,
              can_follow_weekly_meal_plans BOOLEAN NOT NULL,
              can_carry_out_food_preparation BOOLEAN NOT NULL,
              diet_type VARCHAR(255) NOT NULL,
              willing_to_eat VARCHAR(255) NOT NULL,
              meals_per_day VARCHAR(255) NOT NULL,
              daily_meals_include VARCHAR(255) NOT NULL,
              food_intolerances_allergies VARCHAR(255) NOT NULL,
              foods_you_crave VARCHAR(255) NOT NULL,
              drink_sugary_drinks VARCHAR(255) NOT NULL,
              interested_in_fitness_plan BOOLEAN NOT NULL,
              fitness_plan_type VARCHAR(255) NOT NULL,
              restorative_exercises VARCHAR(255) NOT NULL,
              challenging_exercises VARCHAR(255) NOT NULL,
              exercises_willing_to_do VARCHAR(255) NOT NULL,
              currently_exercising VARCHAR(255) NOT NULL,
              exercise_schedule VARCHAR(255) NOT NULL,
              exercise_time_per_day VARCHAR(255) NOT NULL,
              training_location VARCHAR(255) NOT NULL,
              has_personal_trainer BOOLEAN NOT NULL,
              personal_trainer_frequency VARCHAR(255) NOT NULL,
              regular_yoga_practice BOOLEAN NOT NULL,
              flexibility_rating INT NOT NULL,
              increase_flexibility BOOLEAN NOT NULL,
              strength_rating INT NOT NULL,
              increase_strength BOOLEAN NOT NULL,
              fitness_rating INT NOT NULL,
              increase_fitness VARCHAR(30) NOT NULL,
              physical_injuries BOOLEAN NOT NULL,
              injury_details VARCHAR(30) NOT NULL,
              mindfulness_stress_management_plan BOOLEAN NOT NULL,
              bedtime VARCHAR(60) NOT NULL,
              fall_asleep_easily BOOLEAN NOT NULL,
              wake_up_during_night BOOLEAN NOT NULL,
              difficult_to_get_back_to_sleep BOOLEAN NOT NULL,
              average_sleep_hours VARCHAR(60) NOT NULL,
              wake_up_time VARCHAR(255) NOT NULL,
              wake_up_feeling_rested BOOLEAN NOT NULL,
              morning_energy_rating INT NOT NULL,
              challenging_to_unwind_after_work BOOLEAN NOT NULL,
              unwind_methods VARCHAR(255) NOT NULL,
              mental_health_rating INT NOT NULL,
              incorporate_mindfulness BOOLEAN NOT NULL,
              incorporate_stress_management BOOLEAN NOT NULL,
              incorporate_stretches BOOLEAN NOT NULL,
              incorporate_meditation BOOLEAN NOT NULL,
              enjoy_walking_for_exercise BOOLEAN NOT NULL,
              walking_time_per_day VARCHAR(60) NOT NULL,
              wellbeing_changes VARCHAR(100) NOT NULL,
              smoking BOOLEAN NOT NULL,
              quit_smoking_desire VARCHAR(255) NOT NULL,
              taking_supplements BOOLEAN NOT NULL,
              supplement_details VARCHAR(255) NOT NULL,
              on_medication BOOLEAN NOT NULL,
              medication_details VARCHAR(255) NOT NULL,
              digestive_health_problems BOOLEAN NOT NULL,
              digestive_health_details VARCHAR(255) NOT NULL,
              diagnosed_health_concerns BOOLEAN NOT NULL,
              health_concern_details VARCHAR(255) NOT NULL,
              under_guidance_of_naturopath_dietician_nutritionist BOOLEAN NOT NULL,
              guidance_details VARCHAR(255) NOT NULL,
              questions_or_concerns VARCHAR(255) NOT NULL,
              is_sent BOOLEAN NOT NULL DEFAULT false,
              PRIMARY KEY (id)
            );
            """
        self.execute_query(create_table_query)

    def add_data(self, data):
        """function will add the data to database table"""
        if not data:
            return
        insert_query = """
        INSERT INTO workplace_wellness_member_intake_form
        (event_id, form_id, landed_at, submitted_at, first_name, last_name, company_name, company_tenure, job_title, location, email, phone_number, sex, pregnant, perimenopausal, postmenopausal, age, height, weight, bmi, lose_weight, weight_loss_goal, improve_body_composition, energy_level, stress_level, sleep_duration, go_chemical_free, drink_caffeine, cups_of_caffeine_per_day, willing_to_be_caffeine_free, willing_to_change_to_decaf, alcohol_nights_per_week, alcohol_free_nights_per_week, cups_of_water_per_day, avoid_processed_foods, interested_in_nutrition_plan, can_follow_weekly_meal_plans, can_carry_out_food_preparation, diet_type, willing_to_eat, meals_per_day, daily_meals_include, food_intolerances_allergies, foods_you_crave, drink_sugary_drinks, interested_in_fitness_plan, fitness_plan_type, restorative_exercises, challenging_exercises, exercises_willing_to_do, currently_exercising, exercise_schedule, exercise_time_per_day, training_location, has_personal_trainer, personal_trainer_frequency, regular_yoga_practice, flexibility_rating, increase_flexibility, strength_rating, increase_strength, fitness_rating, increase_fitness, physical_injuries, injury_details, mindfulness_stress_management_plan, bedtime, fall_asleep_easily, wake_up_during_night, difficult_to_get_back_to_sleep, average_sleep_hours, wake_up_time, wake_up_feeling_rested, morning_energy_rating, challenging_to_unwind_after_work, unwind_methods, mental_health_rating, incorporate_mindfulness, incorporate_stress_management, incorporate_stretches, incorporate_meditation, enjoy_walking_for_exercise, walking_time_per_day, wellbeing_changes, smoking, quit_smoking_desire, taking_supplements, supplement_details, on_medication, medication_details, digestive_health_problems, digestive_health_details, diagnosed_health_concerns, health_concern_details, under_guidance_of_naturopath_dietician_nutritionist, guidance_details, questions_or_concerns)
        VALUES
        (%(event_id)s, %(form_id)s, %(landed_at)s, %(submitted_at)s, %(first_name)s, %(last_name)s, %(company_name)s, %(company_tenure)s, %(job_title)s, %(location)s, %(email)s, %(phone_number)s, %(sex)s, %(pregnant)s, %(perimenopausal)s, %(postmenopausal)s, %(age)s, %(height)s, %(weight)s, %(bmi)s, %(lose_weight)s, %(weight_loss_goal)s, %(improve_body_composition)s, %(energy_level)s, %(stress_level)s, %(sleep_duration)s, %(go_chemical_free)s, %(drink_caffeine)s, %(cups_of_caffeine_per_day)s, %(willing_to_be_caffeine_free)s, %(willing_to_change_to_decaf)s, %(alcohol_nights_per_week)s, %(alcohol_free_nights_per_week)s, %(cups_of_water_per_day)s, %(avoid_processed_foods)s, %(interested_in_nutrition_plan)s, %(can_follow_weekly_meal_plans)s, %(can_carry_out_food_preparation)s, %(diet_type)s, %(willing_to_eat)s, %(meals_per_day)s, %(daily_meals_include)s, %(food_intolerances_allergies)s, %(foods_you_crave)s, %(drink_sugary_drinks)s, %(interested_in_fitness_plan)s, %(fitness_plan_type)s, %(restorative_exercises)s, %(challenging_exercises)s, %(exercises_willing_to_do)s, %(currently_exercising)s, %(exercise_schedule)s, %(exercise_time_per_day)s, %(training_location)s, %(has_personal_trainer)s, %(personal_trainer_frequency)s, %(regular_yoga_practice)s, %(flexibility_rating)s, %(increase_flexibility)s, %(strength_rating)s, %(increase_strength)s, %(fitness_rating)s, %(increase_fitness)s, %(physical_injuries)s, %(injury_details)s, %(mindfulness_stress_management_plan)s, %(bedtime)s, %(fall_asleep_easily)s, %(wake_up_during_night)s, %(difficult_to_get_back_to_sleep)s, %(average_sleep_hours)s, %(wake_up_time)s, %(wake_up_feeling_rested)s, %(morning_energy_rating)s, %(challenging_to_unwind_after_work)s, %(unwind_methods)s, %(mental_health_rating)s, %(incorporate_mindfulness)s, %(incorporate_stress_management)s, %(incorporate_stretches)s, %(incorporate_meditation)s, %(enjoy_walking_for_exercise)s, %(walking_time_per_day)s, %(wellbeing_changes)s, %(smoking)s, %(quit_smoking_desire)s, %(taking_supplements)s, %(supplement_details)s, %(on_medication)s, %(medication_details)s, %(digestive_health_problems)s, %(digestive_health_details)s, %(diagnosed_health_concerns)s, %(health_concern_details)s, %(under_guidance_of_naturopath_dietician_nutritionist)s, %(guidance_details)s, %(questions_or_concerns)s)
        """

        cursor = self.conn.cursor()
        cursor.execute(insert_query, data)
        self.conn.commit()  # Commit changes to the database

        cursor.close()


# Example usage
if __name__ == "__main__":
    db = MySQLDatabase()
    db.connect()
    db.create_table_if_not_exists()
    db.disconnect()
