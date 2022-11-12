'''
2022 GNU LICENSE
ALL RIGHTS ARE RESERVED TO THE /OSINT TEAM
'''
from os import system, name, path, getcwd

def clear():
    if name == 'nt':
        system('cls')
        return
    system('clear')


if sys.version_info[0] == 3:
    version = "pip3"
    
else:
    version = "pip"


clear()
print("Installation des packages...\n\n\n\n\n\n\n")
system(f"{version} install gitpython")

from git import Repo

data = {
   1: pseudo,
   2: email,
   3: numtel,
   4: linkedin,
   5: mc,
   6: rs,
   7: of,
   0: tout
}

def main():
    clear()
    print("""
            ____ ____ _ _  _ ___    _    ____ ___  
            |  | [__  | |\ |  |     |    |__| |__] 
            |__| ___] | | \|  |     |___ |  | |__] 

                By Sale Gosse & Noémie - discord.gg/osint                     """)
    
    choix = input("Marquez le chiffre de la catégorie que vous voulez installer.\n\t[1] - Pseudo\n\t[2] - Email\n\t[3] - Numéro de téléphone\n\t[4] - Linkedin\n\t[5] - Minecraft\n\t[6] - Réseaux Sociaux\n\t[7] - Outils Français\n\t[0] - Tout")
    for i in choix:
        try:
            data[int(i)]()
        except KeyError:
            print(f"Option invalide {i}")
        except ValueError:
            print(f"Nous pensions avoir un nombre et nous avons eu un texte {i}")

def tout() -> None:
    for i, k in data:
        if i != 0:
            k()

def pseudo() -> None: 
    print('\n--> Les tools Pseudo sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/sherlock-project/sherlock', path.abspath(getcwd())+'/Pseudo/Sherlock/')
    

def email() -> None: 
    print('\n--> Les tools Email sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/megadose/holehe', path.abspath(getcwd())+'/Email/Holehe/')
    Repo.clone_from('https://github.com/novitae/emdofi', path.abspath(getcwd())+'/Email/Emdofi/')
    Repo.clone_from('https://github.com/mxrch/GHunt', path.abspath(getcwd())+'/Email/GHunt/')
    

def numtel() -> None: 
    print('\n--> Les tools de Numéro de téléphone sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/megadose/ignorant', path.abspath(getcwd())+'/NumeroDeTelephone/Ignorant/')
    Repo.clone_from('https://github.com/sundowndev/phoneinfoga', path.abspath(getcwd())+'/NumeroDeTelephone/Phoneinfoga/')
    

def linkedin() -> None: 
    print('\n--> Les tools Linkedin sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/megadose/nqntnqnqmb', path.abspath(getcwd())+'/Linkedin/nqntnqnqmb/')
    Repo.clone_from('https://github.com/mxrch/revealin', path.abspath(getcwd())+'/Linkedin/Revealin/')
    

def mc() -> None: 
    print('\n--> Les tools Minecraft sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/gg-osint/rinaorc-osint', path.abspath(getcwd())+'/Minecraft/Rinaorc/')
    

def rs() -> None: 
    print('\n--> Les tools "Réseaux Sociaux" sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/megadose/facebook_totem', path.abspath(getcwd())+'/ReseauxSociaux/Facebook/Facebook_totem/')
    Repo.clone_from('https://github.com/megadose/toutatis', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/toutatis')
    Repo.clone_from('https://github.com/Datalux/Osintgram', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/Osintgram')
    

def of() -> None: 
    print('\n--> Les tools Français sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    Repo.clone_from('https://github.com/megadose/Fl0wj0b', path.abspath(getcwd())+'/OutilsFrance/Numero/Fl0wj0b/')
    Repo.clone_from('https://github.com/daprofiler/DaProfiler', path.abspath(getcwd())+'/OutilsFrance/Global/DaProfiler/')
    
while True:
    main()
