---
title: Guardar Documento PDF usando C++
linktitle: Guardar
type: docs
weight: 30
url: es/cpp/save-pdf-document/
description: Aprenda cómo guardar un archivo PDF con la biblioteca Aspose.PDF para C++.
lastmod: "2021-11-01"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Guardar documento PDF en el sistema de archivos

Puede guardar el documento PDF creado o manipulado en el sistema de archivos usando el método Save de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).

```cpp
void SaveDocument()
{
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);
    // realizar alguna manipulación, por ejemplo, agregar una nueva página vacía
    document->get_Pages()->Add();
    document->Save(_dataDir + modifiedFileName);
}
```

## Guardar documento PDF en flujo

También puede guardar el documento PDF creado o manipulado en un flujo usando sobrecargas de los métodos Save.

```cpp
void SaveDocumentStream()
{
    // Cadena para nombre de ruta
    String _dataDir("C:\\Samples\\");

    String originalFileName("SimpleResume.pdf");
    String modifiedFileName("SimpleResumeModified.pdf");

    auto document = MakeObject<Document>(_dataDir + originalFileName);

    // realizar alguna manipulación, por ejemplo, agregar una nueva página vacía
    document->get_Pages()->Add();

    auto fileStream = System::IO::File::OpenWrite(_dataDir + modifiedFileName);
    document->Save(fileStream);
}
```

## Guardar en formato PDF/A o PDF/X

PDF/A es una versión del Formato de Documento Portátil (PDF) estandarizada por ISO para su uso en el archivo y la preservación a largo plazo de documentos electrónicos. PDF/A se diferencia de PDF en que prohíbe características no adecuadas para el archivo a largo plazo, como el enlace de fuentes (a diferencia de la incrustación de fuentes) y el cifrado. Los requisitos ISO para los visores de PDF/A incluyen pautas de gestión de color, soporte de fuentes incrustadas y una interfaz de usuario para leer anotaciones incrustadas.

PDF/X es un subconjunto del estándar ISO PDF. El propósito de PDF/X es facilitar el intercambio de gráficos y, por lo tanto, tiene una serie de requisitos relacionados con la impresión que no se aplican a los archivos PDF estándar.

En ambos casos, el método Guardar se utiliza para almacenar los documentos, mientras que los documentos deben ser preparados usando las [PdfFormatConversionOptions](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.pdf_format_conversion_options).

```cpp
void SaveDocumentAsPDFx()
{
    // String para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // String para el nombre del archivo
    String infilename("SimpleResume.pdf");
    String outfilename("SimpleResume_A3U.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    auto options = new PdfFormatConversionOptions(Aspose::Pdf::PdfFormat::PDF_A_3U);
    try
    {
        document->Convert(options);
    }
    catch (const std::exception& e)
    {
        std::cerr << e.what();
    }

    document->Save(_dataDir + outfilename);
}
```