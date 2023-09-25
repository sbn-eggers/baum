#!/usr/bin/python

baum_ungeschmueckt="""
             /\\
            /  \\
           /    \\
          /      \\
          /      \\
         /        \\
        /          \\
        /          \\
       /            \\
      /              \\
      /              \\
     /                \\
    /                 \\
    /                  \\
   /                    \\
  /                      \\
  /                      \\
 /                        \\
/,.,.,.,.,.,.,.,.,.,.,.,.,.\\
           |   |
          |`````|
          \_____/
  
"""

baum_geschmueckt="""
             /\\
            <  >
             \/
             /\\
            /  \\
           /++++\\
          /  ()  \\
          /      \\
         /~`~`~`~`\\
        /  ()  ()  \\
        /          \\
       /*&*&*&*&*&*&\\
      /  ()  ()  ()  \\
      /              \\
     /++++++++++++++++\\
    /  ()  ()  ()  ()  \\
    /                  \\
   /~`~`~`~`~`~`~`~`~`~`\\
  /  ()  ()  ()  ()  ()  \\
  /*&*&*&*&*&*&*&*&*&*&*&\\
 /                        \\
/,.,.,.,.,.,.,.,.,.,.,.,.,.\\
           |   |
          |`````|
          \_____/
  
"""




if __name__ == "__main__":
    
    print("Oh je, der Baum ist ja noch garnicht geschmückt!")
    print(baum_ungeschmueckt)
    print("Boty McBotface - hilfreich wie er ist - unterstützt dich gern beim Baumschmücken. \
    Gib das richtige Codewort ein und lass ihn für dich arbeiten.")

    codewort = input("Codewort: ")

    with open("flag.txt", "r") as flag_file:
        flag = flag_file.readline().strip()

    if codewort == flag:
        print(baum_geschmueckt)
        print("Na, jetzt kann Weihnachten ja kommen!")
    else:
        print("Das hat Boty leider nicht verstanden.")
        print("Schau doch mal auf unserem Github vorbei: https://github.com/sbn-eggers/baum")
