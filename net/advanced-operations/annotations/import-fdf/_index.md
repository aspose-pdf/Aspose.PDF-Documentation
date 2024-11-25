---
title: Import FDF format annotations to PDF via C#
linktitle: Import FDF format annotations to PDF
type: docs
weight: 50
url: /net/import-fdf/
description: Use existing Form.ImportFdf() or add PdfAnnotationEditor.ImportAnnotationsFromFdf() methods for import FDF format annotations to PDF with Aspose.PDF for .NET.
lastmod: "2024-09-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import FDF format annotations to PDF via C#",
    "alternativeHeadline": "Effortlessly Import FDF Annotations to PDF with C#",
    "abstract": "Import FDF format annotations to PDF files seamlessly using Aspose.PDF for .NET, enhancing your PDF management capabilities. With the Form.ImportFdf() and PdfAnnotationEditor.ImportAnnotationsFromFdf() methods, you can effortlessly integrate form data and comments from lightweight FDF files into your PDF documents, streamlining data submission and annotation processes",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Import FDF, FDF format annotations, PDF annotations, Aspose.PDF for .NET, Form.ImportFdf(), PdfAnnotationEditor, import annotations from FDF, lightweight PDF, fill form fields, exchange annotations",
    "wordcount": "350",
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
    "url": "/net/import-fdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-fdf/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

FDF (Forms Data Format) is a file format that stores and transmits form data and annotations in PDF documents. It is a lightweight PDF version that contains only the form field values or comments, without the full content of the original PDF file. FDF files are often used when submitting form data to a server, or when exchanging annotations without needing to send the entire PDF file. They can be imported back into a PDF to fill in form fields or apply comments.

{{% /alert %}}

[PDFAnnotationEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/) class contains method to work with import of annotations from FDF file. [PdfAnnotationEditor.ImportAnnotationsFromFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfannotationeditor/importannotationsfromfdf/) method provides the functionality to import annotations from a FDF document to PDF file.

Also, [Class Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/) include the [Form.ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/importfdf/) method - imports the content of the fields from the FDF file and put them into the new PDF.

The following code snippet shows you how to Import FDF format annotations to PDF with Form.ImportFdf() method:

```csharp
var fdfPath = Params.InputPath + "test.fdf";
var templatePath = Params.InputPath + "Empty.pdf";
var outputPath = Params.OutputPath + "test_form.pdf";

using (var form = new Aspose.Pdf.Facades.Form(templatePath))
{
    using (var fdfInputStream = new FileStream(fdfPath, FileMode.Open))
    {
        form.ImportFdf(fdfInputStream);
    }

    form.Save(outputPath);
}
```

The next code snippet shows how to import FDF format annotations to PDF with PdfAnnotationEditor.ImportAnnotationsFromFdf() method:

```csharp
var fdfPath = Params.InputPath + "test.fdf";
var templatePath = Params.InputPath + "Empty.pdf";
var outputPath = Params.OutputPath + "test_annEditor.pdf";

var editor = new PdfAnnotationEditor();
editor.BindPdf(new Document(templatePath));
editor.ImportAnnotationsFromFdf(fdfPath);
editor.Save(outputPath);
```
