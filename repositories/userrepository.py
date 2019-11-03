from datasources.filedatasource import FileDataSource


class UserRepository():
    # Realiza el login del usuario.
    # @param entity_login: Objeto con un atributo usuario y password
    # @return Entidad UserDataEntity (lo que va en session!!! )
    # Rise Exception Login error si el login falla
    def user_login(entity_login):
        pass

    # Comprueba si el usuario ya existe
    # @param: un String con el nombre del usuario
    def check_user(user_name):
        pass

    # Da de alta un nuevo usuario en el datasource
    # @param entity_register_user: Objeto con los datos de registro del usuario
    def create_user(entity_register_user):
        pass
