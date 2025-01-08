import os
import shutil
from pathlib import Path


ROOT_PATH = Path(__file__).parent

#os.mkdir(ROOT_PATH / "NOVO_diretorio")  # Lembrando que o mkdir é para criar uma nova pasta (Diretorio).

#arquivo = open(ROOT_PATH / "novo.txt" , "w")
#arquivo.close()


#os.rename(ROOT_PATH /"novo.txt" , ROOT_PATH / "novo_nome.txt")


os.remove(ROOT_PATH / "novo_nome.txt")

