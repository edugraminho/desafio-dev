import os
import datetime

from environs import Env
from config import DATA_PATH, EXTENSIONS

env = Env()
env.read_env()


class Cnab:
    @staticmethod
    def treatment_txt(filename):
        """Funcao resposavel por tratar o arquivo .txt

        Args:
            filename (path file): arquivo recebido
        """
        types_transactions = {
            1: ["Débito", "Entrada"],
            2: ["Boleto", "Saída"],
            3: ["Financiamento", "Saída"],
            4: ["Crédito", "Entrada"],
            5: ["Recebimento Empréstimo", "Entrada"],
            6: ["Vendas", "Entrada"],
            7: ["Recebimento TED", "Entrada"],
            8: ["Recebimento DOC", "Entrada"],
            9: ["Aluguel", "Saída"], }

        with open(filename, 'r') as file:
            transfers_list = []
            for line in file.readlines():

                trans_type = ""
                for k, v in types_transactions.items():
                    if int(line[0]) == k:
                        trans_type = v[0]
                
                date = datetime.datetime(int(line[1:5]), int(line[5:7]), int(line[7:9]))\
                    .strftime("%d/%m/%Y")

                transfers = {
                    "trans_type" : trans_type,
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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in EXTENSIONS
           