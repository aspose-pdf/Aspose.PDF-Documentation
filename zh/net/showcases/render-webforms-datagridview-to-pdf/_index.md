---
title: 将 WebForms DataGridView 渲染为 PDF
linktitle: 将 WebForms DataGridView 渲染为 PDF
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 20
url: /zh/net/render-webforms-datagridview-to-pdf/
description: 本示例展示了如何使用 Aspose.PDF 库将 WebForm 渲染为 PDF。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Render WebForms DataGridView to PDF",
    "alternativeHeadline": "Effortlessly Convert WebForms DataGridView to PDF",
    "abstract": "该功能允许使用 Aspose.PDF for .NET 库无缝地将 WebForms DataGridView 转换为 PDF。此功能通过集成专用的 GridView 导出控件简化了数据导出的过程，确保直接从 Web 应用程序高质量地渲染 PDF。非常适合寻求高效文档生成解决方案的开发人员。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "165",
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
    "url": "/net/render-webforms-datagridview-to-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/render-webforms-datagridview-to-pdf/"
    },
    "dateModified": "2025-04-11",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 如何使用 Aspose.PDF/Aspose.HTML 将 WebForm 导出为 PDF

### 介绍

通常，将 WebForm 转换为 PDF 文档需要额外的工具。本示例展示了如何使用 Aspose.PDF 库将 WebForm 渲染为 PDF。此示例中还包含 Aspose 导出 GridView 到 PDF 控件，以展示如何将 _GridView 控件渲染为 PDF 文档_。

## 如何将 WebForm 渲染为 PDF

将 WebForm 渲染为 PDF 的原始想法是创建一个帮助类，该类继承自 [System.Web.UI.Page](https://msdn.microsoft.com/en-US/library/System.Web.UI.Page.aspx)，并重写 Render 方法。</em></p>

```csharp
void Render(HtmlTextWriter writer)
{
    if (RenderToPDF)
    {
        // render web page for PDF document
    }
    else
    {
        // render web page in browser
        base.Render(writer);
    }
}
```

有两个 Aspose 工具可以用于将 HTML 渲染为 PDF：

- Aspose.PDF for .NET。
- Aspose 导出 GridView 控件（基于 Aspose.PDF）。

## 源文件

您可以在 [这里](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.Pdf.GridViewExport) 找到整个项目的代码。

- _Default.aspx_ 演示了如何使用 Aspose.PDF 导出为 PDF。
- _Report2.aspx_ 演示了如何使用 Aspose 导出 GridView 控件（基于 Aspose.PDF）导出为 PDF。

## 附加文件

`Helpers\PdfPage.cs` - 包含一个帮助类，展示了如何使用 Aspose.PDF API。</em>

Aspose.Pdf.GridViewExport 项目包含扩展的 GridView 控件，用于在 `Report2.aspx` 中演示。