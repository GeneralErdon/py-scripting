from pathlib import Path

class Serializador:
    """
    #? Serializador Sinteg - Sisalud
    Serializador de la estructura de los reportes del SISALUD
    hacia la estructura de nuestra Base de datos de SINTEG
    """
    def __init__(self) -> None:
        pass


class Main:
    def __init__(self) -> None:
        self._excel_file_path = None
        self._excel_file = None
    
    @property
    def excel_file_path(self) -> Path:
        if self._excel_file_path is not None:
            return self._excel_file_path
        
        self._excel_file_path = Path(input("Ingrese la ruta del archivo excel a comparar ->"))
    

    def main(self, ):
        
        
        
        return







Main().main()