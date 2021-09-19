import sys

def shortest_and_longest_name_on_the_list(list):
    smaller = ""
    bigger = ""
    i=0
    for item in list:
        if((smaller == "") or (len(item) < len(smaller))):
            smaller = item
        if ((bigger == "") or (len(item) > len(bigger))):
            bigger = item
        i+=1
    smaller = smaller.lower()
    bigger = bigger.lower()
    return smaller.capitalize(), bigger.capitalize()

def lexicography(list):
    smaller = ""
    bigger = ""
    i=0
    for item in list:
        if((smaller == "") or (item < smaller)):
            smaller = item
        if((bigger == "") or (item > bigger)):
            bigger = item
        i+=1
    smaller = smaller.lower()
    bigger = bigger.lower()
    return smaller.capitalize(), bigger.capitalize()

if __name__ == "__main__":
    list = ["Anne","Jammie","Bruce","Beatrice","Oleg","Leann","Regina","Laurice","Collene","Erinn","Janie","Grayce","Krissy","Angie","Madonna","Juan","Gabriel","Stanley","Maryland", "Marieva"]
    print(shortest_and_longest_name_on_the_list(list))
    print(lexicography(list))