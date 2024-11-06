---
title: Ajouter un objet Rectangle au fichier PDF
linktitle: Ajouter Rectangle
type: docs
weight: 50
url: fr/java/add-rectangle/
description: Cet article explique comment créer un objet Rectangle dans votre PDF en utilisant Aspose.PDF pour Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ajouter un objet Rectangle

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple graphique, ligne, rectangle, etc.) aux documents PDF. Vous avez également la possibilité d'ajouter un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) où vous pouvez également remplir l'objet rectangle avec une certaine couleur, contrôler l'ordre de superposition, ajouter un remplissage de couleur dégradé, etc.

Tout d'abord, examinons la possibilité de créer un objet Rectangle.

Suivez les étapes ci-dessous :

1. Créez un nouveau [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) PDF

1. Ajoutez une [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à la collection de pages du fichier PDF

1. Ajouter [Fragment de texte](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) à la collection de paragraphes de l'instance de page

1. Créer une instance de [Graphique](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)

1. Définir la bordure pour l'[Objet de dessin](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. Créer une instance de Rectangle

1. Ajouter l'objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) à la collection de formes de l'objet Graphique

1. Ajouter l'objet graphique à la collection de paragraphes de l'instance de page

1. Ajouter [Fragment de texte](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) à la collection de paragraphes de l'instance de page

1. Et enregistrer votre fichier PDF

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // Créer un nouveau document PDF
        Document pdfDocument = new Document();

        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();

        // Ajouter un fragment de texte à la collection de paragraphes de l'instance de page
        page.getParagraphs().add(new TextFragment("Texte avant l'objet Graphique"));

        // Créer une instance de Graphique
        Graph graph = new Graph(400, 200);

        // Définir la bordure pour l'objet de dessin
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // Créer une instance de Rectangle
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // Ajouter l'objet rectangle à la collection de formes de l'objet Graphique
        graph.getShapes().add(rect);

        // Ajouter l'objet graphique à la collection de paragraphes de l'instance de page
        page.getParagraphs().add(graph);

        // Ajouter un fragment de texte à la collection de paragraphes de l'instance de page
        page.getParagraphs().add(new TextFragment("Texte après l'objet Graphique"));

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Create Rectangle](create_rectangle.png)

## Créer un Objet Rectangle Rempli

Aspose.PDF pour Java offre également la possibilité de remplir un objet rectangle avec une certaine couleur.

L'extrait de code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) qui est rempli de couleur.

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // Ajouter une page à la collection de pages du fichier PDF
        Page page = pdfDocument.getPages().add();
        // Créer une instance de Graph
        Graph graph = new Graph(100, 400);

        // Ajouter un objet graphique à la collection de paragraphes de l'instance de page
        page.getParagraphs().add(graph);

        // Créer une instance de Rectangle
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // Spécifier la couleur de remplissage pour l'objet Graph
        rect.getGraphInfo().setFillColor(Color.getRed());

        // Ajouter un objet rectangle à la collection de formes de l'objet Graph
        graph.getShapes().add(rect);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


Regardez le résultat du rectangle rempli d'une couleur unie :

![Rectangle Rempli](fill_rectangle.png)

## Ajouter un dessin avec remplissage en dégradé

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajout d'objets graphiques aux documents PDF et il est parfois nécessaire de remplir les objets graphiques avec une couleur en dégradé. Pour remplir les objets graphiques avec une couleur en dégradé, nous devons définir setPatternColorSpace avec un objet gradientAxialShading comme suit.

Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) qui est rempli avec une couleur en dégradé.

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // Spécifier la couleur de remplissage en dégradé pour l'objet Graph et remplir
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## Créer un Rectangle avec un canal de couleur Alpha

Aspose.PDF pour Java prend en charge le remplissage d'un objet rectangle avec une certaine couleur. Un objet rectangle peut également avoir un canal de couleur Alpha pour donner une apparence transparente. Le code suivant montre comment ajouter un objet [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) avec un canal de couleur Alpha.

Les pixels de l'image peuvent stocker des informations sur leur opacité ainsi que sur la valeur de couleur. Cela permet de créer des images avec des zones transparentes ou semi-transparentes.

Au lieu de rendre une couleur transparente, chaque pixel stocke des informations sur son opacité. Ces données d'opacité sont appelées canal alpha et sont généralement stockées après les canaux de couleur du pixel.

Dans notre extrait de code, nous avons utilisé la méthode [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) de [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color).
 Nous devons spécifier des valeurs où les 3 premiers sont des composants de couleur, spécifiés dans la plage de 0 à 255, et le dernier est le niveau d'opacité (canal alpha), spécifié par des nombres fractionnaires de 0 à 1.

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Créer une instance de Graph
        Graph graph = new Graph(100, 400);

        // Créer un objet rectangle avec des dimensions spécifiques
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // Ajouter l'objet rectangle à la collection de formes de l'instance Graph
        graph.getShapes().add(rect1);

        // Créer un second objet rectangle
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // Ajouter l'instance de graph à la collection de paragraphes de l'objet page
        page.getParagraphs().add(graph);

        // Enregistrer le fichier PDF
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Contrôler l'ordre Z du rectangle

Aspose.PDF pour Java prend en charge la fonctionnalité d'ajouter des objets graphiques (par exemple, graphique, ligne, rectangle, etc.) aux documents PDF. Lors de l'ajout de plusieurs instances du même objet dans un fichier PDF, nous pouvons contrôler leur rendu en spécifiant l'ordre Z. L'ordre Z est également utilisé lorsque nous devons rendre les objets les uns sur les autres.

Le code suivant montre les étapes pour rendre des objets [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) les uns sur les autres.

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Créer un nouveau rectangle avec la couleur rouge, l'ordre Z à 0 et certaines dimensions
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // Créer un nouveau rectangle avec la couleur bleue, l'ordre Z à 0 et certaines dimensions
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // Créer un nouveau rectangle avec la couleur verte, l'ordre Z à 0 et certaines dimensions
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // Enregistrer le fichier PDF résultant
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![Contrôler l'ordre Z](control.png)