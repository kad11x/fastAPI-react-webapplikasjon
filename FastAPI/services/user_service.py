def add_user(user_Password, user_Name, user_Email, db):
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO user (user_Password, user_Name, user_Email)
        VALUES (?, ?, ?)
    """,
        (user_Password, user_Name, user_Email),
    )
    db.commit()

    # Print statement to show the added user details
    print(f"Added user: Password={user_Password}, Name={user_Name}, Email={user_Email}")


# def login_user(password,email):
