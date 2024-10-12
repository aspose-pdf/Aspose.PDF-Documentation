---
title: Mover páginas de PDF programáticamente C++
linktitle: Mover páginas de PDF
type: docs
weight: 20
url: /cpp/move-pages/
description: Intente mover páginas a la ubicación deseada o al final de un archivo PDF usando Aspose.PDF para C++.
lastmod: "2021-12-09"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mover una página de un documento PDF a otro

Mover páginas de PDF en un documento es una tarea muy interesante y popular. Este tema explica cómo mover una página de un documento PDF al final de otro documento usando C++. Para mover una página debemos:

1. Crear un objeto de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el archivo PDF de origen.
1. Obtener la página de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Agregar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) la página al documento de destino.
1. Guardar el PDF de salida usando el método Save.
1. [Eliminar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) página en el documento fuente.
1. Guarde el PDF fuente usando el método Save.

El siguiente fragmento de código te muestra cómo mover una página.

```cpp
void MovePage()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    dstDocument->get_Pages()->Add(page);
    // Guardar archivo de salida
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete(2);
    srcDocument->Save(dstFileName);
}
```

## Mover un conjunto de páginas de un documento PDF a otro

1. Cree un objeto de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el archivo PDF fuente.
1. Defina un arreglo con los números de página a mover.
1. Recorrer bucle a través de un array:
1. Obtener Página de la colección de [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Agregar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) página al documento de destino.
1. Guardar el PDF de salida usando el método Guardar.
1. [Eliminar](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) página en el documento fuente.
1. Guardar el PDF de origen usando el método Guardar.

El siguiente fragmento de código muestra cómo insertar una página vacía al final de un archivo PDF.

```cpp
void MoveBunchPages()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();


    auto pages = MakeArray<int>({ 1,3 });

    for (auto pageIndex : pages)
    {
        auto page = srcDocument->get_Pages()->idx_get(pageIndex);
        dstDocument->get_Pages()->Add(page);
    }
    // Guardar archivos de salida
    dstDocument->Save(srcFileName);
    srcDocument->get_Pages()->Delete();
    srcDocument->Save(dstFileName);
}
```
## Mover una página a una nueva ubicación en el documento PDF actual

1. Cree un objeto de clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el archivo PDF de origen.
1. Obtenga la página de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection).
1. [Añada](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) la página a la nueva ubicación (por ejemplo, al final).
1. [Elimine](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#afaa57836d1b206e396f2cb7dd91b5d15) la página en la ubicación anterior.
1. Guarde el archivo PDF de salida utilizando el método Save.

```cpp
void MovePagesInOnePDF()
{
    // Abrir documento
    String _dataDir("C:\\Samples\\");
    String srcFileName("<enter file name>");
    String dstFileName("<enter file name>");

    auto srcDocument = MakeObject<Document>(_dataDir + srcFileName);
    auto dstDocument = MakeObject<Document>();

    auto page = srcDocument->get_Pages()->idx_get(2);
    srcDocument->get_Pages()->Add(page);
    srcDocument->get_Pages()->Delete(2);

    // Guardar archivo de salida
    srcDocument->Save(dstFileName);
}
```