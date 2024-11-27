---
title: Import and Export Form Field
type: docs
weight: 80
url: /net/import-export-form-field/
description: Fill Form fields using DataTable with  FormEditor Class by Aspose.PDF for .NET
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Form Field",
    "alternativeHeadline": "Streamline PDF Form Management with Import/Export Features",
    "abstract": "The Import and Export Form Field feature in Aspose.PDF for .NET allows users to seamlessly fill and manipulate PDF form fields using various data sources such as FDF, XFDF, XML, and even System.Data.DataTable objects. This powerful API enables automated data handling, enhancing the efficiency of PDF form management and streamlining the data input process",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "252",
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
    "url": "/net/import-export-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-export-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

Aspose.PDF for .NET provides great capabilities for create/manipulating form fields inside PDF document. Using this API, you can programmatically fill form fields inside PDF file, fill form fields by [Import Data from FDF into a PDF File](/pdf/net/import-and-export-data/), [Import Data from XFDF into a PDF File](/pdf/net/import-and-export-data/), [Import Data from XML into a PDF File](/pdf/net/import-and-export-data/) or even you can import data from [System.Data.DataTable](https://reference.aspose.com/pdf/net/aspose.pdf.table/importdatatable/methods/1) object.

```csharp
public static void ImportData()
{
    var editor = new Form();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.ImportFdf(System.IO.File.OpenRead(dataDir + "Sample-Form-01-upd.fdf"));
    editor.ImportXml(System.IO.File.OpenRead(dataDir + "Sample-Form-01-upd.xml"));
    editor.ImportXfdf(System.IO.File.OpenRead(dataDir + "Sample-Form-01-upd.xfdf"));
    editor.Save(dataDir + "Sample-Form-01-updated.pdf");
}
```

## Export Data from FDF into a PDF File

```csharp
public static void ExportData()
{
    var editor = new Form();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.ExportFdf(System.IO.File.OpenWrite(dataDir + "Sample-Form-01-mod.fdf"));
    editor.ExportXml(System.IO.File.OpenWrite(dataDir + "Sample-Form-01-mod.xml"));
    editor.ExportXfdf(System.IO.File.OpenWrite(dataDir + "Sample-Form-01-mod.xfdf"));
}
```
