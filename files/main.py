__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import pathlib, os, shutil, glob, zipfile

def main():
    print(find_password(cached_files()))

def clean_cache():
    # current_dir = pathlib.Path(__file__).parent
    current_dir = os.getcwd()
    path = f'{current_dir}\cache'
    files = glob.glob(f'{path}\*')
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print(f'Creating of the directory {path} failed')
        else:
            print(f'Successfully created directory {path}')
    else:
        # shutil.rmtree(path)
        # os.mkdir(path)
        for f in files:
            os.remove(f)

def cache_zip(file_path, cache_dir_path):
    clean_cache()
    with zipfile.ZipFile(file_path) as zipped_data:
        zipped_data.extractall(cache_dir_path)

zip_file_path = os.path.abspath('data.zip')
target_path = f'{os.getcwd()}\cache'

cache_zip(file_path=zip_file_path, cache_dir_path=target_path)

def cached_files():
    path = f'{os.getcwd()}\cache'
    files_list = []
    cached_files_list = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        files_list.extend(filenames)
        break
    for f in filenames:
        cached_files_list.append(f'{path}\{f}')
    return cached_files_list       

def find_password(cached_files):
    password_file = []
    password = ''
    for path in cached_files:
        with open(path, 'r') as file:
            file_lines = file.read()
            if 'password' in file_lines:
                file.close()
                correct_file = open(path, 'r')
                password_file.extend(correct_file.readlines())
                correct_file.close()
                break
            else:
                continue
    for i in password_file:
        if 'password' in i:
            password = str(i.split()[-1])  
    return password

if __name__ == '__main__':
    main()