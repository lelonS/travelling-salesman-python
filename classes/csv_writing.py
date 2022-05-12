import csv


class csv_writing:
    file_path = ""
    file = None
    writer = None
    file_opened = False

    def __init__(self, path, open_path=False):
        self.file_path = path
        if open_path:
            self.open_file("a")

    def open_file(self, mode, _encoding="UTF-8", _newline=""):
        # mode = "w", "r" or "a"
        if mode not in "war":
            return
        if not self.file_opened:
            self.file = open(self.file_path, mode,
                             encoding=_encoding, newline=_newline)
            self.writer = csv.writer(self.file)
            self.file_opened = True

    def close_file(self):
        if self.file_opened:
            self.writer = None
            self.file.close()
            self.file_opened = False

    def add_line(self, line):
        if self.file_opened:
            self.writer.writerow(line)

    def remove_line(self):
        pass

    def clear_and_write(self):
        pass
