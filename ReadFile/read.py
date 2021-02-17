import pandas as pd


def func_read():
    CSV_FILE_PATH_1 = r'D:\wutianhe_document\NUS_project\VSN.csv'
    CSV_FILE_PATH_2 = r'D:\wutianhe_document\NUS_project\AGM.csv'
    file_1 = pd.read_csv(CSV_FILE_PATH_1)
    file_2 = pd.read_csv(CSV_FILE_PATH_2)
    vsn = pd.DataFrame(file_1)
    agm = pd.DataFrame(file_2)
    return vsn, agm

