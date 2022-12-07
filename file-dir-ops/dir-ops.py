import os

project_path_abs = "/Users/yulm/Documents/learn-python"
project_path = "~/Documents/learn-python"


if __name__ == "__main__":
    # print(os.listdir(project_path_abs))
    print('--------')
    print(os.scandir(project_path_abs))