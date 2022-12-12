from pathlib import Path
import pandas as pd
from dataclasses import dataclass


# todo  put in class
@dataclass()
class FileLoader:
    file_in: Path

    def make_dataframe(self):
        if Path(self.file_in).suffix == ".csv":
            dataframe_file_to_generate_on = pd.read_csv(self.file_in, ";")

        elif Path(self.file_in).suffix == ".xlsx":
            dataframe_file_to_generate_on = pd.read_excel(self.file_in, engine="openpyxl")

        elif Path(self.file_in).suffix == ".xls":
            dataframe_file_to_generate_on = pd.read_excel(self.file_in)

        # file_to_generate_on.replace(['nan', 'None'], '')
        return dataframe_file_to_generate_on


def main():
    print("class work")


if __name__ == '__main__':
    main()
    pad = Path.cwd().parent
    pad1 = pad.joinpath("from_SQL_test_data/select_so_SalesOrderNo_as_ordernummer__s.xlsx")
    pad2 = FileLoader(pad1)

    print(pad1.is_file())
    print(pad2.make_dataframe().head())
    ddf_fiel = pad2.make_dataframe()
