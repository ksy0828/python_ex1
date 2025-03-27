import zipfile
import os 

RESULT_DIR = 'rss_results'

zip_file = zipfile.ZipFile('results.zip', 'w')

for root, dirs, files in os.walk(RESULT_DIR):
    print(root, dirs, files)
    for file in files:
        zip_file.write(os.path.join(root, file))

zip_file.close()



