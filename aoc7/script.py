# %% ==


class Directory:
    def __init__(self, name, parent_dir):
        self.name = name
        self.content = []
        self.parent_dir = parent_dir

    def add_content(self, content):
        self.content.append(content)

    def get_size(self):
        size = 0
        for item in self.content:
            size += item.get_size()
        return size

    def get_subfolder(self, name):
        for item in self.content:
            if item.name == name:
                return item
        return None


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)

    def get_size(self):
        return self.size


root = Directory("/", None)

current_dir = root
with open("input.txt", "r") as f:
    for row in f.readlines():
        r = row.strip()
        if r == "$ cd /":
            current_dir = root
            continue
        tokenized = r.split(" ")
        if tokenized[0] == "dir":
            dir_name = tokenized[1]
            new_dir = Directory(dir_name, parent_dir=current_dir)
            current_dir.add_content(new_dir)
        elif tokenized[0].isnumeric():
            file_name = tokenized[1]
            size = tokenized[0]
            new_file = File(file_name, size)
            current_dir.add_content(new_file)
        elif tokenized[0] == "$":
            if tokenized[1] == "cd":
                if tokenized[2] == "..":
                    current_dir = current_dir.parent_dir
                else:
                    current_dir = current_dir.get_subfolder(tokenized[2])


def print_tree(item, level=0):
    if isinstance(item, Directory):
        print(" " * level * 2, "📂", item.name, f"({item.get_size()})")
        for k in item.content:
            print_tree(k, level=level + 1)
    else:
        print(" " * level * 2, "📝", item.name, f"({item.size})")


print_tree(root)

# %% ==


def calc_size(item):
    if isinstance(item, File):
        return 0
    fsize = item.get_size()
    if fsize > 100000:
        fsize = 0
    sub_fsize = 0
    for thing in item.content:
        sub_fsize += calc_size(thing)
    return fsize + sub_fsize


calc_size(root)


# %% ==

available_space = 70_000_000 - root.get_size()
to_delete = 30_000_000 - available_space
print(to_delete)


def best_folder(folder):
    global to_delete
    current_best_size = folder.get_size()
    for item in folder.content:
        if isinstance(item, File):
            continue
        current_size = best_folder(item)
        if current_size >= to_delete and current_best_size > current_size:
            current_best_size = current_size
    return current_best_size


print(best_folder(root))


# %%
