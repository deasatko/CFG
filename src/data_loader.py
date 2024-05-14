import csv

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.data = []

    def load_data(self):
        with open(self.filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.data.append(row)
        return self.data