---
title: Adicionar Formas de Arco ao PDF em Java
linktitle: Adicionar Arco
type: docs
weight: 10
url: /pt/java/add-arc/
description: Aprenda como desenhar e preencher formas de arco em arquivos PDF em Java.
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Desenhar formas de arco em arquivos PDF usando Java
Abstract: Este artigo mostra como adicionar formas de arco a documentos PDF usando Aspose.PDF for Java. Ele abrange o desenho de vários arcos contornados com cores diferentes e a criação de um segmento de arco preenchido ao combinar um arco com uma linha de fechamento.
---
Aspose.PDF for Java usa `Graph` juntamente com objetos de forma como `Arc` e `Line` para renderizar gráficos vetoriais.

## Adicionar contornos de arco

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Criar um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicioná-lo à página.
1. Criar o [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) forma e configure sua geometria.
1. Adicionar o [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Defina as propriedades da forma exigidas pelo exemplo, incluindo [Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/color/).
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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

O exemplo completo adiciona três arcos com diferentes raios, ângulos e cores ao mesmo gráfico.

## Adicionar um segmento de arco preenchido

1. Criar um novo PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).
1. Adicionar um [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) ao documento.
1. Criar um [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner e adicioná-lo à página.
1. Criar o [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) forma e configure suas coordenadas.
1. Criar o [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) forma e configure sua geometria.
1. Adicionar o [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/line/) e [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/arc/) para o [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/graph/) contêiner.
1. Salve o PDF de saída [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/).

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
