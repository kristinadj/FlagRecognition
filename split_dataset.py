import random
import os
import sys


def split_dataset(dataset_dir):
    test_file = open("test.txt", 'w')
    train_file = open("train.txt", 'w')

    path, dirs, files = next(os.walk(dataset_dir))

    data_size = len(files)
    test_dataset_size = int(0.2 * data_size)
    test_dataset_file_indices = random.sample(range(data_size), k=test_dataset_size)
    idx = 0

    for f in os.listdir(dataset_dir):
        if f.split(".")[3] == "jpg":
            idx += 1

            if idx in test_dataset_file_indices:
                test_file.write(dataset_dir + '/' + f + '\n')
            else:
                train_file.write(dataset_dir + '/' + f + '\n')


if __name__ == "__main__":
    split_dataset(sys.argv[1])
