---
title: Adicionar carimbos de imagem em PDF programaticamente
linktitle: Carimbos de imagem em arquivo PDF
type: docs
weight: 10
url: /java/image-stamps-in-pdf-page/
description: Adicione o carimbo de imagem em seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Imagem em Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) para adicionar uma imagem como um carimbo em um documento PDF. A classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) fornece métodos para especificar altura, largura, opacidade etc.

Para adicionar um carimbo de imagem:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e um objeto ImageStamp usando as propriedades necessárias.

1. Chame o método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para adicionar o carimbo ao PDF.

O trecho de código a seguir mostra como adicionar um carimbo de imagem no arquivo PDF.

```java
public static void AddImageStampInPDFFile() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Criar carimbo de imagem
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // Adicionar carimbo a uma página específica
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // Salvar documento de saída
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## Controlar a Qualidade da Imagem ao Adicionar Carimbo

A classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) permite adicionar uma imagem como carimbo em um documento PDF. Ela também permite controlar a qualidade da imagem ao adicionar uma imagem como marca d'água em um arquivo PDF. Para permitir isso, um método chamado setQuality(...) foi adicionado à classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp). Um método semelhante também pode ser encontrado na classe [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) do pacote com.aspose.pdf.facades.

O trecho de código a seguir mostra como controlar a qualidade da imagem ao adicionar como carimbo no arquivo PDF.

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // Criar carimbo de imagem
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## Carimbo de Imagem como Fundo em Caixa Flutuante

A API Aspose.PDF permite adicionar um carimbo de imagem como fundo em uma caixa flutuante. A propriedade BackgroundImage da classe FloatingBox pode ser usada para definir o carimbo de imagem de fundo para uma caixa flutuante, como mostrado no exemplo de código a seguir.

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // Instanciar objeto Document
        Document doc = new Document();
        // Adicionar página ao documento PDF
        Page page = doc.getPages().add();

        // Criar objeto FloatingBox
        FloatingBox aBox = new FloatingBox(200, 100);

        // Definir posição à esquerda para FloatingBox
        aBox.setLeft(40);
        // Definir posição superior para FloatingBox
        aBox.setTop(80);
        // Definir alinhamento horizontal para FloatingBox
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // Adicionar fragmento de texto à coleção de parágrafos de FloatingBox
        aBox.getParagraphs().add(new TextFragment("texto principal"));
        // Definir borda para FloatingBox
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // Adicionar imagem de fundo
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // Definir cor de fundo para FloatingBox
        aBox.setBackgroundColor(Color.getYellow());

        // Adicionar FloatingBox à coleção de parágrafos do objeto page
        page.getParagraphs().add(aBox);
        // Salvar o documento PDF
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```