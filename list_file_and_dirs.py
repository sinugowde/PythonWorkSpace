import os

# os.chdir('D:\\BITS')

#abs_path = 'D:\\BITS'
abs_path = 'C:\\Users\\sgowdex\\Desktop\\iBTW4869_20.100.0.1G'

# path = {0: os.path.dirname(abs_path)}
# print(abs_path)
path = {}
# i = 1
first_round = False
for basedir, subdir, files in os.walk(abs_path):
    # base_dir = os.path.basename(basedir)
    base_dir = basedir.split('\\')[-1]
    parent = basedir.split('\\')[-2]

    print("parent: {}, base_dir: {}, subdir: {}, files: {}\n".format(parent, base_dir, subdir, files))

    if (first_round is True) and (subdir != []):
        for item in our_dict:
            if base_dir in item:
                for key in subdir:
                    item[base_dir].append({key: []})
                item[base_dir].append({'files': files})
        print("item: {}\n".format(item))
        # print("path-2: {}\n".format(path))
        # break
    else:
        our_dict = {}
        path[base_dir] = []
        path[base_dir].append([parent, base_dir])
        path[base_dir].append({'files': files})

        for item in subdir:
            # print("item: {}\n".format(item))
            # print("path: {}\n".format(path[base_dir]))
            path[base_dir].append({item: []})
        # pass
    print("path-1: {}\n".format(path))
    first_round = True
    our_dict = path[base_dir]
    print("our_dict: {}\n".format(our_dict))
    parent_dir = base_dir
    base_dir = ''


