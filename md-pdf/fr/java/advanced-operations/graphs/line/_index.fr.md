---
title: Ajouter un objet Ligne au fichier PDF
linktitle: Ajouter Ligne
type: docs
weight: 40
url: /java/add-line/
description: Cet article explique comment créer un objet ligne dans votre PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Ligne

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graph, ligne, rectangle etc.) aux documents PDF. Vous avez également la possibilité d'ajouter un objet [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line) où vous pouvez également spécifier le modèle de tiret, la couleur et d'autres formats pour l'élément Ligne.

Suivez les étapes ci-dessous :

1. Créez une instance de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Ajoutez une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à la collection de pages du fichier PDF.

1. Créez une instance de [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph).

1. Ajoutez un objet Graph à la collection de paragraphes de l'instance de page.

1. Créez une instance de [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).

1. Définissez la largeur de la ligne.

1. Ajoutez l'objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) à la collection de formes de l'objet Graph.

1. Enregistrez votre fichier PDF.

Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) qui est rempli de couleur.

```java
 public static void ExampleLine() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();
        // Créer une instance de Graph
        Graph graph = new Graph(100, 400);

        // Ajouter l'objet graph à la collection de paragraphes de l'instance de page
        page.getParagraphs().add(graph);

        // Créer une instance de Rectangle
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Ajouter l'objet rectangle à la collection de formes de l'objet Graph
        graph.getShapes().add(line);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Add Line](add_line.png)

## Comment ajouter une ligne pointillée à votre document PDF

```java
public static void ExampleDashedLine() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet de dessin avec certaines dimensions
        Graph canvas = new Graph(100, 400);
        // Ajouter un objet de dessin à la collection de paragraphes de l'instance de page
        page.getParagraphs().add(canvas);

        // Créer un objet Ligne
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Définir la couleur pour l'objet Ligne
        line.getGraphInfo().setColor(Color.getRed());
        // Spécifier le tableau de tirets pour l'objet ligne
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Définir la phase de tirets pour l'instance Ligne
        line.getGraphInfo().setDashPhase(1);
        // Ajouter la ligne à la collection de formes de l'objet de dessin
        canvas.getShapes().add(line);
        // Sauvegarder le document PDF
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


Let's check the result:

![Dashed Line](dash_line.png)

## Tracer une ligne à travers la page

Nous pouvons également utiliser un objet ligne pour dessiner une croix allant du coin inférieur gauche au coin supérieur droit et du coin supérieur gauche au coin inférieur droit.

Veuillez consulter l'extrait de code suivant pour répondre à cette exigence.

```java
    public static void ExampleLineAcrossPage() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();
        // Définir la marge de la page sur tous les côtés à 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // Créer un objet Graph avec une largeur et une hauteur égales aux dimensions de la page
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // Créer le premier objet ligne allant du coin inférieur gauche au coin supérieur droit de la page
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Ajouter la ligne à la collection de formes de l'objet Graph
        graph.getShapes().add(line);
        // Dessiner une ligne du coin supérieur gauche de la page au coin inférieur droit de la page
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Ajouter la ligne à la collection de formes de l'objet Graph
        graph.getShapes().add(line2);
        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![Ligne de dessin](draw_line.png)