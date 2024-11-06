---
title: Adicionar Objeto Arco ao Arquivo PDF
linktitle: Adicionar Arco
type: docs
weight: 10
url: pt/java/add-arc/
description: Este artigo explica como criar um objeto arco no seu PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto Arco

Aspose.PDF para Java suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Ele também oferece a funcionalidade de preencher o objeto arco com uma certa cor.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Crie um [Objeto de Desenho](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) com certas dimensões

1. Defina a [Borda](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) para o Objeto de Desenho

1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) à coleção de parágrafos da página

1. Salve nosso arquivo PDF


O trecho de código a seguir mostra como adicionar um objeto [Arc](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Arc).

```java
    public static void ExampleArc() {
        // Criar instância do Documento
        Document pdfDocument = new Document();
        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Criar objeto de Desenho com certas dimensões
        Graph graph = new Graph(400, 400);
        // Definir borda para o objeto de Desenho
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc1 = new Arc(100, 100, 95, 0, 90);
        arc1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(arc1);

        Arc arc2 = new Arc(100, 100, 90, 70, 180);
        arc2.getGraphInfo().setColor(Color.getDarkBlue());
        graph.getShapes().add(arc2);

        Arc arc3 = new Arc(100, 100, 85, 120, 210);
        arc3.getGraphInfo().setColor(Color.getRed());
        graph.getShapes().add(arc3);

        // Adicionar objeto Graph à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


## Criar Objeto de Arco Preenchido

O próximo exemplo mostra como adicionar um objeto Arco que é preenchido com cor e certas dimensões.

```java
    public static void ExampleFilledArc() {
        // Criar uma instância de Documento
        Document pdfDocument = new Document();
        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Criar objeto de Desenho com certas dimensões
        Graph graph = new Graph(400, 400);
        // Definir borda para o objeto de Desenho
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Arc arc = new Arc(100, 100, 95, 0, 90);
        arc.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(arc);

        Line line = new Line(new float[] { 195, 100, 100, 100, 100, 195 });
        line.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(line);

        // Adicionar objeto Gráfico à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "DrawingArc_out.pdf");

    }
```


Vamos ver o resultado de adicionar um Arco preenchido:

![Arco Preenchido](filled_arc.png)