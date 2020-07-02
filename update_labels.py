import random
import os
import sys


def update_labels(labels_dir):
    for file in os.listdir(labels_dir):
        path = os.path.join(labels_dir, file)

        f = open(path, "r")
        lines = f.readlines()
        new_lines = []

        for line in lines:
            tokenized_content = line.split(" ")
            if (tokenized_content[0] == '3'):
                tokenized_content[0] = '0'
                new_content = " ".join(tokenized_content);
                new_lines.append(new_content)
            elif (tokenized_content[0] == '4'):
                tokenized_content[0] = '1'
                new_content = " ".join(tokenized_content);
                new_lines.append(new_content)
            elif (tokenized_content[0] == '8'):
                tokenized_content[0] = '2'
                new_content = " ".join(tokenized_content);
                new_lines.append(new_content)
        f.close()

        f = open(path, "w")
        new_content = " ".join(new_lines);
        f.write(new_content)
        f.close()

if __name__ == "__main__":
    update_labels(sys.argv[1])