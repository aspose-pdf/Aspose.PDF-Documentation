---
title: Adicione formas de arco ao PDF em Java
linktitle: Adicionar arco
type: docs
weight: 10
url: /java/add-arc/
description: Aprenda como desenhar e preencher formas de arco em arquivos PDF em Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhe formas de arco em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de arco a documentos PDF usando Aspose.PDF para Java. Abrange o desenho de vários arcos delineados com cores diferentes e a criação de um segmento de arco preenchido combinando um arco com uma linha de fechamento.
---
Aspose.PDF para Java usa `Graph` junto com objetos de forma como `Arc` e `Line` para renderizar gráficos vetoriais.

## Adicionar contornos de arco

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) e configure sua geometria.
1. Adicione o [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) ao contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Defina as propriedades de forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

O exemplo completo adiciona três arcos com raios, ângulos e cores diferentes ao mesmo gráfico.

## Adicione um segmento de arco preenchido

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicione uma [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Crie um contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) e adicione-o à página.
1. Crie a forma [Linha](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) e configure suas coordenadas.
1. Crie a forma [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) e configure sua geometria.
1. Adicione [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) e [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) ao contêiner [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/).
1. Salve o PDF de saída [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
