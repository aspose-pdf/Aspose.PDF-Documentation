---
title: Eliminar páginas PDF programáticamente 
linktitle: Eliminar páginas PDF
type: docs
weight: 30
url: es/cpp/delete-pages/
description: Puede eliminar páginas de su archivo PDF utilizando la biblioteca C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Puede eliminar páginas de un archivo PDF usando Aspose.PDF para C++. Para eliminar una página en particular de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).

## Eliminar página de archivo PDF

1. Llame al método [Delete](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page#a02bb7a96e66ef6e10bcf4930b299b3b7) y especifique el índice de la página
1. Llame al método Save para guardar el archivo PDF actualizado
El siguiente fragmento de código muestra cómo eliminar una página en particular del archivo PDF usando C++.

```cpp
void DeletePDFPages() {
    String _dataDir("C:\\Samples\\");
    String inputFileName("DeleteParticularPage.pdf");

    // Abrir documento
    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Eliminar una página en particular
    document->get_Pages()->Delete(2);

    // Guardar PDF actualizado
    document->Save(_dataDir + inputFileName);
}
```