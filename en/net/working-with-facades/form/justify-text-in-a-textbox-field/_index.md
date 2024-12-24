---
title: Justify Text in a Textbox Field
type: docs
weight: 20
url: /net/justify-text-in-a-textbox-field/
description: This article shows you how to Justify Text in a Textbox Field using Form Class.
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Justify Text in a Textbox Field",
    "alternativeHeadline": "Justify Text in PDF Textbox Fields Effortlessly",
    "abstract": "The feature allows users to justify text within a textbox field in PDF documents using the FormEditor class from Aspose.Pdf.Facades namespace. By utilizing the AlignJustified option, users can achieve visually appealing text alignment while maintaining functionality, even though justified alignment is not supported during active input. This enhances the presentation of form data in PDF files",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "283",
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
    "url": "/net/justify-text-in-a-textbox-field/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/justify-text-in-a-textbox-field/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF can perform not only simple and easy tasks but also cope with more complex goals. Check the next section for advanced users and developers."
}
</script>

{{% alert color="primary" %}}

In this article, we’ll show you how to justify text in a textbox field in a PDF file.

{{% /alert %}}

## Implementation details

[FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class in [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/net/aspose.pdf.facades) offers the capability to decorate a PDF form field. Now, if your requirement is to justify the text in a textbox field, you can easily achieve that using [AlignJustified](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade/fields/alignjustified) value of [FormFieldFacade](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formfieldfacade) enumeration and calling the [FormEditor.DecorateField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/decoratefield/index) method. In the below example, first we will fill a Textbox Field using the [FillField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/fillfield/index) method of [Form](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form) class. After that we will use FormEditor class to justify the Text in the Textbox Field. The following code snippet shows you how to justify text in a Textbox Field.

```csharp
private static void JustifyTextInTextboxField()
{
    string dataDir = RunExamples.GetDataDir_AsposePdfFacades_TechnicalArticles();
    using (var source = File.Open(dataDir + "JustifyText.pdf", FileMode.Open))
    {
        using(var ms = new System.IO.MemoryStream())
        {
            // Create Form Object
            var form = new Aspose.Pdf.Facades.Form();
            // Open Source File
            form.BindPdf(source);
            // Fill Text Field
            form.FillField("Text1", "Thank you for using Aspose");

            // Save the document in Memory Stream
            form.Save(ms);

            ms.Seek(0, SeekOrigin.Begin);

            var(var dest = new FileStream(dataDir + "JustifyText_out.pdf", FileMode.Create))
            {
                // Create formEditor Object
                var formEditor = new Aspose.Pdf.Facades.FormEditor();

                // Open PDF from memory stream
                formEditor.BindPdf(ms);

                // Set Text Alignment as Justified
                formEditor.Facade.Alignment = Aspose.Pdf.Facades.FormFieldFacade.AlignJustified;

                // Decorate form field.
                formEditor.DecorateField();

                // Save te resultant file.
                formEditor.Save(dest);
            }
        }
    }
}
```
Please note that justified alignment is not supported by PDF that's why text will be aligned left when you input the text in the Textbox Field. But when field is not active text is justified.
