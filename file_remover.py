import os
import argparse
from name_reader import read_names

def parser():
    parser = argparse.ArgumentParser(description='File Remover')
    parser.add_argument('--folder', type=str, required=True, help='Path to folder')
    parser.add_argument('--names', type=str, help='Path to names file')

    return parser.parse_args()

def remove_txt_files(folder, names_file):
    names = read_names(names_file)

    for person in names:
        path = os.path.join(folder, person)

        for file in os.listdir(path):
            if file.endswith('.txt'): 
                file_path = os.path.join(path, file)
                os.remove(file_path)

if __name__=='__main__':
    args = parser()    
    remove_txt_files(args.folder, args.names)