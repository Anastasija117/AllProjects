# Python writing files(.txt,.json,.csv)
import json
import csv


employee = [["Name","Age","Job"],
            ["Spongebob",30,"Cook"],
            ["Patrcik",37,"Unemployed"],
            ["Sandy",27,"Scientist"]]

file_path = "C:/Users/User/Desktop/output.csv"

try:
    with open(file=file_path,mode="w") as file:
        writer = csv.writer(file)
        for row in employee:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")
except FileExistsError:
    print("That file already exists")