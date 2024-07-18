import sqlite3

DATABASE_NAME = "mydatabase.db"


def get_database_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_database_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id_User INTEGER PRIMARY KEY AUTOINCREMENT,
            user_Password TEXT,
            user_Name TEXT,
            user_Email TEXT
        )
    """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exercise (
            id_Exercise INTEGER PRIMARY KEY AUTOINCREMENT,
            exercise_Name TEXT,
            exercise_Info TEXT
        )
    """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS template (
            id_Template INTEGER PRIMARY KEY AUTOINCREMENT,
            template_name TEXT,
            user_idUser INTEGER,
            FOREIGN KEY(user_idUser) REFERENCES user(id_User)
        )
    """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS exercise_set (
            id_Set INTEGER PRIMARY KEY AUTOINCREMENT,
            set_Kg TEXT,
            set_Reps TEXT,
            Exercise_idExercise INTEGER,
            Template_idTemplate INTEGER,
            FOREIGN KEY(Exercise_idExercise) REFERENCES exercise(id_Exercise),
            FOREIGN KEY(Template_idTemplate) REFERENCES template(id_Template)
        )
    """
    )

    conn.commit()
    conn.close()
