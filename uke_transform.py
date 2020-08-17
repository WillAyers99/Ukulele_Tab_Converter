
notes= [
"lc" , ["- ","- ","0","- "],
    "lcs" , ["- ","- ","1","- "],
"ld" , ["- ","- ","2","- "],
    "lds" , ["- ","- ","3","- "],
"le" , ["- ","0","- ","- "],

"lf" , ["- ","1","- ","- "],
    "lfs" , ["- ","2","- ","- "],
"lg" , ["- ","3","- ","- "],
    "lgs" , ["- ","4","- ","- "],
"la" , ["0","- ","- ","- "],
    "lbf" , ["1","- ","- ","- "],
"lb" , ["2","- ","- ","- "],

"mc" , ["3","- ","- ","- "],
    "mcs" , ["4","- ","- ","- "],
"hd" , ["5","- ","- ","- "],
    "hds" , ["6","- ","- ","- "],
"he" , ["7","- ","- ","- "],

"hf" , ["8","- ","- ","- "],
    "hfs" , ["9","- ","- ","- "],
"hg" , ["10","- ","- ","- "],
    "hgs" , ["11","- ","- ","- "],
"ha" , ["12","- ","- ","- "],
    "hbf" , ["13","- ","- ","- "],
"hb" , ["14","- ","- ","- "],

"hc" , ["15","- ","- ","- "]]

while True:

    song = input("Input notes separated by comma or \"end\" to exit:")
    if(song == "end"):
        print("Exiting...")
        break
    song = song.split(',')
    print("\n")
    print(song)
    j=0
    translation = []
    for note in song:
        for i in range(0, len(notes)):
            if(note==notes[i]):
                translation.append(notes[i+1])
        j+=1
        if(j==16):
            j=0
            translation.append("nl")

    for i in range (0,4):
        for item in translation:
            if(item=="nl"):
                continue
            if(item[i] == "- "):
                print(item[i]+' ', end='')
            else:
                if(int(item[i]) <=15 and int(item[i]) > 10):
                    print(item[i]+' ', end='')
                else:
                    print(item[i]+'  ', end='')
        print()
    print("done!")


