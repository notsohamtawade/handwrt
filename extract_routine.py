import os
import extract

# Replace this line with the absolute path to the "images" directory
os.chdir(r"C:\Users\dell\Desktop\Hndwrt\ml-graphology-master\ml-graphology-master\images")
files = [f for f in os.listdir(".") if os.path.isfile(f)]
os.chdir("..")

page_ids = []
if os.path.isfile("raw_feature_list.txt"):
    print("Info: raw_feature_list found.")
    with open("raw_feature_list.txt", "r") as label:
        for line in label:
            content = line.split()
            page_id = content[-1]
            page_ids.append(page_id)

with open("raw_feature_list.txt", "a") as label:
    count = len(page_ids)
    for file_name in files:
        if file_name in page_ids:
            continue
        features = extract.start(file_name)
        features.append(file_name)
        for feature in features:
            label.write("%s\t" % feature)
        label.write("\n")
        count += 1
        progress = (count * 100) / len(files)
        print(f"{count} {file_name} {progress:.2f}%")
    print("Done!")
