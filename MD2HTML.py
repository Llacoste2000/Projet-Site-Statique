
import os

#GLOBAL VARS

convertDone = False
prefix = "M2H>>"
commands = ["-h", "--help", "-i", "--input-directory", "-o", "--output-directory", "-q", "--quitter"]
command = ""

#dessins de départ + conseil --help
def init() :

    print("                                                             ,----,                 ,--, ")
    print("          ____                                   ,--,      ,/   .`|        ____  ,---.'|    ")
    print("        ,'  , `.    ,---,        ,----,        ,--.'|    ,`   .'  :      ,'  , `.|   | :  ")
    print("     ,-+-,.' _ |  .'  .' `\    .'   .' \    ,--,  | :  ;    ;     /   ,-+-,.' _ |:   : |    ")
    print("  ,-+-. ;   , ||,---.'     \ ,----,'    |,---.'|  : '.'___,/    ,' ,-+-. ;   , |||   ' :    ")
    print(" ,--.'|'   |  ;||   |  .`\  ||    :  .  ;|   | : _' ||    :     | ,--.'|'   |  ;|;   ; '    ")
    print("|   |  ,', |  '::   : |  '  |;    |.'  / :   : |.'  |;    |.';  ;|   |  ,', |  ':'   | |__  ")
    print("|   | /  | |  |||   ' '  ;  :`----'/  ;  |   ' '  ; :`----'  |  ||   | /  | |  |||   | :.'| ")
    print("'   | :  | :  |,'   | ;  .  |  /  ;  /   '   |  .'. |    '   :  ;'   | :  | :  |,'   :    ; ")
    print(";   . |  ; |--' |   | :  |  ' ;  /  /-,  |   | :  | '    |   |  ';   . |  ; |--' |   |  ./  ")
    print("|   : |  | ,    '   : | /  ; /  /  /.`|  '   : |  : ;    '   :  ||   : |  | ,    ;   : ;    ")
    print("|   : '  |/     |   | '` ,/./__;      :  |   | '  ,/     ;   |.' |   : '  |/     |   ,/  ")
    print(";   | |`-'      ;   :  .'  |   :    .'   ;   : ;--'      '---'   ;   | |`-'      '---'      ")
    print("|   ;/          |   ,.'    ;   | .'      |   ,/                  |   ;/                     ")
    print("'---'           '---'      `---'         '---'                   '---'                      ")
    print("")

    print("Bienvenue sur le convertisseur de fichier Markdown vers fichier HTML !")
    print("pour plus de renseignements sur comment utiliser les commandes de ce \n convertisseur utilisez \"mth -h\" ou \"--help\"")

    print("")

#vérifie si la string entrée correspond à une commande
def validCommand(str) :

    args = []
    arg = ""
    quote = False

    for lettre in str :

        if lettre == "\"":
            if quote :
                quote = False
                args.append(arg)
                arg = ""
            else :
                quote = True
        elif lettre == " " and not quote:
            args.append(arg)
            arg = ""
        else :
            arg = arg + lettre

    if arg != "":
        args.append(arg)

    testArgs = True
    i = 0

    if len(args) == 1 and args[0] != "mth" :
        return 1
    else :

        #si tout va bien alors vérification des arguments

        if args[1] == commands[0] or args[1] == commands[1]:

            return "help"

        elif args[1] == commands[6] or args[1] == commands[7] :

            return "quitter"

        elif args[1] == commands[2] or args[1] == commands[3]:

            if len(args) == 3:
                return "convertSameDirectory"
            else :
                print("il manque le chemin d'input")

        elif len(args) == 5 and ((args[1] == commands[2] or args[1] == commands[3]) and (args[2] != "" or args[2] != None) or (args[3] == commands[4] or args[3] == commands[5])):

            return "convertToDirectory"

        else :
            #sinon erreur dans la commande entrée
            return 2

#Montre tableau explication des arguments
def showHelp() :

    print("----------HELP----------")
    print("Command usage : mth [-h | --help] [-q | --quitter] [-i | input-directory] \"Path\" [-o | --output-directory] \"Path\"")
    print("")
    print("* : argument obligatoire")
    print("")
    print("-i | --input-directory  *: Spécifie le chemin du fichier a convertir (si cet argument \n                           est seul, le fichier final sera dans le même dossier \n                           que le fichier Markdown, et aura le même nom)")
    print("-o | --output-directory  : Spécifie le chemin de dépot du fichier convertit (les noms \n                           de fichiers avec espaces ne sont pas acceptés)")
    print("")
    print("-q | --quitter           : quitte le convertisseur")

#Fonction de convertion type MD vers HTML
def md_to_html(file, htmlTable):

    htmlFileLines = htmlTable
    ulOpen = False
    breakLine = False

    lines = file.read().splitlines()

    for line in lines:

        line = line.encode("latin1").decode("utf-8")

        if breakLine :
            breakLine = False
            htmlFileLines.append("<br>")

        line = line.replace("**", "<b>")

        if line.startswith("# "):
            htmlFileLines.append("<h1>" + line[2:] + "</h1>")

        elif line.startswith("## "):
            htmlFileLines.append("<h2>" + line[3:] + "</h2>")

        elif line.startswith("### "):
            htmlFileLines.append("<h3>" + line[4:] + "</h3>")

        elif line.startswith("http://") or line.startswith("https://"):
            htmlFileLines.append("<a href=\"" + line + "\">" + line + "</a>")
            breakLine = True

        elif line.startswith("- "):

            if not ulOpen:
                htmlFileLines.append("<ul>")
                ulOpen = True

            htmlFileLines.append("<li>" + line[2:] + "</li>")

        elif not line.startswith("- ") and (line != "" or line != None) and ulOpen:
            htmlFileLines.append("</ul>")
            ulOpen = False

        else :
            htmlFileLines.append(line)


#vérifie si le chmin entré en variable d'argument est valide
def checkPath(path, type):
    if type == "input":
        try:
            with open(path) as file:
                return 1
        except IOError:
            return 0

    if type == "output" :
        if os.path.isdir(path) :
            return 1
        else :
            return 0

#si les deux arguments sont présents (-o, -i)
def convertToDirectory(inputPath, outputPath) :

    htmlLines = []

    if checkPath(inputPath, "input"):

        if checkPath(outputPath, "output") :

            file = open(inputPath, "r")
            fileNameExt = file.name
            fileName = fileNameExt[:-3]
            fileExt = fileNameExt[-3:]

            if fileExt == ".md" :

                print(outputPath + "/" + fileName+ ".html")

                print("début de la convertion du fichier...")

                md_to_html(file, htmlLines)

                if os.path.isfile(outputPath + "/" + fileName+ ".html") :

                    overWriteCase = False

                    while not overWriteCase:

                        overWrite = input("le fichier existe déjà, voulez-vous le replacer ? (yes/no)")

                        if overWrite == "yes":

                            os.remove(outputPath + "/" + fileName+ ".html")

                            htmlFile = open(outputPath + "/" + fileName+ ".html", "a")

                            for line in htmlLines:
                                htmlFile.write(line)

                            htmlFile.close()
                            print("Convertion terminée")

                            overWriteCase = True

                        elif overWrite == "no":

                            print("Convertion annulée")
                            overWriteCase = True

                        else:

                            print("je n'ai pas compris votre choix")

                else :

                    htmlFile = open(outputPath + "/" + fileName + ".html", "a")

                    for line in htmlLines:
                        htmlFile.write(line)
                    print("convertion terminé")

            else :
                print("Le fichier donné n'est pas un markdown")

        else :
            print("Le chemin d'output est incorrect")

    else :

        print("Le chemin d'input est incorrect")

#si seulement l'argument input(-i)
def convertSameDirectory(inputPath) :

    htmlLines = []

    if checkPath(inputPath, "input"):

        file = open(inputPath, "r")
        fileNameExt = file.name
        fileName = fileNameExt[:-3]
        fileExt = fileNameExt[-3:]

        if fileExt == ".md" :

            print("convertion du fichier en cours dans le même fichier")

            #presets func

            md_to_html(file, htmlLines)

            #début de l'écriture du fichier html

            if os.path.isfile(inputPath[:-3]+".html"):

                overWriteCase = False

                while not overWriteCase:

                    overWrite = input("le fichier existe déjà, voulez-vous le replacer ? (yes/no)")

                    if overWrite == "yes" :

                        os.remove(inputPath[:-3]+".html")

                        htmlFile = open(inputPath[:-3] + ".html", "a")

                        for line in htmlLines:
                            htmlFile.write(line)

                        htmlFile.close()
                        print("Convertion terminée")

                        overWriteCase = True

                    elif overWrite == "no" :

                        print("Convertion annulée")
                        overWriteCase = True

                    else :

                        print("je n'ai pas compris votre choix")

        else :
            print("Le fichier donné n'est pas un markdown")

    else :

        print("Le chemin est incorrect")

init()

while convertDone != True:

    command = input(prefix)
    args = command.split(" ")

    valid = validCommand(command)

    if valid == 1:

        print("Vous devez commencer par m'appeler poliment ! \n"
              "Commencez par \"mth\"")

    elif valid == 2:

        print("Un argument est manquant, mal marqué ou même en trop si ça se trouve...")

    else:

        if valid == "help":

            showHelp()

        elif valid == "quitter" :

            quitter = ""
            quitter_case = False

            while not quitter_case:

                quitter = input("voulez-vous vraiment quitter le convertisseur ?(yes/no)")

                if quitter == "yes" :
                    quitter_case = True
                    convertDone = True

                elif quitter == "no" :
                    quitter_case = True
                    continue

                else :

                    print("je n'ai pas compris votre choix")


        elif valid == "convertToDirectory":

            convertToDirectory(args[2], args[4])

        elif valid == "convertSameDirectory":

            convertSameDirectory(args[2])