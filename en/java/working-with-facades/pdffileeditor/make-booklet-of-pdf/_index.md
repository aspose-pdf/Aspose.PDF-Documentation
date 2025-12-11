---
title: Make Booklet of PDF
type: docs
ai_search_scope: pdf_java
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 80
url: /java/make-booklet-of-pdf/
description: This section explains how to make booklet of PDF with com.aspose.pdf.facades using PdfFileEditor class.
lastmod: "2025-12-11s"
draft: false
---


## Make Booklet of PDF Using File Paths

[MakeBooklet] method of [PdfFileEditor]class allows you to make booklet of the input PDF file and save it to the output PDF file. 
This overload allows you to make booklet using file paths. The following code snippet shows you how to make booklet using file paths.

```java

private static void makeBookletOfPdfUsingFilePaths()
{

	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Make booklet
	pdfEditor.makeBooklet(dataDir + "MakeBookletInput.pdf", dataDir + "MakeBookletUsingPaths_out.pdf");
	}
```

## Make Booklet of PDF Using Page Size and File Paths

[MakeBooklet] method of [PdfFileEditor]class allows you to make booklet of the input PDF file and save it to the output PDF file. 
This overload allows you to make booklet using file paths. You can also set the page size of the output PDF file with this overlaod. 
The following code snippet shows you how to make booklet using page size and file paths.

```java

private static void makeBookletOfPdfUsingPageSizeAndFilePaths()
{
    
	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Make booklet
	pdfEditor.makeBooklet(dataDir + "MakeBookletInput.pdf", 
			dataDir + "MakeBookletUsingPaths_out.pdf", PageSize.getA5());
}
```

## Make Booklet of PDF Using Page Size, Specified Left and Right Pages, and File Paths

[MakeBooklet]method of [PdfFileEditor] class allows you to make booklet of the input PDF file and save it to the output PDF file. 
This overload allows you to make booklet using file paths. 
You can also set the page size of the output PDF file and specify particular pages for the left and right sides of the output PDF file with this overlaod. 
The following code snippet shows you how to make booklet using page size, specified left and right pages and file paths.


```java

private static void makeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndFilePaths()
{

        // The path to the documents directory
        String dataDir = "C:\\Workspace\\";

        // Create PdfFileEditor object
        com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

        // Set left and right pages
        int[] leftPages = new int[] { 1, 5 };
        int[] rightPages = new int[] { 2, 3 };
        // Make booklet
        pdfEditor.makeBooklet(dataDir + "MakeBookletInput.pdf",
                dataDir + "MakeBookletUsingPaths_out.pdf", PageSize.getA5(), leftPages, rightPages);
}
				
```

## Make Booklet of PDF Using Specified Left and Right Pages, and File Paths

[MakeBooklet]  method of [PdfFileEditor] class allows you to make booklet of the input PDF file and save it to the output PDF file. 
This overload allows you to make booklet using file paths. You can also specify particular pages for the left and right sides of the output PDF file with this overload.
The following code snippet shows you how to make booklet using specified left and right pages and file paths.

```java

private static void makeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndFilePaths()
{
	 // The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Set left and right pages
	int[] leftPages = new int[] { 1, 5 };
	int[] rightPages = new int[] { 2, 3 };
	// Make booklet
	pdfEditor.makeBooklet(dataDir + "MakeBookletInput.pdf",
			dataDir + "MakeBookletUsingPaths_out.pdf",  leftPages, rightPages);
}
```

## Make Booklet of PDF Using Streams

[MakeBooklet]method of [PdfFileEditor]class allows you to make booklet of the input PDF stream and save it to the output PDF streams. 
This overload allows you to make booklet using streams instead of file paths. The following code snippet shows you how to make booklet using streams.

```java
private static void makeBookletOfPdfUsingStreams()
{
    
	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeBookletInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeBookletUsingStreams_out.pdf"))
		{
			// Make booklet
			pdfEditor.makeBooklet(inputStream, outputStream);
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Make Booklet of PDF Using Page Size and Streams

[MakeBooklet] method of [PdfFileEditor]class allows you to make booklet of the input PDF stream and save it to the output PDF stream. 
This overload allows you to make booklet using streams instead of file paths. You can also set the page size of the output PDF stream with this overload. 
The following code snippet shows you how to make booklet using page size and streams.

```java

private static void makeBookletOfPdfUsingPageSizeAndStreams()
{
    
	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeBookletInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeBookletUsingStreams_out.pdf"))
		{
			// Make booklet
			pdfEditor.makeBooklet(inputStream, outputStream, PageSize.getA5());
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Make Booklet of PDF Using Page Size, Specified Left and Right Pages, and Streams

[MakeBooklet]  method of [PdfFileEditor] class allows you to make booklet of the input PDF stream and save it to the output PDF stream. 
This overload allows you to make booklet using streams instead of file paths. You can also set the page size of the output PDF file and specify particular pages for the left and right sides of the output PDF stream with this overload. The following code snippet shows you how to make booklet using page size, specified left and right pages, and streams.

```java

private static void makeBookletOfPdfUsingPageSizeSpecifiedLeftAndRightPagesAndStreams()
{
  
	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeBookletInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeBookletUsingStreams_out.pdf"))
		{

			// Set left and right pages
			int[] leftPages = new int[] { 1, 5 };
			int[] rightPages = new int[] { 2, 3 };
			
			// Make booklet
			pdfEditor.makeBooklet(inputStream, outputStream, PageSize.getA5(), leftPages, rightPages);
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Make Booklet of PDF Using Specified Left and Right Pages, and Streams

[MakeBooklet] method of [PdfFileEditor]class allows you to make booklet of the input PDF stream and save it to the output PDF stream. 
This overload allows you to make booklet using streams instead of file paths. You can also specify particular pages for the left and right sides of the output PDF stream with this overlaod. The following code snippet shows you how to make booklet using specified left and right pages and streams.

```java

private static void makeBookletOfPdfUsingSpecifiedLeftAndRightPagesAndStreams()
{

	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeBookletInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeBookletUsingStreams_out.pdf"))
		{

			// Set left and right pages
			int[] leftPages = new int[] { 1, 5 };
			int[] rightPages = new int[] { 2, 3 };

			// Make booklet
			pdfEditor.makeBooklet(inputStream, outputStream, leftPages, rightPages);
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```