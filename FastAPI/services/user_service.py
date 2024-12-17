def add_user(user_Password, userName, user_Fierstname, user_Lastname, user_Email, db):
    # i need to hash the password here, but cant get the passlib library to work...
    cursor = db.cursor()
    cursor.execute(
        """
        INSERT INTO user (user_Password, userName, user_FierstName, user_Lastname, user_Email)
        VALUES (?, ?, ?, ?, ?)
    """,
        (user_Password, userName, user_Fierstname, user_Lastname, user_Email),
    )
    db.commit()

    # Print statement to show the added user details
    print(
        f"Added user: Password={user_Password}, Name={userName},Name={user_Fierstname},Name={user_Lastname}, Email={user_Email}"
    )


def delete_user(id_User, db):
    cursor = db.cursor()
    cursor.execute("DELETE FROM user WHERE id_User = ?", (id_User,))
    db.commit()
    # Print statement to show the deleted user ID
    print(f"Deleted user with ID: {id_User}")


# def login_user(password,email):
