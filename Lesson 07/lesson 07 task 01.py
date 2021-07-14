import os


def main_dir(dir_name):
    try:
        os.path.exists(dir_name)
        os.mkdir(dir_name)
    except FileExistsError as e:
        print(f'dir exist: {e.filename}')
    return 0


def create_dir_in_main(*dir_in_main_dir):
    for el in dir_in_main_dir:
        try:
            dir_in_main = 'my project', el
            dir_path = os.path.join(*dir_in_main)
            os.path.exists(dir_path)
            os.mkdir(dir_path)
        except FileExistsError as e:
            print(f'dir exist: {e.filename}')
    return 0

main_dir('my project')
create_dir_in_main('settings', 'mainapp', 'adminapp', 'authapp')
