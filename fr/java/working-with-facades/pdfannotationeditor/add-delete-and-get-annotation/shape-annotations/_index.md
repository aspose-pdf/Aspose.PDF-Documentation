---
title: Annotations de forme via Java
linktitle: Annotations de forme
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: Découvrez comment ajouter, inspecter et supprimer des annotations de carrés, de cercles, de polygones et de polylignes dans des documents PDF à l'aide de Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Travailler avec des annotations PDF géométriques en Java
Abstract: Cet article explique comment créer, inspecter et supprimer des annotations géométriques dans des documents PDF à l'aide de Java. Il couvre les annotations de carrés, de cercles, de polygones et de polylignes avec la configuration de la couleur, de l'opacité, des fenêtres contextuelles et des points.
---
## Ajouter des annotations de forme


1. 
Ouvrez le PDF d'entrée et choisissez la page et le rectangle qui contiendront l'annotation de forme.

2. 
Créez l'annotation de forme requise, puis définissez son titre, ses couleurs, son opacité et ses points si nécessaire.

3. 
Ajoutez l'annotation à la page et enregistrez le PDF modifié.

```java
public static void squareAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SquareAnnotation squareAnnotation = new SquareAnnotation(
                document.getPages().get_Item(1), new Rectangle(60, 600, 250, 450, true));
        squareAnnotation.setTitle("John Smith");
        squareAnnotation.setColor(Color.getBlue());
        squareAnnotation.setInteriorColor(Color.getBlueViolet());
        squareAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(squareAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void polygonAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        PolygonAnnotation polygonAnnotation = new PolygonAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(200, 300, 400, 400, true),
                new Point[]{
                        new Point(200, 300),
                        new Point(220, 300),
                        new Point(250, 330),
                        new Point(300, 304),
                        new Point(300, 400)
                });
        polygonAnnotation.setTitle("John Smith");
        polygonAnnotation.setColor(Color.getBlue());
        polygonAnnotation.setInteriorColor(Color.getBlueViolet());
        polygonAnnotation.setOpacity(0.25);

        document.getPages().get_Item(1).getAnnotations().add(polygonAnnotation);
        document.save(outputFile.toString());
    }
}
```
