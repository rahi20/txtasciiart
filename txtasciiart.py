import sys

def main():
    l = 4
    h = 5
    t = sys.argv[1:]

    rows = [
        " #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ##   #  ##   ## ### # # # # # # # # # # ### ### ",
        "# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # # # # # # # #    #  # # # # # # # # # #   #   # ",
        "### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ##  # # ##   #   #  # # # # ###  #   #   #   ## ",
        "# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # #    ## # #   #  #  # # # # ### # #  #  #       ",
        "# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  #     # # # ##   #  ###  #  # # # #  #  ###  #  "
    ]

    if len(t) > 0 :
        t = " ".join(t)

        init = ord("A")
        ascii = []
        for i in range(h):
            row = rows[i]
            line = ""
            for c in list(t) :
             
                diff = ord(c.upper()) - init
            
                if c == " " : 
                    line += "    "
                    continue 

                if diff > (ord("Z") - init) or diff < 0 :
                    line += row[-1-(l-1):] 
                    continue

                line += row[diff * l : diff * l + l]

            ascii.append(line)

        for line in ascii:
            print(line)
    else : 
        sys.exit("No arguments passed")

    

