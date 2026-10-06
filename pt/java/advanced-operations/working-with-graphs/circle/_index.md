---
title: Adicionar formas de círculo ao PDF em Java
linktitle: Adicionar círculo
type: docs
weight: 20
url: /pt/java/add-circle/
description: Aprenda como desenhar e preencher formas de círculo em arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de círculo em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de círculo a documentos PDF usando Aspose.PDF for Java. Ele abrange o desenho de contornos de círculos, o preenchimento de círculos com cor e a inserção de texto dentro de uma forma de círculo.
---
## Adicionar um contorno de círculo

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicione-o à página.
1. Crie o [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) forma e configure sua geometria.
1. Adicione o [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Adicionar um círculo preenchido com texto

1. Crie um novo documento PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicione-o à página.
1. Crie o [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) forma e configure sua geometria.
1. Adicione o [Circle](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) e [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
