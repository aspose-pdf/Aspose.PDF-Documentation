---
title: Update, Delete and Get Bookmarks
type: docs
weight: 30
url: /net/update-delete-and-get-bookmarks/
description: Esta sección explica cómo actualizar, eliminar y obtener marcadores con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Actualizar un Marcador Existente en el Archivo PDF

Para actualizar un marcador existente en un archivo PDF, necesita usar el método [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks). Este método toma dos argumentos: título de origen (el título del marcador a modificar), título de destino (el título que se va a reemplazar). Necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas llamar al método [ModifyBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/modifybookmarks), y luego guardar el PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo modificar un marcador existente en un archivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-UpdateBookmark-UpdateBookmark.cs" >}}

## Eliminar todos los marcadores del archivo PDF

Puedes eliminar todos los marcadores del archivo PDF utilizando el método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) sin ningún parámetro. En primer lugar, necesitas crear un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y enlazar el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas llamar al método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) y luego guardar el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo eliminar todos los marcadores del archivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteAllBookmarks-DeleteAllBookmarks.cs" >}}

## Eliminar un Marcador Particular de un Archivo PDF

Para eliminar un marcador particular, necesitas llamar al método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) con el parámetro de cadena (título). El *título* aquí representa el marcador que se eliminará del PDF. Cree un objeto de la clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincule el archivo PDF de entrada utilizando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, llame al método [DeleteBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor/methods/deletebookmarks) y luego guarde el archivo PDF actualizado utilizando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código le muestra cómo eliminar un marcador particular de un archivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-DeleteABookmark-DeleteABookmark.cs" >}}

## Obtener marcadores del documento PDF Facades

La clase [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) proporciona la funcionalidad para manipular marcadores en un archivo PDF existente. Proporciona varias propiedades para obtener/establecer información sobre los marcadores. El siguiente fragmento de código muestra cómo obtener información relacionada con cada marcador en un archivo PDF.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-GetFromPDF-GetFromPDF.cs" >}}

## Extraer marcadores de un archivo PDF existente

El método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) te permite extraer marcadores de un archivo PDF. En orden de extraer los marcadores, necesitas crear un objeto [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y enlazar el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3). Después de eso, necesitas llamar al método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3). El método [ExtractBookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/extractbookmarks/methods/3) devuelve el objeto [Bookmarks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmarks/methods/index). Luego puedes recorrer estos marcadores y obtener objetos [Bookmark](https://reference.aspose.com/pdf/net/aspose.pdf.facades/bookmark) individuales. Finalmente, guarda el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo exportar marcadores a un archivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExtractBookmarks-ExtractBookmarks.cs" >}}