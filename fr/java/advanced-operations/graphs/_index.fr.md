---
title: Travailler avec des Graphiques
linktitle: Travailler avec des Graphiques
type: docs
weight: 70
url: /java/graphs/
description: Cet article explique ce qu'est un graphique, comment créer un objet rectangle rempli, comment ajouter du texte à l'intérieur d'un objet graphique, comment ajouter un objet ligne au PDF, etc.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Qu'est-ce qu'un Graphique

Le principal objectif du graphique est de montrer des faits numériques sous forme visuelle afin qu'ils puissent être compris rapidement, facilement et clairement. Ainsi, les graphiques sont des représentations visuelles des données collectées. Les données peuvent également être présentées sous forme de tableau ; cependant, une présentation graphique est plus facile à comprendre. C'est particulièrement vrai lorsqu'il y a une tendance ou une comparaison à montrer.

Ajouter des graphiques aux documents PDF est une tâche très courante pour les développeurs travaillant avec Adobe Acrobat Writer ou d'autres applications de traitement de PDF.
 Il existe de nombreux types de graphiques qui peuvent être utilisés dans les applications PDF. Les opérateurs graphiques utilisés dans les flux de contenu PDF décrivent l'apparence des pages qui doivent être reproduites sur un appareil de sortie raster.

[Aspose.PDF pour Java](/pdf/java/) prend également en charge l'ajout de graphiques aux documents PDF. À cet effet, la classe Graph est fournie. Graph est un élément de niveau paragraphe et peut être ajouté à la collection Paragraphs dans une instance Page. Une instance de Graph contient une collection de Shapes.

Les types de formes suivants sont pris en charge par la classe [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) :

- [Arc](/pdf/java/add-arc/) - parfois également appelé drapeau, est une paire ordonnée de sommets adjacents, mais parfois aussi appelé une ligne dirigée.
- [Cercle](/pdf/java/add-circle/) - affiche des données à l'aide d'un cercle divisé en secteurs. Nous utilisons un graphique circulaire (également appelé diagramme circulaire) pour montrer comment les données représentent des portions d'un tout ou d'un groupe.

- [Courbe](/pdf/java/add-curve/) - est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en des points doubles ordinaires.- [Line](/pdf/java/add-line) - les graphiques en ligne sont utilisés pour afficher des données continues et peuvent être utiles pour prédire des événements futurs lorsqu'ils montrent des tendances au fil du temps.
- [Rectangle](/pdf/java/add-rectangle/) - est l'une des nombreuses formes fondamentales que vous verrez dans les graphiques, elle peut être très utile pour vous aider à résoudre un problème.
- [Ellipse](/pdf/java/add-ellipse/) - est un ensemble de points sur un plan, créant une forme ovale et courbée.

Les détails ci-dessus sont également illustrés dans les figures ci-dessous :

![Figures in Graphs](graph.png)