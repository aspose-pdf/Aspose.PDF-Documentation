---
title: Adicionar Objeto Linha ao arquivo PDF
linktitle: Adicionar Linha
type: docs
weight: 40
url: pt/java/add-line/
description: Este artigo explica como criar um objeto de linha no seu PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto Linha

Aspose.PDF para Java suporta a funcionalidade de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Você também tem a vantagem de adicionar o objeto [Line](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Line) onde você pode especificar o padrão tracejado, cor e outras formatações para o elemento Linha.

Siga os passos abaixo:

1. Crie uma instância do [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document).

1. Adicione uma [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à coleção de páginas do arquivo PDF.

1. Crie uma instância do [Graph](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph).

1. Adicione o objeto Graph à coleção de parágrafos da instância da página.

1. Crie uma instância de [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle).

1. Defina a largura da linha.

1. Adicione o objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) à coleção de formas do objeto Graph.

1. Salve seu arquivo PDF.

O trecho de código a seguir mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) que é preenchido com cor.

```java
 public static void ExampleLine() {
        // Crie uma instância de Document
        Document pdfDocument = new Document();
        // Adicione uma página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();
        // Crie uma instância de Graph
        Graph graph = new Graph(100, 400);

        // Adicione o objeto gráfico à coleção de parágrafos da instância de página
        page.getParagraphs().add(graph);

        // Crie uma instância de Rectangle
        Line line = new Line(new float[] { 100, 100, 200, 100 });
        
        line.getGraphInfo().setLineWidth(5);
        
        // Adicione o objeto retângulo à coleção de formas do objeto Graph
        graph.getShapes().add(line);

        // Salve o arquivo PDF
        pdfDocument.save(_dataDir + "LineAdded.pdf");
    }
```


![Adicionar Linha](add_line.png)

## Como adicionar Linha Tracejada Pontilhada ao seu documento PDF

```java
public static void ExampleDashedLine() {
        // Criar instância do Documento
        Document pdfDocument = new Document();
        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Criar objeto de Desenho com certas dimensões
        Graph canvas = new Graph(100, 400);
        // Adicionar objeto de desenho à coleção de parágrafos da instância da página
        page.getParagraphs().add(canvas);

        // Criar objeto Linha
        Line line = new Line(new float[] { 100, 100, 200, 100 });

        // Definir cor para o objeto Linha
        line.getGraphInfo().setColor(Color.getRed());
        // Especificar matriz de traços para o objeto linha
        line.getGraphInfo().setDashArray(new int[] { 0, 1, 0 });
        // Definir a fase de traço para a instância Linha
        line.getGraphInfo().setDashPhase(1);
        // Adicionar linha à coleção de formas do objeto de desenho
        canvas.getShapes().add(line);
        // Salvar documento PDF
        pdfDocument.save(_dataDir + "DashLength_out.pdf");
    }
```


Vamos verificar o resultado:

![Linha Tracejada](dash_line.png)

## Desenhar Linha Através da Página

Também podemos usar o objeto linha para desenhar uma cruz começando do canto Esquerdo-Inferior para o canto Superior-Direito e do canto Esquerdo-Superior para o canto Inferior-Direito.

Por favor, dê uma olhada no trecho de código a seguir para realizar este requisito.

```java
    public static void ExampleLineAcrossPage() {
        // Criar instância de Documento
        Document pdfDocument = new Document();
        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();
        // Definir margem da página em todos os lados como 0

        page.getPageInfo().getMargin().setLeft(0);
        page.getPageInfo().getMargin().setRight(0);
        page.getPageInfo().getMargin().setBottom(0);
        page.getPageInfo().getMargin().setTop(0);

        // Criar objeto Gráfico com Largura e Altura iguais às dimensões da página
        Graph graph = new Graph((float) page.getPageInfo().getWidth(), (float) page.getPageInfo().getHeight());

        // Criar primeiro objeto linha começando do canto Inferior-Esquerdo para o canto Superior-Direito da página
        Line line = new Line(new float[] { (float) page.getRect().getLLX(), 0, (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getURY() });

        // Adicionar linha à coleção de formas do objeto Gráfico
        graph.getShapes().add(line);
        // Desenhar linha do canto Superior-Esquerdo da página para o canto Inferior-Direito da página
        Line line2 = new Line(new float[] { 0, (float) page.getRect().getURY(), (float) page.getPageInfo().getWidth(),
                (float) page.getRect().getLLX() });

        // Adicionar linha à coleção de formas do objeto Gráfico
        graph.getShapes().add(line2);
        // Adicionar objeto Gráfico à coleção de parágrafos da página
        page.getParagraphs().add(graph);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "DrawingLine_out.pdf");
    }
```


![Desenho de Linha](draw_line.png)