import os

# os.chdir('D:\\BITS')

abs_path = 'D:\\BITS'

# path = {0: os.path.dirname(abs_path)}
# print(abs_path)
path = {}
# i = 1
first_round = False
for basedir, subdir, files in os.walk(abs_path):
    base_dir = os.path.basename(basedir)

    if (first_round is True) and (subdir != []):
        # for folder in subdir:
        #     for item in len(parent_dir[0]):
        #         if item == folder:
        #             path[parent_dir[0][path[parent_dir][0][0]]] = folder
        # pass
        break
    else:
        path[base_dir] = []
        for item in subdir:
            path[base_dir][item] = {}
        path[base_dir]['file'] = files
        pass

    first_round = True
    parent_dir = base_dir
    base_dir = ''
print(path)
    # path[os.path.basename(basedir)] = [subdir, files]
    # print('{}: {}; {}; {}'.format(i, os.path.basename(basedir), subdir, files))
    # path[i] = [os.path.basename(basedir), subdir, files]
    # i += 1

# for i in range(1, len(path)):
#     print(path[i][1])


# for key, value in path.items():
#     print("{}: {}".format(key, value))

