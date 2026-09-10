---
title: Ajouter des formes de cercle au PDF en Java
linktitle: Ajouter un cercle
type: docs
weight: 20
url: /java/add-circle/
description: Apprenez à dessiner et remplir des formes de cercle dans des fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessinez des formes de cercle dans des fichiers PDF à l'aide de Java
Abstract: Cet article montre comment ajouter des formes de cercle aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le dessin des contours des cercles, le remplissage des cercles avec de la couleur et le placement du texte à l'intérieur d'une forme de cercle.
---
## Ajouter un contour de cercle


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Cercle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) et configurez sa géométrie.
1. Ajoutez le [Cercle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Définissez les propriétés de forme requises par l'exemple, notamment [Couleur] (https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addCircle(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```

## 
Ajouter un cercle rempli de texte


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Cercle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) et configurez sa géométrie.

1. 
Ajoutez le [Cercle] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Définissez les propriétés de forme requises par l'exemple, notamment [Color] (https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) et [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCircleFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Circle circle = new Circle(100, 100, 40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());
        circle.getGraphInfo().setFillColor(Color.getGreen());
        circle.setText(new TextFragment("Circle"));
        graph.getShapes().addItem(circle);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
