---
title: Ajouter un objet Courbe au fichier PDF
linktitle: Ajouter Courbe
type: docs
weight: 30
url: fr/java/add-curve/
description: Cet article explique comment créer un objet courbe dans votre PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Courbe

Un graphe [Courbe](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) est une union connectée de lignes projectives, chaque ligne rencontrant trois autres en points doubles ordinaires.

Aspose.PDF pour Java montre comment utiliser les courbes de Bézier dans vos graphes. Les courbes de Bézier sont largement utilisées en infographie pour modéliser des courbes lisses. La courbe est entièrement contenue dans l'enveloppe convexe de ses points de contrôle, les points peuvent être affichés graphiquement et utilisés pour manipuler intuitivement la courbe. L'ensemble de la courbe est contenu dans le quadrilatère dont les coins sont les quatre points donnés (leur enveloppe convexe).

Dans cet article, nous allons examiner simplement les courbes graphiques et les courbes remplies que vous pouvez créer dans votre document PDF.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Créez un [objet de dessin](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) avec des dimensions spécifiques.

1. Définissez une [Bordure](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) pour l'objet de dessin.

1. Ajoutez l'objet [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) à la collection de paragraphes de la page.

1. Enregistrez votre fichier PDF

```java
    public static void ExampleCurve() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet de dessin avec des dimensions spécifiques
        Graph graph = new Graph(400, 200);
        // Définir la bordure pour l'objet de dessin
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


La photo suivante montre le résultat exécuté avec notre extrait de code :

![Courbe Dessinée](drawing_curve.png)

## Créer un Objet Courbe Rempli

Cet exemple montre comment ajouter un objet Courbe qui est rempli de couleur.

```java
    public static void ExampleFilledCurve() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet Dessin avec certaines dimensions
        Graph graph = new Graph(400, 200);
        // Définir la bordure pour l'objet Dessin
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Regardez le résultat de l'ajout d'une Courbe remplie :

![Filled Curve](filled_curve.png)