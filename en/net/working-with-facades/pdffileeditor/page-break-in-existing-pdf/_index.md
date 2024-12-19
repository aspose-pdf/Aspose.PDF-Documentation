---
title: Page Break in existing PDF
type: docs
weight: 30
url: /net/page-break-in-existing-pdf/
description: Discover how to insert page breaks in an existing PDF file in .NET using Aspose.PDF for better page management.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Page Break in existing PDF",
    "alternativeHeadline": "Insert Custom Page Breaks in PDF Files",
    "abstract": "Introducing the page break functionality in the PdfFileEditor class, enabling users to control the layout of existing PDF documents with precision. This feature allows for the insertion of page breaks at specific locations within the document, enhancing customization and improving the overall presentation of content. With simple method calls, users can easily modify their PDFs to meet specific formatting requirements",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "369",
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
    "url": "/net/page-break-in-existing-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/page-break-in-existing-pdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

As a default layout, the contents inside PDF files are added in Top-Left to Bottom-Right layout. Once the contents exceed beyond page bottom margin, the page break occurs. However you may come across a requirement to insert page break depending upon requirement. A method named AddPageBreak(...) method is added in [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) class to accomplish this requirement.)

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1).
1. [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2).
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor/methods/addpagebreak).

- src is source document/path to document/stream with source document.
- dest is destination document/path where document will be saved/stream where document will be saved.
- PageBreak is array of page break objects. It have two properties: index of page where page break must be placed and vertical position of the page break on the page.

## Example 1 (Add page break)

```csharp
private static void PageBrakeExample01()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf();
    
    // Instantiate Document instance
    using (Document document = new Aspose.Pdf.Document(dataDir + "Sample-Document-01.pdf"))
    {
        // Instantiate blank Document instance
        using (Document dest = new Aspose.Pdf.Document())
        {
            // Create PdfFileEditor object
            PdfFileEditor fileEditor = new Aspose.Pdf.Facades.PdfFileEditor();
            fileEditor.AddPageBreak(document, dest, new PdfFileEditor.PageBreak[]
            {
                new PdfFileEditor.PageBreak(1, 450)
            });
            // Save resultant file
            dest.Save(dataDir + "PageBreak_out.pdf"); 
        }
    }
}
```

## Example 2

```csharp
public static void PageBrakeExample02()
{
    // Create PdfFileEditor object
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(dataDir + "Sample-Document-02.pdf",
        dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Example 3

```csharp
public static void PageBrakeExample03()
{
    using (Stream src = new FileStream(dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read))
    {
        using (Stream dest = new FileStream(dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite))
        {
            PdfFileEditor fileEditor = new PdfFileEditor();
            fileEditor.AddPageBreak(src, dest,
                new PdfFileEditor.PageBreak[]
                {
                    new PdfFileEditor.PageBreak(1, 450)
                });
        }
    }
}
```
