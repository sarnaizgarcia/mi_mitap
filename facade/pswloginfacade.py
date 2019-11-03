from validations.requirevalidation import field_required


class PswLoginFacade():
    def validate_loginpsw(self, password):
        return field_required(password)


login_psw_facade = PswLoginFacade()
