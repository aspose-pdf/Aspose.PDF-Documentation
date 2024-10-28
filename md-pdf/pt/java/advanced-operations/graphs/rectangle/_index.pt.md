---
title: Adicionar Objeto Retângulo ao Arquivo PDF
linktitle: Adicionar Retângulo
type: docs
weight: 50
url: /java/add-rectangle/
description: Este artigo explica como criar um objeto Retângulo no seu PDF usando Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Adicionar objeto Retângulo

Aspose.PDF para Java suporta o recurso de adicionar objetos de gráfico (por exemplo, gráfico, linha, retângulo, etc.) a documentos PDF. Você também tem a vantagem de adicionar o objeto [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) onde você também oferece o recurso de preencher o objeto retângulo com uma certa cor, controlar a ordem Z, adicionar preenchimento de cor gradiente e etc.

Primeiro, vamos ver a possibilidade de criar um objeto Retângulo.

Siga os passos abaixo:

1. Crie um novo [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) PDF

1. Adicione [Página](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) à coleção de páginas do arquivo PDF

1. Adicione [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) à coleção de parágrafos da instância da página

1. Crie uma instância de [Gráfico](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Graph)

1. Defina a borda para o [objeto de Desenho](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/package-frame)

1. Crie uma instância de Retângulo

1. Adicione o objeto [Retângulo](https://reference.aspose.com/pdf/java/com.aspose.pdf.drawing/Rectangle) à coleção de formas do objeto Gráfico

1. Adicione o objeto gráfico à coleção de parágrafos da instância da página

1. Adicione [Fragmento de Texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragment) à coleção de parágrafos da instância da página

1. E salve o seu arquivo PDF

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.BorderInfo;
import com.aspose.pdf.BorderSide;
import com.aspose.pdf.Color;
import com.aspose.pdf.Document;
import com.aspose.pdf.Page;
import com.aspose.pdf.Point;
import com.aspose.pdf.TextFragment;
import com.aspose.pdf.drawing.*;

public class WorkingWithGraphs {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/";

    public static void ExampleRectangle() {

        // Crie um novo documento PDF
        Document pdfDocument = new Document();

        // Adicione uma página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();

        // Adicione um fragmento de texto à coleção de parágrafos da instância da página
        page.getParagraphs().add(new TextFragment("Texto antes do objeto Gráfico"));

        // Crie uma instância de Gráfico
        Graph graph = new Graph(400, 200);

        // Defina a borda para o objeto de Desenho
        BorderInfo borderInfo = new BorderInfo(BorderSide.All, Color.getRed());
        graph.setBorder(borderInfo);

        // Crie uma instância de Retângulo
        Rectangle rect = new Rectangle(10, 10, 380, 180);

        // Adicione o objeto retângulo à coleção de formas do objeto Gráfico
        graph.getShapes().add(rect);

        // Adicione o objeto gráfico à coleção de parágrafos da instância da página
        page.getParagraphs().add(graph);

        // Adicione um fragmento de texto à coleção de parágrafos da instância da página
        page.getParagraphs().add(new TextFragment("Texto após o objeto Gráfico"));

        // Salve o arquivo PDF
        pdfDocument.save(_dataDir + "CreateRectangle_out.pdf");
    }
```


![Criar Retângulo](create_rectangle.png)

## Criar Objeto Retângulo Preenchido

Aspose.PDF para Java também oferece o recurso de preencher um objeto retângulo com uma certa cor.

O trecho de código a seguir mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) que é preenchido com cor.

```java
   public static void ExampleRectangleFilledSolidColor() {

        Document pdfDocument = new Document();

        // Adicionar página à coleção de páginas do arquivo PDF
        Page page = pdfDocument.getPages().add();
        // Criar instância de Graph
        Graph graph = new Graph(100, 400);

        // Adicionar objeto gráfico à coleção de parágrafos da instância de página
        page.getParagraphs().add(graph);

        // Criar instância de Rectangle
        Rectangle rect = new Rectangle(100, 100, 200, 120);

        // Especificar cor de preenchimento para o objeto Graph
        rect.getGraphInfo().setFillColor(Color.getRed());

        // Adicionar objeto retângulo à coleção de formas do objeto Graph
        graph.getShapes().add(rect);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "CreateFilledRectangle_out.pdf");
    }
```


Olhe para o resultado do retângulo preenchido com cor sólida:

![Retângulo Preenchido](fill_rectangle.png)

## Adicionar Desenho com Preenchimento Gradiente

Aspose.PDF para Java suporta o recurso de adicionar objetos gráficos a documentos PDF e, às vezes, é necessário preencher objetos gráficos com Cor de Gradiente. Para preencher objetos gráficos com Cor de Gradiente, precisamos definir setPatterColorSpace com objeto gradientAxialShading conforme a seguir.

O trecho de código a seguir mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) que é preenchido com Cor de Gradiente.

```java
   public static void ExampleRectangleFilledGradient() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        Graph graph = new Graph(300, 300);
        page.getParagraphs().add(graph);
        Rectangle rect = new Rectangle(0, 0, 300, 300);
        graph.getShapes().add(rect);

        // Especificar cor de preenchimento gradiente para o objeto Graph e preencher
        Color gradientFill = new com.aspose.pdf.Color();
        rect.getGraphInfo().setFillColor(gradientFill);

        GradientAxialShading gradientAxialShading = new GradientAxialShading(Color.getRed(), Color.getBlue());

        gradientAxialShading.setStart(new Point(0, 0));
        gradientAxialShading.setEnd(new Point(300, 300));
        gradientFill.setPatternColorSpace(gradientAxialShading);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "AddDrawingWithGradientFill_out.pdf");
    }
```


![Gradient Rectangle](gradient.png)

## Criar Retângulo com Canal de Cor Alpha

Aspose.PDF para Java suporta preencher o objeto retângulo com uma determinada cor. Um objeto retângulo também pode ter um canal de cor Alpha para dar uma aparência transparente. O seguinte trecho de código mostra como adicionar um objeto [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) com canal de cor Alpha.

Os pixels da imagem podem armazenar informações sobre sua opacidade junto com o valor da cor. Isso permite criar imagens com áreas transparentes ou semi-transparentes.

Em vez de tornar uma cor transparente, cada pixel armazena informações sobre quão opaco ele é. Esses dados de opacidade são chamados de canal alpha e geralmente são armazenados após os canais de cor do pixel.

Em nosso trecho de código, usamos o método [fromArgb](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color#fromArgb-int-int-int-) da classe [com.aspose.pdf.Color](https://reference.aspose.com/pdf/java/com.aspose.pdf/Color).
 Precisamos especificar valores onde os primeiros 3 são componentes de cor, especificados no intervalo de 0 a 255, e o último é o nível de opacidade (canal alpha), especificado por números fracionários de 0 a 1.

```java
    public static void ExampleRectangleAlphaChannelColor() {
        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Criar uma instância de Graph
        Graph graph = new Graph(100, 400);

        // Criar objeto retângulo com dimensões específicas
        Rectangle rect1 = new Rectangle(100, 100, 200, 100);
        Color color1 = Color.fromArgb(128, 224, 0, 224);
        rect1.getGraphInfo().setFillColor(color1);
        // Adicionar objeto retângulo à coleção de formas da instância de Graph
        graph.getShapes().add(rect1);

        // Criar segundo objeto retângulo
        Rectangle rect2 = new Rectangle(200, 150, 200, 100);
        Color color2 = Color.fromArgb(64, 0, 224, 224);
        rect2.getGraphInfo().setFillColor(color2);
        graph.getShapes().add(rect2);

        // Adicionar instância de graph à coleção de parágrafos do objeto page
        page.getParagraphs().add(graph);

        // Salvar arquivo PDF
        pdfDocument.save(_dataDir + "CreateRectangleWithAlphaColor_out.pdf");
    }
```

![Rectangle Alpha Channel Color](rectangle_color.png)

## Controlar a Ordem Z do Retângulo

Aspose.PDF para Java suporta o recurso de adicionar objetos gráficos (por exemplo, gráfico, linha, retângulo etc.) a documentos PDF. Ao adicionar mais de uma instância do mesmo objeto dentro do arquivo PDF, podemos controlar sua renderização especificando a Ordem Z. A Ordem Z também é usada quando precisamos renderizar objetos sobrepostos.

O trecho de código a seguir mostra as etapas para renderizar objetos [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/Rectangle) sobrepostos.

```java
   public static void Controlling_Z_Order() {

        Document pdfDocument = new Document();
        Page page = pdfDocument.getPages().add();

        // Cria um novo retângulo com a cor vermelha, ordem Z como 0 e certas dimensões
        AddRectangle(page, 50, 40, 60, 40, Color.getRed(), 2);
        // Cria um novo retângulo com a cor azul, ordem Z como 0 e certas
        // dimensões
        AddRectangle(page, 20, 20, 30, 30, Color.getBlue(), 1);
        // Cria um novo retângulo com a cor verde, ordem Z como 0 e certas
        // dimensões
        AddRectangle(page, 40, 40, 60, 30, Color.getGreen(), 0);

        // Salva o arquivo PDF resultante
        pdfDocument.save(_dataDir + "ControlRectangleZOrder_out.pdf");

    }
```


![Controlando a Ordem Z](control.png)