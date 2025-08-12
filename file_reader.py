class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path


    def open_read_file(self):
        file_to_open = open("expenses.csv")
        try:
            with open(self.file_path, "r") as file_to_open:
                file_info = file_to_open.read()
                print(self.create_list_info(file_info))
        except FileNotFoundError:
            print("The file could not be opened or does note exists")


    def create_list_info(self,info_csv: str):
        split_jump = info_csv.split("\n")
        
        split_info = []
        for i in split_jump:
            split_comma = i.split(",")
            split_comma[1] = float(split_comma[1])
            split_info.append(split_comma)
        return split_info


    def set_file_path(self, new_path:str):
        self.file_path = new_path


    def get_file_path(self):
        return self.file_path


file_reader = FileReader("expenses.csv")
file_reader.open_read_file()