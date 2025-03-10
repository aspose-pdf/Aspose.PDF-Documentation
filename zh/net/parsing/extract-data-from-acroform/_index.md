---
title: 使用 C# 从 AcroForm 提取数据
linktitle: 从 AcroForm 提取数据
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 50
url: /zh/net/extract-data-from-acroform/
description: Aspose.PDF 使从 PDF 文件中提取表单字段数据变得简单。了解如何从 AcroForms 中提取数据并将其保存为 JSON、XML 或 FDF 格式。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Extract Data from AcroForm using C#",
    "alternativeHeadline": "Effortlessly Extract Acrobat Form Data with C#",
    "abstract": "发现 Aspose.PDF for .NET 中的新功能，简化了从 PDF 文档中的 AcroForms 提取表单字段数据的过程。通过将数据导出为 JSON、XML、FDF 和 XFDF 格式，用户可以高效管理表单数据，同时利用简洁的代码示例无缝集成到应用程序中。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "826",
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
    "url": "/net/extract-data-from-acroform/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/extract-data-from-acroform/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 从 PDF 文档中提取表单字段

除了使您能够生成表单字段和填写表单字段外，Aspose.PDF for .NET 还使从 PDF 文件中提取表单字段数据或有关表单字段的信息变得简单。

在下面的示例代码中，我们演示了如何遍历 PDF 中的每一页，以提取有关 PDF 中所有 AcroForm 的信息以及表单字段值。此示例代码假定您事先不知道表单字段的名称。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFields()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
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

如果您知道要提取值的表单字段名称，则可以使用 Documents.Form 集合中的索引器快速检索此数据。请查看本文底部的示例代码，了解如何使用该功能。

## 按标题检索表单字段值

表单字段的 Value 属性允许您获取特定字段的值。要获取值，请从 Document 对象的 Form 集合中获取表单字段。此示例选择一个 TextBoxField 并使用 Value 属性检索其值。

## 从 PDF 文档提取表单字段到 JSON

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExtractFormFieldsToJson()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "StudentInfoFormElectronic.pdf"))
    {
        // Extract form fields and convert to JSON
        var formData = document.Form.Cast<Aspose.Pdf.Forms.Field>().Select(f => new { Name = f.PartialName, f.Value });
        string jsonString = System.Text.Json.JsonSerializer.Serialize(formData);

        // Output the JSON string
        Console.WriteLine(jsonString);
    }
}
```

## 从 PDF 文件导出数据到 XML

Form 类允许您使用 ExportXml 方法将数据从 PDF 文件导出到 XML 文件。为了将数据导出到 XML，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportXml 方法。最后，您可以关闭 FileStream 对象并释放 Form 对象。以下代码片段向您展示如何将数据导出到 XML 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportFormDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            form.ExportXml(xmlOutputStream);
        }
    }
}
```

## 从 PDF 文件导出数据到 FDF

Form 类允许您使用 ExportFdf 方法将数据从 PDF 文件导出到 FDF 文件。为了将数据导出到 FDF，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportFdf 方法。最后，您可以使用 Form 类的 Save 方法保存 PDF 文件。以下代码片段向您展示如何将数据导出到 FDF 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create fdf file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            form.ExportFdf(fdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToPdf_out.pdf");
    }
}
```

## 从 PDF 文件导出数据到 XFDF

Form 类允许您使用 ExportXfdf 方法将数据从 PDF 文件导出到 XFDF 文件。为了将数据导出到 XFDF，您需要创建一个 Form 类的对象，然后使用 FileStream 对象调用 ExportXfdf 方法。最后，您可以使用 Form 类的 Save 方法保存 PDF 文件。以下代码片段向您展示如何将数据导出到 XFDF 文件。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDF()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    // Create form
    using (var form = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        form.BindPdf(dataDir + "input.pdf");

        // Create xfdf file
        using (var xfdfOutputStream = new FileStream(dataDir + "student1.xfdf", FileMode.Create))
        {
            // Export data
            form.ExportXfdf(xfdfOutputStream);
        }

        // Save PDF document
        form.Save(dataDir + "ExportDataToXFDF_out.pdf");
    }
}
```