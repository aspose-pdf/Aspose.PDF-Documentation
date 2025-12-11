---
title: Insert PDF pages
type: docs
ai_search_scope: pdf_java
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /java/insert-pdf-pages/
description: This section explains how to insert PDF pages with com.aspose.pdf.facades using PdfFileEditor class.
lastmod: "2025-12-11"
draft: false
---


## Insert PDF Pages Between Two Numbers Using File Paths

A particular range of pages can be inserted from one PDF into another using [Insert] method of [PdfFileEditor] class. 
In order to do that, you need an input PDF file in which you want to insert the pages, a port file from which the pages need to be taken for insertion, a location where the pages are to be inserted, and a range of pages of the port file which have to be inserted in the input PDF file. This range is specified with start page and end page parameters. Finally, the output PDF file is saved with the specified range of pages inserted in the input file. The following code snippet shows you how to insert PDF pages between two numbers using file streams.

```java
private static void insertPdfPagesBetweenTwoNumbersUsingFilePaths()
{
        // The path to the documents directory
        String dataDir = "C:\\Workspace\\";

        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

        // Insert pages
        pdfEditor.insert(
                dataDir + "MultiplePages.pdf", 1,
                dataDir + "InsertPages.pdf", 2, 5,
                dataDir + "InsertPagesBetweenNumbers_out.pdf");
}
```

## Insert Array of PDF Pages Using File Paths

If you want to insert some specified pages into another PDF file, then you can use an overload of the [Insert] method which requires an integer array of pages. 
In this array, you can specify which particular pages you want to insert in the input PDF file. In order to do that, you need an input PDF file in which you want to insert the pages, a port file from which the pages need to be taken for insertion, a location where the pages are to be inserted, and integer array of the pages from port file which have to be inserted in the input PDF file. This array contains a list of particular pages which you’re interested to insert in the input PDF file. Finally, the output PDF file is saved with the specified array of pages inserted in the input file.
The following code snippet shows you how to insert array of PDF pages using file paths.

```java

private static void insertArrayOfPdfPagesUsingFilePaths()
{
    // The path to the documents directory
        String dataDir = "C:\\Workspace\\";

        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

        int[] pagesToInsert = new int[] { 2, 3 };
        // Insert pages
        pdfEditor.insert(
                dataDir + "MultiplePages.pdf", 1,
                dataDir + "InsertPages.pdf", pagesToInsert,
                dataDir + "InsertArrayOfPages_out.pdf");
}
```

## Insert PDF Pages between Two Numbers Using Streams

If you want to insert the range of pages using streams, you only need to use the appropriate overload of the [Insert] method of [PdfFileEditor] class. 
In order to do that, you need an input PDF stream in which you want to insert the pages, a port stream from which the pages need to be taken for insertion, a location where the pages are to be inserted, and a range of pages of the port stream which have to be inserted in the input PDF stream. This range is specified with start page and end page parameters. Finally, the output PDF stream is saved with the specified range of pages inserted in the input stream. The following code snippet shows you how to insert PDF pages between two numbers using streams.

```java

private static void insertPdfPagesBetweenTwoNumbersUsingStreams()
{
    // The path to the documents directory
        String dataDir = "C:\\Workspace\\";

        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

        // Create streams
        try (FileInputStream inputStream = new FileInputStream(dataDir + "MultiplePages.pdf"))
        {
            try (FileInputStream portStream = new FileInputStream(dataDir + "InsertPages.pdf"))
            {
                try (FileOutputStream outputStream = new FileOutputStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf"))
                {
                    // Insert pages
                    pdfEditor.insert(inputStream, 1, portStream, 1, 4, outputStream);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
}
```

## Insert Array of PDF Pages Using Streams

You can also insert an array of pages into another PDF file using streams with the helps of appropriate overload of the Insert method which requires an integer array of pages. In this array, you can specify which particular pages you want to insert in the input PDF stream. In order to do that, you need an input PDF stream in which you want to insert the pages, a port stream from which the pages need to be taken for insertion, a location where the pages are to be inserted, and integer array of the pages from port stream which have to be inserted in the input PDF file. This array contains a list of particular pages which you’re interested to insert in the input PDF stream. Finally, the output PDF stream is saved with the specified array of pages inserted in the input file.The following code snippet shows you how to insert array of PDF pages using streams.

```java

private static void insertArrayOfPdfPagesUsingStreams()
{
     // The path to the documents directory
        String dataDir = "C:\\Workspace\\";

        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();
        // Pages to insert
        int[] pagesToInsert = new int[] { 2, 3 };
        // Create streams
        try (FileInputStream inputStream = new FileInputStream(dataDir + "MultiplePages.pdf"))
        {
            try (FileInputStream portStream = new FileInputStream(dataDir + "InsertPages.pdf"))
            {
                try (FileOutputStream outputStream = new FileOutputStream(dataDir + "InsertPagesBetweenNumbersUsingStreams_out.pdf"))
                {
                    // Insert pages
                    pdfEditor.insert(inputStream, 1, portStream, pagesToInsert, outputStream);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
}
```