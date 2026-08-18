---
title: Anotações de forma via Java
linktitle: Anotações de forma
type: docs
weight: 40
url: /java/pdfannotationeditor-class/shape-annotations/
description: Aprenda como adicionar, inspecionar e excluir anotações quadradas, circulares, poligonais e polilinhas em documentos PDF usando Java.
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: Trabalhe com anotações geométricas de PDF em Java
Abstract: Este artigo explica como criar, inspecionar e remover anotações geométricas em documentos PDF usando Java. Abrange anotações de quadrado, círculo, polígono e polilinha com configuração de cor, opacidade, pop-up e ponto.
---
## Adicionar anotações de forma

1. Abra o PDF de entrada e escolha a página e o retângulo que conterá a anotação da forma.
2. Crie a anotação de forma necessária e defina seu título, cores, opacidade e pontos quando necessário.
3. Adicione a anotação à página e salve o PDF modificado.

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
