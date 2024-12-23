---
title: Flatten Annotation from PDF to XFDF 
type: docs
weight: 40
url: /net/flatten-annotation/
description: This section explains how to export annotations from PDF file to XFDF with Aspose.PDF Facades.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Flatten Annotation from PDF to XFDF",
    "alternativeHeadline": "Export PDF Annotations as Non-Editable XFDF Format",
    "abstract": "The Flatten Annotation from PDF to XFDF feature allows users to export annotations from PDF files into XFDF format while preserving their visual representation. This functionality ensures that annotations remain visible in the document but become uneditable, providing a way to permanently apply notes or comments for viewers who may not support annotation features",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "191",
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
    "url": "/net/flatten-annotation/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/flatten-annotation/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

The flattening process means when an annotation is removed from a document, its visual representation is kept intact. A flattened annotation is still visible but is no longer editable by your users or by your app. This can be used, for example, to permanently apply annotations to your document or to make annotations visible to viewers that otherwise can’t show annotations. If not specified, an export will keep all annotations as they are.

When this option is selected, your annotations will be included in your exported PDF as PDF-standard annotations.

Check how the [flatteningAnnotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/methods/flatteningannotations) method used in the next code snippet.

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FlattenAnnotationFromPdf()
{
    // The path to the documents directory
    string dataDir = RunExamples.GetDataDir_AsposePdf();
    // Create PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        annotationEditor.BindPdf(dataDir + "input.pdf");
        // Create FlattenSettings
        var flattenSettings = new Aspose.Pdf.Forms.Form.FlattenSettings
        {
            ApplyRedactions = true,
            CallEvents = false,
            HideButtons = true,
            UpdateAppearances = true
        };
        annotationEditor.FlatteningAnnotations(flattenSettings);
        // Save document
        annotationEditor.Save(dataDir + "FlattenAnnotation_out.pdf");
    }
}
```
