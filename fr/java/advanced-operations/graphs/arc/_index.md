---
title: Ajouter un objet Arc au fichier PDF
linktitle: Ajouter Arc
type: docs
weight: 10
url: /fr/java/add-arc/
description: Cet article explique comment créer un objet arc dans votre PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Arc

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Il offre également la possibilité de remplir un objet arc avec une certaine couleur.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Créez un [objet de dessin](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) avec des dimensions spécifiques

1. Définissez la [Bordure](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) pour l'objet de dessin

1. Ajoutez un objet [Graphique](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) à la collection de paragraphes de la page

1. Enregistrez notre fichier PDF

Le code suivant montre comment ajouter un objet [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc).

```java
    public static void ExampleArc() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet Drawing avec certaines dimensions
        Graph graph = new Graph(400, 400);
        // Définir la bordure pour l'objet Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## Créer un Objet Arc Rempli

L'exemple suivant montre comment ajouter un objet Arc qui est rempli avec une couleur et des dimensions spécifiques.

```java
    public static void ExampleFilledArc() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet Drawing avec des dimensions spécifiques
        Graph graph = new Graph(400, 400);
        // Définir une bordure pour l'objet Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Let's see the result of adding a filled Arс:

![Arc rempli](filled_arc.png)