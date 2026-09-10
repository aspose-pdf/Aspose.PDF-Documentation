---
title: Ajouter des formes rectangulaires au PDF en Java
linktitle: Ajouter un rectangle
type: docs
weight: 50
url: /java/add-rectangle/
description: Apprenez à dessiner et à remplir des formes rectangulaires dans des fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessinez des formes rectangulaires dans des fichiers PDF à l'aide de Java
Abstract: Cet article montre comment ajouter des formes rectangulaires aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre les rectangles décrits, les remplissages unis, les remplissages dégradés, la transparence alpha et le contrôle de l'ordre z pour les formes qui se chevauchent.
---
## Ajouter un contour de rectangle


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) et configurez sa géométrie.
1. Ajoutez le [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 300.0);
        page.getParagraphs().add(graph);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        Rectangle rectangle = new Rectangle(20, 20, 350, 250);
        graph.getShapes().addItem(rectangle);

        document.save(outputFile.toString());
    }
}
```

## 
Remplissez un rectangle avec une couleur unie ou dégradée



Les exemples de rectangles incluent :


- 
`createRectangleFilled` pour un remplissage solide avec `Color.getRed()`
- `addDrawingWithGradientFill` pour un remplissage `GradientAxialShading`


## 
Utiliser la transparence alpha



`createRectangleWithAlphaColorChannel` applique des couleurs translucides avec `Color.fromArgb(...)` afin que les rectangles qui se chevauchent restent visibles.


## 
Contrôler l'ordre z des rectangles


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Définissez la taille de [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) requise.

1. 
Ajoutez les formes [Rectangle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/rectangle/) configurées à la page cible avec l'ordre z requis.

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void controlZOrderOfRectangle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.setPageSize(375, 300);
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setTop(0);

        addRectangleToPage(page, 50, 40, 60, 40, Color.getRed(), 2);
        addRectangleToPage(page, 20, 20, 30, 30, Color.getBlue(), 1);
        addRectangleToPage(page, 40, 40, 60, 30, Color.getGreen(), 0);

        document.save(outputFile.toString());
    }
}
```
