Tu as une erreur quand tu utilises [Import.java](https://jolanphilippe.github.io/course/docs/24-prog1/Import.java) ? La fonction `.toList()` n'est pas reconnue ? Pas de problème, je suis là pour t'aider.

# Mettre à jour Java

`.toList()` est une méthode apparue avec Java 16. Ainsi, si ta version de Java est antérieure à Java 16, ton éditeur préféré affichera une erreur.

## VSCode

VSCode utilise une variable d'environnement `$JAVA_HOME` pour retrouver les executables Java.

Avant tout, vérifions ensemble quelle version de Java tu es en train d'utiliser.
Dans un terminal:

```
java --version
```

Si la version affichée est antérieure à Java 16, alors les prochaines étapes sont à suivre avec attention. Sinon, le problème vient d'ailleurs.

### Télécharger un Java Development Kit (JDK) 

La dernière version de Java est disponible ici: https://www.oracle.com/fr/java/technologies/downloads/ 
Il faut alors télécharger l'archive correspondante à votre architecture de processeur. Dans le doute, il s'agit surement de [x64 Compressed Archive](https://download.oracle.com/java/23/latest/jdk-23_linux-x64_bin.tar.gz).

### Déplacer et décompresser l'archive 

Il faut tout d'abord déplacer votre archives dans un dossier autre que `Téléchargement` (e.g, `Document/Softwares/`). L'archive devrait être ensuite extraite. Note: il est possible de le faire depuis le terminal en utilisant la commande:
```
tar -xzvf fichier.tar.gz
```

### Modifier ses variables d'environnement

Il va falloir modifier le fichier `~/.bashrc` et y ajouter les lignes suivantes.
Il est possible de l'ouvrir avec VSCode en utilisant `code ~/.bashrc`
Attention, il faudra adapter la commander suivante en utilisant le chemin vers le nouveau JDK.
```
export JAVA_HOME="~/Documents/Software/jdk-21_linux-x64_bin/jdk-21.0.5"
export PATH=$JAVA_HOME/bin:$PATH
```
Une fois les lignes ajoutées à la fin du fichier, il suffit de relancer VSCode et normalement, Java sera correctement configuré.
Il est aussi possible de vérifier l'installation en lançant, dans un nouveau terminal,
```
java --version
```
## Eclipse

La version du du JRE (Java Runtime Env.) peut être modifié dans `Window/Preferences`, et ensuite dans `Java\Installed JREs`

## IntelliJ

La version du JDK/SDK peut être modifiée dans `File/Project Structure` (Ctrl+Alt+Shift+S).


