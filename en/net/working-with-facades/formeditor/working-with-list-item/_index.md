---
title: Working with List Item
type: docs
weight: 50
url: /net/working-with-list-item/
description: This section explains how to work with List Item with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with List Item",
    "alternativeHeadline": "Enhance PDF Forms with List Item Management",
    "abstract": "Enhance your PDF forms with the List Item feature in Aspose.PDF for .NET. Easily add or delete items from ListBox fields using the FormEditor class, allowing for dynamic and customizable user input. This functionality streamlines form management, making it simpler to tailor content to your needs",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "325",
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
    "url": "/net/working-with-list-item/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/working-with-list-item/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Add List Item in an Existing PDF File

[AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) method allows you to add an item in a [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield) field. The first argument is the field name and second argument in the field item. You can either pass a single field item or you can pass an array of string contains a list of items. This method is provided by [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to add list items in a PDF file.

```csharp
public static void AddListItem()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
    editor.AddListItem("Country", "USA");
    editor.AddListItem("Country", "Canada");
    editor.AddListItem("Country", "France");
    editor.AddListItem("Country", "Spain");
    editor.Save(dataDir + "Sample-Form-01-mod.pdf");
}
```

## Delete List Item from an Existing PDF File

[DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) method allows you to delete a particular item from the [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). The first parameter is the field name while second parameter is the item which you want to delete from the list. This method is provided by [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to delete a list item from the PDF file.

```csharp
public static void DelListItem()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-04.pdf");
    editor.DelListItem("Country", "France");
    editor.Save(dataDir + "Sample-Form-04-mod.pdf");
}
```
