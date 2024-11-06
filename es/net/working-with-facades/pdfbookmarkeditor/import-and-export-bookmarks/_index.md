---
title: Importar y Exportar Marcadores
type: docs
weight: 20
url: es/net/import-and-export-bookmarks/
description: Esta sección explica cómo importar y exportar Marcadores con Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Importar Marcadores desde XML a un Archivo PDF Existente

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) método le permite importar marcadores a un archivo PDF desde un archivo XML. Para importar los marcadores, necesitas crear un objeto [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) y vincular el archivo PDF usando el método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Después de eso, necesitas llamar al método [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1). Finalmente, guarda el archivo PDF actualizado usando el método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). El siguiente fragmento de código te muestra cómo importar marcadores desde un archivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## Exportar Marcadores a XML desde un Archivo PDF Existente

El método ExportBookmarksToXml te permite exportar marcadores de un archivo PDF a un archivo XML.

Para exportar marcadores:

1. Crea un objeto PdfBookmarkEditor y vincula el archivo PDF utilizando el método BindPdf.
1. Llama al método ExportBookmarksToXml.
1. Guarda el archivo PDF actualizado utilizando el método Save.

El siguiente fragmento de código te muestra cómo exportar marcadores a un archivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}