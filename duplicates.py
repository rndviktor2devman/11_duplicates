import os
import sys
import shutil


def are_files_duplicates(file_path1, file_path2):
    if os.path.basename(file_path1) == os.path.basename(file_path2):
        if os.path.getsize(file_path1) == os.path.getsize(file_path2):
            return True

    return False


def get_folders(path):
    folders_paths = []
    for root, dirs, files in os.walk(path):
        for name in dirs:
            folders_paths.append(os.path.join(root, name))
    return folders_paths


def get_files(path):
    files_paths = []
    for root, dirs, files in os.walk(path):
        for name in files:
            files_paths.append(os.path.join(root, name))
    return files_paths


def remove_dirs(paths_list):
    for path in paths_list:
        shutil.rmtree(path)


def remove_fs_files(paths_list):
    for path in paths_list:
        os.remove(path)


def deletion_message(path_list, item_name="directory"):
    for path in path_list:
        print("removing {} {}".format(item_name, path))


def get_duplicates(paths_list):
    file_number = 1
    deletion_list = []

    for filepath in paths_list[:-1]:
        for filepath2 in paths_list[file_number:]:
            if are_files_duplicates(filepath, filepath2):
                deletion_list.append(filepath2)

        file_number += 1

    return deletion_list


if __name__ == '__main__':
    if len(sys.argv) > 1:
        rootdir = sys.argv[1]
    else:
        rootdir = os.getcwd()

    folders = get_folders(rootdir)
    duplicate_folders = get_duplicates(folders)
    deletion_message(duplicate_folders)
    remove_dirs(duplicate_folders)
    files = get_files(rootdir)
    duplicate_files = get_duplicates(files)
    deletion_message(duplicate_files, "file")
    remove_fs_files(duplicate_files)

