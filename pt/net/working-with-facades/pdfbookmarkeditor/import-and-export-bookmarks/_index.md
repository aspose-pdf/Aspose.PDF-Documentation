---
title: Importar e Exportar Favoritos
type: docs
weight: 20
url: /pt/net/import-and-export-bookmarks/
description: Esta seção explica como importar e exportar Favoritos com Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Importar Favoritos de XML para um Arquivo PDF Existente

O método [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) permite importar favoritos para um arquivo PDF a partir de um arquivo XML. Para importar os favoritos, você precisa criar um objeto [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) e vincular o arquivo PDF usando o método [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index). Depois disso, você precisa chamar o método [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1). Por fim, salve o arquivo PDF atualizado usando o método [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save). O trecho de código a seguir mostra como importar favoritos de um arquivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## Exportar Favoritos para XML de um Arquivo PDF Existente

O método ExportBookmarksToXml permite exportar favoritos de um arquivo PDF para um arquivo XML.

Para exportar favoritos:

1. Crie um objeto PdfBookmarkEditor e vincule o arquivo PDF usando o método BindPdf.  
1. Chame o método ExportBookmarksToXml.  
1. Salve o arquivo PDF atualizado usando o método Save.  

O trecho de código a seguir mostra como exportar marcadores para um arquivo XML.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}