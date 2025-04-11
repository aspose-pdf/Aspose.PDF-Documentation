---
title: 使用 XFA 表单
linktitle: XFA 表单
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/xfa-forms/
description: Aspose.PDF for .NET API 让您在 PDF 文档中处理 XFA 和 XFA Acroform 字段。Aspose.Pdf.Facades.
lastmod: "2022-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Working with XFA Forms",
    "alternativeHeadline": "Enhance PDF handling with XFA form support",
    "abstract": "Aspose.PDF for .NET 现在提供了处理 XFA 表单的高级功能，允许开发人员在 PDF 文档中填写、转换和管理 XFA Acroform 字段。此功能简化了动态表单的操作，使得能够无缝访问字段值和属性，同时提供从 XFA 到标准 AcroForms 的高效转换。通过这个强大的解决方案增强您的 PDF 处理工作流程，以处理复杂的表单结构。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "XFA Forms, Aspose.PDF for .NET, fill XFA form, convert XFA to Acroform, get XFA field properties, dynamic forms, XML Forms Architecture, manipulate XFA fields, AcroForm fields, PDF document generation",
    "wordcount": "684",
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
    "url": "/net/xfa-forms/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/xfa-forms/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF for .NET API 让您在 PDF 文档中处理 XFA 和 XFA Acroform 字段。Aspose.Pdf.Facades."
}
</script>

{{% alert color="primary" %}}

动态表单基于一种称为 XFA 的 XML 规范，即“XML 表单架构”。它还可以将动态 XFA 表单转换为标准 Acroform。关于表单的信息（就 PDF 而言）非常模糊——它指定了字段的存在、属性和 JavaScript 事件，但没有指定任何渲染。XFA 表单的对象在加载文档时绘制。

{{% /alert %}}

表单类提供了处理静态 AcroForm 的能力，您可以使用 Form 类的 GetFieldFacade(..) 方法获取特定字段实例。然而，XFA 字段无法通过 Form.GetFieldFacade(..) 方法访问。相反，请使用 [Document.Form.XFA](https://reference.aspose.com/pdf/zh/net/aspose.pdf.forms/form/properties/xfa) 来获取/设置字段值并操作 XFA 字段模板（设置字段属性）。

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

## 填写 XFA 字段

以下代码片段演示了如何填写 XFA 表单中的字段。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void FillXFAFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "FillXFAFields.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
    }
}
```

## 将 XFA 转换为 Acroform

{{% alert color="primary" %}}

在线尝试
您可以通过此链接检查 Aspose.PDF 转换的质量并在线查看结果：[products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

动态表单基于一种称为 XFA 的 XML 规范，即“XML 表单架构”。关于表单的信息（就 PDF 而言）非常模糊——它指定了字段的存在、属性和 JavaScript 事件，但没有指定任何渲染。

目前，PDF 支持两种不同的方法来集成数据和 PDF 表单：

- AcroForms（也称为 Acrobat 表单），在 PDF 1.2 格式规范中引入并包含。
- Adobe XML 表单架构（XFA）表单，在 PDF 1.5 格式规范中作为可选功能引入（XFA 规范未包含在 PDF 规范中，仅作引用）。

我们无法提取或操作 XFA 表单的页面，因为表单内容是在运行时（在查看 XFA 表单时）在尝试显示或渲染 XFA 表单的应用程序中生成的。Aspose.PDF 具有一个功能，允许开发人员将 XFA 表单转换为标准 AcroForms。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ConvertDynamicXFAToAcroForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Load dynamic XFA form
    using (var document = new Aspose.Pdf.Document(dataDir + "DynamicXFAToAcroForm.pdf"))
    {
        // Set the form fields type as standard AcroForm
        document.Form.Type = Aspose.Pdf.Forms.FormType.Standard;

        // Save PDF document
        document.Save(dataDir + "StandardAcroForm_out.pdf");
    }
}
```

## 获取 XFA 字段属性

要访问字段属性，首先使用 Document.Form.XFA.Template 访问字段模板。以下代码片段展示了获取 XFA 表单字段的 X 和 Y 坐标的步骤。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void GetXFAProperties()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Forms();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "GetXFAProperties.pdf"))
    {
        // Get names of XFA form fields
        var names = document.Form.XFA.FieldNames;

        // Set field values
        if (names.Length > 0)
        {
            document.Form.XFA[names[0]] = "Field 0";
        }
        if (names.Length > 1)
        {
            document.Form.XFA[names[1]] = "Field 1";
        }

        // Get field position
        if (names.Length > 0)
        {
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["x"].Value);
            Console.WriteLine(document.Form.XFA.GetFieldTemplate(names[0]).Attributes["y"].Value);
        }

        // Save PDF document
        document.Save(dataDir + "FilledXfa_out.pdf");
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