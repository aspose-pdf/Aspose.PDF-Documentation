---
title: Split PDF pages
type: docs
ai_search_scope: pdf_java
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 60
url: /java/split-pdf-pages/
description: This section explains how to split PDF pages with com.aspose.pdf.facades Facades using PdfFileEditor class.
lastmod: "2025-12-11"
draft: false
---


## Split PDF Pages from First Using File Paths

[SplitFromFirst] method of [PdfFileEditor] class allows you to split the PDF file starting from the first page and ending at the specified page number. 
If you want to manipulate the PDF files from the disk, you can pass the file paths of the intput and output PDF files to this method. The following code snippet shows you how to split PDF pages from first using file paths.

```java

private static void SplitPdfPagesFromFirstUsingFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Split pages
	pdfEditor.splitFromFirst(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesUsingPaths_out.pdf");

}
```

## Split PDF Pages from First Using File Streams

[SplitFromFirst]  method of [PdfFileEditor] class allows you to split the PDF file starting from the first page and ending at the specified page number. 
If you want to manipulate the PDF files from the streams, you can pass the input and output PDF streams to this method. The following code snippet shows you how to split PDF pages from first using file streams.

```java

private static void SplitPdfPagesFromFirstUsingFileStreams()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

	// Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "MakeBookletInput.pdf"))
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeBookletUsingStreams_out.pdf"))
		{
			// Split pages
			pdfEditor.splitFromFirst(inputStream, 3, outputStream);
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}

}
```

## Split PDF Pages to Bulk Using File Paths

[SplitToBulks] method of [PdfFileEditor] class allows you to split the PDF file into multiple sets of pages. 
In this example, we require two sets of pages (1, 2) and (5, 6). If you want to access the PDF file from the disk, you need to pass the input PDF as file path. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using file paths.

```java

private static void SplitPdfPagesToBulkUsingFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    int fileNumber = 1;
	// Create array of pages to split
	int[][] numberOfPages = new int[][] { new int[] { 1, 2 }, new int[] { 3, 4 } };
	// Split to bulk
	ByteArrayInputStream[] outBuffer = pdfEditor.splitToBulks(dataDir + "MultiplePages.pdf", numberOfPages);
	// Save individual files
	for (ByteArrayInputStream outStream : outBuffer)
	{
		try (FileOutputStream outFileStream = new FileOutputStream(dataDir + "File_" + fileNumber + "_out.pdf"))
		{
			// Convert ByteArrayInputStream to byte array and write
			byte[] buffer = new byte[1024];
			int bytesRead;
			while ((bytesRead = outStream.read(buffer)) != -1) {
				outFileStream.write(buffer, 0, bytesRead);
			}
			fileNumber++;
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
```

## Split PDF Pages to Bulk Using Streams

[SplitToBulks] method of [PdfFileEditor] class allows you to split the PDF file into multiple sets of pages. 
In this example, we require two sets of pages (1, 2) and (5, 6). You can pass a stream to this method instead of accessing the file from the disk. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using streams.

```java

private static void SplitPdfPagesToBulkUsingStreams()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

   try (FileInputStream inputStream1 = new FileInputStream(dataDir + "splitPdfToIndividualPagesInput.pdf")) {
		int fileNumber = 1;
		// Create array of pages to split
		int[][] numberOfPages = new int[][]{new int[]{1, 2}, new int[]{3, 4}};
		// Split to bulk

		ByteArrayInputStream[] outBuffer = pdfEditor.splitToBulks(inputStream1, numberOfPages);
		// Save individual files
		for (ByteArrayInputStream outStream : outBuffer) {
			try (FileOutputStream outFileStream = new FileOutputStream(dataDir + "File_" + fileNumber + "_out.pdf")) {
				// Convert ByteArrayInputStream to byte array and write
				byte[] buffer = new byte[1024];
				int bytesRead;
				while ((bytesRead = outStream.read(buffer)) != -1) {
					outFileStream.write(buffer, 0, bytesRead);
				}
				fileNumber++;
			} catch (IOException e) {
				throw new RuntimeException(e);
			}
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Split PDF Pages to End Using File Paths

[SplitToEnd] method of [PdfFileEditor] class allows you to split the PDF from the specified page number to the end of the PDF file and save it as a new PDF. 
In order to do this, using file paths, you need to pass input and output file paths and the page number from where the split needs to be started. The output PDF will be saved to the disk. The following code snippet shows you how to split PDF pages to end using file paths.

```java

private static void SplitPdfPagesToEndUsingFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    // Split pages
    pdfEditor.splitToEnd(dataDir + "MultiplePages.pdf", 3, dataDir + "SplitPagesToEndUsingPaths_out.pdf");
}
```

## Split PDF Pages to End Using Streams

[SplitToEnd] method of [PdfFileEditor] class allows you to split the PDF from the specified page number to the end of the PDF file and save it as a new PDF. 
In order to do this, using streams, you need to pass input and output streams and the page number from where the split needs to be started. 
The output PDF will be saved to the output stream. The following code snippet shows you how to split PDF pages to end using streams.

```java

private static void SplitPdfPagesToEndUsingStreams()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    // Create streams
	try (FileInputStream inputStream = new FileInputStream(dataDir + "splitPdfToIndividualPagesInput.pdf")) 
	{
		try (FileOutputStream outputStream = new FileOutputStream(dataDir + "MakeNUpUsingStreams_out.pdf"))
		{
			// Split pages
			pdfEditor.splitToEnd(inputStream, 3, outputStream);
		}
	} catch (IOException e) {
		throw new RuntimeException(e);
	}
}
```

## Split PDF to Individual Pages Using File Paths

{{% alert color="primary" %}}

You can try to split PDF document and view the results online at this link:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

In order to split PDF file to individual pages, you need to pass the PDF as file path to the [SplitToPages](https://reference.aspose.com/pdf/java/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) method. This method will return an array of MemoryStream containing individual pages of the PDF file. You can loop through this array of MemoryStream and save individual pages as individual PDF files on the disk. The following code snippet shows you how to split PDF to individual pages using file paths.

```java

private static void SplitPdfToIndividualPagesUsingFilePaths()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    int fileNumber = 1;
	ByteArrayInputStream[] outBuffer = pdfEditor.splitToPages(dataDir + "splitPdfToIndividualPagesInput.pdf");
	// Save individual files
	for (ByteArrayInputStream outStream : outBuffer) {
		try (FileOutputStream outFileStream = new FileOutputStream(dataDir + "File_" + fileNumber + "_out.pdf")) {
			// Convert ByteArrayInputStream to byte array and write
			byte[] buffer = new byte[1024];
			int bytesRead;
			while ((bytesRead = outStream.read(buffer)) != -1) {
				outFileStream.write(buffer, 0, bytesRead);
			}
			fileNumber++;
		} catch (IOException e) {
			throw new RuntimeException(e);
		}
	}
}
```

## Split PDF to Individual Pages Using Streams

In order to split PDF file to individual pages, you need to pass the PDF as stream to the [SplitToPages] method.
 This method will return an array of MemoryStream containing individual pages of the PDF file. 
 You can loop through this array of MemoryStream and save individual pages as individual PDF files on the disk, or you can keep these individual pages in the memory stream for later use in your application. The following code snippet shows you how to split PDF to individual pages using streams.

```java

private static void SplitPdfToIndividualPagesUsingStreams()
{
    // The path to the documents directory
	String dataDir = "C:\Workspace\";

	// Create PdfFileEditor object
	com.aspose.pdf.facades.PdfFileEditor pdfEditor = new com.aspose.pdf.facades.PdfFileEditor();

    try (FileInputStream inputStream = new FileInputStream(dataDir + "splitPdfToIndividualPagesInput.pdf")) {
            int fileNumber = 1;
            ByteArrayInputStream[] outBuffer = pdfEditor.splitToPages(inputStream);
            // Save individual files
            for (ByteArrayInputStream outStream : outBuffer) {
                try (FileOutputStream outFileStream = new FileOutputStream(dataDir + "File_" + fileNumber + "_out.pdf")) {
                    // Convert ByteArrayInputStream to byte array and write
                    byte[] buffer = new byte[1024];
                    int bytesRead;
                    while ((bytesRead = outStream.read(buffer)) != -1) {
                        outFileStream.write(buffer, 0, bytesRead);
                    }
                    fileNumber++;
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
}
```