---
title: Editing a PDF's individual pages
type: docs
weight: 20
url: /net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/
description: This section explains how to edit PDF's individual pages using PdfPageEditor class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Editing PDF individual pages",
    "alternativeHeadline": "Edit Individual Pages of PDF Easily with PdfPageEditor",
    "abstract": "The PdfPageEditor class in Aspose.PDF for .NET offers users the ability to efficiently manipulate individual pages of a PDF file with functions such as rotation, alignment, and transition effects. This specialized tool enhances control over page display and formatting, allowing for a tailored presentation of PDF content. Experience seamless editing capabilities to optimize how each page is viewed and interacted with",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "593",
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
    "url": "/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/editing-a-pdf-s-individual-pages-using-pdfpageeditor-class/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

Aspose.Pdf.Facades namespace in [Aspose.PDF for .NET](/pdf/net/) allows you to manipulate individual pages in a PDF file. This feature helps you work with the page display, alignment, and transition etc. PdfpageEditor class helps to achieve this functionality. In this article, we’ll look into the properties and methods provided by this class and the working of these methods as well.

{{% /alert %}}

## Explanation

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class is different from [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) and [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) class. First we need to understand the difference, and then we’ll be able to better understand the PdfPageEditor class. PdfFileEditor class allows you manipulate all the pages in a file like adding, deleting, or concatenating pages etc, while PdfContentEditor class helps you manipulate the contents of a page i.e. text and other objects etc. Whereas, PdfPageEditor class only works with the individual page itself like rotating, zooming, and aligning a page etc.

We can divide the features provided by this class into three main categories i.e. Transition, Alignment, and Display. We’re going to discuss these categories below:

### Transition

This class contains two properties related to transition i.e. [TransitionType](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitiontype) and [TransitionDuration](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/transitionduration). TransitionType specifies the transition style to be used when moving to this page from another page during a presentation. TransitionDuration specifies display duration for the pages.

### Alignment

PdfPageEditor class supports both horizontal and vertical alignments. It provides two properties to serve the purpose i.e. [Alignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/alignment) and [VerticalAlignment](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/VerticalAlignment). Alignment property is used to align the contents horizontally. Alignment property takes a value of AlignmentType, which contains three options i.e. Center, Left, and Right. VerticalAlignment property takes a value of VerticalAlignmentType, which contains three options i.e. Bottom, Center, and Top.

### Display

Under display category we can include properties like PageSize, Rotation, Zoom, and DisplayDuration. PageSize property specifies the size of individual page in the file. This property takes PageSize object as an input, which encapsulates predefined page size like A0, A1, A2, A3, A4, A5, A6, B5, Letter, Ledger, and P11x17. Rotation property is used to set the rotation of an individual page. It can take values 0, 90, 180, or 270. Zoom property sets the zoom coefficient for the page, and it takes a float value as an input. This class also provides method to get page size and page rotation of the individual page in the file.

You can find samples of the above mentioned methods in the code snippet given below:



{{< gist "aspose-pdf" "4a12f0ebd453e7f0d552ed6658ed3253" "Examples-CSharp-AsposePdfFacades-TechnicalArticles-EditPdfPages-EditPdfPages.cs" >}}

## Conclusion

{{% alert color="primary" %}}
In this article, we have taken a closer look on the [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class. We have elaborated the properties and methods provided by this class. It makes the manipulation of individual pages in a class a very easy and simple task.
{{% /alert %}}