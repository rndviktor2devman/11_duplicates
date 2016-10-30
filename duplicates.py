import os
import sys
import shutil


def are_files_duplicates(file_path1, file_path2):
    if os.path.basename(file_path1) == os.path.basename(file_path2):
        if os.path.getsize(file_path1) == os.path.getsize(file_path2):
            return True

    return False


def are_folders_duplicates(folder_path1, folder_path2):
    if folder_path1.startswith(folder_path2) or folder_path2.startswith(folder_path1):
        return False

    if os.path.basename(folder_path1) == os.path.basename(folder_path2):
        if not os.listdir(folder_path1) and not os.listdir(folder_path2):
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


def notify_deletion(path_list, item_name):
    for path in path_list:
        print("removing {} {}".format(item_name, path))


def get_duplicates(paths_list, check_function):
    file_number = 1
    deletion_list = set()

    for filepath in paths_list[:-1]:
        for filepath2 in paths_list[file_number:]:
            if check_function(filepath, filepath2):
                deletion_list.add(filepath2)

        file_number += 1

    return deletion_list


if __name__ == '__main__':
    if len(sys.argv) > 1:
        rootdir = sys.argv[1]
    else:
        rootdir = os.getcwd()

    files = get_files(rootdir)
    duplicate_files = get_duplicates(files, are_files_duplicates)
    notify_deletion(duplicate_files, "file")
    list(map(os.remove, duplicate_files))
    folders = get_folders(rootdir)
    duplicate_folders = get_duplicates(folders, are_folders_duplicates)
    notify_deletion(duplicate_folders, "directory")
    list(map(shutil.rmtree, duplicate_folders))
