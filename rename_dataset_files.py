import random
import os
import sys


def rename_files(dataset_dir):
    for f in os.listdir(dataset_dir):
        name_parts = f.split(".")
        new_name = name_parts[0] + "-" + name_parts[3] + "." + name_parts[4]

        old_file = os.path.join(dataset_dir, f)
        new_file = os.path.join(dataset_dir, new_name)

        os.rename(old_file, new_file)


if __name__ == "__main__":
    images = sys.argv[1]
    labels = sys.argv[2]
    rename_files(images)
    rename_files(labels)