---
title: Concatenate PDF documents
type: docs
weight: 20
url: /net/concatenate-pdf-documents/
description: This section explains how to concatenate PDF documents with Aspose.PDF Facades using PdfFileEditor class.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

In this article, we’ll show you how to concatenate multiple PDF files using MemoryStreams.

{{% /alert %}}

## Concatenate PDF files using file paths

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) is the class in [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) which allows you to concatenate multiple PDF files. You can not only concatenate files using FileStreams but also using MemoryStreams as well. In this article, the process of concatenating the files using MemoryStreams will be explained and then shown using the code snippet.

[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class can be used to concatenate two PDF files. The [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method allows you to pass three parameters: first input PDF, second input PDF, and output PDF. The final output PDF contains both the input PDF files.

The following code snippet shows you how to concatenate PDF files using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

In some cases, when there are a lot of outlines, users may disable them with setting CopyOutlines to false and improve performance of concatenation.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## Concatenate multiple PDF files using MemoryStreams

[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class takes the source PDF files and the destination PDF file as parameters. These parameters can be either paths to the PDF files on the disk or they could be MemoryStreams. Now, for this example, we’ll first create two files streams to read the PDF files from the disk. Then we’ll convert these files into byte arrays. These byte arrays of the PDF files will be converted to MemoryStreams. Once we get the MemoryStreams out of PDF files, we’ll be able to pass them on to the concatenate method and merge into a single output file.

The following code snippet shows you how to concatenate multiple PDF files using MemoryStreams:

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Concatenate Array of PDF Files Using File Paths

If you want to concatenate multiple PDF files, you can use the overload of the [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method, which allows you to pass an array of PDF files. The final output is saved as a merged file created from all the files in the array.The following code snippet shows you how to concatenate array of PDF files using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Concatenate Array of PDF Files Using Streams

Concatenating an array of PDF files is not limited to only files residing on the disk. You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method. First, you need to create an array of input streams and one stream for output PDF and then call the [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method. The output will be saved in the output stream.The following code snippet shows you how to concatenate array of PDF files using streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Concatenating all Pdf files in Particular folder

You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following code snippet to achieve this functionality.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Concatenate PDF Forms and keep fields names unique

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class in [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offers the capability to concatenate the PDF files. Now, if the Pdf files which are to be concatenated have form fields with similar field names, Aspose.PDF provides the feature to keep the fields in the resultant Pdf file as unique and also you can specify the suffix to make the field names unique. [KeepFieldsUnique](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) property of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) as true will make field names unique when Pdf forms are concatenated. Also, [UniqueSuffix](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) property of PdfFileEditor can be used to specify the user defined format of the suffix which is added to field name to make it unique when forms are concatenated. This string must contain `%NUM%` substring which will be replaced with numbers in the resultant file.

Please see the following simple code snippet to achieve this functionality.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}

## Concatenate PDF files and create Table Of Contents

## Concatenate PDF files

Please take a look over following code snippet for information on how to merge the PDF files.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-ConcatenatePdfFilesAndCreateTOC.cs" >}}

### Insert blank page

Once the PDF files have been merged, we can insert a blank page at the beginning of document on which can can create Table Of contents. In order to accomplish this requirement, we can load the merged file into **Document** object and we need to call Page.Insert(...) method to insert a blank page.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}

### Add Text Stamps

In order to create a Table of Contents, we need to add Text stamps on first page using [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) and [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp) objects. Stamp class provides `BindLogo(...)` method to add [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) and we can also specify the location to add these text stamps using `SetOrigin(..)` method. In this article, we are concatenating two PDF files, so we need to create two text stamp objects pointing to these individual documents.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

### Create local links

Now we need to add links towards the pages inside the concatenated file. In order to accomplish this requirement, we can use `CreateLocalLink(..)` method of [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class. In following code snippet, we have passed Transparent as 4th argument so that the rectangle around link is not visible.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}

### Complete code

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}


## Concatenate PDF files in folder

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class in Aspose.Pdf.Facades namespace offers you the capability to concatenate the PDF file. You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following code snippet to achieve this functionality from Aspose.PDF:

```csharp
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

// Retrieve names of all the Pdf files in a particular Directory
string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");

// Get the current System date and set its format
string date = DateTime.Now.ToString("MM-dd-yyyy");
// Get the current System time and set its format
string hoursSeconds = DateTime.Now.ToString("hh-mm");
// Set the value for the final Resultant Pdf document
string masterFileName = date + "_" + hoursSeconds + "_out.pdf";

// Instantiate PdfFileEditor object
Aspose.Pdf.Facades.PdfFileEditor pdfEditor = new PdfFileEditor();

// Call Concatenate method of PdfFileEditor object to concatenate all input files
// Into a single output file
pdfEditor.Concatenate(fileEntries, dataDir + masterFileName);
```
