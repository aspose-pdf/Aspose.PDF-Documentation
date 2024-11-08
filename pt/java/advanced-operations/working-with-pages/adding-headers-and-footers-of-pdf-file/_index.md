---
title: Adicionar Cabeçalho e Rodapé em PDF 
linktitle: Adicionar Cabeçalho e Rodapé 
type: docs
weight: 70
url: /pt/java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para Java permite que você adicione cabeçalhos e rodapés ao seu arquivo PDF usando a classe TextStamp.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Carimbos em PDF são frequentemente usados em contratos, relatórios e materiais restritos, para provar que os documentos foram revisados e marcados como "lido", "qualificado" ou "confidencial", etc. Este artigo mostrará como podemos adicionar carimbos de imagem e carimbos de texto a documentos PDF usando **Aspose.PDF para Java**.

Se você ler os trechos de código acima linha por linha, deve achar que a sintaxe e a lógica do código são bastante fáceis de entender.

## Adicionando Texto no Cabeçalho do Arquivo PDF

Você pode usar a classe [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) para adicionar texto no cabeçalho de um arquivo PDF.
 TextStamp class fornece as propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no cabeçalho, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Page para adicionar o texto no cabeçalho do PDF.

Você precisa definir a propriedade TopMargin de forma que ajuste o texto na área do cabeçalho do seu PDF. Você também precisa definir HorizontalAlignment para Center e VerticalAlignment para Top.

O seguinte trecho de código mostra como adicionar texto no cabeçalho de um arquivo PDF com Java.

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // O caminho para o diretório de documentos.
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // Criar cabeçalho
        TextStamp textStamp = new TextStamp("Header Text");

        // Definir propriedades do carimbo
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // Adicionar cabeçalho em todas as páginas
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // Salvar documento atualizado
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## Adicionando Texto no Rodapé do Arquivo PDF

Você pode usar a classe TextStamp para adicionar texto no rodapé de um arquivo PDF. A classe TextStamp fornece propriedades necessárias para criar um carimbo baseado em texto, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar texto no rodapé, você precisa criar um objeto Document e um objeto TextStamp usando as propriedades requeridas. Depois disso, você pode chamar o método AddStamp da Página para adicionar o texto no rodapé do PDF.

O trecho de código a seguir mostra como adicionar texto no rodapé de um arquivo PDF com Java.

```java
    public static void AddingTextInFooterOfPDFFile() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // Criar rodapé
        TextStamp textStamp = new TextStamp("Texto do Rodapé");
        // Definir propriedades do carimbo
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Adicionar rodapé em todas as páginas
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // Salvar arquivo PDF atualizado
        pdfDocument.save(_dataDir);
    }
```


## Adicionando Imagem no Cabeçalho do Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) para adicionar uma imagem no cabeçalho de um arquivo PDF. A classe Image Stamp fornece propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no cabeçalho, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) da Página para adicionar a imagem no cabeçalho do PDF.

```java
public static void AddingImageInHeaderOfPDFFile() {

// Abrir documento
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// Criar cabeçalho
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// Definir propriedades do carimbo
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// Adicionar cabeçalho em todas as páginas
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// Salvar arquivo PDF atualizado
pdfDocument.save(_dataDir);
}
```


O seguinte trecho de código mostra como adicionar uma imagem no cabeçalho de um arquivo PDF com Java.

## Adicionando Imagem no Rodapé de um Arquivo PDF

Você pode usar a classe Image Stamp para adicionar imagem no rodapé de um arquivo PDF. A classe Image Stamp fornece as propriedades necessárias para criar um carimbo baseado em imagem, como tamanho da fonte, estilo da fonte e cor da fonte, etc. Para adicionar uma imagem no rodapé, você precisa criar um objeto Document e um objeto Image Stamp usando as propriedades necessárias. Depois disso, você pode chamar o método AddStamp da Page para adicionar a imagem no rodapé do PDF.

{{% alert color="primary" %}}

Você precisa definir a propriedade BottomMargin de tal forma que ajuste a imagem na área do rodapé do seu PDF. Você também precisa definir [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) para `Center` e [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) para `Bottom`.

{{% /alert %}}

O seguinte trecho de código mostra como adicionar uma imagem no rodapé de um arquivo PDF com Java.

```java
    public static void AddingImageInFooterOfPDFFile() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // Criar rodapé
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // Definir propriedades do carimbo
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // Adicionar rodapé em todas as páginas
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // Salvar arquivo PDF atualizado
        pdfDocument.save(_dataDir);
    }
```

## Adicionando diferentes Cabeçalhos em um Arquivo PDF

Sabemos que podemos adicionar TextStamp na seção de Cabeçalho/Rodapé do documento usando as propriedades TopMargin ou Bottom Margin, mas às vezes podemos ter a necessidade de adicionar múltiplos cabeçalhos/rodapés em um único documento PDF.
 **Aspose.PDF for Java** explica como fazer isso.

Para cumprir este requisito, criaremos objetos individuais [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) (o número de objetos depende do número de cabeçalhos/rodapés necessários) e os adicionaremos ao documento PDF. Também podemos especificar diferentes informações de formatação para cada objeto de carimbo individual. No exemplo a seguir, criamos um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e três objetos [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) e, em seguida, usamos o método [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) da página para adicionar o texto na seção do cabeçalho do PDF. O snippet de código a seguir mostra como adicionar uma imagem no rodapé de um arquivo PDF com Aspose.PDF para Java.

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // Abrir documento de origem
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // Criar três carimbos
        TextStamp stamp1 = new TextStamp("Cabeçalho 1");
        TextStamp stamp2 = new TextStamp("Cabeçalho 2");
        TextStamp stamp3 = new TextStamp("Cabeçalho 3");

        // Definir alinhamento do carimbo (colocar carimbo no topo da página, centralizado horizontalmente)
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // Especificar o estilo da fonte como Negrito
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // Definir a cor do primeiro plano do texto como vermelho
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // Especificar o tamanho da fonte como 14
        stamp1.getTextState().setFontSize(14);

        // Agora precisamos definir o alinhamento vertical do segundo objeto de carimbo como Top
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // Definir informações de alinhamento horizontal para o carimbo como centralizado
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // Definir o fator de zoom para o objeto de carimbo
        stamp2.setZoom (10);

        // Definir a formatação do terceiro objeto de carimbo
        // Especificar informações de alinhamento vertical para o objeto de carimbo como TOP
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // Definir informações de alinhamento horizontal para o objeto de carimbo como centralizado
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // Definir o ângulo de rotação para o objeto de carimbo
        stamp3.setRotateAngle(35);
        // Definir rosa como cor de fundo para o carimbo
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // Alterar informações da fonte do carimbo para Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // Primeiro carimbo é adicionado na primeira página;
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // Segundo carimbo é adicionado na segunda página;
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // Terceiro carimbo é adicionado na terceira página.
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // Salvar arquivo PDF atualizado
        pdfDocument.save(_dataDir);
    }

}
```