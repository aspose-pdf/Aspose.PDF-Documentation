---
title: Crear Marcadores
type: docs
weight: 10
url: /net/create-bookmarks/
description: Esta sección explica cómo crear marcadores en su archivo PDF con Aspose.PDF Facades utilizando la Clase PdfBookmarEditor.
lastmod: "2021-06-05"
draft: false
---

## Crear Marcadores de Todas las Páginas

Para crear marcadores de todas las páginas, necesita usar el método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) sin ningún parámetro. La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) le permite crear marcadores de todas las páginas de un archivo PDF. Primero, necesita crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y enlazar el PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debe llamar al método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) y guardar el archivo PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo crear Marcadores.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksAll-CreateBookmarksAll.cs" >}}

## Crear Marcadores de Todas las Páginas con Propiedades

La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) le permite crear marcadores de todas las páginas de un archivo PDF y especificar las propiedades (Color, Negrita, Cursiva). Puedes hacer eso con la ayuda del método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Primero, necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y enlazar el PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, tienes que llamar al método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) y guardar el archivo PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo crear marcadores de todas las páginas con propiedades.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarksPagesProperties-CreateBookmarksPagesProperties.cs" >}}

## Crear un Marcador de una Página en Particular

Puedes crear un marcador de una página en particular en un archivo PDF existente usando el método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1). Este método toma dos argumentos: título del marcador y número de página. Primero, necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y enlazar el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debes llamar al método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) y guardar el archivo PDF de salida usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo crear un marcador de una página en particular.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPage-CreateBookmarkPage.cs" >}}

## Crear marcadores de un rango de páginas

La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) te permite crear marcadores de un rango de páginas. Puedes utilizar el método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) con dos parámetros: lista de marcadores (la lista de los títulos de los marcadores) y lista de páginas (la lista de las páginas para marcar). Primero, necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y enlazar el archivo PDF de entrada usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Luego, debes llamar al método [CreateBookmarkOfPage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarkofpage/methods/1) y guardar el PDF de salida utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo crear marcadores de un rango de páginas.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-CreateBookmarkPageRange-CreateBookmarkPageRange.cs" >}}
## Añadir Marcador en un Archivo PDF Existente

Puede añadir un marcador en un archivo PDF existente utilizando la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Para crear el marcador, necesita crear un objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) y establecer los atributos requeridos del marcador. Después de eso, debe pasar el objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) al método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2) de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). Finalmente, necesita guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo añadir el marcador en un archivo PDF existente.




{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-AddBookmark-AddBookmark.cs" >}}

## Agregar Marcador Hijo en un Archivo PDF Existente

Puede agregar marcadores hijos en un archivo PDF existente usando la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). En orden de añadir marcadores secundarios, necesitas crear objetos [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark). You can add individual [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) objects into [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks) object.

Puedes agregar objetos [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) individuales en el objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Necesitas crear un objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) y configurar su propiedad [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) a un objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks). Luego, necesitas pasar este objeto [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) con [ChildItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark/properties/childitem) al método [CreateBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/createbookmarks/methods/2). Finalmente, necesitas guardar el PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor). El siguiente fragmento de código te muestra cómo añadir marcadores secundarios en un archivo PDF existente.
## Ver también

Intenta comparar y encontrar una manera de trabajar con marcadores que te convenga. Aprendamos la sección [Trabajando con marcadores en PDF](/pdf/net/bookmarks/).