
import csv

def to_csv(filename, data, quiet=False):
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        if not quiet:
            print(f"[+] {filename} successfully created!")
