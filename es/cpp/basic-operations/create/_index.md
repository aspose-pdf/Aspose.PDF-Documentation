---
title: Crear Documento PDF usando C++
linktitle: Crear
type: docs
weight: 10
url: es/cpp/create-document/
description: La tarea más popular y básica al trabajar con un archivo PDF es crear un documento desde cero. Utilice la biblioteca Aspose.PDF para C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF para C++** API permite a los desarrolladores de aplicaciones C++ integrar la funcionalidad de procesamiento de documentos PDF en sus aplicaciones. Se puede utilizar para crear y leer archivos PDF sin la necesidad de tener instalado ningún otro software en la máquina subyacente. Aspose.PDF para C++ se puede usar en una variedad de tipos de aplicaciones C++ como QT, MFC y aplicaciones de consola.

## Cómo crear un archivo PDF usando C++

Para crear un archivo PDF usando C++, se pueden seguir los siguientes pasos.

1. Instanciar un objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document)
1. Agregar una [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page/) al objeto del documento
1. Crea un objeto [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/)
1. Añade [TextFragment](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.te_x_fragment/) a la colección [Paragraph](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.paragraphs/) de la página
1. Guarda el documento PDF resultante

```cpp
void CreatePDF() {
    // Cadena para el nombre de la ruta.
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo.
    String filename("sample-new.pdf");

    // Inicializar objeto de documento
    auto document = MakeObject<Document>();
    // Añadir página
    auto page = document->get_Pages()->Add();

    // Añadir texto a la nueva página
    auto textFragment = MakeObject<TextFragment>(u"Hello World!");
    page->get_Paragraphs()->Add(textFragment);

    // Guardar PDF actualizado
    String outputFileName = _dataDir + filename;

    document->Save(outputFileName);
}
```