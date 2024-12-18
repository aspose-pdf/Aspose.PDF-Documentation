---
title: Concatenate PDF documents in C#
linktitle: Concatenate PDF documents
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
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Concatenate PDF documents in C#",
    "alternativeHeadline": "Effortlessly Merge PDF Files in C#",
    "abstract": "The functionality in Aspose.PDF for .NET allows developers to efficiently concatenate multiple PDF documents using the PdfFileEditor class in C#. This feature supports merging files through file paths and MemoryStreams, creating unique field names in PDF forms, and even generating a Table of Contents within the final document, providing a streamlined solution for document management and integration",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1615",
    "proficiencyLevel": "Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF for .NET",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/net/concatenate-pdf-documents/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/concatenate-pdf-documents/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## **Overview**

This article explains how to merge, combine or concatenate different PDF files into single PDF using C#. It covers topics e.g.

- [C# Merge PDF Files](#concatenate-pdf-files-using-file-paths)
- [C# Combine PDF Files](#concatenate-pdf-files-using-file-paths)
- [C# Merge Multiple PDF files into one PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Combine Multiple PDF files into one PDF](#concatenate-array-of-pdf-files-using-file-paths)
- [C# Merge all PDF files in a folder](#concatenating-all-pdf-files-in-particular-folder)
- [C# Combine all PDF files in a folder](#concatenating-all-pdf-files-in-particular-folder)
- [C# Merge PDF files using file paths](#concatenate-pdf-files-using-file-paths)
- [C# Combine PDF files using streams](#concatenate-array-of-pdf-files-using-streams)
- [C# Concatenate all PDF files in folder](#concatenate-pdf-files-in-folder)

## Concatenate PDF files using file paths

[PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) is the class in [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) which allows you to concatenate multiple PDF files. You can not only concatenate files using FileStreams but also using MemoryStreams as well. In this article, the process of concatenating the files using MemoryStreams will be explained and then shown using the code snippet.

[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class can be used to concatenate two PDF files. The [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method allows you to pass three parameters: first input PDF, second input PDF, and output PDF. The final output PDF contains both the input PDF files.

The following C# code snippet shows you how to concatenate PDF files using file paths.

```csharp
private static void ConcatenatePdfFilesUsingFilePaths()
{
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Concatenate files
    pdfEditor.Concatenate(dataDir + "input.pdf", dataDir + "input2.pdf", dataDir + "ConcatenateUsingPath_out.pdf");
}
```

In some cases, when there are a lot of outlines, users may disable them with setting CopyOutlines to false and improve performance of concatenation.

```csharp
private static void ConcatenatePdfFilesUsingFilePaths_CopyOutlinesDisabled()
{ 
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Create PdfFileEditor object
    var pfe = new Aspose.Pdf.Facades.PdfFileEditor();
    // Get files from dataDir
    string[] files = Directory.GetFiles(dataDir);
    // Setting CopyOutlines to false
    pfe.CopyOutlines = false;
    // Concatenate files
    pfe.Concatenate(files, dataDir + "ConcatenateUsingPath_CopyOutlinesDisabled_out.pdf");
}
```

## Concatenate multiple PDF files using MemoryStreams

[Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class takes the source PDF files and the destination PDF file as parameters. These parameters can be either paths to the PDF files on the disk or they could be MemoryStreams. Now, for this example, we’ll first create two files streams to read the PDF files from the disk. Then we’ll convert these files into byte arrays. These byte arrays of the PDF files will be converted to MemoryStreams. Once we get the MemoryStreams out of PDF files, we’ll be able to pass them on to the concatenate method and merge into a single output file.

The following C# code snippet shows you how to concatenate multiple PDF files using MemoryStreams:

```csharp
private static void ConcatenateMultiplePdfFilesUsingMemoryStreams()
{
    // The path to the documents directory.
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();

    string document1Path = dataDir + "document1.pdf";
    string document2Path = dataDir + "document2.pdf";
    string resultPdfPath = dataDir + "concatenated_out.pdf";
    
    // Create two file streams to read PDF files
    using (var fs1 = new FileStream(document1Path, FileMode.Open, FileAccess.Read))
    {
        using (var fs2 = new FileStream(document2Path, FileMode.Open, FileAccess.Read))
        {
            // Create byte arrays to keep the contents of PDF files
            var buffer1 = new byte[Convert.ToInt32(fs1.Length)];
            var buffer2 = new byte[Convert.ToInt32(fs2.Length)];

            var i = 0;
            // Read PDF file contents into byte arrays
            i = fs1.Read(buffer1, 0, Convert.ToInt32(fs1.Length));
            i = fs2.Read(buffer2, 0, Convert.ToInt32(fs2.Length));

            // Now, first convert byte arrays into MemoryStreams and then concatenate those streams
            using (var pdfStream = new MemoryStream())
            {
                using (var fileStream1 = new MemoryStream(buffer1))
                {
                    using (var fileStream2 = new MemoryStream(buffer2))
                    {
                        // Create instance of PdfFileEditor class to concatenate streams
                        var pdfEditor = new PdfFileEditor();
                        // Concatenate both input MemoryStreams and save to output MemoryStream
                        pdfEditor.Concatenate(fileStream1, fileStream2, pdfStream);
                        // Convert MemoryStream back to byte array
                        var data = pdfStream.ToArray();
                        // Create a FileStream to save the output PDF file
                        var output = new FileStream(resultPdfPath, FileMode.Create, FileAccess.Write);
                        // Write byte array contents in the output file stream
                        output.Write(data, 0, data.Length);
                        // Close output file
                        output.Close();
                    }
                }
            }
            // Close input files
            fs1.Close();
            fs2.Close();
        }
    }
}
```

## Concatenate Array of PDF Files Using File Paths

If you want to concatenate multiple PDF files, you can use the overload of the [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method, which allows you to pass an array of PDF files. The final output is saved as a merged file created from all the files in the array.The following C# code snippet shows you how to concatenate array of PDF files using file paths.

```csharp
private static void ConcatenateArrayOfPdfFilesUsingFilePaths()
{
    // The path to the documents directory.
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Array of files
    var filesArray = new string[2];
    filesArray[0] = dataDir + "input.pdf";
    filesArray[1] = dataDir + "input2.pdf";
    // Concatenate files
    pdfEditor.Concatenate(filesArray, dataDir + "ConcatenateArrayOfPdfFilesUsingFilePaths_out.pdf");
}
```

## Concatenate Array of PDF Files Using Streams

Concatenating an array of PDF files is not limited to only files residing on the disk. You can also concatenate an array of PDF files from streams. If you want to concatenate multiple PDF files, you can use the appropriate overload of the [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method. First, you need to create an array of input streams and one stream for output PDF and then call the [Concatenate](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/concatenate/index) method. The output will be saved in the output stream.The following C# code snippet shows you how to concatenate array of PDF files using streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-ConcatenateDocuments-ConcatenateArrayOfPdfUsingStreams-ConcatenateArrayOfPdfUsingStreams.cs" >}}

## Concatenating all Pdf files in Particular folder

You can even read all the Pdf files in a particular folder at runtime and concatenate them, without even knowing the file names. Simply provide the path of directory, which contains the PDF documents, that you would like to concatenate.

Please try using the following C# code snippet to achieve this functionality.

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

Please try using the following C# code snippet to achieve this functionality from Aspose.PDF:

```csharp
private static void ConcatenatePdfFilesInFolder()
{ 
    // The path to the documents directory.
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    // Retrieve names of all the Pdf files in a particular Directory
    string[] fileEntries = Directory.GetFiles(dataDir, "*.pdf");
    // Create PdfFileEditor
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Call Concatenate method of PdfFileEditor object to concatenate all input files
    // Into a single output file
    pdfEditor.Concatenate(fileEntries, dataDir + "concatenate_out.pdf");
}
```
