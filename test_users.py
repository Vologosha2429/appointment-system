from users import UsersModule

def test_user_registration():
    users = UsersModule()

    result = users.register_user("Ivan", "ivan@test.com")

    assert result["status"] == "ok"
    assert result["user_id"] == 1
    assert users.users[1]["name"] == "Ivan"
    assert users.users[1]["email"] == "ivan@test.com"
