---
title: 提取 AcroForm - 从 PDF 中提取表单数据 C#
linktitle: 提取 AcroForm
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 30
url: /zh/net/extract-form/
description: 使用 Aspose.PDF for .NET 库从您的 PDF 文档中提取表单。获取 PDF 文件中单个字段的值。
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract AcroForm - Extract Form Data from PDF in C#",
    "alternativeHeadline": "Effortlessly Extract PDF Form Data Using C#",
    "abstract": "Aspose.PDF for .NET 中的新提取 AcroForm 功能使开发人员能够轻松从 PDF 文档中提取表单数据。此功能允许用户从 PDF 中的单个字段或所有字段中检索值，从而增强 C# 应用程序中的数据管理和操作能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "extract form data, PDF in C#, Aspose.PDF for .NET, AcroForm extraction, get field values PDF, PDF form fields, individual field value, get fields in region, manipulate PDF forms, C# PDF library",
    "wordcount": "673",
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
    "url": "/net/extract-form/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-form/"
    },
    "dateModified": "2024-11-25",
    "description": "使用 Aspose.PDF for .NET 库从您的 PDF 文档中提取表单。获取 PDF 文件中单个字段的值。"
}
</script>

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

## 从表单中提取数据

### 获取 PDF 文档中所有字段的值

要获取 PDF 文档中所有字段的值，您需要遍历所有表单字段，然后使用 Value 属性获取值。从 Form 集合中获取每个字段，在名为 Field 的基本字段类型中访问其 Value 属性。

以下 C# 代码片段演示了如何获取 PDF 文档中所有字段的值。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValuesFromFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValuesFromAllFields.pdf"))
    {
        // Get values from all fields
        foreach (Aspose.Pdf.Forms.Field formField in document.Form)
        {
            Console.WriteLine("Field Name : {0} ", formField.PartialName);
            Console.WriteLine("Value : {0} ", formField.Value);
        }
    }
}
```

### 获取 PDF 文档中单个字段的值

表单字段的 Value 属性允许您获取特定字段的值。要获取值，从 Document 对象的 Form 集合中获取表单字段。此 C# 示例选择一个 [TextBoxField](https://reference.aspose.com/pdf/zh/net/aspose.pdf.forms/textboxfield) 并使用 Value 属性检索其值。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetValueFromField()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get a field
        if (document.Form["textbox1"] is Aspose.Pdf.Forms.TextBoxField textBoxField)
        {
            // Get field value
            Console.WriteLine("PartialName : {0} ", textBoxField.PartialName);
            Console.WriteLine("Value : {0} ", textBoxField.Value);
        }
    }
}
```

要获取提交按钮的 URL，请使用以下代码行。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetSubmitFormActionUrl()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetValueFromField.pdf"))
    {
        // Get the SubmitFormAction from the form field
        if (document.Form[1].OnActivated is Aspose.Pdf.Annotations.SubmitFormAction act)
        {
            // Output the URL of the SubmitFormAction
            Console.WriteLine(act.Url.Name);
        }
    }
}
```

### 从 PDF 文件的特定区域获取表单字段

有时，您可能知道文档中表单字段的位置，但不知道它的名称。例如，如果您只有打印表单的示意图。使用 Aspose.PDF for .NET，这不是问题。您可以找出 PDF 文件中给定区域的字段。要从 PDF 文件的特定区域获取表单字段：

1. 使用 [Document](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document) 对象打开 PDF 文件。
1. 从文档的 Forms 集合中获取表单。
1. 指定矩形区域并将其传递给 Form 对象的 GetFieldsInRect 方法。返回一个 Fields 集合。
1. 使用此集合来操作字段。

以下 C# 代码片段演示了如何获取 PDF 文件中特定矩形区域的表单字段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetFieldsFromRegion()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetFieldsFromRegion.pdf"))
    {
        // Create rectangle object to get fields in that area
        var rectangle = new Aspose.Pdf.Rectangle(35, 30, 500, 500);

        // Get the PDF form
        var form = document.Form;

        // Get fields in the rectangular area
        var fields = form.GetFieldsInRect(rectangle);

        // Display Field names and values
        foreach (var field in fields)
        {
            // Display image placement properties for all placements
            Console.Out.WriteLine("Field Name: " + field.FullName + "-" + "Field Value: " + field.Value);
        }
    }
}
```

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