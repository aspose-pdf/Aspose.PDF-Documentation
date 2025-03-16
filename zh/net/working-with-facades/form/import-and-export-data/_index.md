---
title: 导入和导出数据
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 70
url: /zh/net/import-and-export-data/
description: 本节解释如何使用表单类通过 Aspose.PDF Facades 导入和导出数据。
lastmod: "2024-06-05"
draft: false
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Import and Export Data",
    "alternativeHeadline": "Effortless Data Import and Export for PDF Forms",
    "abstract": "导入和导出数据功能在 Aspose.PDF for .NET 中允许通过启用用户利用 XML、FDF、XFDF 和 JSON 格式导入和导出 PDF 表单数据，从而实现文档数据管理的无缝集成。此功能增强了数据处理能力，使得自动化工作流程和直接从 PDF 文档维护准确记录变得更加容易。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "1085",
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
    "url": "/net/import-and-export-data/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/import-and-export-data/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类允许您使用 [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades.form/importxml/methods/1) 方法从 XML 文件导入数据到 PDF 文件。为了从 XML 导入数据，您需要创建一个 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的对象，然后使用 FileStream 对象调用 [ImportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxml/index) 方法。最后，您可以使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 方法保存 PDF 文件。以下代码片段演示了如何从 XML 文件导入数据。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open xml file
        using (var xmlInputStream = new FileStream(dataDir + "input.xml", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXml(xmlInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXML_out.pdf");
        }
    }
}
```

## 从 PDF 文件导出数据到 XML

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类允许您使用 [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) 方法从 PDF 文件导出数据到 XML 文件。为了导出数据到 XML，您需要创建一个 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的对象，然后使用 FileStream 对象调用 [ExportXml](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxml) 方法。最后，您可以关闭 FileStream 对象并释放 Form 对象。以下代码片段演示了如何导出数据到 XML 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXml()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XML file
        using (var xmlOutputStream = new FileStream(dataDir + "input.xml", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXml(xmlOutputStream);
        }
    }
}
```

## 从 FDF 导入数据到 PDF 文件

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类允许您使用 [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) 方法从 FDF 文件导入数据到 PDF 文件。为了从 FDF 导入数据，您需要创建一个 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的对象，然后使用 FileStream 对象调用 [ImportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importfdf) 方法。最后，您可以使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 方法保存 PDF 文件。以下代码片段演示了如何从 FDF 文件导入数据。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromPdfIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");
        
        // Open FDF file
        using (var fdfInputStream = new FileStream(dataDir + "student.fdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportFdf(fdfInputStream);         

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromPdf_out.pdf");
        }
    }
}
```

## 从 PDF 文件导出数据到 FDF

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类允许您使用 [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) 方法从 PDF 文件导出数据到 FDF 文件。为了导出数据到 FDF，您需要创建一个 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的对象，然后使用 FileStream 对象调用 [ExportFdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportfdf) 方法。最后，您可以使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 方法保存 PDF 文件。以下代码片段演示了如何导出数据到 FDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToPdfFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create FDF file
        using (var fdfOutputStream = new FileStream(dataDir + "student.fdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportFdf(fdfOutputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToPdf_out.pdf"); 
        }
    }
}
```

## 从 XFDF 导入数据到 PDF 文件

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类允许您使用 [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) 方法从 XFDF 文件导入数据到 PDF 文件。为了从 XFDF 导入数据，您需要创建一个 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的对象，然后使用 FileStream 对象调用 [ImportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/importxfdf) 方法。最后，您可以使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 方法保存 PDF 文件。以下代码片段演示了如何从 XFDF 文件导入数据。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportDataFromXFDIntoPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Open XFDF file
        using (var xfdfInputStream = new FileStream(dataDir + "test2.xfdf", FileMode.Open))
        {
            // Import data
            pdfForm.ImportXfdf(xfdfInputStream);           

            // Save PDF document
            pdfForm.Save(dataDir + "ImportDataFromXFDF_out.pdf");
        }
    }
}
```

## 从 PDF 文件导出数据到 XFDF

[Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类允许您使用 [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) 方法从 PDF 文件导出数据到 XFDF 文件。为了导出数据到 XFDF，您需要创建一个 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的对象，然后使用 FileStream 对象调用 [ExportXfdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/exportxfdf) 方法。最后，您可以使用 [Form](https://reference.aspose.com/pdf/net/aspose.pdf.forms/form) 类的 [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/save) 方法保存 PDF 文件。以下代码片段演示了如何导出数据到 XFDF 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportDataToXFDFFromPdf()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var pdfForm = new Aspose.Pdf.Facades.Form())
    {
        // Bind PDF document
        pdfForm.BindPdf(dataDir + "input.pdf");

        // Create XFDF file
        using (var xfdfOutputStream = new FileStream(dataDir + "out.xfdf", FileMode.Create))
        {
            // Export data
            pdfForm.ExportXfdf(xfdfOutputStream);

            // Save PDF document
            pdfForm.Save(dataDir + "ExportDataToXFDF_out.pdf");
        }
    }
}
```

## 从字段导出值到 JSON 文件

Aspose.Pdf.Facades 提供了一个替代 API 用于处理表单字段。此代码片段演示了如何使用此 API 导出和导入字段值。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ExportValuesFromFieldsToJSON()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();
    
    using (var form = new Aspose.Pdf.Facades.Form())
    {       
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Create JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Create))
        {
            // Export data
            form.ExportJson(jsonStream);
        }
    }
}
```

## 从 JSON 文件导入值到字段

此代码片段演示了如何使用 Aspose.Pdf.Facades API 从 JSON 文件导入值到 PDF 文档的表单字段。FileStream 用于处理 JSON 文件。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void ImportValuesFromJsonToForm()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Forms();

    using (var form = new Aspose.Pdf.Facades.Form())
    {        
        // Bind PDF document
        form.BindPdf(dataDir + "Test2.pdf");

        // Import from JSON file
        using (FileStream jsonStream = new FileStream(dataDir + "Test2.json", FileMode.Open))
        {
            // Export data
            form.ImportJson(jsonStream);
        }
    }
}
```