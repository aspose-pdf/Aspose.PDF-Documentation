---
title: Ajouter un objet Ellipse au fichier PDF
linktitle: Ajouter Ellipse
type: docs
weight: 60
url: /java/add-ellipse/
description: Cet article explique comment créer un objet Ellipse dans votre PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Ellipse

Aspose.PDF pour Java prend en charge l'ajout d'objets [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) aux documents PDF. Il offre également la fonctionnalité de remplir l'objet ellipse avec une certaine couleur.

```java
public static void ExampleEllipse() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet Drawing avec certaines dimensions
        Graph graph = new Graph(400, 400);
        // Définir la bordure pour l'objet Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(50, 50, 18, 300);
        ellipse2.getGraphInfo().setColor(Color.getDarkRed());

        graph.getShapes().add(ellipse2);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");
    }
```


![Ajouter Ellipse](ellipse.png)

## Créer un Objet Ellipse Rempli

Le fragment de code suivant montre comment ajouter un objet [Ellipse](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Ellipse) qui est rempli de couleur.

```java
    public static void ExampleFilledEllipse() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet de dessin avec certaines dimensions
        Graph graph = new Graph(400, 400);
        // Définir une bordure pour l'objet de dessin
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(ellipse1);

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());
        graph.getShapes().add(ellipse2);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingEllipse_out.pdf");

    }
```


![Ellipse Rempli](fill_ellipse.png)

## Ajouter du texte à l'intérieur de l'ellipse

Aspose.PDF pour Java prend en charge l'ajout de texte à l'intérieur de l'objet Graph. La propriété Text de l'objet Graph offre la possibilité de définir le texte de l'objet Graph. Le code suivant montre comment ajouter du texte à l'intérieur d'un objet Rectangle.

```java

public static void ExampleEllipseWithText() {
        // Créer une instance de Document
        Document pdfDocument = new Document();
        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Créer un objet de dessin avec certaines dimensions
        Graph graph = new Graph(400, 400);
        // Définir la bordure pour l'objet de dessin
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().add(ellipse1);
        

        Ellipse ellipse2 = new Ellipse(200, 150, 180, 120);
        ellipse2.getGraphInfo().setFillColor(Color.getDarkRed());        
        ellipse2.setText(textFragment);
        graph.getShapes().add(ellipse2);

        // Ajouter l'objet Graph à la collection de paragraphes de la page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "DrawingEllipseText_out.pdf");

    }
 ```


Je suis désolé, mais je suis incapable de traduire le texte à partir d'une image. Toutefois, si vous pouviez fournir le texte sous forme écrite, je serais heureux de vous aider à le traduire en français tout en respectant vos consignes concernant la mise en forme markdown et les paires clé-valeur.