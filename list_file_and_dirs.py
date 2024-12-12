import os

abs_path = r'D:\Samanvay'
tree_dict = {}


def display_tree():
    path = []
    # for item in tree_dict:
    #     print(item+"\n")
    base_dir = os.path.basename(abs_path)
    path.append(base_dir)

    id = 0
    while True:
        print(base_dir + '\n')
        base = tree_dict[base_dir]
        child = base['children']

        if child.__len__():
            base_dir = child[id]
            node = base_dir + '-' + str(id)
            if node is path[-1]:
                break
            else:
                path.append(node)

    return


started = False
for basedir, subdir, files in os.walk(abs_path):
    # print("basedir: {}, subdir: {}, files: {}".format(basedir, subdir, files))
    if not started:
        temp_dict = {'root': True}
        started = True
    else:
        temp_dict = {'root': False}

    temp_dict['parent'] = os.path.dirname(basedir)
    temp_dict['children'] = subdir
    temp_dict['files'] = files
    tree_dict[os.path.basename(basedir)] = temp_dict
    temp_dict = None

print("\ntree_dict: {}".format(tree_dict))



