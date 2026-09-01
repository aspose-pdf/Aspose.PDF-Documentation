---
title: Ajouter des formes de courbe au PDF en Java
linktitle: Ajouter une courbe
type: docs
weight: 30
url: /java/add-curve/
description: Apprenez à dessiner et à remplir des formes de courbes dans des fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessinez des formes de courbes dans des fichiers PDF à l'aide de Java
Abstract: Cet article montre comment ajouter des formes de courbe aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre la création d'une courbe à partir de tableaux de coordonnées et l'application d'une couleur de trait ou d'une couleur de remplissage à l'intérieur d'un conteneur graphique.
---
Les courbes dans Aspose.PDF pour Java sont définies par un tableau de coordonnées flottantes transmis à `Curve`.


## 
Ajouter un contour de courbe


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.
1. Créez la forme [Courbe] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) et configurez ses points de contrôle.

1. 
Ajoutez la [Courbe] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/curve/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Définissez les propriétés de forme requises par l'exemple, notamment [Couleur] (https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addCurve(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 200.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Curve curve1 = new Curve(new float[]{10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(curve1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
