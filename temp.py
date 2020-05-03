import os


vers = os.listdir("neat-checkpoints")
vers = [int(name.split("-")[2]) for name in vers]
print(vers)

