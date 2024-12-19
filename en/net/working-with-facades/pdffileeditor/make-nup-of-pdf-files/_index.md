---
title: Make NUp of PDF files
type: docs
weight: 90
url: /net/make-nup-of-pdf-files/
description: This article shows how to make NUp of PDF files work with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Make NUp of PDF files",
    "alternativeHeadline": "Create NUp PDFs with Flexible Input Methods",
    "abstract": "The NUp feature in Aspose.PDF for .NET allows users to efficiently combine multiple PDF files into a single output document, customizing page size and layout configurations. This functionality supports both file paths and streams, enabling flexible integration into various workflows while enhancing document presentation",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "895",
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
    "url": "/net/make-nup-of-pdf-files/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/make-nup-of-pdf-files/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Make NUp of PDF Using File Paths

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF file and save it to the output PDF file. This overload allows you to make NUp using file paths.The following code snippet shows you how to make NUP using file paths.

```csharp
private static void MakeNupOfPdfUsingFilePaths()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "input.pdf", dataDir + "input2.pdf", "MakeNUpUsingPaths_out.pdf");
}
```

## Make NUp Using Page Size and File Paths

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF file and save it to the output PDF file. This overload allows you to make NUp using file paths. You can also set the page size of the output PDF file using this overload.The following code snippet shows you how to make NUp using page size and file paths.

```csharp
private static void MakeNupUsingPageSizeAndFilePaths()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "MultiplePages.pdf", dataDir + "MakeNUpUsingPageSizeAndPaths_out.pdf", 2, 3, PageSize.A5);
}
```

## Make NUp of PDF Using Page Size, Horizontal and Vertical Values, and File Paths

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF file and save it to the output PDF file. This overload allows you to make NUp using file paths. You can also set the page size of the output PDF file and horizontal and vertical number of pages on each output page using this overload. The following code snippet shows you how to make NUp using page size, horizontal and vertical values, and file paths.

```csharp
private static void MakeNupOfPdfUsingPageSizeHorizontalAndVerticalValuesAndFilePaths()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Make NUp
    pdfEditor.MakeNUp(dataDir + "input.pdf", "UsingPageSizeHorizontalAndVerticalValues_out.pdf", 2, 3);
}
```

## Make NUp of PDF Using Array Of PDF Files and File Paths

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of an array of input PDF files and save them to a single output PDF file. This overload allows you to make NUp using file paths.The following code snippet shows you hot make NUp using array of PDF files and file paths.

```csharp
private static void MakeNupOfPdfUsingArrayOfPdfFilesAndFilePaths()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create array of files
    string[] filesArray = new string[2];
    filesArray[0] = dataDir + "input.pdf";
    filesArray[1] = dataDir + "input2.pdf";
    // Make NUp
    pdfEditor.MakeNUp(filesArray, dataDir + "UsingArrayOfFilesAndPaths_out.pdf", true);
}
```

## Make NUp of PDF Using Streams

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF stream and save it to the output PDF stream. This overload allows you to make NUp using streams instead of file paths. The following code snippet shows you how to make NUp using streams.

```csharp
private static void MakeNupOfPdfUsingStreams()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream1 = new FileStream(dataDir + "input.pdf", FileMode.Open))
    {
        using (var inputStream2 = new FileStream(dataDir + "input2.pdf", FileMode.Open))
        {
            using (var outputStream = new FileStream(dataDir + "MakeNUpUsingStreams_out.pdf", FileMode.Create))
            {
                // Make NUp
                pdfEditor.MakeNUp(inputStream1, inputStream2, outputStream);
            }
        }
    }
}
```

## Make NUp of PDF Using Page Size and Streams

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF stream and save it to the output PDF stream. This overload allows you to make NUp using streams instead of file paths. You can also set the page size of the output PDF stream using this overload. The following code snippet shows you how to make NUp using page size and streams.

```csharp
private static void MakeNupOfPdfUsingPageSizeAndStreams()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_Pages();
    // Create PdfFileEditor object
    var pdfEditor = new Aspose.Pdf.Facades.PdfFileEditor();
    // Create streams
    using (var inputStream = new FileStream(dataDir + "input.pdf", FileMode.Open))
    {
        using (var outputStream = new FileStream(dataDir + "MakeNUpUsingPageSizeAndStreams_out.pdf", FileMode.Create))
        {
            // Make NUp
            pdfEditor.MakeNUp(inputStream, outputStream, 2, 3, PageSize.A5);    
        }    
    }
}
```

## Make NUp of PDF Using Page Size, Horizontal and Vertical Values, and Streams

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of the input PDF stream and save it to the output PDF stream. This overload allows you to make NUp using streams instead of file paths. You can also set the page size of the output PDF stream and horizontal and vertical number of pages on each output page using this overload. The following code snippet shows you how to make NUp using page size, horizontal and vertical values, and streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-MakeNUp-UsingPageSizeHorizontalVerticalValuesAndStreams-UsingPageSizeHorizontalVerticalValuesAndStreams.cs" >}}

## Make NUp of PDF Using Array Of PDF Files and Streams

[MakeNUp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/makenup/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to make NUp of an array of input PDF streams and save them to a single output PDF stream. This overload allows you to make NUp using streams instead of file paths. The following code snippet shows you how to make NUp using array of PDF files using streams.



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-MakeNUp-UsingArrayOfFilesAndStreams-UsingArrayOfFilesAndStreams.cs" >}}
