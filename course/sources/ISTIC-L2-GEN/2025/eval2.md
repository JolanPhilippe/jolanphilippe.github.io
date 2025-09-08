# Barème d'évaluation – Projet Java : VisuStats

**Total : 20 points**

---

## 1. Implémentation du modèle – 6 points
    * Alpha: 6/6
    * Angle-mort (Bravo): 5/6

- Lecture et chargement du fichier JSON : 1 point  
    * Alpha: 1/1
    * Angle-mort (Bravo): 1/1
- Création des diagrammes (1 point par type correctement implémenté) :  
  - Camembert, barres, colonnes, etc. : jusqu'à 3 points
    * Alpha: 3/3
    * Angle-mort (Bravo): 3/3
- Tests unitaires sur le modèle : 1 point  
    * Alpha: 1/1
    * Angle-mort (Bravo): 0/1
- Documentation du code (classes et méthodes) : 1 point  
    * Alpha: 1/1
    * Angle-mort (Bravo): 1/1

---

## 2. Implémentation du contrôleur – 7 points
    * Alpha: 5/7
    * Angle-mort (Bravo): 6.5/7

- Filtrage des données par granularité (région / département) : 1 point  
    * Alpha: 1/1
    * Angle-mort (Bravo): 0.5/1
- Sélection et filtre critères (1 point par critère correctement géré) : 
  - domaine thematique, categorie, themes, personnage phare, etc. : jusqu'à 3 points 
    * Alpha: 2/3
    * Angle-mort (Bravo): 3/3
- Sélection et calcul des statistiques (1 point par statistique intégrée) : 
  - nombre de musées par domaine, par dpt/region, année de creation, etc. : jusqu'à 3 points points  
    * Alpha: 2/3
    * Angle-mort (Bravo): 3/3

---

## 3. Implémentation de la vue – 3 points
    * Alpha: 3/3
    * Angle-mort (Bravo): 1/3

- Génération d'un rapport web (HTML, SVG, etc.) : 1 point  
    * Alpha: 1/1
    * Angle-mort (Bravo): 0/1
- Interface utilisateur Swing fonctionnelle et claire : 2 points  
    * Alpha: 2/2
    * Angle-mort (Bravo): 1/2

---

## 4. Livrables – 4 points
    * Alpha: 3/4
    * Angle-mort (Bravo): 0.5/4

- Fichier `.jar` exécutable avec l'application complète : 1 point  
    * Alpha 1/1
    * Angle-mort (Bravo): 0/1 point, pas de .jar
- Documentation technique complète :
  - Diagrammes UML, choix de conception, dépendances : 2 points  
    * Alpha 1/2
    * Angle-mort (Bravo): 0.5/2 point, pas de doc, mais les dependance .jar sont dans le projet
- Présence d'un fichier `README.md` ou d'un manuel utilisateur : 1 point    
    * Alpha 1/1
    * Angle-mort (Bravo): 0/1, pas de manuel. README d'origine 

---

## 5. Bonus et Malus

- Bonus UX (expérience utilisateur fluide, ergonomie, personnalisation) : jusqu'à +2 points  
    * Alpha +1
    * Angle-mort (Bravo) 0
- Malus pour code peu lisible ou non conforme aux conventions Java : jusqu'à –2 points  
    * Alpha 0
    * Angle-mort (Bravo) -2
