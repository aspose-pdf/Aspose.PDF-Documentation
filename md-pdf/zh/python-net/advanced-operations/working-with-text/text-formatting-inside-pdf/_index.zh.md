---
title: 使用 Python 在 PDF 中格式化文本
linktitle: 在 PDF 中格式化文本
type: docs
weight: 30
url: /python-net/text-formatting-inside-pdf/
description: 本页面解释了如何在 PDF 文件中格式化文本。包括添加行缩进、添加文本边框、添加下划线文本等。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "使用 Python 在 PDF 中格式化文本",
    "alternativeHeadline": "如何在 PDF 文件中格式化文本",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, format text in pdf",
    "wordcount": "302",
    "proficiencyLevel":"Beginner",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF Doc Team",
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
    "url": "/python-net/text-formatting-inside-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/text-formatting-inside-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "本页面解释了如何在 PDF 文件中格式化文本。包括添加行缩进、添加文本边框、添加下划线文本等。"
}
</script>


## 如何向 PDF 添加行缩进

Aspose.PDF for .NET 提供的 [TextFormattingOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textformattingoptions) 类中的 SubsequentLinesIndent 属性。可以在使用 TextFragment 和 Paragraphs 集合的 PDF 生成场景中指定行缩进。

请使用以下代码片段来使用该属性：

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 创建新的文档对象
Aspose.Pdf.Document document = new Aspose.Pdf.Document();
Aspose.Pdf.Page page = document.Pages.Add();

string textFragment = string.Concat(Enumerable.Repeat("A quick brown fox jumped over the lazy dog. ", 10));

Aspose.Pdf.Text.TextFragment text = new Aspose.Pdf.Text.TextFragment(textFragment);

// 初始化文本片段的 TextFormattingOptions 并指定 SubsequentLinesIndent 值
text.TextState.FormattingOptions = new Aspose.Pdf.Text.TextFormattingOptions()
{
    SubsequentLinesIndent = 20
};

page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line2");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line3");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line4");
page.Paragraphs.Add(text);

text = new Aspose.Pdf.Text.TextFragment("Line5");
page.Paragraphs.Add(text);

document.Save(dataDir + "SubsequentIndent_out.pdf");
```


## 如何添加文本边框

以下代码片段演示了如何使用 TextBuilder 并设置 TextState 的 DrawTextRectangleBorder 属性来为文本添加边框：

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 创建新的文档对象
Document pdfDocument = new Document();
// 获取特定页面
Page pdfPage = (Page)pdfDocument.Pages.Add();
// 创建文本片段
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);
// 设置文本属性
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// 设置 StrokingColor 属性以在文本矩形周围绘制边框（描边）
textFragment.TextState.StrokingColor = Aspose.Pdf.Color.DarkRed;
// 将 DrawTextRectangleBorder 属性值设置为 true
textFragment.TextState.DrawTextRectangleBorder = true;
TextBuilder tb = new TextBuilder(pdfPage);
tb.AppendText(textFragment);
// 保存文档
pdfDocument.Save(dataDir + "PDFWithTextBorder_out.pdf");
```


## 如何添加下划线文本

以下代码片段展示了如何在创建新的 PDF 文件时添加下划线文本。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 创建文档对象
Document pdfDocument = new Document();
// 向 PDF 文档添加页面
pdfDocument.Pages.Add();
// 为第一页创建 TextBuilder
TextBuilder tb = new TextBuilder(pdfDocument.Pages[1]);
// 带有示例文本的 TextFragment
TextFragment fragment = new TextFragment("Test message");
// 为 TextFragment 设置字体
fragment.TextState.Font = FontRepository.FindFont("Arial");
fragment.TextState.FontSize = 10;
// 将文本格式设置为下划线
fragment.TextState.Underline = true;
// 指定 TextFragment 需要放置的位置
fragment.Position = new Position(10, 800);
// 将 TextFragment 附加到 PDF 文件
tb.AppendText(fragment);

dataDir = dataDir + "AddUnderlineText_out.pdf";

// 保存生成的 PDF 文档。
pdfDocument.Save(dataDir);
```


## 如何在添加的文本周围添加边框

您可以控制添加文本的外观。下面的示例显示了如何通过在添加的文本周围绘制一个矩形来添加边框。了解有关 [PdfContentEditor](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor) 类的更多信息。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

PdfContentEditor editor = new PdfContentEditor();
editor.BindPdf(dataDir + "input.pdf");
LineInfo lineInfo = new LineInfo();
lineInfo.LineWidth = 2;
lineInfo.VerticeCoordinate = new float[] { 0, 0, 100, 100, 50, 100 };
lineInfo.Visibility = true;
editor.CreatePolygon(lineInfo, 1, new System.Drawing.Rectangle(0, 0, 0, 0), "");

dataDir = dataDir + "AddingBorderAroundAddedText_out.pdf";

// 保存生成的 PDF 文档。
editor.Save(dataDir);
```

## 如何添加换行符

TextFragment不支持文本中的换行符。然而，为了添加带有换行符的文本，请使用带有TextParagraph的TextFragment：

- 在TextFragment中使用"\r\n"或Environment.NewLine代替单个"\n";
- 创建TextParagraph对象。它将添加分行的文本;
- 使用TextParagraph.AppendLine添加TextFragment;
- 使用TextBuilder.AppendParagraph添加TextParagraph。
请使用下面的代码片段。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 使用包含所需换行符的文本初始化新的TextFragment
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 如果需要，设置文本片段属性
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// 创建TextParagraph对象
TextParagraph par = new TextParagraph();

// 向段落添加新的TextFragment
par.AppendLine(textFragment);

// 设置段落位置
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// 创建TextBuilder对象
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// 使用TextBuilder添加TextParagraph
textBuilder.AppendParagraph(par);

dataDir = dataDir + "AddNewLineFeed_out.pdf";

// 保存生成的PDF文档。
pdfApplicationDoc.Save(dataDir);
```


## 如何添加删除线文本

TextState 类提供了设置 PDF 文档中 TextFragments 格式的功能。您可以使用此类将文本格式设置为粗体、斜体、下划线，并且从此版本开始，API 已提供将文本格式标记为删除线的功能。请尝试使用以下代码片段添加带有删除线格式的 TextFragment。

请使用完整的代码片段：

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 打开文档
Document pdfDocument = new Document();
// 获取特定页面
Page pdfPage = (Page)pdfDocument.Pages.Add();

// 创建文本片段
TextFragment textFragment = new TextFragment("main text");
textFragment.Position = new Position(100, 600);

// 设置文本属性
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;
// 设置删除线属性
textFragment.TextState.StrikeOut = true;
// 将文本标记为粗体
textFragment.TextState.FontStyle = FontStyles.Bold;

// 创建 TextBuilder 对象
TextBuilder textBuilder = new TextBuilder(pdfPage);
// 将文本片段附加到 PDF 页面
textBuilder.AppendText(textFragment);

dataDir = dataDir + "AddStrikeOutText_out.pdf";

// 保存生成的 PDF 文档。
pdfDocument.Save(dataDir);
```


## 应用渐变阴影到文本

在文本编辑场景的 API 中，文本格式化得到了进一步增强，现在您可以在 PDF 文档中添加带有图案颜色空间的文本。Aspose.Pdf.Color 类通过引入新的 PatternColorSpace 属性得到了进一步增强，该属性可用于指定文本的阴影颜色。这个新属性为文本添加了不同的渐变阴影，例如：轴向阴影、径向（类型 3）阴影，如以下代码片段所示：

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

using (Document pdfDocument = new Document(dataDir + "text_sample4.pdf"))
{
    TextFragmentAbsorber absorber = new TextFragmentAbsorber("Lorem ipsum");
    pdfDocument.Pages.Accept(absorber);

    TextFragment textFragment = absorber.TextFragments[1];

    // 创建带有图案颜色空间的新颜色
    textFragment.TextState.ForegroundColor = new Aspose.Pdf.Color()
    {
        PatternColorSpace = new Aspose.Pdf.Drawing.GradientAxialShading(Color.Red, Color.Blue)
    };
    textFragment.TextState.Underline = true;

    pdfDocument.Save(dataDir + "text_out.pdf");
}
```


>要应用径向渐变，可以在上面的代码片段中将“PatternColorSpace”属性设置为‘Aspose.Pdf.Drawing.GradientRadialShading(startingColor, endingColor)’

## 如何将文本对齐到浮动内容

Aspose.PDF 支持为 Floating Box 元素中的内容设置文本对齐。可以使用 Aspose.Pdf.FloatingBox 实例的对齐属性来实现，如以下代码示例所示。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document doc = new Document();
doc.Pages.Add();

Aspose.Pdf.FloatingBox floatBox = new Aspose.Pdf.FloatingBox(100, 100);
floatBox.VerticalAlignment = VerticalAlignment.Bottom;
floatBox.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox.Paragraphs.Add(new TextFragment("FloatingBox_bottom"));
floatBox.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox);

Aspose.Pdf.FloatingBox floatBox1 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox1.VerticalAlignment = VerticalAlignment.Center;
floatBox1.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox1.Paragraphs.Add(new TextFragment("FloatingBox_center"));
floatBox1.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox1);

Aspose.Pdf.FloatingBox floatBox2 = new Aspose.Pdf.FloatingBox(100, 100);
floatBox2.VerticalAlignment = VerticalAlignment.Top;
floatBox2.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Right;
floatBox2.Paragraphs.Add(new TextFragment("FloatingBox_top"));
floatBox2.Border = new Aspose.Pdf.BorderInfo(Aspose.Pdf.BorderSide.All, Aspose.Pdf.Color.Blue);
doc.Pages[1].Paragraphs.Add(floatBox2);

doc.Save(dataDir + "FloatingBox_alignment_review_out.pdf");
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for .NET 库",
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
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "销售",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "销售",
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