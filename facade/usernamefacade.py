from validations.requirevalidation import field_required


class UserNameFacade():
    def validate_username(self, user_name):
        return field_required(user_name)


user_name_facade = UserNameFacade()
