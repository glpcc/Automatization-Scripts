import os
import shutil

# the null forlder would mean no moving
custom_folders_for_extensions: dict[str,str] = {
    '.jpeg': 'images',
    '.png': 'images',
    '.gif': 'images',
    '.ini': '',
}
# This desides if non especified extensions should go the their extension folder
move_to_extension_folder : bool = True

downloads_folder: str = os.path.expanduser('~') + '\\Downloads'
# Change this if you want the final folders in another folder
dest_folder: str = downloads_folder


def move_file(file_path,file_name,dest_folder):
    if os.path.isdir(dest_folder) and not os.path.isfile(dest_folder):
        shutil.move(file_path,dest_folder + '\\' + file_name )
    elif not os.path.isfile(dest_folder) and not os.path.isdir(dest_folder) :
        os.mkdir(dest_folder)
        shutil.move(file_path,dest_folder + '\\' + file_name )

for file in os.listdir(downloads_folder):
    file_path = downloads_folder + '\\'+ file
    if os.path.isfile(file_path):
        extension = os.path.splitext(file)[1]
        if extension in custom_folders_for_extensions:
            if custom_folders_for_extensions[extension]:
                move_file(file_path,file,dest_folder + '\\' + custom_folders_for_extensions[extension])
        elif move_to_extension_folder:
            move_file(file_path,file,dest_folder + '\\' + extension[1:])
