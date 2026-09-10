---
title: Ajouter des formes d'ellipse au PDF en Java
linktitle: Ajouter une ellipse
type: docs
weight: 60
url: /java/add-ellipse/
description: Apprenez à dessiner, remplir et étiqueter des formes d'ellipse dans des fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessinez des formes d'ellipse dans des fichiers PDF à l'aide de Java
Abstract: Cet article montre comment ajouter des formes d'ellipse aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre les ellipses décrites, les ellipses remplies et le placement de fragments de texte à l'intérieur de formes d'ellipse.
---
## Ajouter des contours d'ellipse


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Ellipse] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) et configurez sa géométrie.
1. Ajoutez l'[Ellipse] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Définissez les propriétés de forme requises par l'exemple, notamment [Color] (https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) et [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Ellipse ellipse1 = new Ellipse(150, 100, 120, 60);
        ellipse1.getGraphInfo().setColor(Color.getGreenYellow());
        ellipse1.setText(new TextFragment("Ellipse"));
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```


L’exemple complet ajoute deux ellipses de contour différentes au même graphique.


## 
Ajouter des ellipses remplies

`createEllipseFilled` remplit deux ellipses avec `Color.getGreenYellow()` et `Color.getDarkRed()`.


## 
Ajouter du texte à l'intérieur des ellipses


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un [TextFragment] (https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) et définissez les options de formatage de texte requises.
1. Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Ellipse] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) et configurez sa géométrie.

1. 
Ajoutez l'[Ellipse] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/ellipse/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addTextInsideEllipse(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        TextFragment textFragment = new TextFragment("Ellipse");
        textFragment.getTextState().setFont(FontRepository.findFont("Helvetica"));
        textFragment.getTextState().setFontSize(24);

        Ellipse ellipse1 = new Ellipse(100, 100, 120, 180);
        ellipse1.getGraphInfo().setFillColor(Color.getGreenYellow());
        ellipse1.setText(textFragment);
        graph.getShapes().addItem(ellipse1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
