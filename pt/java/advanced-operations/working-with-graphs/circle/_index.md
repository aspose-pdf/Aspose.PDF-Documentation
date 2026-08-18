---
title: Adicione formas circulares ao PDF em Java
linktitle: Adicionar círculo
type: docs
weight: 20
url: /java/add-circle/
description: Aprenda como desenhar e preencher formas circulares em arquivos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas circulares em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas circulares a documentos PDF usando Aspose.PDF para Java. Abrange desenhar contornos de círculos, preencher círculos com cores e colocar texto dentro de um círculo.
---
## Adicione um contorno circular

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) e configure sua geometria.
1. Adicione o [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) ao contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Adicione um círculo preenchido com texto

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) e configure sua geometria.
1. Adicione o [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/circle/) ao contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/) e [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/).
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
