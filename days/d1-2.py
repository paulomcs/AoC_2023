
def analise_line(line):
    line_value = ""
    i = 0
    j = len(line) - 1
    condi = True
    condj = True
    while i < j or (condi or condj):
        if line[i].isdigit() and condi:
            line_value = line[i] + line_value 
            condi = False
        if line[j].isdigit() and condj:
            line_value =  line_value + line[j]
            condj = False
        i += 1
        j -= 1
    return line_value

def letter_to_number(line):
    words = {
        "one": 1,
        "two": 2,
        
    }

def main():
    with open("../inputs/d1-1") as f:
        result = 0
        for line in f:
            print(a)
        print(result)

if __name__ == "__main__":
    main()