---
title: Field appearance and attributes
type: docs
weight: 40
url: /net/changing-field-appearance-and-attributes/
description: This section explains how you can change field appearance and attributes with FormEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Field appearance and attributes",
    "alternativeHeadline": "Enhance Form Fields with Custom Appearance and Behavior",
    "abstract": "The feature introduced in the FormEditor class of the Aspose.Pdf.Facades namespace enables users to customize both the appearance and attributes of form fields in PDFs. By utilizing methods such as SetFieldAppearance and SetFieldAttributes, developers can easily modify visual elements and behaviors, including field limits, to enhance user interaction and data input efficiency. This functionality offers greater flexibility in designing form fields tailored to specific application needs",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "259",
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
    "url": "/net/changing-field-appearance-and-attributes/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/changing-field-appearance-and-attributes/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) class of [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) allows you to not only change the look and feel of the form field, but also the behavior of the field. In this article, we will see how we can use FormEditor class to change the field appearance, field attributes, and the field limit as well.

{{% /alert %}}

## Implementation details

[SetFieldAppearance](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldappearance) method is used to the change the appearance of a form field. It takes AnnotationFlag as a parameter. AnnotationFlag is an enumeration which has different members like Hidden or NoRotate etc.

[SetFieldAttributes](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldattribute) method is used to change the attribute of a form field. A parameter passed to this method is PropertyFlag enumeration which contains members like ReadOnly or Required etc.

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/FormEditor) class also provides a method to set the field limit. It tells the field that how much characters it can be filled with. The bellow code snippet shows you how all of these methods can be used.



```csharp
private static void AddFieldAndSetAttributes()
{
    // Define the path to the directory containing the input PDF
    var dataDir = RunExamples.GetDataDir_AsposePdf();

    // Open the existing PDF document
    var doc = new Aspose.Pdf.Document(dataDir + "FilledForm.pdf");

    // Create an instance of FormEditor to manipulate form fields
    var formEditor = new Aspose.Pdf.Facades.FormEditor(doc);

    // Add a new text field to the form on page 1 at the specified coordinates and size
    formEditor.AddField(Aspose.Pdf.Facades.FieldType.Text, "text1", 1, 200, 550, 300, 575);

    // Set the field attribute to make the text field required (user must fill it)
    formEditor.SetFieldAttribute("text1", Aspose.Pdf.Facades.PropertyFlag.Required);

    // Set a character limit for the field (maximum 20 characters)
    formEditor.SetFieldLimit("text1", 20);

    // Save the modified PDF with the added field and attributes
    formEditor.Save(dataDir + "ChangingFieldAppearance_out.pdf");
}
```
