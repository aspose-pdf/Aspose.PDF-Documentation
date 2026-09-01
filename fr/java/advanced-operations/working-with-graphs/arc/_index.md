---
title: Ajouter des formes d'arc au PDF en Java
linktitle: Ajouter un arc
type: docs
weight: 10
url: /java/add-arc/
description: Apprenez à dessiner et à remplir des formes d'arc dans des fichiers PDF en Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Dessinez des formes d'arc dans des fichiers PDF à l'aide de Java
Abstract: Cet article montre comment ajouter des formes d'arc aux documents PDF à l'aide d'Aspose.PDF pour Java. Il couvre le dessin de plusieurs arcs décrits avec différentes couleurs et la création d'un segment d'arc rempli en combinant un arc avec une ligne de fermeture.
---
Aspose.PDF pour Java utilise `Graph` avec des objets de forme tels que `Arc` et `Line` pour restituer des graphiques vectoriels.


## 
Ajouter des contours d'arc


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.
1. Créez la forme [Arc] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) et configurez sa géométrie.

1. 
Ajoutez le [Arc] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Définissez les propriétés de forme requises par l'exemple, notamment [Couleur] (https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).


```java
public static void addArc(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc1);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```


L'exemple complet ajoute trois arcs avec des rayons, des angles et des couleurs différents au même graphique.

## Ajouter un segment d'arc rempli


1. 
Créez un nouveau [Document] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

1. 
Ajoutez une [Page] (https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) au document.

1. 
Créez un conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) et ajoutez-le à la page.

1. 
Créez la forme [Ligne] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) et configurez ses coordonnées.
1. Créez la forme [Arc] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) et configurez sa géométrie.

1. 
Ajoutez la [Ligne] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) et l'[Arc] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) au conteneur [Graph] (https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).

1. 
Enregistrez le PDF de sortie [Document] (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

```java
public static void addArcFilled(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();
        Graph graph = new Graph(400.0, 400.0);
        graph.setBorder(new BorderInfo(BorderSide.All, Color.getGreen()));

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(arc);

        Line line = new Line(new float[]{195, 100, 100, 100, 100, 195});
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().addItem(line);

        page.getParagraphs().add(graph);
        document.save(outputFile.toString());
    }
}
```
