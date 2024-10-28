---
title: Import and Export Bookmarks
type: docs
weight: 20
url: /net/import-and-export-bookmarks/
description: This section explains how to import and export Bookmarks with Aspose.PDF Facades.
lastmod: "2021-06-05"
draft: false
---

## Import Bookmarks from XML to an Existing PDF File

[ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) method allows you to import bookmarks into a PDF file from an XML file. In order to import the bookmarks, you need to create [PdfBookmarkEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfbookmarkeditor) object and bind the PDF file using [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/bindpdf/index) method. After that, you need to call [ImportBookmarksWithXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfbookmarkeditor/importbookmarkswithxml/methods/1) method. Finally, save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save) method. The following code snippet shows you how to import bookmarks from an XML file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ImportFromXML-ImportFromXML.cs" >}}

## Export Bookmarks to XML from an Existing PDF File

The ExportBookmarksToXml method allows you to export bookmarks from a PDF file to an XML file.

To export bookmarks:

1. Create a PdfBookmarkEditor object and bind the PDF file using the BindPdf method.
1. Call the ExportBookmarksToXml method.
1. Save the updated PDF file using the Save method.

The following code snippet shows you how to export bookmarks to an XML file.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Bookmarks-ExportToXML-ExportToXML.cs" >}}
