from validations.comparepsw import check_if_psw_is_equal


class ComparePassword():
    def validate_secondpsw(self, password, rep_password):
        return check_if_psw_is_equal(password, rep_password)


compare_psw = ComparePassword()
