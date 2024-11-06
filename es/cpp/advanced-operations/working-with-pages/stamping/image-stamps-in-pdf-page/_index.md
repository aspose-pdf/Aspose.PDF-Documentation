---
title: Añadir sellos de imagen en PDF programáticamente
linktitle: Sellos de imagen en archivo PDF
type: docs
weight: 10
url: es/cpp/image-stamps-in-pdf-page/
description: Añade el sello de imagen en tu documento PDF utilizando la clase ImageStamp con la biblioteca Aspose.PDF para C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir sello de imagen en archivo PDF

Puedes usar la clase ImageStamp para añadir un sello de imagen a un archivo PDF. La clase ImageStamp proporciona las propiedades necesarias para crear un sello basado en imagen, como altura, ancho, opacidad, entre otros.

Para añadir un sello de imagen:

1. Crea un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) y un objeto ImageStamp utilizando las propiedades requeridas.
1. Llama al método [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) de la clase [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) para añadir el sello al PDF.

El siguiente fragmento de código muestra cómo añadir un sello de imagen en el archivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddImageStampToPDFFile()
{    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("AddImageStamp.pdf");

    String outputFileName("AddImageStamp_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear sello de imagen
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");
    imageStamp->set_Background(true);
    imageStamp->set_XIndent(100);
    imageStamp->set_YIndent(100);
    imageStamp->set_Height(48);
    imageStamp->set_Width(225);
    imageStamp->set_Rotate(Rotation::on270);
    imageStamp->set_Opacity(0.5);
   
    // Agregar sello a una página en particular    
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);

    // Guardar documento de salida
    document->Save(_dataDir + outputFileName);
}
```

## Controlar la calidad de la imagen al agregar un sello

Al agregar una imagen como un objeto de sello, puede controlar la calidad de la imagen. La propiedad Quality de la clase [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) se utiliza para este propósito. Indica la calidad de la imagen en porcentajes (los valores válidos son 0..100).

```cpp
void ControlImageQualityWhenAddingStamp() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("ControlImageQuality_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear sello de imagen
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    imageStamp->set_Quality(10);
    document->get_Pages()->idx_get(1)->AddStamp(imageStamp);    
    document->Save(_dataDir + u"ControlImageQuality_out.pdf");
}
```

## Sello de Imagen como Fondo en Caja Flotante

La API de Aspose.PDF te permite añadir un sello de imagen como fondo en una caja flotante. La propiedad BackgroundImage de la clase FloatingBox se puede usar para establecer la imagen de fondo para un cuadro flotante como se muestra en el siguiente ejemplo de código.

```cpp
void ImageStampAsBackgroundInFloatingBox() {
    
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo de entrada
    String inputFileName("AddImageStamp.pdf");
    String outputFileName("AddImageStampAsBackgroundInFloatingBox_out.pdf");

    // Instanciar objeto Document
    auto document = MakeObject<Document>();

    // Agregar página al documento PDF
    auto page = document->get_Pages()->Add();

    // Crear objeto FloatingBox
    auto aBox = MakeObject<FloatingBox>(200, 100);

    // Establecer posición izquierda para FloatingBox
    aBox->set_Left(40);
    // Establecer posición superior para FloatingBox
    aBox->set_Top(80);
    // Establecer la alineación horizontal para FloatingBox
    aBox->set_HorizontalAlignment(HorizontalAlignment::Center);
    
    // Agregar fragmento de texto a la colección de párrafos de FloatingBox    
    aBox->get_Paragraphs()->Add(MakeObject<TextFragment>(u"main text"));

    // Establecer borde para FloatingBox
    aBox->set_Border(MakeObject<BorderInfo>(BorderSide::All, Color::get_Red()));

    // Agregar imagen de fondo
    auto image = MakeObject<Image>();
    image->set_File(_dataDir + u"aspose-logo.png");
    aBox->set_BackgroundImage(image);

    // Establecer color de fondo para FloatingBox
    aBox->set_BackgroundColor(Color::get_Yellow());

    // Agregar FloatingBox a la colección de párrafos del objeto página
    page->get_Paragraphs()->Add(aBox);
    // Guardar el documento PDF
    document->Save(_dataDir + outputFileName);
}
```