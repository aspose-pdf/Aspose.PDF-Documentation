---
title: Dividir PDF programáticamente
linktitle: Dividir archivos PDF
type: docs
weight: 60
url: /cpp/split-pdf-document/
description: Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales con C++.
lastmod: "2022-09-01"
sitemap:
    changefreq: "monthy"
    priority: 0.7
---

## Ejemplo en vivo

[Aspose.PDF Splitter](https://products.aspose.app/pdf/splitter) es una aplicación web gratuita en línea que te permite investigar cómo funciona la funcionalidad de división de presentaciones.

[![Aspose Split PDF](splitter.png)](https://products.aspose.app/pdf/splitter)

Este tema muestra cómo dividir páginas de PDF en archivos PDF individuales en tus aplicaciones C++. Para dividir páginas de PDF en archivos PDF de una sola página usando C++, se pueden seguir los siguientes pasos:

1. Recorre las páginas del documento PDF a través de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Para cada iteración, crea un nuevo objeto Document y copia el objeto [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) individual en el documento vacío.  
1. Guarda el nuevo PDF usando el método Save.

El siguiente fragmento de código C++ te muestra cómo dividir páginas PDF en archivos PDF individuales.

```cpp
void SplittingDocuments() {
    // Cadena para el nombre de la ruta
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String documentFileName("sample.pdf");
    
    // Abre el documento
    auto document = MakeObject<Document>(_dataDir + documentFileName);

    int pageCount = 1;

    // Recorre todas las páginas
    for(auto page : document->get_Pages())
    {
        auto newDocument = MakeObject<Document>(_dataDir + documentFileName);
        newDocument->get_Pages()->CopyPage(page);
        newDocument->Save(_dataDir + u"page_" + pageCount + u"_out.pdf");
        pageCount++;
    }
}
```