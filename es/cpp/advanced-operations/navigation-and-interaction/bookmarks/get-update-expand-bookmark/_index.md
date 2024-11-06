---
title: Obtener, Actualizar y Expandir un Marcador
linktitle: Obtener, Actualizar y Expandir un Marcador
type: docs
weight: 20
url: es/cpp/get-update-and-expand-bookmark/
description: La biblioteca Aspose.PDF para C++ le permite obtener y actualizar en un archivo PDF con nuestro.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Obtener Marcadores

La colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) del objeto [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document) contiene todos los marcadores de un archivo PDF. Este artículo explica cómo obtener marcadores de un archivo PDF y cómo obtener en qué página se encuentra un marcador en particular.

Para obtener los marcadores, recorra la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection) y obtenga cada marcador en la OutlineItemCollection. El OutlineItemCollection proporciona acceso a todos los atributos del marcador. El siguiente fragmento de código muestra cómo obtener marcadores del archivo PDF.

```cpp
void GettingBookmarks() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Recorrer todos los marcadores

for (auto outlineItem : pdfDocument->get_Outlines()) {


Console::WriteLine(u"Título :- " + outlineItem->get_Title());


Console::WriteLine(u"Es Cursiva :- " + outlineItem->get_Italic());


Console::WriteLine(u"Es Negrita :- " + outlineItem->get_Bold());


Console::WriteLine(u"Color :- {0}", outlineItem->get_Color());

}
}
```

## Obtener el Número de Página de un Marcador

Una vez que hayas agregado un marcador, puedes averiguar en qué página está obteniendo el PageNumber de destino asociado con el objeto Bookmark.

```cpp
void GettingBookmarksPageNumber() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Crear PdfBookmarkEditor

auto bookmarkEditor = MakeObject<Aspose::Pdf::Facades::PdfBookmarkEditor>();

// Abrir archivo PDF

bookmarkEditor->BindPdf(_dataDir + u"UpdateBookmarks.pdf");

// Extraer marcadores

auto bookmarks = bookmarkEditor->ExtractBookmarks();

for (auto bookmark : bookmarks) {


String strLevelSeprator("");


for (int i = 1; i < bookmark->get_Level(); i++) {



strLevelSeprator += u"---- ";


}


Console::WriteLine(u"Título :- " + strLevelSeprator + bookmark->get_Title());


Console::WriteLine(u"Número de Página :- " + strLevelSeprator + bookmark->get_PageNumber());


Console::WriteLine(u"Acción de Página :- " + strLevelSeprator + bookmark->get_Action());

}
}
```
## Actualizar Marcadores en un Documento PDF

Para actualizar un marcador en un archivo PDF, primero obtén el marcador específico de la colección OutlineColletion del objeto Document especificando el índice del marcador. Una vez que hayas recuperado el marcador en el objeto [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection), puedes actualizar sus propiedades y luego guardar el archivo PDF actualizado utilizando el método Save. Los siguientes fragmentos de código muestran cómo actualizar marcadores en un documento PDF.

```cpp
void UpdateBookmarksInPDFDocument() {

String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Obtener un objeto de marcador

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// Actualizar el objeto de marcador

pdfOutline->set_Title(u"Updated Outline");

pdfOutline->set_Italic(true);

pdfOutline->set_Bold(true);

// Establecer la página de destino como 2

pdfOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));

// Guardar salida

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Actualizar Marcadores Hijos en un Documento PDF

Para actualizar un marcador hijo:

1. Recupere el marcador hijo que desea actualizar del archivo PDF obteniendo primero el marcador principal y luego el marcador hijo utilizando valores de índice apropiados.
1. Guarde el archivo PDF actualizado utilizando el método Save.

{{% alert color="primary" %}}

Obtenga un marcador de la colección OutlineCollection del objeto Document especificando el índice del marcador, y luego obtenga el marcador hijo especificando el índice de este marcador principal.

{{% /alert %}}

El siguiente fragmento de código le muestra cómo actualizar marcadores hijos en un documento PDF.

```cpp
void UpdateChildBookmarksInPDFDocument() {


String _dataDir("C:\\Samples\\Bookmarks\\");

// Abrir documento

auto pdfDocument = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// Obtener un objeto de marcador

auto pdfOutline = pdfDocument->get_Outlines()->idx_get(1);

// Obtener objeto de marcador hijo

auto childOutline = pdfOutline->idx_get(1);


// Actualizar el objeto de marcador

childOutline->set_Title(u"Updated Outline");

childOutline->set_Italic(true);

childOutline->set_Bold(true);

// Establecer la página de destino como 2

childOutline->set_Destination(MakeObject<Aspose::Pdf::Annotations::GoToAction>(pdfDocument->get_Pages()->idx_get(2)));


// Guardar salida

pdfDocument->Save(_dataDir + u"Bookmarkupdated_output.pdf");
}
```

## Marcadores ampliados al ver el documento

Los marcadores se mantienen en la colección [OutlineItemCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_item_collection) del objeto Document, que a su vez está en la colección [OutlineCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.outline_collection). Sin embargo, podemos tener el requisito de que todos los marcadores estén expandidos al ver el archivo PDF.

Para cumplir con este requisito, podemos establecer el estado abierto para cada elemento de esquema/marcador como Abierto. El siguiente fragmento de código muestra cómo establecer el estado abierto para cada marcador como expandido en un documento PDF.

```cpp
void ExpandedBookmarks() {


String _dataDir("C:\\Samples\\Bookmarks\\");


auto doc = MakeObject<Document>(_dataDir + u"UpdateBookmarks.pdf");

// establecer el modo de vista de página, es decir, mostrar miniaturas, pantalla completa, mostrar panel de adjuntos

doc->set_PageMode(PageMode::UseOutlines);

// imprimir el conteo total de marcadores en el archivo PDF

Console::WriteLine(doc->get_Outlines()->get_Count());

// recorrer cada elemento de esquema en la colección de esquemas del archivo PDF

for (int counter = 1; counter <= doc->get_Outlines()->get_Count(); counter++) {


// establecer estado abierto para el elemento de esquema


doc->get_Outlines()->idx_get(counter)->set_Open(true);

}

// guardar el archivo PDF

doc->Save(_dataDir + u"Bookmarks_Expanded.pdf");
}
```