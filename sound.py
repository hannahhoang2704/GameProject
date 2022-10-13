class bcolors:
    GREEN = '\033[92m'
    RESET = '\033[0m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'

import pyfiglet

T = "Game over"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(bcolors.BLUE + ASCII_art_1 + bcolors.RESET)

T = "YOU WON!"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(bcolors.GREEN + ASCII_art_1 + bcolors.RESET)

print(bcolors.YELLOW +"""            ______
            _\ _~-\___
    =  = ==(____AA____D
                \_____\___________________,-~~~~~~~`-.._
                /     o O o o o o O O o o o o o o O o  |\_
                `~-.__        ___..----..                  )
                      `---~~\___________/------------`````
                      =  ===(_________D
""" + bcolors.RESET)

print(bcolors.RED + """   ,--.
  ()   \\
   /    \\
 _/______\_
(__________)
(/  @  @  \)
(`._,()._,')
(  `-'`-'  )
 \        /
  \,,,,,,/


""" + bcolors.RESET)
