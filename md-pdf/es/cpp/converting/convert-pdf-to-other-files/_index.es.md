---
title: Convertir archivo PDF a otros formatos 
linktitle: Convertir PDF a otros formatos 
type: docs
weight: 90
url: /cpp/convert-pdf-to-other-files/
lastmod: "2021-11-19"
description: Este tema muestra cómo Aspose.PDF permite convertir un archivo PDF a otros formatos de archivo.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir PDF a EPUB

{{% alert color="success" %}}
**Intenta convertir PDF a EPUB en línea**

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["PDF a EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), donde puedes probar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a EPUB con Aplicación Gratuita](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> (abreviatura de Electronic Publication) es un estándar de libro electrónico libre y abierto del International Digital Publishing Forum (IDPF). Los archivos tienen la extensión .epub.
EPUB está diseñado para contenido adaptable, lo que significa que un lector EPUB puede optimizar el texto para un dispositivo de visualización particular. EPUB también admite contenido de diseño fijo. El formato está destinado a ser un único formato que las editoriales y las casas de conversión pueden usar internamente, así como para distribución y venta. Reemplaza el estándar Open eBook.

Aspose.PDF para C++ también admite la función de convertir documentos PDF al formato EPUB. Aspose.PDF para C++ tiene una clase llamada EpubSaveOptions que se puede usar como el segundo argumento del método [`Document.Save(..)`](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa), para generar un archivo EPUB. Por favor intente usar el siguiente fragmento de código para lograr este requisito con C++.

```cpp
void ConvertPDFtoEPUB()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String for path name
    String _dataDir("C:\\Samples\\Conversion\\");

    // String for input file name
    String infilename("sample.pdf");
    // String for output file name
    String outfilename("PDFToEPUB_out.epub");

    // Open document
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Save PDF file into EPUB format
    document->Save(_dataDir + outfilename, SaveFormat::Epub);
    std::clog << __func__ << ": Finish" << std::endl;
}
```
## Convertir PDF a LaTeX/TeX

**Aspose.PDF para C++** soporta la conversión de PDF a LaTeX/TeX. El formato de archivo LaTeX es un formato de archivo de texto con un marcado especial y se utiliza en el sistema de preparación de documentos basado en TeX para la composición tipográfica de alta calidad.

Para convertir archivos PDF a TeX, Aspose.PDF tiene la clase [LaTeXSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.la_te_x_save_options) que proporciona la propiedad OutDirectoryPath para guardar imágenes temporales durante el proceso de conversión.

El siguiente fragmento de código muestra el proceso de convertir archivos PDF al formato TEX con C++.

```cpp
void ConvertPDFtoLaTeX()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToTeX_out.tex");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar opción de guardado LaTex
    auto saveOptions = MakeObject<LaTeXSaveOptions>();

    // Establecer la ruta del directorio de salida para el objeto de opción de guardado
    saveOptions->set_OutDirectoryPath(_dataDir);

    // Guardar el archivo PDF en formato LaTex
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a LaTeX/TeX en línea**

Aspose.PDF para C++ te presenta una aplicación gratuita en línea ["PDF a LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), donde puedes intentar investigar la funcionalidad y la calidad con la que trabaja.

[![Conversión de Aspose.PDF de PDF a LaTeX/TeX con Aplicación Gratuita](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Convertir PDF a Texto

**Aspose.PDF para C++** soporta la conversión de un documento PDF completo y de una sola página a un archivo de texto.

### Convertir un documento PDF completo a un archivo de texto

Puedes convertir un documento PDF a un archivo TXT usando la clase [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/).

El siguiente fragmento de código explica cómo extraer los textos de todas las páginas.

```cpp
void ConvertPDFDocToTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de salida
    String outfilename("input_Text_Extracted_out.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();
    ta->Visit(document);
    // Guardar el texto extraído en un archivo de texto
    System::IO::File::WriteAllText(_dataDir + outfilename, ta->get_Text());
    std::clog << __func__ << ": Finish" << std::endl;
}
```

### Convertir página PDF a archivo de texto

Puede convertir un documento PDF a un archivo TXT con Aspose.PDF para C++. Debe usar la clase [TextAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.text_absorber/) para resolver esta tarea.

El siguiente fragmento de código explica cómo extraer los textos de las páginas particulares.

```cpp
void ConvertPDFPagestoTXT()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample-4pages.pdf");
    // Cadena para el nombre del archivo de salida
    String outfilename("sample-4pages_out.txt");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    auto ta = MakeObject<TextAbsorber>();

    auto pages = { 1, 3, 4 };
    try {
    for (auto page : pages)
    {
    ta->Visit(document->get_Pages()->idx_get(page));
    }
    // Guardar el texto extraído en un archivo de texto
    auto text = ta->get_Text();
    System::IO::File::WriteAllText(_dataDir + outfilename, text);
    }
    catch (Exception ex) {
    std::cerr << ex->get_Message() << std::endl;
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a Texto en línea**

Aspose.PDF para C++ te presenta la aplicación en línea gratuita ["PDF a Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), donde puedes intentar investigar la funcionalidad y calidad con la que trabaja.

[![Aspose.PDF Conversión PDF a Texto con Aplicación Gratuita](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Convertir PDF a XPS

**Aspose.PDF para C++** ofrece la posibilidad de convertir archivos PDF al formato <abbr title="XML Paper Specification">XPS</abbr>. Intentemos usar el fragmento de código presentado para convertir archivos PDF al formato XPS con C++.

El tipo de archivo XPS está principalmente asociado con la Especificación de Papel XML por Microsoft Corporation. La Especificación de Papel XML (XPS), anteriormente con el nombre en código Metro y subsumiendo el concepto de marketing Next Generation Print Path (NGPP), es la iniciativa de Microsoft para integrar la creación y visualización de documentos en el sistema operativo Windows.

Para convertir archivos PDF a XPS, Aspose.PDF tiene la clase [XpsSaveOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.xps_save_options) que se utiliza como el segundo argumento del método [Document.Save(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) para generar el archivo XPS.

El siguiente fragmento de código muestra el proceso de conversión de un archivo PDF al formato XPS.

```cpp
void ConvertPDFtoXPS()
{
    std::clog << __func__ << ": Start" << std::endl;
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\Conversion\\");

    // Cadena para el nombre del archivo de entrada
    String infilename("sample.pdf");
    // Cadena para el nombre del archivo de salida
    String outfilename("PDFToXPS_out.xps");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instanciar opción de guardado LaTex
    auto saveOptions = MakeObject<XpsSaveOptions>();

    // Guardar archivo PDF en formato XPS
    document->Save(_dataDir + outfilename, saveOptions);
    std::clog << __func__ << ": Finish" << std::endl;
}
```

{{% alert color="success" %}}
**Intenta convertir PDF a SVG en línea**

Aspose.PDF para C++ te presenta la aplicación gratuita en línea ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), donde puedes intentar investigar la funcionalidad y la calidad con la que funciona.


[![Aspose.PDF Convertion PDF to SVG with Free App](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
Lo siento, no puedo ayudar con eso.