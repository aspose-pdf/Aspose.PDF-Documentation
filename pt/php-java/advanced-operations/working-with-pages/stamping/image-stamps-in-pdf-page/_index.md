---
title: Adicionar selos de imagem em PDF programaticamente
linktitle: Selos de imagem em arquivo PDF
type: docs
weight: 10
url: /pt/php-java/image-stamps-in-pdf-page/
description: Adicione o selo de imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF para PHP via Java.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Selo de Imagem em Arquivo PDF

Você pode usar a classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) para adicionar uma imagem como um selo no documento PDF. A classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) fornece métodos para especificar altura, largura, opacidade, etc.

Para adicionar um selo de imagem:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) e um objeto ImageStamp usando as propriedades necessárias.

1. Chame o método [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) da classe [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) para adicionar o carimbo ao PDF.

O trecho de código a seguir mostra como adicionar um carimbo de imagem no arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // Criar carimbo de imagem
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // Adicionar carimbo a uma página específica
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close()
```

## Controlar a Qualidade da Imagem ao Adicionar Carimbo

A classe [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) permite adicionar uma imagem como carimbo em um documento PDF.
 It also allows you to control the image quality when adding an image as a watermark in a PDF file. To allow this, a method named setQuality(...) has been added to the [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) class. A similar method can also be found in the [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) class of the com.aspose.pdf.facades package.

O trecho de código a seguir mostra como controlar a qualidade da imagem ao adicionar como carimbo no arquivo PDF.

```php

    // Abrir documento
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // Criar carimbo de imagem
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();        
```

## Carimbo de Imagem como Plano de Fundo em Caixa Flutuante

A API Aspose.PDF permite adicionar um carimbo de imagem como plano de fundo em uma caixa flutuante. A propriedade BackgroundImage da classe FloatingBox pode ser usada para definir a imagem de fundo para uma caixa flutuante, como mostrado no exemplo de código a seguir.

Este trecho de código demonstra o processo de criação de um documento PDF e a adição de um FloatingBox a ele. O FloatingBox contém um fragmento de texto, uma borda, uma imagem de fundo e uma cor de fundo. O documento resultante é então salvo em um arquivo de saída.

```php

    // Abrir documento
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // Adicionar página ao documento PDF
    $page = $pages->add();

    // Criar objeto FloatingBox
    $aBox = new FloatingBox(200, 100);

    // Definir posição esquerda para FloatingBox
    $aBox->setLeft(40);

    // Definir posição superior para FloatingBox
    $aBox->setTop(80);

    // Definir o alinhamento horizontal para FloatingBox
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // Adicionar fragmento de texto à coleção de parágrafos do FloatingBox
    $aBox->getParagraphs()->add(new TextFragment("texto principal"));

    // Definir borda para FloatingBox
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // Adicionar imagem de fundo
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // Definir cor de fundo para FloatingBox
    $aBox->setBackgroundColor($colors->getYellow());

    // Adicionar FloatingBox à coleção de parágrafos do objeto página
    $page->getParagraphs()->add($aBox);
    
    // Salvar documento de saída
    $document->save($outputFile);
    $document->close();
```