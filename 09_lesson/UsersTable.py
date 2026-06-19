from sqlalchemy import create_engine, text


class UsersTable:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string)
        self.__scripts = {
            "select": text("SELECT * FROM users"),
            "insert": text("INSERT INTO users ("
                           "user_id, user_email, subject_id"") VALUES ("
                           "'435', 'dmitry.l@gmail.com', 1)"),
            "delete by id": text("DELETE FROM users WHERE user_id = :id"),
            "edit by id": text("UPDATE users SET user_email = :new_email "
                               "WHERE user_id = :id"),
            "get user by id": text(
                "SELECT * FROM USERS WHERE user_id = :id")
            }

    def get_users(self):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def add_user(self, user_id, user_email, subject_id):
        conn = self.db.connect()
        result = conn.execute(self.__scripts["insert"])
        conn.commit()
        conn.close()
        return result

    def delete_user(self, user_id):
        conn = self.db.connect()
        conn.execute(self.__scripts['delete by id'], {'id': user_id})
        conn.commit()
        conn.close()

    def edit_user(self, user_id, new_userEmail):
        conn = self.db.connect()
        conn.execute(self.__scripts['edit by id'], {
            'id': user_id, 'new_email': new_userEmail})
        conn.commit()
        conn.close()

    def get_user_by_id(self, user_id):
        conn = self.db.connect()
        result = conn.execute(self.__scripts[
            'get user by id'], {'id': user_id})
        rows = result.mappings().first()
        conn.close()
        return rows
