
# Confectionné par les administrateurs de discord.gg/osint


from os import system, name, path, getcwd
import sys 
import time



def clear(): ## emerce noémie
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
system(version+" install gitpython")


import git




def main():

    clear()

    
    print("""
            ____ ____ _ _  _ ___    _    ____ ___  
            |  | [__  | |\ |  |     |    |__| |__] 
            |__| ___] | | \|  |     |___ |  | |__] 

                By Sale Gosse - discord.gg/osint                     """)
    

    # Les petits choix

    choix = input("""
 Marquez le chiffre de la catégorie que vous voulez installer.

[1] - Pseudo
[2] - Email
[3] - Numéro de téléphone
[4] - Linkedin
[5] - Minecraft
[6] - Réseaux Sociaux
[7] - Outils Français


[0] - Tout

                    """)

 ## Je voulais faire un système de plusieurs choix d'un coup mais j'ai laissé ça comme ça, Noémié si tu passes par là 

    if "1" in choix:
        pseudo()
    elif "2" in choix:
        email()
    elif "3" in choix:
        numtel()
    elif "4" in choix:
        linkedin()
    elif "5" in choix:
        mc()
    elif "6" in choix:
        rs()
    elif "7" in choix:
        of()
    
    elif "0" in choix:
        tout()


def tout():
    print('\n--> Les tools Pseudo sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/sherlock-project/sherlock', path.abspath(getcwd())+'/Pseudo/Sherlock/')

    print('\n--> Les tools Email sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/holehe', path.abspath(getcwd())+'/Email/Holehe/')
    git.Repo.clone_from('https://github.com/novitae/emdofi', path.abspath(getcwd())+'/Email/Emdofi/')
    git.Repo.clone_from('https://github.com/mxrch/GHunt', path.abspath(getcwd())+'/Email/GHunt/')

    print('\n--> Les tools de Numéro de téléphone sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/ignorant', path.abspath(getcwd())+'/NumeroDeTelephone/Ignorant/')
    git.Repo.clone_from('https://github.com/sundowndev/phoneinfoga', path.abspath(getcwd())+'/NumeroDeTelephone/Phoneinfoga/')

    print('\n--> Les tools Linkedin sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/nqntnqnqmb', path.abspath(getcwd())+'/Linkedin/nqntnqnqmb/')
    git.Repo.clone_from('https://github.com/mxrch/revealin', path.abspath(getcwd())+'/Linkedin/Revealin/')

    print('\n--> Les tools Minecraft sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/gg-osint/rinaorc-osint', path.abspath(getcwd())+'/Minecraft/Rinaorc/')

    print('\n--> Les tools "Réseaux Sociaux" sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/facebook_totem', path.abspath(getcwd())+'/ReseauxSociaux/Facebook/Facebook_totem/')
    git.Repo.clone_from('https://github.com/megadose/toutatis', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/toutatis')
    git.Repo.clone_from('https://github.com/Datalux/Osintgram', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/Osintgram')


    print('\n--> Les tools Français sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/Fl0wj0b', path.abspath(getcwd())+'/OutilsFrance/Numero/Fl0wj0b/')
    git.Repo.clone_from('https://github.com/daprofiler/DaProfiler', path.abspath(getcwd())+'/OutilsFrance/Global/DaProfiler/')
    
    
    main()



def pseudo(): 


    print('\n--> Les tools Pseudo sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/sherlock-project/sherlock', path.abspath(getcwd())+'/Pseudo/Sherlock/')
    main()
    

def email(): 


    print('\n--> Les tools Email sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/holehe', path.abspath(getcwd())+'/Email/Holehe/')
    git.Repo.clone_from('https://github.com/novitae/emdofi', path.abspath(getcwd())+'/Email/Emdofi/')
    git.Repo.clone_from('https://github.com/mxrch/GHunt', path.abspath(getcwd())+'/Email/GHunt/')
    main()
    

def numtel(): 


    print('\n--> Les tools de Numéro de téléphone sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/ignorant', path.abspath(getcwd())+'/NumeroDeTelephone/Ignorant/')
    git.Repo.clone_from('https://github.com/sundowndev/phoneinfoga', path.abspath(getcwd())+'/NumeroDeTelephone/Phoneinfoga/')
    main()
    

def linkedin(): 


    print('\n--> Les tools Linkedin sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/nqntnqnqmb', path.abspath(getcwd())+'/Linkedin/nqntnqnqmb/')
    git.Repo.clone_from('https://github.com/mxrch/revealin', path.abspath(getcwd())+'/Linkedin/Revealin/')
    main()
    

def mc(): 


    print('\n--> Les tools Minecraft sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/gg-osint/rinaorc-osint', path.abspath(getcwd())+'/Minecraft/Rinaorc/')
    main()
    

def rs(): 


    print('\n--> Les tools "Réseaux Sociaux" sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/facebook_totem', path.abspath(getcwd())+'/ReseauxSociaux/Facebook/Facebook_totem/')
    git.Repo.clone_from('https://github.com/megadose/toutatis', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/toutatis')
    git.Repo.clone_from('https://github.com/Datalux/Osintgram', path.abspath(getcwd())+'/ReseauxSociaux/Instagram/Osintgram')
    main()
    

def of(): 


    print('\n--> Les tools Français sont entrain de s\'installer, le temps va dépendre de votre connexion.')
    git.Repo.clone_from('https://github.com/megadose/Fl0wj0b', path.abspath(getcwd())+'/OutilsFrance/Numero/Fl0wj0b/')
    git.Repo.clone_from('https://github.com/daprofiler/DaProfiler', path.abspath(getcwd())+'/OutilsFrance/Global/DaProfiler/')
    main()
    

main()

