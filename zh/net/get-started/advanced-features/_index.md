---
title: 高级功能
type: docs
ai_search_scope: pdf_net
ai_search_endpoint: https://docsearch.api.aspose.cloud/ask
weight: 140
url: /zh/net/advanced-features/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "Advanced Features",
    "alternativeHeadline": "Streamlined PDF Handling and Mathematical Expression Support in C#",
    "abstract": "发现 Aspose.PDF for .NET 中的最新增强功能，允许无缝将 PDF 文档发送到网页浏览器以直接下载，而无需物理存储。此功能不仅简化了文件传递，还包括提取嵌入文件和使用 LaTeX 结合复杂数学表达式的高级能力，使其成为处理 PDF 格式的开发人员的必备工具。",
    "author": {
        "@type": "Person",
        "name": "Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url": "https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "wordcount": "386",
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
    "url": "/net/advanced-features/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/net/advanced-features/"
    },
    "dateModified": "2024-11-25",
    "description": "Aspose.PDF 不仅可以执行简单和容易的任务，还可以应对更复杂的目标。请查看下一部分以获取高级用户和开发人员的信息。"
}
</script>

## 将 PDF 发送到浏览器以供下载

有时，当您开发 ASP.NET 应用程序时，您需要将 PDF 文件发送到网页浏览器以供下载，而无需将其物理保存。为了实现这一点，您可以在生成 PDF 文档后将其保存到 MemoryStream 对象中，并将该 MemoryStream 的字节传递给 Response 对象。这样做将使浏览器下载生成的 PDF 文档。

以下代码片段演示了上述功能：
```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private void Page_Load(object sender, EventArgs e)
{
    // Clear the response before writing to it
    Response.Clear();
    // Set content type for PDF
    Response.ContentType = "application/pdf";
    // Set the response header for file download
    Response.AddHeader("content-disposition", "attachment; filename=TestDocument.pdf");

    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add Page in Pages Collection
        var page = document.Pages.Add();
        var textFragment = new Aspose.Pdf.Text.TextFragment("Hello World");
        page.Paragraphs.Add(textFragment);
        
        // Save PDF document to a MemoryStream
        using (var ms = new MemoryStream())
        {
            document.Save(ms);
             // Reset the stream position to the beginning
            ms.Position = 0;

            // Write the MemoryStream to the response
            ms.CopyTo(Response.OutputStream);
            Response.AddHeader("content-length", ms.Length.ToString());
            Response.Flush();
            // Suppress the remaining content
            Response.SuppressContent = true; 
        }
    }
    // End the response to prevent further processing
    Response.End(); 
}
```

## 使用 LaTeX 脚本添加数学表达式

使用 Aspose.PDF，您可以使用 LaTeX 脚本在 PDF 文档中添加数学表达式/公式。以下示例展示了如何以两种不同的方式使用此功能，以便在表格单元格中添加数学公式：

### 无前言和文档环境

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET      
private static void LatexWithoutPreambleAndDocEnvironment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        // Create a Table
        var table = new Aspose.Pdf.Table();
        // Add a row into Table
        var row = table.Rows.Add();
        // Add Cell with Latex Script to add methematical expressions/formulae
        var latexText1 = "$123456789+\\sqrt{1}+\\int_a^b f(x)dx$";
        var cell = row.Cells.Add();
        cell.Margin = new MarginInfo { Left = 20, Right = 20, Top = 20, Bottom = 20 };
        // Second TeXFragment constructor bool parameter provides LaTeX paragraph indents elimination
        var ltext1 = new Aspose.Pdf.TeXFragment(latexText1, true);
        cell.Paragraphs.Add(ltext1);
        // Add table inside page
        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "LatextScriptInPdf_out.pdf");
    }
}
```

### 有前言和文档环境

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexWithPreambleAndDocEnvironment()
{
    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    // Open PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = doc.Pages.Add();
        // Create a Table
        var table = new Aspose.Pdf.Table();
        // Add a row into Table
        var row = table.Rows.Add();
       // Add Cell with Latex Script to add methematical expressions/formulae
        var latexText2 = @"\documentclass{article}
                            \begin{document}
                            Latex and the document class will normally take care of page layout issues for you. For submission to an academic publication, this entire topic will be out
                            \end{document}";
        var cell = row.Cells.Add();
        cell.Margin = new Aspose.Pdf.MarginInfo { Left = 20, Right = 20, Top = 20, Bottom = 20 };
        var text2 = new Aspose.Pdf.HtmlFragment(latexText2);
        cell.Paragraphs.Add(text2);
        // Add table inside page
        page.Paragraphs.Add(table);
        // Save PDF document
        document.Save(dataDir + "LatextScriptInPdf2_out.pdf");
    }
}
```

### 对 LaTeX 标签的支持

对齐环境在 amsmath 包中定义，证明环境在 amsthm 包中定义。因此，您必须在文档前言中使用 \usepackage 命令指定这些包。这意味着您必须将 LaTeX 文本封装在文档环境中，如以下代码示例所示。

```csharp
// For complete examples and data files, visit https://github.com/aspose-pdf/Aspose.PDF-for-.NET
private static void LatexTagsSupport()
{
    var s = @"
    \usepackage{amsmath,amsthm}
    \begin{document}
    \begin{proof} The proof is a follows: 
    \begin{align}
    (x+y)^3&=(x+y)(x+y)^2
    (x+y)(x^2+2xy+y^2)\\
    &=x^3+3x^2y+3xy^3+x^3.\qedhere
    \end{align}
    \end{proof}
    \end{document}";

    // The path to the documents directory
    var dataDir = RunExamples.GetDataDir_AsposePdf_Text();
    
    // Create PDF document
    using (var document = new Aspose.Pdf.Document())
    {
        // Add page
        var page = document.Pages.Add();
        var latex = new Aspose.Pdf.TeXFragment(s);
        page.Paragraphs.Add(latex);
        // Save PDF document
        document.Save(dataDir + "Script_out.pdf");
    }
}
```