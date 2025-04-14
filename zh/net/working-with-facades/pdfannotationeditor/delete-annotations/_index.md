---
title: 删除注释（外观）
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/delete-annotations/
description: 本节解释如何使用 PdfAnnotationEditor 类删除 Aspose.PDF 外观中的注释。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Delete Annotations (facades)",
    "alternativeHeadline": "Effortlessly Remove Specific PDF Annotations with Ease",
    "abstract": "Aspose.PDF for .NET 外观功能允许用户使用 PdfAnnotationEditor 类高效地从现有 PDF 文件中删除注释。用户可以选择删除所有注释或针对特定注释类型，从而简化文档编辑并增强 PDF 管理能力。此功能通过提供简单的注释删除方法，简化了维护干净和专注的 PDF 文档的过程。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "427",
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
    "url": "/net/delete-annotations/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/delete-annotations/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一节以获取高级用户和开发人员的信息。"
}
</script>

## 从现有 PDF 文件中删除所有注释

[PdfAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 允许您从现有 PDF 文件中删除所有注释。首先，创建一个 [PdfAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。之后，调用 [DeleteAnnotations](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) 方法以删除文件中的所有注释，然后使用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段演示了如何从 PDF 文件中删除所有注释。

{{< tabs tabID="1" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
    {
        // Bind PDF document
        annotationEditor.BindPdf(dataDir + "DeleteAllAnnotationsFromPage.pdf");

        // Delete all annoations
        annotationEditor.DeleteAnnotations();

        // Save PDF document
        annotationEditor.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotations()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Bind PDF document
    annotationEditor.BindPdf(dataDir + "DeleteAllAnnotationsFromPage.pdf");

    // Delete all annoations
    annotationEditor.DeleteAnnotations();

    // Save PDF document
    annotationEditor.Save(dataDir + "DeleteAllAnnotationsFromPage_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 按指定类型删除所有注释

您可以使用 [PdfAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 类按指定注释类型从现有 PDF 文件中删除所有注释。为此，您需要创建一个 [PdfAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。之后，调用 [DeleteAnnotations](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotations) 方法，并传入字符串参数，以删除文件中的所有注释；字符串参数表示要删除的注释类型。最后，使用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save) 方法保存更新后的 PDF 文件。以下代码片段演示了如何按指定注释类型删除所有注释。

{{< tabs tabID="2" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotationByType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf"))
    {
        // Collect all annotation types from all pages
        var annotationTypes = new List<string>();
        foreach (Aspose.Pdf.Page page in document.Pages)
        {
            // If page has no annotations, skip it
            if (page.Annotations == null)
            {
                continue;
            }

            // Retrieve each annotation type from the page
            IEnumerable<string> pageAnnotationTypes = page.Annotations.Select(ann => ann.AnnotationType.ToString());
            annotationTypes.AddRange(pageAnnotationTypes);
        }

        // Make the list of annotation types distinct
        annotationTypes = annotationTypes.Distinct().ToList();

        // Display each annotation type to the user
        int index;
        for (index = 0; index < annotationTypes.Count; index++)
        {
            Console.WriteLine($"{index + 1}. {annotationTypes[index]}");
        }

        // Prompt user to choose the annotation type to delete
        Console.Write("Please enter number: ");
        index = int.Parse(Console.ReadLine()) - 1;

        // Create an instance of PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Delete the annotation selected by the user
            annotationEditor.DeleteAnnotations(annotationTypes[index]);

            // Save PDF document
            annotationEditor.Save(dataDir + "DeleteAllAnnotationByType_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAllAnnotationByType()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf");

    // Collect all annotation types from all pages
    var annotationTypes = new List<string>();
    foreach (Aspose.Pdf.Page page in document.Pages)
    {
        // If page has no annotations, skip it
        if (page.Annotations == null)
        {
            continue;
        }

        // Retrieve each annotation type from the page
        IEnumerable<string> pageAnnotationTypes = page.Annotations.Select(ann => ann.AnnotationType.ToString());
        annotationTypes.AddRange(pageAnnotationTypes);
    }

    // Make the list of annotation types distinct
    annotationTypes = annotationTypes.Distinct().ToList();

    // Display each annotation type to the user
    int index;
    for (index = 0; index < annotationTypes.Count; index++)
    {
        Console.WriteLine($"{index + 1}. {annotationTypes[index]}");
    }

    // Prompt user to choose the annotation type to delete
    Console.Write("Please enter number: ");
    index = int.Parse(Console.ReadLine()) - 1;

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Bind PDF document
    annotationEditor.BindPdf(document);

    // Delete the annotation selected by the user
    annotationEditor.DeleteAnnotations(annotationTypes[index]);

    // Save PDF document
    annotationEditor.Save(dataDir + "DeleteAllAnnotationByType_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}

## 按指定名称删除注释

您可以使用 [PdfAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 类按其 **唯一名称** 删除现有 PDF 文件中的特定注释。为此，您需要创建一个 [PdfAnnotationEditor](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor) 对象，并使用 [BindPdf](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法绑定输入 PDF 文件。之后，调用 [DeleteAnnotation](https://reference.aspose.com/pdf/zh/net/aspose.pdf.facades/pdfannotationeditor/methods/deleteannotation) 方法，传入要删除的注释名称。最后，使用 [Save](https://reference.aspose.com/pdf/zh/net/aspose.pdf/document/methods/save) 方法存储更新后的 PDF 文件。以下代码片段演示了如何按名称删除注释。

{{< tabs tabID="3" tabTotal="2" tabName1=".NET Core 3.1" tabName2=".NET 8" >}}
{{< tab tabNum="1" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAnnotationByName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf"))
    {
        // Display the list of annotations in the first page (adjust as needed for multiple pages)
        int index;
        for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
        {
            Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
        }

        // Prompt the user to enter the index of the annotation to delete
        Console.Write("Please enter number: ");
        index = int.Parse(Console.ReadLine());

        // Create an instance of PdfAnnotationEditor
        using (var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor())
        {
            // Bind PDF document
            annotationEditor.BindPdf(document);

            // Delete the annotation selected by the user
            annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

            // Save PDF document
            annotationEditor.Save(dataDir + "DeleteAnnotationByName_out.pdf");
        }
    }
}
```
{{< /tab >}}

{{< tab tabNum="2" >}}
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.Pdf-for-.NET
private static void DeleteAnnotationByName()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdfFacades_Annotations();

    // Open PDF document
    using var document = new Aspose.Pdf.Document(dataDir + "DeleteAllAnnotations.pdf");

    // Display the list of annotations in the first page (adjust as needed for multiple pages)
    int index;
    for (index = 1; index <= document.Pages[1].Annotations.Count; index++)
    {
        Console.WriteLine($"{index}. {document.Pages[1].Annotations[index].Name} {document.Pages[1].Annotations[index].AnnotationType}");
    }

    // Prompt the user to enter the index of the annotation to delete
    Console.Write("Please enter number: ");
    index = int.Parse(Console.ReadLine());

    // Create an instance of PdfAnnotationEditor
    using var annotationEditor = new Aspose.Pdf.Facades.PdfAnnotationEditor();

    // Bind PDF document
    annotationEditor.BindPdf(document);

    // Delete the annotation selected by the user
    annotationEditor.DeleteAnnotation(document.Pages[1].Annotations[index].Name);

    // Save PDF document
    annotationEditor.Save(dataDir + "DeleteAnnotationByName_out.pdf");
}
```
{{< /tab >}}
{{< /tabs >}}