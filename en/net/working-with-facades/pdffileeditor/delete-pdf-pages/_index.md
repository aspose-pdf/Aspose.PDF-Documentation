---
title: Delete PDF pages
type: docs
weight: 70
url: /net/delete-pdf-pages/
description: This section explains how to delete PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2021-06-05"
draft: false
---

If you want to delete a number of pages from the PDF file which is residing on the disk then you can use the overload of the [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) method which takes following three parameters: intput file path, array of page numbers to be deleted, and output PDF file path. The second parameter is an integer array representing all of the pages which need to be deleted. The specified pages are removed from the intput file and the result is saved as output file. The following code snippet shows you how to delete PDF pages using file paths.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingFilePath-DeletePagesUsingFilePath.cs" >}}

## Delete PDF Pages Using Streams

The [Delete](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/delete/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class also provides an overload which allows you to delete the pages from the input PDF file, while both the input and output files are in the streams. This overload takes following three parameters: intput stream, integer array of PDF pages to be deleted, and output stream.The following code snippet shows you how to delete PDF pages using streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-DeletePages-DeletePagesUsingStream-DeletePagesUsingStream.cs" >}}
