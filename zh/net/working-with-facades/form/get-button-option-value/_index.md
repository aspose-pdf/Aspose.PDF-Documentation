---
title: 获取按钮选项值
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 40
url: /zh/net/get-button-option-value/
description: 本节解释如何使用 Aspose.PDF Facades 的 Form 类获取按钮选项值。
lastmod: "2021-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Get Button Option Value",
    "alternativeHeadline": "Retrieve Button Option Values from PDF Efficiently",
    "abstract": "了解如何使用 Aspose.PDF Facades 高效地从现有 PDF 文件中检索按钮选项值。通过 Form 类的 GetButtonOptionValues 和 GetButtonOptionCurrentValue 方法，您可以轻松获取单选按钮的所有可用选项，以及当前选定的值，从而增强您的 PDF 表单管理能力。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "275",
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
    "url": "/net/get-button-option-value/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/get-button-option-value/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 从现有 PDF 文件获取按钮选项值

单选按钮提供了一种显示不同选项的方法。[Form](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/form) 类允许您获取特定单选按钮的所有按钮选项值。您可以使用 [GetButtonOptionValues](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/form/methods/getbuttonoptionvalues) 方法获取这些值。此方法需要单选按钮的名称作为输入参数，并返回一个 Hashtable。您可以遍历此 Hashtable 以获取选项值。以下代码片段向您展示如何从现有 PDF 文件中获取按钮选项值。
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetButtonOptions()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        var optionValues = pdfForm.GetButtonOptionValues("Gender");

        IDictionaryEnumerator optionValueEnumerator = optionValues.GetEnumerator();

        while (optionValueEnumerator.MoveNext())
        {
            Console.WriteLine("Key : {0} , Value : {1} ", optionValueEnumerator.Key, optionValueEnumerator.Value);
        }
    }
}
```

## 从现有 PDF 文件获取当前按钮选项值

单选按钮提供了一种设置选项值的方法，但一次只能选择其中一个。如果您想获取当前选定的选项值，则可以使用 [GetButtonOptionCurrentValue](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/form/methods/getbuttonoptioncurrentvalue) 方法。[Form](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/form) 类提供了此方法。该方法需要单选按钮名称作为输入参数，并返回值作为字符串。以下代码片段向您展示如何从现有 PDF 文件中获取当前按钮选项值。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void GetCurremtButtonOptionValue()
{    
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "FormField.pdf");

        // Get button option values
        string optionValue = pdfForm.GetButtonOptionCurrentValue("Gender");

        Console.WriteLine("Current Value : {0} ", optionValue);
    }
}
```