class FileDataSource():
    # Dado un path devuelve True si existe el fichero del path
    def exist_file(self, path):
        pass

    # Lee el fichero al que apunta el path y devuelve el objeto asociado al JSON que contiene el fichero
    # Rise exception si el fichero no se puede leer o el path no es correcto
    def read_file(self, path):
        pass

    # Convierta el data en un JSON y lo escribe en un fichero al que apunta el path
    # Rise exception si el fichero no se escribir
    def write_file(self, path, data):
        pass
