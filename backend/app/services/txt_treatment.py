import os
import datetime

from environs import Env
from config import DATA_PATH

env = Env()
env.read_env()

fieldnames = ['id', 'trans_type', 'date', 'value','cpf','card','hour','store_owner','store_name']



class Cnab:

    # def __init__(self, trans_type, date, value,cpf,card,hour,store_owner,store_name):
    #     self.trans_type = trans_type
    #     self.date = date
    #     self.value = value
    #     self.cpf = cpf
    #     self.card = card
    #     self.hour = hour
    #     self.store_owner = store_owner
    #     self.store_name = store_name


    @staticmethod
    def treatment_txt(filename):
        """Funcao resposavel por tratar o arquivo .txt

        Args:
            filename (path file): arquivo recebido
        """
        with open(filename, 'r') as file:
            transfers_list = []
            for line in file.readlines():
                
                date = datetime.datetime(int(line[1:5]), int(line[5:7]), int(line[7:9]))\
                    .strftime("%d/%m/%Y")

                transfers = {
                    "trans_type" : int(line[0]),
                    "date" : str(date),
                    "value" : int(line[9:19]) * 100,
                    "cpf" : int(line[19:30]),
                    "card" : str(line[30:42]),
                    "hour" : f'{line[42:44]}:{line[44:46]}:{line[46:48]}',
                    "store_owner" : line[48:62].lower().strip(),
                    "store_name" : line[62:80].lower().strip(),
                }
                transfers_list.append(transfers)

        return transfers_list



def read_files_data():
    treatment = Cnab()

    for file in os.listdir(DATA_PATH):
        read_txt = treatment.treatment_txt(os.path.join(DATA_PATH, file))

    return read_txt
