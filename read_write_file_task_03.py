import os

# list directory
path = "./sorted"
files = [f for f in os.listdir(path) if os.path.isfile(f"{path}/{f}")]

# create dictionary {name: count lines}
files_info = {}
for file in files:
    with open(f"{path}/{file}") as f:
        files_info[file] = len(f.readlines())

files_info_sorted = dict(sorted(files_info.items(), key=lambda x: x[1]))

# write final file
with open("result.txt", 'w'): pass

for name, count in files_info_sorted.items():
    with open(f"{path}/{name}") as t:
        text = t.read()

    with open("result.txt", 'a') as r:
        r.writelines("{}\n{}\n{}\n".format(name, count, text))
