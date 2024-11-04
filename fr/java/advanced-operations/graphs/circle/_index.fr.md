---
title: Ajouter un objet cercle au fichier PDF
linktitle: Ajouter un cercle
type: docs
weight: 20
url: /java/add-circle/
description: Cet article explique comment créer un objet cercle dans votre PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet cercle

Comme les graphiques à barres, les graphiques en cercle peuvent être utilisés pour afficher des données dans un certain nombre de catégories distinctes. Contrairement aux graphiques à barres, cependant, les graphiques en cercle ne peuvent être utilisés que lorsque vous avez des données pour toutes les catégories qui composent l'ensemble. Voyons donc comment ajouter un objet [Cercle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) avec Aspose.PDF pour Java.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Créez un [objet de dessin](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) avec certaines dimensions

1. Définir [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) pour l'objet Drawing

1. Ajouter un objet [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) à la collection de paragraphes de la page

1. Enregistrer notre fichier PDF

```java
public static void ExampleCircle() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet Drawing avec certaines dimensions
        Graph graph = new Graph(400, 200);
        // Définir la bordure pour l'objet Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // Ajouter un objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


Notre cercle dessiné ressemblera à ceci :

![Dessiner un cercle](drawing_circle.png)

## Créer un objet cercle rempli

Cet exemple montre comment ajouter un objet cercle rempli de couleur.

```java

    public static void ExampleFilledCircle() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet Drawing avec certaines dimensions
        Graph graph = new Graph(400, 200);
        // Définir la bordure pour l'objet Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

Voyons le résultat de l'ajout d'un cercle rempli :

![Filled Circle](filled_circle.png)