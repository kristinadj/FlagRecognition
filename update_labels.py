import random
import os
import sys


def update_labels(labels_dir):
    for file in os.listdir(labels_dir):
        path = os.path.join(labels_dir, file)
        f = open(path, "r")
        old_content = f.read()
        tokenized_content = old_content.split(" ")
        if (tokenized_content[0] == '3'):
            tokenized_content[0] = '0'
        elif (tokenized_content[0] == '4'):
            tokenized_content[0] = '1'
        else:
            tokenized_content[0] = '2'
        f.close()

        f = open(path, "w")
        new_content = " ".join(tokenized_content);
        f.write(new_content)
        f.close()

if __name__ == "__main__":
    update_labels(sys.argv[1])