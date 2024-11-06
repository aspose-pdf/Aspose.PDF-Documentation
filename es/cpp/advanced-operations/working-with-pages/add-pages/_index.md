---
title: Agregar Páginas en PDF con C++
linktitle: Agregar Páginas
type: docs
weight: 10
url: es/cpp/add-pages/
description: Este artículo enseña cómo insertar (agregar) una página en la ubicación deseada de un archivo PDF. Aprenda cómo mover, eliminar (borrar) páginas de un archivo PDF usando C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Esta sección muestra cómo agregar páginas a un PDF usando la biblioteca **Aspose.PDF para C++**.

Aspose.PDF para C++ API proporciona total flexibilidad para trabajar con páginas en un documento PDF usando C++.

Mantiene todas las páginas de un documento PDF en [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) que se puede usar para trabajar con páginas PDF.
Aspose.PDF para C++ le permite insertar una página en un documento PDF en cualquier ubicación en el archivo, así como agregar páginas al final de un archivo PDF.

## Agregar o Insertar Página en un Archivo PDF

Aspose.PDF para C++ le permite insertar una página en un documento PDF en cualquier ubicación en el archivo, así como agregar páginas al final de un archivo PDF.

### Insertar Página Vacía en un Archivo PDF en la Ubicación Deseada

El siguiente ejemplo de código te explica cómo agregar una página en un documento PDF.

1. Crea un objeto de la clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el archivo PDF de entrada.
1. Llama al método [Insert](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#a1fb1fe44df4d325df5ad41b691501bb2) de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection) con el índice especificado.
1. Guarda el PDF de salida.

El siguiente fragmento de código te muestra cómo insertar una página en un archivo PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;


void InsertEmptyPageAtDesiredLocation() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insertar una página vacía en un PDF
    document->get_Pages()->Insert(2);

    // Guardar archivo de salida
    document->Save(_dataDir + outputFileName);
}
```

En el siguiente ejemplo de código, puede insertar una página vacía en la ubicación deseada copiando los parámetros de la página especificada:

```cpp
void InsertEmptyPageAtDesiredLocation2() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String inputFileName("InsertEmptyPage.pdf");

    String outputFileName("InsertEmptyPage_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);
    auto page = document->get_Pages()->idx_get(1);
    // Insertar una página vacía en un PDF
    auto pageNew = document->get_Pages()->Insert(2);

    // copiar parámetros de la página 1
    pageNew->set_ArtBox(page->get_ArtBox());
    pageNew->set_BleedBox(page->get_BleedBox());
    pageNew->set_CropBox(page->get_CropBox());
    pageNew->set_MediaBox(page->get_MediaBox());
    pageNew->set_TrimBox(page->get_TrimBox());

    // Guardar archivo de salida
    document->Save(_dataDir + outputFileName);
}
```

### Agregar una Página Vacía al Final de un Archivo PDF

A veces, desea asegurarse de que un documento termine en una página vacía. Este tema explica cómo insertar una página vacía al final del documento PDF.

Para insertar una página vacía al final de un archivo PDF:

1. Cree un objeto de clase [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) con el archivo PDF de entrada.
1. Llame al método [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection#abb0362ffa129a1e2e5650a2f2e7057c1) de la colección [PageCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page_collection), sin ningún parámetro.
1. Guarde el PDF de salida usando el método Save.

El siguiente fragmento de código muestra cómo insertar una página vacía al final de un archivo PDF.

```cpp
void AddEmptyPageEnd() {
    // Abrir documento
    String _dataDir("C:\\Samples\\");

    // Cadena para el nombre del archivo de entrada
    String inputFileName("InsertEmptyPageAtEnd.pdf");
    String outputFileName("InsertEmptyPageAtEnd_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    // Insertar una página vacía al final de un archivo PDF
    document->get_Pages()->Add();

    // Guardar archivo de salida
    document->Save(_dataDir + outputFileName);
}
```