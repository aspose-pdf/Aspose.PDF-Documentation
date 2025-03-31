---
title: 创建符合 PDF/3-A 标准的 PDF 并在 C# 中附加 ZUGFeRD 发票
linktitle: 将 ZUGFeRD 附加到 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 10
url: /zh/net/attach-zugferd/
description: 了解如何生成带有 ZUGFeRD 的 PDF 文档
lastmod: "2023-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Creating PDF/3-A compliant PDF and attaching ZUGFeRD invoice in C#",
    "alternativeHeadline": "Attach ZUGFeRD Invoices to PDF in C#",
    "abstract": "发现新功能，允许开发人员生成符合 PDF/A-3B 的 PDF 文档，并使用 C# 无缝附加 ZUGFeRD 发票。此功能简化了在 PDF 文件中嵌入发票元数据的过程，确保长期文档保存和符合电子发票标准",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "429",
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
    "url": "/net/attach-zugferd/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/attach-zugferd/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 将 ZUGFeRD 附加到 PDF

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

我们建议按照以下步骤将 ZUGFeRD 附加到 PDF：

* 定义一个路径变量，指向输入和输出 PDF 文件所在的文件夹。
* 通过从路径加载现有 PDF 文件（例如 "ZUGFeRD-test.pdf"）来创建文档对象。
* 通过提供路径和另一个名为 "factur-x.xml" 的文件的描述来创建 [FileSpecification](https://reference.aspose.com/pdf/zh/net/aspose.pdf/filespecification/) 对象，该文件包含符合 ZUGFeRD 标准的发票元数据。
* 向文件规范对象添加属性，例如描述、MIME 类型和 AF 关系。AF 关系指示嵌入文件与 PDF 文档的关系。在这种情况下，它被设置为 "Alternative"，意味着嵌入文件是 PDF 内容的替代表示。
* 将文件规范对象添加到文档的嵌入文件集合中。文件名应符合 ZUGFeRD 标准，例如 "factur-x.xml"。
* 将文档转换为 PDF/A-3B 格式，这是 PDF 的一个子集，确保电子文档的长期保存。PDF/A-3B 允许在 PDF 文档中嵌入任何格式的文件。
* 将转换后的文档保存为新的 PDF 文件（例如 "ZUGFeRD-res.pdf"）。

```cs
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void AttachZUGFeRD()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_DocumentConversion();
    
    // Open PDF document
    using (var document = new Aspose.Pdf.Document(dataDir + "ZUGFeRD-testInput.pdf"))
    {
        // Setup new file to be added as attachment
        var description = "Invoice metadata conforming to ZUGFeRD standard";
        var fileSpecification = new Aspose.Pdf.FileSpecification(dataDir + "ZUGFeRD-testXmlInput.xml", description)
        {
            Description = "Zugferd",
            MIMEType = "text/xml",
            Name = "factur-x.xml"
        };
        // Add attachment to document's attachment collection
        document.EmbeddedFiles.Add(fileSpecification);
        document.Convert(new MemoryStream(), Aspose.Pdf.PdfFormat.ZUGFeRD, Aspose.Pdf.ConvertErrorAction.Delete);
        // Save PDF document
        document.Save(dataDir + "AttachZUGFeRD_out.pdf");
    }
}
```

转换方法接受一个流、一个 PDF 格式和一个转换错误操作作为参数。流参数可用于保存转换日志。转换错误操作参数指定在转换过程中发生任何错误时该怎么办。在这种情况下，它被设置为 "Delete"，这意味着任何不符合 PDF/A-3B 格式的元素将从文档中删除。