---
title: 在 PDF 中旋转文本使用 Python
linktitle: 在 PDF 中旋转文本
type: docs
weight: 50
url: /zh/python-net/rotate-text-inside-pdf/
description: 学习不同的方法在 PDF 中旋转文本。Aspose.PDF 允许您旋转文本到任何角度，旋转文本片段或整个段落。
lastmod: "2024-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "在 PDF 中旋转文本使用 Python",
    "alternativeHeadline": "如何旋转 PDF 文件中的文本",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf 文档生成",
    "keywords": "pdf, python, 文档生成",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF 文档团队",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
    "url": "/python-net/rotate-text-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/rotate-text-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "学习不同的方法在 PDF 中旋转文本。Aspose.PDF 允许您旋转文本到任何角度，旋转文本片段或整个段落。"
}
</script>


## 使用旋转属性在PDF中旋转文本

通过使用[TextFragment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment)类的旋转属性，您可以在不同的角度旋转文本。在文档生成的不同场景中可以使用文本旋转。您可以指定旋转角度以根据您的需求旋转文本。请查看以下不同的场景，您可以在其中实现文本旋转。

## 使用TextFragment和TextBuilder实现旋转

```csharp
// 有关完整的示例和数据文件，请访问https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 初始化文档对象
Document pdfDocument = new Document();
// 获取特定页面
Page pdfPage = (Page)pdfDocument.Pages.Add();
// 创建文本片段
TextFragment textFragment1 = new TextFragment("main text");
textFragment1.Position = new Position(100, 600);
// 设置文本属性
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 创建旋转的文本片段
TextFragment textFragment2 = new TextFragment("rotated text");
textFragment2.Position = new Position(200, 600);
// 设置文本属性
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment2.TextState.Rotation = 45;
// 创建旋转的文本片段
TextFragment textFragment3 = new TextFragment("rotated text");
textFragment3.Position = new Position(300, 600);
// 设置文本属性
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment3.TextState.Rotation = 90;
// 创建TextBuilder对象
TextBuilder textBuilder = new TextBuilder(pdfPage);
// 将文本片段附加到PDF页面
textBuilder.AppendText(textFragment1);
textBuilder.AppendText(textFragment2);
textBuilder.AppendText(textFragment3);
// 保存文档
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated1_out.pdf");
```


## 使用 TextParagraph 和 TextBuilder 实现旋转（旋转的片段）

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 初始化文档对象
Document pdfDocument = new Document();
// 获取特定页面
Page pdfPage = (Page)pdfDocument.Pages.Add();
TextParagraph paragraph = new TextParagraph();
paragraph.Position = new Position(200, 600);
// 创建文本片段
TextFragment textFragment1 = new TextFragment("rotated text");
// 设置文本属性
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 设置旋转
textFragment1.TextState.Rotation = 45;
// 创建文本片段
TextFragment textFragment2 = new TextFragment("main text");
// 设置文本属性
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 创建文本片段
TextFragment textFragment3 = new TextFragment("another rotated text");
// 设置文本属性
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 设置旋转
textFragment3.TextState.Rotation = -45;
// 将文本片段添加到段落中
paragraph.AppendLine(textFragment1);
paragraph.AppendLine(textFragment2);
paragraph.AppendLine(textFragment3);
// 创建 TextBuilder 对象
TextBuilder textBuilder = new TextBuilder(pdfPage);
// 将文本段落添加到 PDF 页面
textBuilder.AppendParagraph(paragraph);
// 保存文档
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated2_out.pdf");
```


## 实现使用 TextFragment 和 Page.Paragraphs 的旋转

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 初始化文档对象
Document pdfDocument = new Document();
// 获取特定页面
Page pdfPage = (Page)pdfDocument.Pages.Add();
// 创建文本片段
TextFragment textFragment1 = new TextFragment("main text");
// 设置文本属性
textFragment1.TextState.FontSize = 12;
textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 创建文本片段
TextFragment textFragment2 = new TextFragment("rotated text");
// 设置文本属性
textFragment2.TextState.FontSize = 12;
textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 设置旋转
textFragment2.TextState.Rotation = 315;
// 创建文本片段
TextFragment textFragment3 = new TextFragment("rotated text");
// 设置文本属性
textFragment3.TextState.FontSize = 12;
textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
// 设置旋转
textFragment3.TextState.Rotation = 270;
pdfPage.Paragraphs.Add(textFragment1);
pdfPage.Paragraphs.Add(textFragment2);
pdfPage.Paragraphs.Add(textFragment3);
// 保存文档
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated3_out.pdf");
```


## 使用 TextParagraph 和 TextBuilder 实现旋转（整段旋转）

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 初始化文档对象
Document pdfDocument = new Document();
// 获取特定页面
Page pdfPage = (Page)pdfDocument.Pages.Add();
for (int i = 0; i < 4; i++)
{
    TextParagraph paragraph = new TextParagraph();
    paragraph.Position = new Position(200, 600);
    // 指定旋转
    paragraph.Rotation = i * 90 + 45;
    // 创建文本片段
    TextFragment textFragment1 = new TextFragment("段落文本");
    // 创建文本片段
    textFragment1.TextState.FontSize = 12;
    textFragment1.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment1.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment1.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // 创建文本片段
    TextFragment textFragment2 = new TextFragment("第二行文本");
    // 设置文本属性
    textFragment2.TextState.FontSize = 12;
    textFragment2.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment2.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment2.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    // 创建文本片段
    TextFragment textFragment3 = new TextFragment("还有更多文本...");
    // 设置文本属性
    textFragment3.TextState.FontSize = 12;
    textFragment3.TextState.Font = FontRepository.FindFont("TimesNewRoman");
    textFragment3.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
    textFragment3.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    textFragment3.TextState.Underline = true;
    paragraph.AppendLine(textFragment1);
    paragraph.AppendLine(textFragment2);
    paragraph.AppendLine(textFragment3);
    // 创建 TextBuilder 对象
    TextBuilder textBuilder = new TextBuilder(pdfPage);
    // 将文本片段附加到 PDF 页面
    textBuilder.AppendParagraph(paragraph);
}
// 保存文档
pdfDocument.Save(dataDir + "TextFragmentTests_Rotated4_out.pdf");
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
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
                "contactType": "销售",
                "areaServed": "美国",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "销售",
                "areaServed": "英国",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "销售",
                "areaServed": "澳大利亚",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "用于 .NET 的 PDF 操作库",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>