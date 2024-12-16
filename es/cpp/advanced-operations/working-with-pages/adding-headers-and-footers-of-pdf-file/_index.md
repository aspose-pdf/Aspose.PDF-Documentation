---
title: Añadir Encabezado y Pie de Página al PDF
linktitle: Añadir Encabezado y Pie de Página al PDF
type: docs
weight: 70
url: /es/cpp/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF para C++ le permite agregar encabezados y pies de página a su archivo PDF utilizando la clase TextStamp.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para C++** le permite agregar encabezado y pie de página en su archivo PDF existente. Puede agregar imágenes o texto a un documento PDF. También, intente agregar diferentes encabezados en un archivo PDF con C++.

## Agregar Texto en el Encabezado del Archivo PDF

Puede usar la clase [TextStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text_stamp) para agregar texto en el encabezado de un archivo PDF. TextStamp class proporciona las propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el encabezado, necesitas crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puedes llamar al método AddStamp de la Page para agregar el texto en el encabezado del PDF.

Necesitas configurar la propiedad TopMargin de tal manera que ajuste el texto en el área del encabezado de tu PDF. También necesitas configurar HorizontalAlignment a Center y VerticalAlignment a Top.

El siguiente fragmento de código te muestra cómo agregar texto en el encabezado de un archivo PDF con C++.

```cpp
void AddingTextInHeaderOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinHeader.pdf");
    String outputFileName("TextinHeader_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto textStamp = MakeObject<TextStamp>(u"Header Text");

    // Set properties of the stamp
    textStamp->set_TopMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Add header on all pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```
## Adding Text in Footer of PDF File

Puede usar la clase TextStamp para agregar texto en el pie de un archivo PDF. La clase TextStamp proporciona las propiedades necesarias para crear un sello basado en texto como tamaño de fuente, estilo de fuente y color de fuente, etc. Para agregar texto en el pie de página, necesita crear un objeto Document y un objeto TextStamp usando las propiedades requeridas. Después de eso, puede llamar al método AddStamp de la página para agregar el texto en el pie de página del PDF.

{{% alert color="primary" %}}

Necesita configurar la propiedad Bottom Margin de tal manera que ajuste el texto en el área del pie de página de su PDF. También necesita configurar HorizontalAlignment a Center y VerticalAlignment a Bottom

{{% /alert %}}

El siguiente fragmento de código le muestra cómo agregar texto en el pie de un archivo PDF con C++.

```cpp
void AddingTextInFooterOfPdfFile() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("TextinFooter.pdf");
    String outputFileName("TextinFooter_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear pie de página
    auto textStamp = MakeObject<TextStamp>(u"Footer Text");

    // Configurar propiedades del sello
    textStamp->set_BottomMargin(10);
    textStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    textStamp->set_VerticalAlignment(HorizontalAlignment::Bottom);

    // Agregar pie de página en todas las páginas
    for (auto page : document->get_Pages())
    {
        page->AddStamp(textStamp);
    }

    // Guardar documento actualizado
    document->Save(_dataDir + outputFileName);
}
```

## Añadir Imagen en el Encabezado del Archivo PDF

Puede utilizar la clase [ImageStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.image_stamp) para añadir una imagen en el encabezado de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen como el tamaño de la fuente, estilo de fuente y color de fuente, etc. Para añadir una imagen en el encabezado, necesita crear un objeto Document y un objeto Image Stamp utilizando las propiedades requeridas. Después de eso, puede llamar al método AddStamp de la Página para añadir la imagen en el encabezado del PDF.

El siguiente fragmento de código le muestra cómo añadir una imagen en el encabezado de un archivo PDF con C++.

```cpp
void AddingImageInHeaderOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinHeader.pdf");
    String outputFileName("ImageinHeader_out.pdf");

    // Open document
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Create header
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Set properties of the stamp
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment (VerticalAlignment::Top);

    // Add header on all pages
    for(auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Save updated document
    document->Save(_dataDir + outputFileName);
}
```

## Adding Image in Footer of PDF File

Puede utilizar la clase Image Stamp para añadir una imagen en el pie de página de un archivo PDF. La clase Image Stamp proporciona las propiedades necesarias para crear un sello basado en imagen como el tamaño de fuente, el estilo de fuente y el color de fuente, etc. Para añadir una imagen en el pie de página, necesita crear un objeto Document y un objeto Image Stamp utilizando las propiedades requeridas. Después de eso, puede llamar al método AddStamp de la página para añadir la imagen en el pie de página del PDF.

Necesita establecer la propiedad [BottomMargin](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.stamp#aeab91949cf3eb473018b31a74fed7173) de tal manera que ajuste la imagen en el área del pie de página de su PDF. También necesita establecer [HorizontalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#aefec9c0bf30ee5e6fb2640e69aed6cd9) a `Center` y [VerticalAlignment](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf#ad4956d03096fc515eaa34319a6bf636a) a `Bottom`.

El siguiente fragmento de código le muestra cómo añadir una imagen en el pie de página de un archivo PDF con C++.

```cpp
void AddingImageInFooterOfPdfFile() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("ImageinFooter.pdf");
    String outputFileName("ImageinFooter_out.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear encabezado
    auto imageStamp = MakeObject<ImageStamp>(_dataDir + u"aspose-logo.jpg");

    // Establecer propiedades del sello
    imageStamp->set_TopMargin(10);
    imageStamp->set_HorizontalAlignment(HorizontalAlignment::Center);
    imageStamp->set_VerticalAlignment(VerticalAlignment::Top);

    // Agregar encabezado en todas las páginas
    for (auto page : document->get_Pages())
    {
        page->AddStamp(imageStamp);
    }

    // Guardar documento actualizado
    document->Save(_dataDir + outputFileName);
}
```

## Agregar diferentes Encabezados en un archivo PDF

Sabemos que podemos agregar TextStamp en la sección de Encabezado/Pie de página del documento utilizando las propiedades TopMargin o Bottom Margin, pero a veces podemos tener la necesidad de agregar múltiples encabezados/pies de página en un único documento PDF. **Aspose.PDF para C++** explica cómo hacer esto.

Para cumplir con este requisito, crearemos objetos TextStamp individuales (el número de objetos depende de la cantidad de Encabezados/Pies de página requeridos) y los agregaremos al documento PDF. También podemos especificar diferente información de formato para cada objeto de sello individual. En el siguiente ejemplo, hemos creado un objeto Document y tres objetos TextStamp y luego hemos utilizado el método [AddStamp](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a3b998038dedf5266b4d60586b1b53d02) de la Página para agregar el texto en la sección del encabezado del PDF. El siguiente fragmento de código le muestra cómo agregar una imagen en el pie de página de un archivo PDF con Aspose.PDF para C++.

```cpp
void AddingDifferentHeadersInOnePDFFile()
{
    String _dataDir("C:\\Samples\\");
    String inputFileName("multiheader.pdf");
    String outputFileName("multiheader_out.pdf");

    // Abrir documento fuente
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Crear tres sellos
    auto stamp1 = MakeObject<TextStamp>("Header 1");
    auto stamp2 = MakeObject<TextStamp>("Header 2");
    auto stamp3 = MakeObject<TextStamp>("Header 3");

    // Establecer alineación del sello (colocar sello en la parte superior de la página, centrado horizontalmente)
    stamp1->set_VerticalAlignment(VerticalAlignment::Top);
    stamp1->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Especificar el estilo de fuente como Negrita
    stamp1->get_TextState()->set_FontStyle(FontStyles::Bold);
    // Establecer información del color de primer plano del texto como rojo
    stamp1->get_TextState()->set_ForegroundColor(Color::get_Red());
    // Especificar el tamaño de fuente como 14
    stamp1->get_TextState()->set_FontSize(14);

    // Ahora necesitamos establecer la alineación vertical del segundo objeto de sello como Superior
    stamp2->set_VerticalAlignment(VerticalAlignment::Top);
    // Establecer información de alineación Horizontal para el sello como Centrados
    stamp2->set_HorizontalAlignment (HorizontalAlignment::Center);
    // Establecer el factor de zoom para el objeto de sello
    stamp2->set_Zoom(10);

    // Establecer el formato del tercer objeto de sello
    // Especificar la información de alineación Vertical para el objeto de sello como SUPERIOR
    stamp3->set_VerticalAlignment(VerticalAlignment::Top);
    // Establecer la información de alineación Horizontal para el objeto de sello como Centrados
    stamp3->set_HorizontalAlignment(HorizontalAlignment::Center);
    // Establecer el ángulo de rotación para el objeto de sello
    stamp3->set_RotateAngle(35);
    // Establecer rosa como color de fondo para el sello
    stamp3->get_TextState()->set_BackgroundColor(Color::get_Pink());
    // Cambiar la información de la cara de la fuente para el sello a Verdana
    stamp3->get_TextState()->set_Font(FontRepository::FindFont(u"Verdana"));

    // El primer sello se añade en la primera página;
    document->get_Pages()->idx_get(1)->AddStamp(stamp1);
    // El segundo sello se añade en la segunda página;
    document->get_Pages()->idx_get(2)->AddStamp(stamp2);
    // El tercer sello se añade en la tercera página.
    document->get_Pages()->idx_get(3)->AddStamp(stamp3);

    // Guardar documento actualizado
    document->Save(_dataDir + outputFileName);
}
```