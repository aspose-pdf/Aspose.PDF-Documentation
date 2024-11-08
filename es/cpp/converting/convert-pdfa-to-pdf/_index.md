---
title: Convertir PDF/A a formato PDF 
linktitle: Convertir PDF/A a formato PDF
type: docs
weight: 110
url: /es/cpp/convert-pdfa-to-pdf/
lastmod: "2021-11-19"
description: Este tema le muestra cómo Aspose.PDF permite convertir un archivo PDF/A a un documento PDF con la biblioteca C++. 
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## Convertir documento PDF/A a PDF

Convertir un documento PDF/A a PDF significa eliminar la restricción <abbr title="Archivo de Formato de Documento Portátil
">PDF/A</abbr> del documento original. La clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) tiene el método 'RemovePdfaCompliance' para eliminar la información de cumplimiento de PDF del archivo de entrada/origen.
Después de [Guardar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document#ac082fe8e67b25685fc51d33e804269fa) el archivo de entrada.

```cpp
void ConvertPDFAtoPDF()
{
    std::clog << "Conversión de PDF/A a PDF: Inicio" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);

    // Eliminar información de cumplimiento de PDF/A
    document->RemovePdfaCompliance();

    // Guardar documento actualizado
    document->Save(_dataDir + outfilename);
    std::clog << "Conversión de PDF/A a PDF: Fin" << std::endl;
}
```

Esta información también se elimina si realizas cambios en el documento (por ejemplo, agregar páginas). En el siguiente ejemplo, el documento de salida pierde la conformidad con PDF/A después de agregar la página.

```cpp
void ConvertPDFAtoPDFAdvanced()
{
    std::clog << "PDF/A to PDF convert: Start" << std::endl;
    String _dataDir("C:\\Samples\\Conversion\\");
    String infilename("sample-pdfa.pdf");
    String outfilename("PDFAToPDF_out.pdf");

    auto document = MakeObject<Document>(_dataDir + infilename);
    // Adding a new (empty) page removes PDF/A compliance information.

    document->get_Pages()->Add();
    // Save updated document
    document->Save(_dataDir + outfilename);
    std::clog << "PDF/A to PDF convert: End" << std::endl;
}
```