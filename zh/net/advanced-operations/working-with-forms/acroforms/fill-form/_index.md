---
title: 填充 AcroForm - 使用 C# 填充 PDF 表单
linktitle: 填充 AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/fill-form/
description: 您可以使用 Aspose.PDF for .NET 库在 PDF 文档中填充表单。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Fill AcroForm - Fill PDF Form using C#",
    "alternativeHeadline": "Effortlessly Fill PDF Forms with C# Integration",
    "abstract": "Aspose.PDF for .NET 库中的新填充 AcroForm 功能允许开发人员使用 C# 高效地以编程方式填充 PDF 表单。此功能简化了填充表单字段的过程，提高了 PDF 文档管理的生产力和准确性。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "Fill PDF Form, AcroForm, Aspose.PDF for .NET, fill PDF forms C#, TextBoxField, PDF document generation, form field value, PDF manipulation library, fill form field, C# PDF library",
    "wordcount": "328",
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
    "url": "/net/fill-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/fill-form/"
    },
    "dateModified": "2025-04-11",
    "description": "您可以使用 Aspose.PDF for .NET 库在 PDF 文档中填充表单。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 在 PDF 文档中填充表单字段

要填充表单字段，从 Document 对象的 Form 集合中获取字段，并使用适合字段类型的属性设置其值（例如，文本字段的 Value，复选框的 Checked，或列表框的 Selected）。

在此示例中，选择了各种字段并设置了它们的属性。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DocumentWithSomeFields.pdf"))
    {
        // Set value for TextBoxField
        var textBoxField = document.Form["textField"] as Aspose.Pdf.Forms.TextBoxField;
        textBoxField.Value = "Value to be filled in the field";

        // Add option for ListBoxField and select it
        var listBoxField = document.Form["listField"] as Aspose.Pdf.Forms.ListBoxField;
        listBoxField.AddOption("Orange");
        listBoxField.Selected = listBoxField.Options.Count;

        // Set check for CheckboxField
        var checkboxField = document.Form["checkField"] as Aspose.Pdf.Forms.CheckboxField;
        checkboxField.Checked = true;

        // Set check for first option of RadioButtonField
        var radioField = document.Form["radioGroup"] as Aspose.Pdf.Forms.RadioButtonField;
        radioField.Options[1].Selected = true;

        // Save PDF document
        document.Save(dataDir + "DocumentWithSomeFields_out.pdf");
    }
}
```

{{< /tab >}}

{{< tab tabNum="2" >}}

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillFormField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DocumentWithSomeFields.pdf");

    // Set value for TextBoxField
    var textBoxField = document.Form.OfType<Aspose.Pdf.Forms.TextBoxField>().First();
    textBoxField.Value = "Value to be filled in the field";

    // Add option for ListBoxField and select it
    var listBoxField = document.Form.OfType<Aspose.Pdf.Forms.ListBoxField>().First();
    listBoxField.AddOption("Orange");
    listBoxField.Selected = listBoxField.Options.Count;

    // Set check for CheckboxField
    var checkboxField = document.Form.OfType<Aspose.Pdf.Forms.CheckboxField>().First();
    checkboxField.Checked = true;

    // Set check for first option of RadioButtonField
    var radioField = document.Form.OfType<Aspose.Pdf.Forms.RadioButtonField>().First();
    radioField.Options[1].Selected = true;

    // Save PDF document
    document.Save(dataDir + "DocumentWithSomeFields_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

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