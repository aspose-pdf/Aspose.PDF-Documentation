---
title: Decorate Form Field in PDF
type: docs
weight: 30
url: /net/decorate-form-field/
description: This section explains how to decorate Form Field in PDF using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Decorate Form Field in PDF",
    "alternativeHeadline": "Enhance PDF Forms with Custom Field Decorations",
    "abstract": "Introducing a powerful feature that enhances PDF form management: the ability to decorate individual or all form fields using the FormEditor Class. This functionality allows users to customize field attributes such as font style, size, border color, and alignment, streamlining the process of creating visually appealing and well-structured PDF forms. Enhance your PDF workflows with this intuitive decoration method for a more polished document presentation",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "609",
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
    "url": "/net/decorate-form-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/decorate-form-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

## Decorate a Particular Form Field in an Existing PDF File

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method present in [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class allows you to decorate a particular form field in a PDF file. If you want to decorate a particular field then you need to pass the field name to this method. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. You also need to assign the [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield) method and finally save the updated PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class.
The following code snippet shows you how to decorate a particular form field.

```csharp
public static void DecorateField()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");

    var cityDecoration = new FormFieldFacade
    {
        Font = FontStyle.Courier,
        FontSize = 12,
        BorderColor = System.Drawing.Color.Black,
        BorderWidth = 2
    };

    editor.Facade = cityDecoration;
    editor.DecorateField("City");
    editor.Save(dataDir + "Sample-Form-02.pdf");
}
```

## Decorate All Fields of a Particular Type in an Existing PDF File

[DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method allows you to decorate all the form fields of a particular type in a PDF file at once. If you want to decorate all fields of a particular type then you need to pass the field type to this method. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) and [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) classes. You also need to assign the [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object to [Facade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/properties/index) property of the [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) object. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) object. Once you have set the attributes, you can call the [DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades.formeditor/decoratefield/methods/1) method and finally save the updated PDF using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to decorate all the fields of a particular type.


```csharp
public static void DecorateField2()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");

    var textFieldDecoration = new FormFieldFacade
    {
        Alignment = FormFieldFacade.AlignCenter,
    };

    editor.Facade = textFieldDecoration;
    editor.DecorateField(FieldType.Text);
    editor.Save(dataDir + "Sample-Form-01-align-text.pdf");
}
```




