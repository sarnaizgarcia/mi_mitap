from validations.strongpsw import strong_password


class PswRegisterFacade():
    def validate_pswregister(self, password):
        return strong_password(password)


register_psw_facade = PswRegisterFacade()
