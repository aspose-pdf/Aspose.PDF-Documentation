---
title: Delete PDF pages
type: docs
ai_search_scope: pdf_java
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /javas/delete-pdf-pages/
description: This section explains how to delete PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2025-12-11"
draft: false
---

If you want to delete a number of pages from the PDF file which is residing on the disk then you can use the overload of the 
[Delete]method which takes following three parameters: intput file path, array of page numbers to be deleted, and output PDF file path. The second parameter is an integer array representing all of the pages which need to be deleted. The specified pages are removed from the intput file and the result is saved as output file. The following code snippet shows you how to delete PDF pages using file paths.

```java

private static void deletePages()
{
        // The path to the documents directory
        String dataDir = getDirectory();
        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();
        // Array of pages to delete
        int[] pagesToDelete = new int[] { 1, 2 };
        // Delete pages
        pdfEditor.delete(dataDir + "DeletePagesInput.pdf", pagesToDelete, dataDir + "DeletePagesUsingFilePath_out.pdf");

}
```

## Delete PDF Pages Using Streams

The [Delete] method of [PdfFileEditor] class also provides an overload which allows you to delete the pages from the input PDF file, while both the input and output files are in the streams. 
This overload takes following three parameters: intput stream, integer array of PDF pages to be deleted, and output stream.
The following code snippet shows you how to delete PDF pages using streams.

```java

private static void deletePagesUsingStreams()
{
        // The path to the documents directory
        String dataDir = getDirectory();

        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();
        // Create streams
        try (FileInputStream inputStream = new FileInputStream(dataDir + "DeletePagesInput.pdf"))
        {
            try (FileOutputStream outputStream = new FileOutputStream(dataDir + "DeletePagesUsingStream_out.pdf"))
            {
                // Array of pages to delete
                int[] pagesToDelete = new int[] { 1, 2 };
                // Delete pages
                pdfEditor.delete(inputStream, pagesToDelete, outputStream);
            }
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
}
```