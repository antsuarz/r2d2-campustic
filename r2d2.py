
def print_r2():
    print(r"""____________________________________________________________
                   _______      _____   ______     _____                           
          ___     |_   __ \    / ___ `.|_   _ `.  / ___ `.		  
         / ()\      | |__) |  |_/___) |  | | `. \|_/___) |                
       _|_____|_    |  __ /    .'____.'  | |  | | .'____.'                      
      | | === | |  _| |  \ \_ / /_____  _| |_.' // /_____                        
      |_|  O  |_| |____| |___||_______||______.' |_______|                            
       ||  O  ||                                  			
       ||__*__||                                   			
      |~ \___/ ~|                                  			
      /=\ /=\ /=\                                 			
______[_]_[_]_[_]___________________________________________""")


def print_version():
    print("")
    print("V-1.0.0 - Campus Tic 2024 - University of Oviedo")
    print("This software uses the 100k worst passwords list defined by OWASP in:")
    print(r"https://github.com/OWASP/passfault/blob/master/wordlists/wordlists/10k-worst-passwords.txt")
    print("")
    print("____________________________________________________________")


if __name__ == '__main__':
    print_r2()
    print_version()
    username = input("Please, enter a username to check its password:")


