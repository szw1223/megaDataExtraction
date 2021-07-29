import os

for root, dirs, files in os.walk(os.path.abspath('2000warcs')):
        print(root)
        directories = root.split('\\')
        print(directories)