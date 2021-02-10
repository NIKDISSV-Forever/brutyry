import sys


class Brutyry:

    def __init__(self, argv):

        self.file_name = "wordlist.txt"
        if "-fn" in argv:
            try:
                self.file_name = argv[
                    argv.index("-fn")+1
                ]
            except:
                pass

        self.len = 4
        if "-len" in argv:
            try:
                self.len = int(
                    argv[
                        argv.index("-len")+1
                    ]
                )
            except:
                pass

        self.append = False
        if "-A" in argv:
            self.append = True

        self.out = False
        if "-out" in argv:
            self.out = True

        self.timer = False
        if "-T" in argv:
            self.timer = True

        if self.out:
            sys.stdout.write(
                f"File: {self.file_name}\nLen of pass: {self.len}\nStdout: {self.out}\n\nIs that correct? (If yes, press Enter) "
            )
            for i in sys.stdin:
                if i.strip() == "":
                    break
                else:
                    sys.stdout.write(
                        "\nRestart the program with the correct parameters.\n\n"
                    )
                    quit(1)

        self.max_ = map(
            lambda x: str(x).rjust(self.len, "0") + "\n",
            range(
                int("9" * self.len) + 1)
        )

        self.generate()

    def generate(self):

        if self.timer:
            from time import time
            TIMED = time()
        with open(self.file_name, ("a" if self.append else "w")) as f:
            args = tuple([f])
            if self.out:
                self.generate_Out(*args)
            else:
                self.generate_noOut(*args)
        if self.timer:
            self.TIMED = time() - TIMED
            sys.stdout.write(str(self.TIMED))

    def generate_noOut(self, fileH):
        for l in self.max_:
            fileH.write(l)

    def generate_Out(self, fileH):
        for l in self.max_:
            fileH.write(l)
            sys.stdout.write(l)

    def generater(self):
        for l in self.max_:
            yield l


if __name__ == "__main__":
    Brutyry(sys.argv)
