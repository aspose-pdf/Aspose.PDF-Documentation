---
title: Concatenate PDF documents
type: docs
weight: 45
url: /net/concatenate-pdf-documents/
description: This section explains how to concatenate PDF documents with Aspose.PDF Facades using PdfFileEditor class.
aliases:
    - /pdf/net/concatenate-multiple-pdf-files-using-memorystreams/
    - /pdf/net/concatenate-pdf-files-and-create-table-of-contents/
    - /pdf/net/concatenate-pdf-forms-and-keep-fields-names-unique/
    - /pdf/net/concatenating-all-pdf-files-in-particular-folder/
    - /pdf/net/how-to-concatenate-pdf-files-in-different-ways/
    - /pdf/net/append-pdf-files/
lastmod: "2021-01-25"
---

{{% alert color="primary" %}}

In this article, we’ll show you how to concatenate multiple PDF files using MemoryStreams.

{{% /alert %}}

## Concatenate PDF files using file paths

[PdfFileEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor) is the class in [Aspose.Pdf.Facades namespace](https://apireference.aspose.com/pdf/net/aspose.pdf.facades) which allows you to concatenate multiple PDF files. You can not only concatenate files using FileStreams but also using MemoryStreams as well. In this article, the process of concatenating the files using MemoryStreams will be explained and then shown using the code snippet.

[Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method of [PdfFileEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class can be used to concatenate two PDF files. The [Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method allows you to pass three parameters: first input PDF, second input PDF, and output PDF. The final output PDF contains both the input PDF files. 

The following code snippet shows you how to concatenate PDF files using file paths. 

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-ConcatenateUsingPath.cs" >}}

In some cases, when there are a lot of outlines, users may disable them with setting CopyOutlines to false and improve performance of concatenation.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingPath-CopyOutline.cs" >}}

## Concatenate multiple PDF files using MemoryStreams

[Concatenate](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method of [PdfFileEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor) class takes the source PDF files and the destination PDF file as parameters. These parameters can be either paths to the PDF files on the disk or they could be MemoryStreams. Now, for this example, we’ll first create two files streams to read the PDF files from the disk. Then we’ll convert these files into byte arrays. These byte arrays of the PDF files will be converted to MemoryStreams. Once we get the MemoryStreams out of PDF files, we’ll be able to pass them on to the concatenate method and merge into a single output file.

The following code snippet shows you how to concatenate multiple PDF files using MemoryStreams:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenateMultiplePDFUsingMemoryStream-ConcatenateMultiplePDFUsingMemoryStream.cs" >}}

## Concatenate Array of PDF Files Using File Paths

If you want to concatenate multiple PDF files, you can use the overload of the [Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method, which allows you to pass an array of PDF files. The final output is saved as a merged file created from all the files in the array.The following code snippet shows you how to concatenate array of PDF files using file paths.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-ConcatenateArrayOfFilesWithPath.cs" >}}

## Concatenate Array of PDF Files Using Streams

Concatenating an array of PDF files is not limited to only files residing on the disk. You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the [Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method. First, you need to create an array of input streams and one stream for output PDF and then call the [Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method. The output will be saved in the output stream.The following code snippet shows you how to concatenate array of PDF files using streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

##  Concatenating all Pdf files in Particular folder

You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following code snippet to achieve this functionality.


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatingAllPdfFiles-ConcatenatingAllPdfFiles.cs" >}}

## Concatenate PDF Forms and keep fields names unique

[PdfFileEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor) class in [Aspose.Pdf.Facades namespace](https://docs-qa.aspose.com/display/pdftemp/Aspose.Pdf.Facades+namespace) offers the capability to concatenate the PDF files. Now, if the Pdf files which are to be concatenated have form fields with similar field names, Aspose.PDF provides the feature to keep the fields in the resultant Pdf file as unique and also you can specify the suffix to make the field names unique. [KeepFieldsUnique](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor/properties/keepfieldsunique) property of [PdfFileEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor) as true will make field names unique when Pdf forms are concatenated. Also, [UniqueSuffix](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/pdffileeditor/properties/uniquesuffix) property of PdfFileEditor can be used to specify the user defined format of the suffix which is added to field name to make it unique when forms are concatenated. This string must contain %NUM% substring which will be replaced with numbers in the resultant file.

Please see the following simple code snippet to achieve this functionality.


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePDFForms-ConcatenatePDFForms.cs" >}}

## Insert blank page

Once the PDF files have been merged, we can insert a blank page at the beginning of document on which can can create Table Of contents. In order to accomplish this requirement, we can load the merged file into [Document](https://apireference.aspose.com/pdf/net/aspose.pdf/document) object and we need to call Page.Insert(...) method to insert a blank page.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-InsertBlankPage.cs" >}}


## Concatenate PDF Files with Blank PDF Using File Paths

One of the overloads of [Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method allows you to merge two PDF documents into a new PDF document with pages in alternate ways and fill the blank places with blank pages; for example, document 1 has 5 pages ( p1, p2, p3, p4, p5 ) and document 2 has 3 page s ( p1', p2', p3' ). Merging the two PDF document s will produce the outupt document with pages in the following order: p1, p1', p2, p2', p3, p3', p4, blank page, p5, blank page.The following code snippet shows you how to concatenate PDF files with blank PDF using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateWithBlankPdf-ConcatenateWithBlankPdf.cs" >}}


### Render the resultant PDF in Browser window

When using PdfFileEditor class to concatenate PDF files in web application, there can be a requirement to display the resultant PDF file in web browser, rather than saving it over the system. In order to accomplish this requirement, PdfFileEditor class provides an overloaded Concatenate method which takes HttpResponse object as an argument. Please take a look over the following code snippet to accomplish this requirement.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-RenderInBrowser.cs" >}}

### Ignore corrupted PDF files during concatenation

Aspose.PDF for .NET supports the feature to ignore Corrupted PDF documents during PDF concatenation process. Please note that following properties/methods are introduced in PdfFileEditor:

1. A new Enumeration [CorruptedFileActions](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/corruptedfileaction) (StopWithError, ConcatenateIgnoringCorrupted) is added.
1. Property [CorruptedFileActions](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/corruptedfileaction) of CorruptedFileActions type is added. This property defines behavior of PDfFileEditor.Concatenate and Append functions when some of files to concatenate/append was corrupted.
- If CorruptedFileAction is "[StopWithError](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/concatenatecorruptedfileaction)" then process will be stopped and exception thrown or false returned as result of unsuccessful operation (in depend of AllowConcatenateExceptions state)
- If CorruptFileAction is "[ConcatenateIgnoringCorrupted](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/concatenatecorruptedfileaction)" then only valid files will be concatenated, so the resultant file will be correct too.
  Information about corrupted files will be collected and accessible in CorruptedItems property.
  No exceptions are thrown in this case (operation is succeeded anyway)
1. [CorruptedItem](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/corrupteditem) class is introduced.
   This class has two properties:
- int Index - index of corrupted file in parameters array
- Exception exception - exception which was encountered for this file to check the reason of failure.
1. [CorruptedItem](https://apireference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/corrupteditem/properties/index) - property which contains information about all corrupted files which were ignored. Please note this array contains information only for corrupted files. If operation was successful, this array will be empty. Corrupted files are not included into resultant files.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfFilesWithPath-CorruptedFiles.cs" >}}


### Concatenating Tagged PDF files

In order to concatenate PDF files, a property [CopyLogicalStructure](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/properties/copylogicalstructure) is added. This property should be set to false in order to turn off logical structure concatenation. The following code snippet shows how to perform concatenation while copying the logical structure:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateUsingStreams-ConcatenateTaggedFiles.cs" >}}

## Concatenate PDF Files with Blank PDF Using Streams

If you’re interested to concatenate PDF files with a blank page using streams then one of the overloads of [Concatenate](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method allows you to do just that. This overload merges two PDF documents into a new PDF document with pages in alternate ways and fill the blank places with blank pages; for example, document 1 has 5 pages ( p1, p2, p3, p4, p5 ) and document 2 has 3 page s ( p1', p2', p3' ). Merging the two PDF documents will produce the outupt document with pages in the following order: p1, p1', p2, p2', p3, p3', p4, blank page, p5, blank page .In this case, you need to create four streams: two input streams, one stream with blank PDF page, and one output stream. The input streams will be merged according to the above plan and output will be saved in the output stream. The following code snippet shows you how to concatenate PDF files with blank PDF using streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateBlankPdfUsingStreams-ConcatenateBlankPdfUsingStreams.cs" >}}



## Add Text Stamps

In order to create a Table of Contents, we need to add Text stamps on first page using [PdfFileStamp](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/PdfFileStamp) and [Stamp](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/Stamp) objects. Stamp class provides [BindLogo(..)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) method to add [FormattedText](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/FormattedText) and we can also specify the location to add these text stamps using [SetOrigin(..)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/setorigin) method. In this article, we are concatenating two PDF files, so we need to create two text stamp objects pointing to these individual documents.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-AddTextStamps.cs" >}}

## Create local links

Now we need to add links towards the pages inside the concatenated file. In order to accomplish this requirement, we can use [CreateLocalLink(..)](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/createlocallink/index) method of [PdfContentEditor](http://www.aspose.com/api/net/pdf/aspose.pdf.facades/PdfContentEditor) class. In following code snippet, we have passed Transparent as 4th argument so that the rectangle around link is not visible.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CreateLocalLinks.cs" >}}

## Complete code


{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-ConcatenatePdfFilesAndCreateTOC-CompletedCode.cs" >}}

{{% alert color="primary" %}} 

You may download the sample documents from following links

- [Input1.pdf](https://docs.aspose.com/download/attachments/7116811/Input1.pdf?version=1&modificationDate=1447483522863&api=v2)
- [Input2.pdf](https://docs.aspose.com/download/attachments/7116811/Input2.pdf?version=1&modificationDate=1447483522883&api=v2)

- [Concatenated_Table_Of_Contents.pdf](https://docs.aspose.com/download/attachments/7116811/Concatenated_Table_Of_Contents.pdf?version=1&modificationDate=1447483522910&api=v2)

{{% /alert %}}
