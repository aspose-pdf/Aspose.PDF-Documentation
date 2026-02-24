---
title: Travailler avec des graphiques dans PDF à l'aide de Python
linktitle: Travailler avec des graphiques
type: docs
weight: 70
url: /fr/python-net/working-with-graphs/
description: Cet article explique ce qu'est un graphique, comment créer un objet rectangle rempli et d'autres fonctions
lastmod: "2025-05-14"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ajouter des graphiques au PDF avec Python
Abstract: L'article aborde l'intégration de graphiques dans les documents PDF, une exigence courante pour les développeurs utilisant Adobe Acrobat Writer ou des outils de traitement PDF similaires. Il présente la classe Graph dans Aspose.PDF pour Python via .NET, qui facilite cette tâche en permettant l'ajout de différents types de formes aux documents PDF. La classe Graph est un élément de niveau paragraphe qui peut être ajouté à la collection Paragraphs d'une instance Page et prend en charge une collection de formes, notamment Arc, Circle, Curve, Line, Rectangle et Ellipse. Chaque forme sert un objectif unique, comme les Arcs représentant l'adjacence, les Cercles illustrant les portions de données, les Courbes décrivant des lignes connectées, les Lignes affichant des tendances de données continues, les Rectangles résolvant des problèmes spatiaux et les Ellipses formant des formes ovales. L'article fournit également des représentations visuelles de ces formes pour faciliter la compréhension.
---

## Qu'est-ce qu'un Graph

L'ajout de graphiques aux documents PDF est une tâche très courante pour les développeurs travaillant avec Adobe Acrobat Writer ou d'autres applications de traitement PDF. Il existe de nombreux types de graphiques qui peuvent être utilisés dans les applications PDF.
[Aspose.PDF for Python via .NET](/pdf/python-net/) prend également en charge l'ajout de graphiques aux documents PDF. À cette fin, la classe Graph est fournie. Graph est un élément de niveau paragraphe et peut être ajouté à la collection Paragraphs d'une instance Page. Une instance Graph contient une collection de Shapes.

Les types de formes suivants sont pris en charge par la classe [Graph](https://reference.aspose.com/pdf/python-net/aspose.pdf.drawing/graph/) :

- [Arc](/pdf/python-net/add-arc/) - parfois aussi appelé drapeau, est une paire ordonnée de sommets adjacents, mais parfois aussi appelé ligne dirigée.
- [Circle](/pdf/python-net/add-circle/) - affiche les données à l'aide d'un cercle divisé en secteurs. Nous utilisons un graphique circulaire (également appelé diagramme circulaire) pour montrer comment les données représentent des portions d'un tout ou d'un groupe.
- [Curve](/pdf/python-net/add-curve/) - est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en points doubles ordinaires.
- [Line](/pdf/python-net/add-line) - les graphiques en ligne sont utilisés pour afficher des données continues et peuvent être utiles pour prédire des événements futurs lorsqu'ils montrent des tendances au fil du temps.
- [Rectangle](/pdf/python-net/add-rectangle/) - est l'une des nombreuses formes fondamentales que l'on retrouve dans les graphiques, elle peut être très utile pour vous aider à résoudre un problème.
- [Ellipse](/pdf/python-net/add-ellipse/) - est un ensemble de points sur un plan, créant une forme ovale et courbée.

Les détails ci-dessus sont également illustrés dans les figures ci-dessous :

![Figures dans les graphiques](graphs.png)


