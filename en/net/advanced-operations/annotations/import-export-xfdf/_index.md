---
title: Import and Export Annotations to XFDF
linktitle: Import and Export Annotations to XFDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /net/import-export-xfdf/
description: You may import and export annotation with XFDF format with C# and Aspose.PDF for .NET library.
lastmod: "2022-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Annotations to XFDF",
    "alternativeHeadline": "Effortless XFDF Annotation Import and Export",
    "abstract": "The new import and export functionality for XFDF in the Aspose.PDF for .NET library enhances PDF document management by allowing seamless transfer of annotation data. This feature enables users to easily integrate annotations from XFDF files and export them back, promoting efficient data exchange and archiving capabilities for PDF forms",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import Annotations, Export Annotations, XFDF Format, Aspose.PDF for .NET, PdfAnnotationEditor, ImportAnnotationFromXfdf, ExportAnnotationsXfdf, PDF Forms Manipulation",
    "wordcount": "670",
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
    "url": "/net/import-export-xfdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-xfdf/"
    },
    "dateModified": "2024-11-25",
    "description": "You may import and export annotation with XFDF format with C# and Aspose.PDF for .NET library."
}
</script>

{{% alert color="primary" %}}

XFDF stand for XML Forms Data Format. It is an XML based file format. This file format is used to represent form data or annotations contained in a PDF form. XFDF can be used for many different purposes, but in our case, it can be used to either send or receive form data or annotations to other computers or servers etc, or it can be used to archive the form data or annotations. In this article, we will see how Aspose.Pdf.Facades has taken this concept into consideration and how we can import and export annotations data to XFDF file.

{{% /alert %}}

**Aspose.PDF for .NET** is a feature rich component when it comes to editing the PDF documents. As we know XFDF is an important aspect of PDF forms manipulation, Aspose.Pdf.Facades namespace in Aspose.PDF for .NET has considered this very well, and have provided methods to import and export annotations data to XFDF files.

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor) class contains two methods to work with import and export of annotations to XFDF file. [ExportAnnotationsXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/exportannotationsxfdf/index) method provides the functionality to export annotations from a PDF document to XFDF file, while [ImportAnnotationFromXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/importannotationfromxfdf/index) method allows you to import annotations from an existing XFDF file. In order to import or export annotations we need to specify the annotation types. We can specify these types in the form of an enumeration and then pass this enumeration as an argument to any of these methods. This way, the annotations of the specified types will only be imported or exported to an XFDF file.

The following code snippet also work with [Aspose.PDF.Drawing](/pdf/net/drawing/) library.

The following code snippet shows you how to export annotations to an XFDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportAnnotationsToXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "AnnotationDemo1.pdf");

        // Define the annotation types to export
        var annotType = new Aspose.Pdf.Annotations.AnnotationType[] { Aspose.Pdf.Annotations.AnnotationType.Line, Aspose.Pdf.Annotations.AnnotationType.Square };

        // Export annotations to XFDF file
        using (var fileStream = File.OpenWrite(dataDir + "exportannotations_out.xfdf"))
        {
            annotationEditor.ExportAnnotationsXfdf(fileStream, 1, 1, annotType);
            fileStream.Flush();
        }
    }
}
```

The next code snippet describes how import annotations from an XFDF file:

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromXfdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create PdfAnnotationEditor object
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Create PDF document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            var page = document.Pages.Add();

            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Define the export file name
            var exportFileName = dataDir + "exportannotations.xfdf";

            // Import annotations from the XFDF file
            annotationEditor.ImportAnnotationsFromXfdf(exportFileName);

            // Save PDF document
            document.Save(dataDir + "ImportAnnotationFromXfdf_out.pdf");
        }
    }
}
```

## Yet another way to export/import annotations at once

In the code below an ImportAnnotations method allows import annotations directly from another PDF doc.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportAnnotationFromPDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Open PDF document
    using (var documentFrom = new Aspose.Pdf.Document(dataDir + "some_doc.pdf"))
    {
        // Create PDF document
        using (var documentTo = new Aspose.Pdf.Document())
        {
            // Add page
            var page = documentTo.Pages.Add();

            // Export/import
            using (var ms = new MemoryStream())
            {
                documentFrom.ExportAnnotationsToXfdf(ms);
                documentTo.ImportAnnotationsFromXfdf(ms);
            }

            // Save PDF document
            documentTo.Save(dataDir + "AnnotationDemo3_out.pdf");
        }
    }
}
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
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
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/net/create-pdf-document/screenshot.png",
    "softwareVersion": "2022.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>
