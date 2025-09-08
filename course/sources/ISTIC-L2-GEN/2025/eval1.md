# 📝 Barème d’évaluation – Projet Java : Formes géométriques en SVG

**Total : 20 points**

---

## 🧱 1. Implémentation du code – **12 points**

| Critère                                                                                      | Points |
|----------------------------------------------------------------------------------------------|--------|
| ✅ Implémentation complète de l'interface `IForme` dans toutes les classes                  | 2 pts  |
| 🧩 Structure des classes : Utilisation d'une classe abstraite et respect principe POO        | 2 pts  |
| 🔧 Fonctionnement correct des méthodes (`deplacer`, `redimensionner`, `dupliquer`, etc.)     | 2.5 pts|
| 👥 Gestion correcte des groupes de formes (`Groupe`)                                         | 2 pts  |
| 🍰 Implémentation correcte de `Secteur` et `Camembert` (formes avancées)                    | 2 pts  |
| 🖼️ Export propre en SVG via la méthode `enSVG()`                                              | 1.5 pt |

---

## 🧪 2. Tests unitaires – **5 points**

| Critère                                                                                      | Points |
|----------------------------------------------------------------------------------------------|--------|
| 📂 Tests présents pour chaque forme                                                          | 1.5 pt |
| 🧪 Tests sur les principales méthodes fonctionnelles                                          | 2 pts  |
| 🛠️ Utilisation d’un framework de test (ex : JUnit)                                           | 0.5 pt |
| 🚨 Tests sur cas limites / erreurs (redimensionnement négatif, rotation extrême, etc.)      | 1 pt   |

---

## 📘 3. Documentation Javadoc – **1.5 point**

| Critère                                                                                      | Points |
|----------------------------------------------------------------------------------------------|--------|
| 📝 Présence de Javadoc sur les classes et méthodes publiques                                 | 1 pt   |
| ✍️ Clarté, concision et utilité des commentaires                                              | 0.5 pt |

---

## 🎨 4. Qualité du code (style Java) – **1.5 point**

| Critère                                                                                      | Points |
|----------------------------------------------------------------------------------------------|--------|
| 🧹 Respect des conventions Java (camelCase, indentation, noms significatifs)                 | 0.5 pt |
| 📐 Lisibilité du code (bonne organisation, clarté, pas de redondance)                        | 0.5 pt |
| 📁 Organisation du projet (structure de dossiers, séparation logique)                        | 0.5 pt |

---

## 🎁 Bonus (facultatif) – **+0.5 à +1 pt**

- Fonctionnalité bonus pertinente (ex : export JSON, GUI, SVG animé)
- Très bonne initiative de conception ou architecture élégante

---

✅ **Rappel des formes attendues** :  
`Cercle`, `Ligne`, `Polygone`, `Rectangle`, `Triangle`, `Groupe`, `Secteur`, `Camembert`  
→ Toutes implémentent l’interface `IForme` et ses méthodes obligatoires :

- `centre()`  
- `colorier(String...)`  
- `deplacer(double, double)`  
- `description(int)`  
- `dupliquer()`  
- `hauteur()`  
- `largeur()`  
- `redimensionner(double, double)`  
- `tourner(int angle)`  
- `aligner(Alignement alignement, double cible)`  
- `enSVG()`

---
