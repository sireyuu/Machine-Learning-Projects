# Python3 Code to rename multiple files in a directory (Usually used for bulk image upload)
import os
import sys

def main():
    directory = input("Enter the destination folder location : ")
    directory = os.path.normpath(directory) + os.sep  

    if not os.path.isdir(directory):
        print('Path is incorrect! Run script again.')
        sys.exit(1)

    print('File order below:')
    filenames = sorted(os.listdir(directory))
    print('\n'.join(filenames))

    check = input("Is the file order correct? (y/n)").lower()
    if check != 'y':
        print("Exiting")
        sys.exit()

    for i, filename in enumerate(filenames, start=1):
        old_path = os.path.join(directory, filename)
        new_name = filename[:-4].replace('-', '_') + '_bau_sqr.jpg'
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)

        print(f"{filename} is replaced with : {new_name}")

if __name__ == '__main__':
    print("Warning: Once renamed, this cannot be undone!!")
    main()