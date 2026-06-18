from UsersTable import UsersTable
from config import MY_URL_BASE
db = UsersTable(MY_URL_BASE)


def test_get_users():
    db_result = db.get_users()
    assert len(db_result) > 0


def test_add_user():
    len_before = db.get_users()
    db.add_user('user_id', 'user_email', 'subject_id')
    db.get_users()
    len_after = db.get_users()
    assert len(len_after) == len(len_before) + 1


def test_delete():
    # Добавили компанию через базу:
    user_id = "435"
    user_email = "dmitry.l@gmail.com"
    subject_id = "1"
    db.add_user(user_id, user_email, subject_id)
    db.delete_user(user_id)
    len_after_delete = db.get_users()
    assert user_id not in [user['user_id'] for user in len_after_delete]


def test_edit_subject():
    user_id = "435"
    user_email = "dmitry.l@gmail.com"
    subject_id = "1"
    new_userEmail = "nikolay345@gmail.com"
    db.add_user(user_id, user_email, subject_id)
    db.edit_user(user_id, new_userEmail)
    updated_user = db.get_user_by_id(user_id)
    assert updated_user['user_email'] == new_userEmail
    db.delete_user(user_id)
