---
title: Convertir archivo PDF a formato HTML 
linktitle: Convertir archivo PDF a formato HTML
type: docs
weight: 50
url: es/cpp/convert-pdf-to-html/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a formato HTML con la biblioteca C++.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

**Aspose.PDF para C++** proporciona muchas características para convertir varios formatos de archivo en documentos PDF y convertir archivos PDF en varios formatos de salida. Este artículo discute cómo convertir un archivo PDF en <abbr title="Lenguaje de Marcado de Hipertexto">HTML</abbr>. Aspose.PDF para C++ ofrece la capacidad de convertir archivos HTML en formato PDF usando el enfoque InLineHtml. Hemos tenido muchas solicitudes para la funcionalidad que convierte un archivo PDF en formato HTML y hemos proporcionado esta característica. Tenga en cuenta que esta función también admite XHTML 1.0.

**Aspose.PDF para C++** soporta las características para convertir un archivo PDF en HTML. Las principales tareas que puedes realizar con la biblioteca Aspose.PDF se enumeran:

- convertir PDF a HTML;
- dividir salida en HTML de varias páginas;
- especificar carpeta para almacenar archivos SVG;
- comprimir imágenes SVG durante la conversión;
- especificar la carpeta de imágenes;
- crear archivos subsiguientes solo con contenido del cuerpo;
- renderizar texto transparente;
- renderizar capas del documento PDF.

Aspose.PDF para C++ proporciona un código de dos líneas para transformar un archivo PDF de origen a HTML. La `enumeración SaveFormat` contiene el valor Html que te permite guardar el archivo de origen en HTML. El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF a HTML.

```cpp
void ConvertPDFtoHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    try {
    // Guardar la salida en formato HTML
    document->Save(outfilename, SaveFormat::Html);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```
{{% alert color="success" %}}
**Intenta convertir PDF a HTML en línea**

Aspose.PDF para C++ te presenta la aplicación en línea gratuita ["PDF to HTML"](https://products.aspose.app/pdf/conversion/pdf-to-html), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a HTML con Aplicación Gratis](pdf_to_html.png)](https://products.aspose.app/pdf/conversion/pdf-to-html)
{{% /alert %}}

## Dividir la salida en HTML de varias páginas

Al convertir un archivo PDF grande con varias páginas al formato HTML, la salida aparece como una sola página HTML. Puede terminar siendo muy larga. Para controlar el tamaño de la página, es posible dividir la salida en varias páginas durante la conversión de PDF a HTML. Por favor, intenta usar el siguiente fragmento de código.

```cpp
void ConvertPDFtoHTML_SplittingOutputToMultiPageHTML()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();
    // Especificar dividir la salida en múltiples páginas
    htmlOptions->set_SplitIntoPages(true);

    try {
    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Especificar Carpeta para Almacenar Archivos SVG

Durante la conversión de PDF a HTML, es posible especificar la carpeta en la que se deben guardar las imágenes SVG. Utilize la [`clase HtmlSaveOption`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options) [`propiedad SpecialFolderForSvgImages`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#ac1bb3905c599118fb3db67fd67a5a06f) para especificar un directorio especial de imágenes SVG. Esta propiedad obtiene o establece la ruta al directorio en el cual las imágenes SVG deben ser guardadas cuando se encuentren durante la conversión. Si el parámetro está vacío o es nulo, entonces cualquier archivo SVG se guarda junto con otros archivos de imagen.

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringSVGfiles()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para nombre de archivo
    String infilename("sample.pdf");
    String outfilename("SaveSVGFiles_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado en HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar la carpeta donde se guardan las imágenes SVG durante la conversión de PDF a HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Compresión de Imágenes SVG Durante la Conversión

Para comprimir imágenes SVG durante la conversión de PDF a HTML, por favor intente usar el siguiente código:

```cpp
void ConvertPDFtoHTML_CompressingSVGimages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre del camino
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opciones de Guardado HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar la carpeta donde se guardan las imágenes SVG durante la conversión de PDF a HTML
    htmlOptions->SpecialFolderForSvgImages = (_dataDir + String("\\svg\\"));

    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Especificar la Carpeta de Imágenes

También podemos especificar la carpeta donde se guardarán las imágenes durante la conversión de PDF a HTML:

```cpp
void ConvertPDFtoHTML_SpecifyFolderForStoringAllImages()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String para el nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // String para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("PDFToHTML.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar la carpeta donde se guardan todas las imágenes durante la conversión de PDF a HTML
    htmlOptions->SpecialFolderForAllImages = (_dataDir + String("\\images\\"));

    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Crear archivos subsecuentes solo con el contenido del cuerpo

Recientemente, se nos pidió que introdujéramos una función donde los archivos PDF se convierten a HTML y el usuario puede obtener solo el contenido de la etiqueta `<body>` para cada página. Esto produciría un archivo con CSS, detalles de `<html>`, `<head>` y todas las páginas en otros archivos solo con los contenidos de `<body>`.

Para cumplir con este requisito, se introdujo una nueva propiedad, HtmlMarkupGenerationMode, en la clase [HtmlSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options).

Con el siguiente fragmento de código simple, puedes dividir el HTML de salida en páginas. En las páginas de salida, todos los objetos HTML deben ir exactamente donde van ahora (procesamiento y salida de fuentes, creación y salida de CSS, creación y salida de imágenes), excepto que el HTML de salida contendrá contenidos que actualmente se colocan dentro de las etiquetas (ahora se omitirán las etiquetas "body"). Sin embargo, al usar este enfoque, el enlace al CSS es responsabilidad de tu código, porque cosas como se eliminarán. Para este propósito, puedes leer el CSS a través de File.ReadAllText() y enviarlo vía AJAX a una página web donde se aplicará mediante jQuery.

```cpp
void ConvertPDFtoHTML_CreateSubsequentFilesWithBodyContentsOnly()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("CreateSubsequentFiles_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->set_SplitIntoPages(true);

    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Renderizado de Texto Transparente

En caso de que el archivo PDF de origen/entrada contenga textos transparentes oscurecidos por imágenes de primer plano, entonces podría haber problemas de renderizado de texto. Así que, para atender tales escenarios, se pueden usar las propiedades [SaveShadowedTextsAsTransparentTexts](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.html_save_options#a6269cf414eb8c252f0ba64a0baf2f9ef) y SaveTransparentTexts.

```cpp
void ConvertPDFtoHTML_TransparentTextRendering()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("TransparentTextRendering_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de Opción de Guardado HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    htmlOptions->HtmlMarkupGenerationMode = HtmlSaveOptions::HtmlMarkupGenerationModes::WriteOnlyBodyContent;
    htmlOptions->SaveShadowedTextsAsTransparentTexts = true;
    htmlOptions->SaveTransparentTexts = true;

    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Renderizado de capas de documentos PDF

Podemos renderizar las capas de documentos PDF en un elemento de tipo capa separado durante la conversión de PDF a HTML:

```cpp
void ConvertPDFtoHTML_DocumentLayersRendering()
{
    std::clog << __func__ << ": Inicio" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo
    String infilename("sample.pdf");
    String outfilename("LayersRendering_out.html");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar objeto de opción de guardado HTML
    auto htmlOptions = MakeObject<HtmlSaveOptions>();

    // Especificar renderizar las capas del documento PDF por separado en el HTML de salida
    htmlOptions->set_ConvertMarkedContentToLayers(true);

    // Guardar la salida en formato HTML
    document->Save(_dataDir + outfilename, htmlOptions);
    std::clog << __func__ << ": Fin" << std::endl;
}
```