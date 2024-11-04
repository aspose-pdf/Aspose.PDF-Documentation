---
title: Adicionar Objeto de Círculo ao Arquivo PDF
linktitle: Adicionar Círculo
type: docs
weight: 20
url: /java/add-circle/
description: Este artigo explica como criar um objeto de círculo no seu PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto de Círculo

Como gráficos de barras, gráficos de círculos podem ser usados para exibir dados em várias categorias separadas. No entanto, ao contrário dos gráficos de barras, os gráficos de círculos só podem ser usados quando você tem dados para todas as categorias que compõem o todo. Então, vamos dar uma olhada em como adicionar um objeto [Círculo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Circle) com Aspose.PDF para Java.

Siga os passos abaixo:

1. Crie uma instância de [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)

1. Crie um [Objeto de Desenho](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) com certas dimensões

1. Defina [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) para o objeto Drawing

1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) à coleção de parágrafos da página

1. Salve nosso arquivo PDF

```java
public static void ExampleCircle() {
        // Crie uma instância de Document
        Document pdfDocument = new Document();
        // Adicione uma página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Crie um objeto Drawing com certas dimensões
        Graph graph = new Graph(400, 200);
        // Defina a borda para o objeto Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);

        circle.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(circle);

        // Adicione o objeto Graph à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salve o arquivo PDF
        pdfDocument.save(_dataDir + "DrawingCircle1_out.pdf");
    }
```


Nosso círculo desenhado ficará assim:

![Desenhando Círculo](drawing_circle.png)

## Criar Objeto de Círculo Preenchido

Este exemplo mostra como adicionar um objeto Círculo que é preenchido com cor.

```java

    public static void ExampleFilledCircle() {
        // Cria instância do Documento
        Document pdfDocument = new Document();
        // Adiciona página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Cria objeto de Desenho com certas dimensões
        Graph graph = new Graph(400, 200);
        // Define a borda para o objeto de Desenho
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Circle circle = new Circle(100,100,40);
        circle.getGraphInfo().setColor(Color.getGreenYellow());       
        circle.getGraphInfo().setFillColor(Color.getGreenYellow());

        graph.getShapes().add(circle);

        // Adiciona objeto Graph à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salva o arquivo PDF
        pdfDocument.save(_dataDir + "DrawingCircle2_out.pdf");
    }
```


Let's see the result of adding a filled Circle:

![Círculo Preenchido](filled_circle.png)