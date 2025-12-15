---
title: Make NUp of PDF files
type: docs
ai_search_scope: pdf_java
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 90
url: /java/make-nup-of-pdf-files/
description: This article shows how to make NUp of PDF files work with com.aspose.pdf.facades using PdfFileEditor class.
lastmod: "2025-12-11"
draft: false
---


## Make NUp of PDF Using File Paths

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of the input PDF file and save it to the output PDF file. 
This overload allows you to make NUp using file paths.The following code snippet shows you how to make NUP using file paths.

```java

private static void makeNupOfPdfUsingFilePaths()
{
 
	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Make NUp
	pdfEditor.makeNUp(dataDir + "MakeNupInput.pdf", dataDir + "MakeNupInput2.pdf", "MakeNUpUsingPaths_out.pdf");
	
}
```

## Make NUp Using Page Size and File Paths

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of the input PDF file and save it to the output PDF file. 
This overload allows you to make NUp using file paths. You can also set the page size of the output PDF file using this overload.The following code snippet shows you how to make NUp using page size and file paths.

```java

private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    // Make NUp
	pdfEditor.makeNUp(dataDir + "MakeNupMultiplePagesInput.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, 
			PageSize.getA5());
}
```

## Make NUp of PDF Using Page Size, Horizontal and Vertical Values, and File Paths

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of the input PDF file and save it to the output PDF file. 
This overload allows you to make NUp using file paths. You can also set the page size of the output PDF file and horizontal and vertical number of pages on each output page using this overload. The following code snippet shows you how to make NUp using page size, horizontal and vertical values, and file paths.

```java

private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    // Make NUp
    pdfEditor.makeNUp(dataDir + "MakeNupInput.pdf", "MakeNUpUsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Make NUp of PDF Using Array Of PDF Files and File Paths

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of an array of input PDF files and save them to a single output PDF file. 
This overload allows you to make NUp using file paths.The following code snippet shows you hot make NUp using array of PDF files and file paths.

```java

private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	String[] filesArray = new String[2];
	filesArray[0] = dataDir + "MakeNupInput.pdf";
	filesArray[1] = dataDir + "MakeNupInput2.pdf";
    // Make NUp
    pdfEditor.makeNUp(filesArray, dataDir + "MakeNupUsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Make NUp of PDF Using Streams

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of the input PDF stream and save it to the output PDF stream.
 This overload allows you to make NUp using streams instead of file paths. The following code snippet shows you how to make NUp using streams.

```java

private static void MakeNupOfPdfUsingStreams()
{
    
	// The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream1 = new FileInputStream(dataDir + "MakeNupInput.pdf"))
	{
		try (FileInputStream inputStream2 = new FileInputStream(dataDir + "MakeNupInput2.pdf"))
		{
			try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeNUpUsingStreams_out.pdf"))
			{
				// Make NUp
				pdfEditor.makeNUp(inputStream1, inputStream2, outputStream);
			}
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Make NUp of PDF Using Page Size and Streams

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of the input PDF stream and save it to the output PDF stream. 
This overload allows you to make NUp using streams instead of file paths. You can also set the page size of the output PDF stream using this overload. The following code snippet shows you how to make NUp using page size and streams.

```java

private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
	String dataDir = "C:\\Workspace\\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    // Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeNupInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeNUpUsingStreams_out.pdf"))
		{
			// Make NUp
			pdfEditor.makeNUp(inputStream, outputStream, 2, 3, PageSize.getA5());
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Make NUp of PDF Using Page Size, Horizontal and Vertical Values, and Streams

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of the input PDF stream and save it to the output PDF stream. 
This overload allows you to make NUp using streams instead of file paths. You can also set the page size of the output PDF stream and horizontal and vertical number of pages on each output page using this overload. The following code snippet shows you how to make NUp using page size, horizontal and vertical values, and streams.

```java

private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndStreams()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeNupInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeNUpUsingStreams_out.pdf"))
		{
			// Make NUp
			pdfEditor.makeNUp(inputStream, outputStream, 2, 3);
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Make NUp of PDF Using Array Of PDF Files and Streams

[MakeNUp] method of [PdfFileEditor] class allows you to make NUp of an array of input PDF streams and save them to a single output PDF stream. 
This overload allows you to make NUp using streams instead of file paths. The following code snippet shows you how to make NUp using array of PDF files using streams.

```java

private static void MakeNupOfPdfUsingArrayOfPdfFilesAndStreams()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    // Create streams
        try (FileInputStream inputStream1 = new FileInputStream(dataDir + "MakeNupInput.pdf"))
        {
            try (FileInputStream inputStream2 = new FileInputStream(dataDir + "MakeNupInput2.pdf"))
            {
                try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeNUpUsingStreams_out.pdf"))
                {
                    FileInputStream[] fileStreams = new FileInputStream[2];
                    fileStreams[0] = inputStream1;
                    fileStreams[1] = inputStream2;
                    // Make NUp
                    pdfEditor.makeNUp(inputStream1, inputStream2, outputStream);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
}
```