import re
import pprint

class Parser():
    def __init__(self):
        self.commands = []

    def command_from_file(self, file_read):
        try:
            data_file = open(file_read, "r")
            dataline= data_file.readlines()
        except:
            print("Error could not open file " +str(file_read))
            return
        
        for element in dataline:
            element = element.upper()
            match = re.search("(X|Y|SLEEP)\s\d*|(#\s.+)"  , element)
             
            if match:
                match = match.string.split()
                anweisung = {}
                anweisung["move_code"] = match[0].strip().upper()
                anweisung["value"] = match[1].strip().upper()
                self.commands.append(anweisung)

        print("closing")
        data_file.close()


if __name__ == "__main__":

    parser = Parser()
    parser.command_from_file("commands.txt")
    pprint.pp(parser.commands)

    for code in parser.commands:
        if code["move_code"] == "X":
            print("Move X-axis %4d" % int(code["value"]))
        elif code["move_code"] == "Y":
            print("Move Y-axis", code["value"])
        elif code["move_code"] == "SLEEP":
            print("Sleep command")
        else:
            print("Hmm don't understand command", code)
    

