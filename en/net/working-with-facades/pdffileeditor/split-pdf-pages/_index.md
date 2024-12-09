---
title: Split PDF pages
type: docs
weight: 60
url: /net/split-pdf-pages/
description: This section explains how to split PDF pages with Aspose.PDF Facades using PdfFileEditor class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Split PDF pages",
    "alternativeHeadline": "Effortlessly Split PDF Pages via File Paths and Streams",
    "abstract": "The new Split PDF Pages feature in Aspose.PDF for .NET allows users to efficiently divide PDF documents into various segments using the PdfFileEditor class. This functionality supports splitting from the first page to a specified page, splitting into bulk sets, and even isolating individual pages, all through file paths or streams, providing versatile options for PDF manipulation",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1017",
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
    "url": "/net/split-pdf-pages/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/split-pdf-pages/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Split PDF Pages from First Using File Paths

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file starting from the first page and ending at the specified page number. If you want to manipulate the PDF files from the disk, you can pass the file paths of the intput and output PDF files to this method. The following code snippet shows you how to split PDF pages from first using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingPaths-SplitPagesUsingPaths.cs" >}}

## Split PDF Pages from First Using File Streams

[SplitFromFirst](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/splitfromfirst/methods/1)  method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file starting from the first page and ending at the specified page number. If you want to manipulate the PDF files from the streams, you can pass the input and output PDF streams to this method. The following code snippet shows you how to split PDF pages from first using file streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesUsingStreams-SplitPagesUsingStreams.cs" >}}

## Split PDF Pages to Bulk Using File Paths

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file into multiple sets of pages. In this example, we require two sets of pages (1, 2) and (5, 6). If you want to access the PDF file from the disk, you need to pass the input PDF as file path. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingPaths-SplitPagesToBulkUsingPaths.cs" >}}

## Split PDF Pages to Bulk Using Streams

[SplitToBulks](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittobulks/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF file into multiple sets of pages. In this example, we require two sets of pages (1, 2) and (5, 6). You can pass a stream to this method instead of accessing the file from the disk. This method returns an array of MemoryStream. You can loop through this array and save the individual sets of pages as separate files. The following code snippet shows you how to split PDF pages to bulk using streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToBulkUsingStreams-SplitPagesToBulkUsingStreams.cs" >}}

## Split PDF Pages to End Using File Paths

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF from the specified page number to the end of the PDF file and save it as a new PDF. In order to do this, using file paths, you need to pass input and output file paths and the page number from where the split needs to be started. The output PDF will be saved to the disk. The following code snippet shows you how to split PDF pages to end using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingPaths-SplitPagesToEndUsingPaths.cs" >}}

## Split PDF Pages to End Using Streams

[SplitToEnd](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittoend/index) method of [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class allows you to split the PDF from the specified page number to the end of the PDF file and save it as a new PDF. In order to do this, using streams, you need to pass input and output streams and the page number from where the split needs to be started. The output PDF will be saved to the output stream. The following code snippet shows you how to split PDF pages to end using streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitPagesToEndUsingStreams-SplitPagesToEndUsingStreams.cs" >}}

## Split PDF to Individual Pages Using File Paths

{{% alert color="primary" %}}

You can try to split PDF document and view the results online at this link:

[products.aspose.app/pdf/splitter](https://products.aspose.app/pdf/splitter) {{% /alert %}}

In order to split PDF file to individual pages, you need to pass the PDF as file path to the [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) method. This method will return an array of MemoryStream containing individual pages of the PDF file. You can loop through this array of MemoryStream and save individual pages as individual PDF files on the disk. The following code snippet shows you how to split PDF to individual pages using file paths.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingPaths-SplitToIndividualPagesUsingPaths.cs" >}}

## Split PDF to Individual Pages Using Streams

In order to split PDF file to individual pages, you need to pass the PDF as stream to the [SplitToPages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/splittopages/index) method. This method will return an array of MemoryStream containing individual pages of the PDF file. You can loop through this array of MemoryStream and save individual pages as individual PDF files on the disk, or you can keep these individual pages in the memory stream for later use in your application. The following code snippet shows you how to split PDF to individual pages using streams.

{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-Pages-SplitPages-SplitToIndividualPagesUsingStreams-SplitToIndividualPagesUsingStreams.cs" >}}
