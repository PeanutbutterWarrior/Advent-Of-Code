class Item:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent

    def __str__(self):
        return str(self.parent) + '/' + self.name

    def __eq__(self, other):
        if type(self) == type(other):
            return self is other
        elif type(other) == str:
            return self.name == other
        return False

    def get_size(self):
        return 0


class Folder(Item):
    def __init__(self, name, parent):
        super().__init__(name, parent)
        self.members = []

    def __contains__(self, item):
        return item in self.members

    def __getitem__(self, item):
        for member in self.members:
            if member == item:
                return member
        raise ValueError

    def add_member(self, member):
        self.members.append(member)

    def get_size(self):
        return sum(member.get_size() for member in self.members)


class File(Item):
    def __init__(self, name, parent, size):
        super().__init__(name, parent)
        self.size = size

    def get_size(self):
        return self.size


class Peekable:
    def __init__(self, iterator):
        self.iterator = iterator
        self.next = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.next is not None:
            tmp = self.next
            self.next = None
            return tmp
        else:
            return next(self.iterator)

    def peek(self):
        if self.next is None:
            self.next = next(self.iterator)
        return self.next


with open("Day7.txt", "r") as file:
    data = file.read()

i = Peekable(iter(data.split('\n')))
cwd = Folder('/', '')
root = cwd
for line in i:
    if line[0] == '$':
        _, command, *args = line.split()
        if command == 'ls':
            try:
                while i.peek()[0] != '$':
                    t, name = next(i).split()
                    if t == 'dir':
                        new_item = Folder(name, cwd)
                    else:
                        new_item = File(name, cwd, int(t))
                    cwd.add_member(new_item)
            except StopIteration:
                pass
        elif command == 'cd':
            if args[0] in cwd:
                cwd = cwd[args[0]]
            elif args[0] == '/':
                cwd = root
            elif args[0] == '..':
                cwd = cwd.parent
            else:
                new_dir = Folder(args[0], cwd)
                cwd = new_dir
    else:
        raise Exception

folder_sizes = []


def get_sizes(folder):
    folder_sizes.append(folder.get_size())
    for item in folder.members:
        if type(item) == Folder:
            get_sizes(item)


get_sizes(root)

print(sum(filter(lambda i: i <= 100000, folder_sizes)))

current_size = root.get_size()
free_space = 70_000_000 - current_size
needed_space = 30_000_000 - free_space

print(min(filter(lambda i: i >= needed_space, folder_sizes)))