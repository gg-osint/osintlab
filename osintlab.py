
# Confectionné par les administrateurs de discord.gg/osint

from os import system, name, getcwd
import os.path as pathUtils

try:
    from alive_progress import alive_bar
    import git
except ImportError:
    print("Merci de faire 'pip install -r requirements.txt' avant de lancer le script!")
    print("Si tu veux installer ces bibliothèques que pour toi, fait 'pip install -r requirements.txt --user'")
    exit(-1)


def clear():  # emerce noémie
    if name == 'nt':
        system('cls')
        return
    system('clear')


def main():
    while True:
        # Le clear déplacé en bas pour avoir les dernières logs

        print("""
                        ____ ____ _ _  _ ___    _    ____ ___
                        |  | [__  | |\ |  |     |    |__| |__]
                        |__| ___] | | \|  |     |___ |  | |__]
                            By Sale Gosse - discord.gg/osint                     """)

        # Les petits choix

        choix = input("""
    Marquez le ou les chiffres de la catégorie que vous voulez installer.
    
    ex: "125" pour installer les outils Pseudo, Email et Numéro de téléphone
    
    [1] - Pseudo
    [2] - Email
    [3] - Numéro de téléphone
    [4] - Linkedin
    [5] - Minecraft
    [6] - Réseaux Sociaux
    [7] - Outils Français
    [0] - Tout

    [x] - Quitter
    """)

    # Je voulais faire un système de plusieurs choix d'un coup mais j'ai laissé ça comme ça, Noémié si tu passes par là
    # Je passe par la, et en en faite suffisait juste de ne pas appeler main() après...

        clear()

        if "1" in choix:
            installPart("Pseudo")
        if "2" in choix:
            installPart("Email")
        if "3" in choix:
            installPart("Tel")
        if "4" in choix:
            installPart("Li")
        if "5" in choix:
            installPart("mc")
        if "6" in choix:
            installPart("Social")
        if "7" in choix:
            installPart("Fr")
        if "0" in choix:
            tout()
        if "x" in choix:
            return


CWD = getcwd()
repos = {
    "Pseudo": {
        "path": "Pseudo",
        "Sherlock": "https://github.com/sherlock-project/sherlock"
    },

    "Email": {
        "path": "Email",
        "Holehe": "https://github.com/megadose/holehe",
        "Emdofi": "https://github.com/novitae/emdofi",
        "GHunt": "https://github.com/mxrch/GHunt"
    },

    "Tel": {
        "path": "NumeroDeTelephone",
        "Ignorant": "https://github.com/megadose/ignorant",
        "Phoneinfoga": "https://github.com/sundowndev/phoneinfoga"
    },

    "Li": {
        "path": "Linkedin",
        "nqntnqnqmb": "https://github.com/megadose/nqntnqnqmb",
        "Revealin": "https://github.com/mxrch/revealin"
    },

    "mc": {
        "path": "Minecraft",
        "Rinaorc": "https://github.com/gg-osint/rinaorc-osint"
    },

    "Social": {
        "path": "ReseauxSociaux",
        "Facebook/Facebook_totem": "https://github.com/megadose/facebook_totem",
        "Instagram/toutatis": "https://github.com/megadose/toutatis",
        "Instagram/Osintgram": "https://github.com/Datalux/Osintgram"
    },

    "Fr": {
        "path": "OutilsFrance",
        "Numero/Fl0wj0b": "https://github.com/megadose/Fl0wj0b",
        "Global/DaProfiler": "https://github.com/daprofiler/DaProfiler"
    }
}


def installPart(choice: str):
    if repos.get(choice) is not None:
        tools = repos[choice]
        print(
            f'\n--> Les tools {tools["path"]} sont entrain de s\'installer, le temps va dépendre de votre connexion.')
        with alive_bar(len(tools), length=20, bar="fish") as bar:
            bar()
            for repo in tools:
                if repo == "path":
                    continue
                path = pathUtils.join(CWD, tools["path"], repo)
                try:
                    _ = git.Repo.clone_from(tools[repo], path)
                except:
                    print(
                        f"Une erreur est survenu sur la repo {tools[repo]}! Passé!\n\n")
                finally:
                    bar()
    else:
        print("Le choix n'existe pas! (ou alors c'est un bug...)\n\n")
    return "\n\n"


def tout():
    j = 0
    print("Installation de tout les outils!")
    print(f"- {len(repos)} module{'s' if len(repos)>1 else ''}")
    for i in repos:
        j += 1
        print(installPart(i))
        print(f"Status: {j}/{len(repos)} modules installés")


clear()
main()
