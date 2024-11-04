---
title: Travailler avec des Graphiques dans PDF
linktitle: Travailler avec des Graphiques
type: docs
weight: 70
url: /cpp/graphs/
description: Cet article explique ce qu'est un Graphique, comment créer un objet rectangle rempli, comment ajouter du texte à l'intérieur d'un objet graphique, comment ajouter un objet ligne au PDF, etc.
lastmod: "2021-12-18"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Qu'est-ce qu'un Graphique

Ajouter des graphiques aux documents PDF est une tâche très courante pour les développeurs lorsqu'ils travaillent avec Adobe Acrobat Writer ou d'autres applications de traitement de PDF. Il existe de nombreux types de graphiques qui peuvent être utilisés dans les applications PDF.
[Aspose.PDF for C++](/pdf/cpp/) prend également en charge l'ajout de graphiques aux documents PDF. À cet effet, la classe Graph est fournie. Graph est un élément de niveau paragraphe et il peut être ajouté à la collection Paragraphs dans une instance de Page. Une instance de Graph contient une collection de Formes.

Les types de formes suivants sont pris en charge par la classe [Graph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.drawing.graph) :


- [Arc](/pdf/cpp/add-arc/) - parfois aussi appelé un drapeau est une paire ordonnée de sommets adjacents, mais parfois aussi appelé une ligne dirigée.
- [Cercle](/pdf/cpp/add-circle/) - affiche des données à l'aide d'un cercle divisé en secteurs. Nous utilisons un graphique en cercle (également appelé graphique circulaire) pour montrer comment les données représentent des portions d'un tout ou d'un groupe.
- [Courbe](/pdf/cpp/add-curve/) - est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en des points doubles ordinaires.
- [Ligne](/pdf/cpp/add-line) - les graphiques en ligne sont utilisés pour afficher des données continues et peuvent être utiles pour prédire des événements futurs lorsqu'ils montrent des tendances au fil du temps.
- [Rectangle](/pdf/cpp/add-rectangle/) - est l'une des nombreuses formes fondamentales que vous verrez dans les graphiques, il peut être très utile pour vous aider à résoudre un problème.
- [Ellipse](/pdf/cpp/add-ellipse/) - est un ensemble de points sur un plan, créant une forme ovale et courbée. 

Les détails ci-dessus sont également représentés dans les figures ci-dessous :

![Figures dans les Graphiques](graph.png)