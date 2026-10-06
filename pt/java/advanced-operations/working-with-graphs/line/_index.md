---
title: Adicionar formas de linha ao PDF em Java
linktitle: Adicionar linha
type: docs
weight: 40
url: /pt/java/add-line/
description: Aprenda como desenhar formas de linha e linhas estilizadas em arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de linha em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de linha a documentos PDF usando Aspose.PDF for Java. Ele aborda a criação de linhas a partir de arrays de coordenadas, a aplicação de estilo tracejado e cor, e o desenho de linhas em toda a área da página.
---
## Adicionar uma linha tracejada

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Criar um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicioná-lo à página.
1. Criar o [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) forma e configure suas coordenadas.
1. Adicionar o [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Salvar o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

## Adicionar uma linha pontilhada ou tracejada colorida

`addDottedDashedLine` usa as mesmas coordenadas e configurações de traço, mas também aplica `Color.getRed()`.

## Desenhar linhas na página

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Criar um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicioná-lo à página.
1. Criar o [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) forma e configure suas coordenadas.
1. Adicionar o [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Salvar o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
