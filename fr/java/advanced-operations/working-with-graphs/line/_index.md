---
title: Ajouter des formes de lignes au PDF en Java
linktitle: Ajouter une ligne
type: docs
weight: 40
url: /java/add-line/
description: Apprenez à dessiner des formes de lignes et des lignes stylisées dans des fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessinez des formes de lignes dans des fichiers PDF à l'aide de Java
Abstract: Cet article montre comment ajouter des formes de lignes aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création de lignes à partir de tableaux de coordonnées, l'application d'un style et d'une couleur en pointillés et le dessin de lignes sur toute la page.
---
## Ajouter une ligne pointillée


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Ligne] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) et configurez ses coordonnées.
1. Ajoutez la [Ligne] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addLine(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(100.0, 400.0);
        page.getParagraphs().add(graph);

        Line line = new Line(new float[]{100, 100, 200, 100});
        line.getGraphInfo().setDashArray(new int[]{0, 1, 0});
        line.getGraphInfo().setDashPhase(1);
        graph.getShapes().addItem(line);

        document.save(outputFile.toString());
    }
}
```

## 
Ajouter une ligne pointillée ou pointillée colorée



`addDottedDashedLine` utilise les mêmes coordonnées et paramètres de tiret, mais applique également `Color.getRed()`.


## 
Tracez des lignes sur la page

1. Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Ligne] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) et configurez ses coordonnées.

1. 
Ajoutez la [Ligne] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void drawLineAcrossPage(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        Graph graph = new Graph(page.getPageInfo().getWidth(), page.getPageInfo().getHeight());
        Line line = new Line(new float[]{
                (float) page.getRect().getLLX(),
                0,
                (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY()
        });
        graph.getShapes().addItem(line);
        page.getParagraphs().add(graph);

        document.save(outputFile.toString());
    }
}
```
