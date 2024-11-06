---
title: Adicionar Carimbos de Imagem em PDF Programaticamente 
linktitle: Carimbos de Imagem em Arquivo PDF
type: docs
weight: 10
url: pt/cpp/image-stamps-in-pdf-page/
description: Adicione o Carimbo de Imagem no seu documento PDF usando a classe ImageStamp com a biblioteca Aspose.PDF para C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Adicionar Carimbo de Imagem em Arquivo PDF

Você pode usar a classe ImageStamp para adicionar um carimbo de imagem a um arquivo PDF. A classe ImageStamp fornece as propriedades necessárias para criar um carimbo baseado em imagem, como altura, largura, opacidade, entre outros.

Para adicionar um carimbo de imagem:

1. Crie um objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) e um objeto ImageStamp usando as propriedades necessárias.
1. Chame o método [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) da classe [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) para adicionar o carimbo ao PDF.

O seguinte trecho de código mostra como adicionar um carimbo de imagem no arquivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar carimbo de imagem
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Adicionar carimbo a uma página específica    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Salvar documento de saída
    document->Save(_dataDir + outputFileName);
}
```

## Controlar a Qualidade da Imagem ao Adicionar Carimbo

Ao adicionar uma imagem como um objeto de carimbo, você pode controlar a qualidade da imagem. A propriedade Quality da classe [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) é usada para este propósito. Ela indica a qualidade da imagem em porcentagem (valores válidos são 0..100).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // String para o nome do arquivo de entrada
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Criar carimbo de imagem
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## Carimbo de Imagem como Fundo em Caixa Flutuante

A API Aspose.PDF permite adicionar carimbo de imagem como fundo em uma caixa flutuante. A propriedade BackgroundImage da classe FloatingBox pode ser usada para definir a imagem de fundo para uma caixa flutuante, como mostrado no exemplo de código a seguir.

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // String para nome do arquivo de entrada
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Instanciar objeto Document
    auto document = MakeObject<Document>();

    // Adicionar página ao documento PDF
    auto page = document->get_Pages()->Add();

    // Criar objeto FloatingBox
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // Definir posição à esquerda para FloatingBox
    aBox->set_Left(40);
    // Definir posição superior para FloatingBox
    aBox->set_Top(80);
    // Definir o alinhamento horizontal para FloatingBox
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // Adicionar fragmento de texto à coleção de parágrafos de FloatingBox
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // Definir borda para FloatingBox
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // Adicionar imagem de fundo
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // Definir cor de fundo para FloatingBox
    aBox->set_BackgroundColor(Color::get_Yellow());

    // Adicionar FloatingBox à coleção de parágrafos do objeto página
    page->get_Paragraphs()->Add(aBox);
    // Salvar o documento PDF
    document->Save(_dataDir + outputFileName);
}
```