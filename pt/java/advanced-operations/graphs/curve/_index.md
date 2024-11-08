---
title: Adicionar Objeto de Curva ao Arquivo PDF
linktitle: Adicionar Curva
type: docs
weight: 30
url: /pt/java/add-curve/
description: Este artigo explica como criar um objeto de curva no seu PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto de Curva

Um gráfico [Curva](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Curve) é uma união conectada de linhas projetivas, cada linha encontrando três outras em pontos duplos ordinários.

Aspose.PDF para Java mostra como usar curvas de Bézier em seus Gráficos. Curvas de Bézier são amplamente utilizadas em computação gráfica para modelar curvas suaves. A curva está completamente contida no invólucro convexo de seus pontos de controle, os pontos podem ser exibidos graficamente e usados para manipular a curva intuitivamente. A curva inteira está contida no quadrilátero cujos cantos são os quatro pontos fornecidos (seu invólucro convexo).

Neste artigo, investigaremos simplesmente curvas gráficas e curvas preenchidas, que você pode criar no seu documento PDF.

Siga os passos abaixo:

1. Crie uma instância de [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Crie um [objeto Drawing](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame) com certas dimensões.

1. Defina o [Border](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph#setBorder-com.aspose.pdf.BorderInfo-) para o objeto Drawing.

1. Adicione o objeto [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph) à coleção de parágrafos da página.

1. Salve seu arquivo PDF

```java
    public static void ExampleCurve() {
        // Crie uma instância de Document
        Document pdfDocument = new Document();
        // Adicione uma página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Crie um objeto Drawing com certas dimensões
        Graph graph = new Graph(400, 200);
        // Defina o border para o objeto Drawing
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});

        curve1.getGraphInfo().setColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Adicione o objeto Graph à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salve o arquivo PDF
        pdfDocument.save(_dataDir + "DrawingCurve1_out.pdf");
    }
```


A imagem a seguir mostra o resultado executado com nosso trecho de código:

![Desenho da Curva](drawing_curve.png)

## Criar Objeto de Curva Preenchida

Este exemplo mostra como adicionar um objeto Curva que é preenchido com cor.

```java
    public static void ExampleFilledCurve() {
        // Criar instância de Documento
        Document pdfDocument = new Document();
        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Criar objeto de Desenho com certas dimensões
        Graph graph = new Graph(400, 200);
        // Definir borda para o objeto de Desenho
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getGreen());
        graph.setBorder(borderInfo);

        Curve curve1 = new Curve(new float[] { 10, 10, 50, 60, 70, 10, 100, 120});
        curve1.getGraphInfo().setFillColor(Color.getGreenYellow());
        graph.getShapes().add(curve1);

        // Adicionar objeto Graph à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "DrawingCurve2_out.pdf");
    }
```


Look at the result of adding a filled Curve:

![Curva Preenchida](filled_curve.png)