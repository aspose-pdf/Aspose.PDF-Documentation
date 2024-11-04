---
title: Fusionar PDF usando C++
linktitle: Fusionar archivos PDF
type: docs
weight: 50
url: /cpp/merge-pdf-documents/
description: Esta página explica cómo fusionar documentos PDF en un solo archivo PDF con C++.
lastmod: "2021-11-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Fusionar archivos PDF no es una tarea fácil, pero es muy popular. Puedes usar la biblioteca Aspose.PDF para C++ para combinar archivos PDF en un documento de manera rápida y sencilla.

## Fusionar archivos PDF usando C++

Para concatenar dos archivos PDF:

1. Crea dos objetos [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), cada uno conteniendo uno de los archivos PDF de entrada.
1. Luego llama al método Add de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) para el objeto Document al que quieres añadir el otro archivo PDF.
1. Añade [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) del segundo documento al primer archivo.
1. Finalmente, guarda el archivo PDF de salida usando el método Save.

El siguiente fragmento de código muestra cómo concatenar archivos PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
void MergingDocuments() {
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String pdfDocumentFileName1("Concat1.pdf");
    String pdfDocumentFileName2("Concat2.pdf");
    String outputFileName("ConcatenatePdfFiles.pdf");

    // Abrir documento
    auto pdfDocument1 = MakeObject<Document>(_dataDir + pdfDocumentFileName1);
    auto pdfDocument2 = MakeObject<Document>(_dataDir + pdfDocumentFileName2);

    // Agregar páginas del segundo documento al primero
    pdfDocument1->get_Pages()->Add(pdfDocument2->get_Pages());

    // Guardar archivo de salida concatenado
    pdfDocument1->Save(_dataDir+outputFileName);
}
```

## Ejemplo en Vivo

[Aspose.PDF Merger](https://products.aspose.app/pdf/merger) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de fusión de presentaciones.

[![Aspose.PDF Merger](merger.png)](https://products.aspose.app/pdf/merger)