---
title: Copy Inner and Outer Field
type: docs
weight: 60
url: /net/copy-inner-and-outer-field/
description: This section explains how to copy Inner and Outer Field with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Copy Inner and Outer Field",
    "alternativeHeadline": "Seamlessly Copy Inner and Outer Fields in PDF",
    "abstract": "The Copy Inner and Outer Field functionality in Aspose.PDF for .NET enhances form editing by allowing users to duplicate fields within the same PDF or transfer them from an external PDF file. With the easy-to-use CopyInnerField and CopyOuterField methods provided by the FormEditor class, users can efficiently manage form fields, ensuring consistency and saving time in document preparation",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "337",
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
    "url": "/net/copy-inner-and-outer-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/copy-inner-and-outer-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) method allows you to copy a field in the same file, at the same coordinates, on the specified page. This method requires the field name which you want to copy, the new field name, and the page number at which the field needs to be copied. [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class provides this method. The following code snippet shows you how to copy the field at the same location in the same file.

```csharp
 // For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyInnerField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor object
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Open PDF document
        using (var document = new Aspose.Pdf.Document(dataDir + "Sample-Form-01.pdf"))
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the field "Last Name" from the first page to "Last Name 2" on the second page
            formEditor.CopyInnerField("Last Name", "Last Name 2", 2);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-01-mod.pdf");
        }
    }
}
```

## Copy Outer Field in an Existing PDF File

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) method allows you to copy a form field from an external PDF file and then add it to the input PDF file at the same location and the specified page number. This method requires the PDF file from which the field needs to be copied, the field name, and the page number at which the field needs to be copied. This method is provided by [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class.The following code snippet shows you how to copy a field from an external PDF file.

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void CopyOuterField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Create an instance of FormEditor 
    using (var formEditor = new Aspose.Pdf.Facades.FormEditor())
    {
        // Create empty document
        using (var document = new Aspose.Pdf.Document())
        {
            // Add page
            document.Pages.Add();

            // Bind PDF document
            formEditor.BindPdf(document);

            // Copy the outer field "First Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "First Name", 1);

            // Copy the outer field "Last Name" from the original document to the new document
            formEditor.CopyOuterField(dataDir + "Sample-Form-01.pdf", "Last Name", 1);

            // Save PDF document
            formEditor.Save(dataDir + "Sample-Form-02-mod.pdf");
        }
    }
}
```


