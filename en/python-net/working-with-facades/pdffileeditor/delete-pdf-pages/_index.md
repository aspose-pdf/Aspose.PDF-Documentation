---
title: Delete PDF pages
type: docs
weight: 70
url: /python-net/delete-pdf-pages/
description: This section explains how to delete PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2026-01-05"
---

If you want to delete a number of pages from the PDF file which is residing on the disk then you can use the overload of the [Delete](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/methods/delete/index) method which takes following three parameters: intput file path, array of page numbers to be deleted, and output PDF file path. The second parameter is an integer array representing all of the pages which need to be deleted. The specified pages are removed from the intput file and the result is saved as output file. The following code snippet shows you how to delete PDF pages using file paths.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePages()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of pages to delete
    var pagesToDelete = new int[] { 1, 2 };
    // Delete pages
    pdfEditor.Delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");
}
```

## Delete PDF Pages Using Streams

The [Delete](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor/methods/delete/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdffileeditor) class also provides an overload which allows you to delete the pages from the input PDF file, while both the input and output files are in the streams. This overload takes following three parameters: intput stream, integer array of PDF pages to be deleted, and output stream.The following code snippet shows you how to delete PDF pages using streams.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void DeletePagesUsingStreams()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "DeletePagesInput.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "DeletePagesUsingStream_out.pdf", FileMode.Create))
        {
            // Array of pages to delete
            var pagesToDelete = new int[] { 1, 2 };
            // Delete pages
            pdfEditor.Delete(inputStream, pagesToDelete, outputStream);
        }
    }
}
```