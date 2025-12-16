class UsersModule:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def register_user(self, name, email):
        user_id = self.next_id
        self.users[user_id] = {
            "id": user_id,
            "name": name,
            "email": email
        }
        self.next_id += 1
        return {"status": "ok", "user_id": user_id}
