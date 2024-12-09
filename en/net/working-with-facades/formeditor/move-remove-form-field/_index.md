---
title: Move and Remove Form Field
type: docs
weight: 70
url: /net/move-remove-form-field/
description: Explore how to manage form fields in PDFs, including moving or removing them, using Aspose.PDF for .NET.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Move and Remove Form Field",
    "alternativeHeadline": "Move and Remove Fields in PDF Forms Efficiently",
    "abstract": "The Move and Remove Form Field feature in the FormEditor class allows users to seamlessly reposition and eliminate form fields within existing PDF documents. By utilizing the MoveField and RemoveField methods, users can efficiently customize forms, enhancing usability and document management. This functionality empowers users to optimize their PDF layouts without requiring extensive technical expertise",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "416",
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
    "url": "/net/move-remove-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/move-remove-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Move Form Field to a New Location in Existing PDF File

If you want to move a form field to a new location then you can use [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. You only need to provide the field name and new location of this field to the [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) method. You also need to save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to move a form field in a new location in a PDF file.

```csharp
public static void MoveField()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-05.pdf");
    editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
    editor.Save(dataDir + "Sample-Form-05-mod.pdf");
}
```

## Delete Form Field from an Existing PDF File 

In order to delete a form field from an existing PDF file, you can use RemoveField method of FormEditor class. This method takes only one argument: field name. You need to create an object of FormEditor class, call [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) method to remove a particular field from the PDF and then call the Save method to save the updated PDF file. The following code snippet shows you how to delete form fields from an existing PDF file.

```csharp
public static void RemoveFields()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.RemoveField("First Name");
    editor.RemoveField("Last Name");
    editor.Save(dataDir + "Sample-Form-01-updated.pdf");
}
```

## Rename Form Fields in PDF

Also you can rename your field using [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class.

```csharp
public static void RenameFields()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.RenameField("Last Name", "LastName");
    editor.RenameField("First Name", "FirstName");
    editor.Save(dataDir + "Sample-Form-01-updated.pdf");
}
```