---
title: 从PDF页面中搜索并获取文本
linktitle: 搜索并获取文本
type: docs
weight: 60
url: /python-net/search-and-get-text-from-pdf/
description: 本文解释了如何使用各种工具从Aspose.PDF for .NET中搜索和获取文本。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "从PDF页面中搜索并获取文本",
    "alternativeHeadline": "从PDF页面中搜索和获取文本的工具",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf document generation",
    "keywords": "pdf, python, search text, get text from pdf",
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
    "url": "/python-net/search-and-get-text-from-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/search-and-get-text-from-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "本文解释了如何使用各种工具从Aspose.PDF for .NET中搜索和获取文本。"
}
</script>


## 从 PDF 文档的所有页面搜索并获取文本

[TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) 类允许您从 PDF 文档的所有页面中查找与特定短语匹配的文本。为了从整个文档中搜索文本，您需要调用 Pages 集合的 Accept 方法。 [Accept](https://reference.aspose.com/pdf/python-net/aspose.pdf.page/accept/methods/3) 方法接受 TextFragmentAbsorber 对象作为参数，该对象返回 TextFragment 对象的集合。您可以遍历所有的片段并获取它们的属性，如文本、位置（XIndent、YIndent）、字体名称、字体大小、是否可访问、是否嵌入、是否子集、前景色等。

以下代码片段向您展示如何从所有页面搜索文本。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("text");

// 接受所有页面的吸收器
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 获取提取的文本片段
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 遍历片段
foreach (TextFragment textFragment in textFragmentCollection)
{

    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```


如果您需要在特定 PDF 页面内搜索文本，请从 Document 实例的页面集合中指定页面编号，并对该页面调用 Accept 方法（如下面的代码行所示）。

```csharp
// 如需完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 对特定页面应用吸收器
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## 从 PDF 文档的所有页面搜索并获取文本片段

为了从所有页面搜索文本片段，您首先需要从文档中获取 TextFragment 对象。
 TextFragmentAbsorber 允许您从 PDF 文档的所有页面中查找匹配特定短语的文本。为了从整个文档中搜索文本，您需要调用 Pages 集合的 Accept 方法。Accept 方法将 TextFragmentAbsorber 对象作为参数，该对象返回一个 TextFragment 对象的集合。一旦从文档中获取了 TextFragmentCollection，您需要遍历这个集合并获取每个 TextFragment 对象的 TextSegmentCollection。之后，您可以获取每个 TextSegment 对象的所有属性。以下代码片段向您展示了如何从所有页面中搜索文本片段。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "SearchAndGetTextPage.pdf");

// 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("Figure");
// 对所有页面接受吸收器
pdfDocument.Pages.Accept(textFragmentAbsorber);
// 获取提取的文本片段
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// 遍历片段
foreach (TextFragment textFragment in textFragmentCollection)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        Console.WriteLine("Text : {0} ", textSegment.Text);
        Console.WriteLine("Position : {0} ", textSegment.Position);
        Console.WriteLine("XIndent : {0} ", textSegment.Position.XIndent);
        Console.WriteLine("YIndent : {0} ", textSegment.Position.YIndent);
        Console.WriteLine("Font - Name : {0}", textSegment.TextState.Font.FontName);
        Console.WriteLine("Font - IsAccessible : {0} ", textSegment.TextState.Font.IsAccessible);
        Console.WriteLine("Font - IsEmbedded : {0} ", textSegment.TextState.Font.IsEmbedded);
        Console.WriteLine("Font - IsSubset : {0} ", textSegment.TextState.Font.IsSubset);
        Console.WriteLine("Font Size : {0} ", textSegment.TextState.FontSize);
        Console.WriteLine("Foreground Color : {0} ", textSegment.TextState.ForegroundColor);
    }
}
```

为了从 PDF 的特定页面搜索和获取 TextSegments，您需要在调用 Accept(..) 方法时指定特定的页面索引。请查看以下代码行。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 接受所有页面的吸收器
pdfDocument.Pages[2].Accept(textFragmentAbsorber);
```

## 使用正则表达式搜索并从所有页面获取文本

TextFragmentAbsorber 帮助您基于正则表达式搜索和检索所有页面的文本。
 首先，你需要将正则表达式作为短语传递给 TextFragmentAbsorber 构造函数。之后，你需要设置 TextFragmentAbsorber 对象的 TextSearchOptions 属性。该属性需要 TextSearchOptions 对象，并且在创建新对象时需要将 true 作为参数传递给其构造函数。由于你想从所有页面中检索匹配的文本，因此需要调用 Pages 集合的 Accept 方法。TextFragmentAbsorber 返回一个 TextFragmentCollection，其中包含所有符合正则表达式指定的条件的片段。以下代码片段展示了如何基于正则表达式搜索并获取所有页面的文本。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionAll.pdf");

// 创建 TextAbsorber 对象以查找所有与正则表达式匹配的短语
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 如 1999-2000

// 设置文本搜索选项以指定正则表达式使用
TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 接受所有页面的吸收器
pdfDocument.Pages.Accept(textFragmentAbsorber);

// 获取提取的文本片段
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 遍历片段
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine("Text : {0} ", textFragment.Text);
    Console.WriteLine("Position : {0} ", textFragment.Position);
    Console.WriteLine("XIndent : {0} ", textFragment.Position.XIndent);
    Console.WriteLine("YIndent : {0} ", textFragment.Position.YIndent);
    Console.WriteLine("Font - Name : {0}", textFragment.TextState.Font.FontName);
    Console.WriteLine("Font - IsAccessible : {0} ", textFragment.TextState.Font.IsAccessible);
    Console.WriteLine("Font - IsEmbedded : {0} ", textFragment.TextState.Font.IsEmbedded);
    Console.WriteLine("Font - IsSubset : {0} ", textFragment.TextState.Font.IsSubset);
    Console.WriteLine("Font Size : {0} ", textFragment.TextState.FontSize);
    Console.WriteLine("Foreground Color : {0} ", textFragment.TextState.ForegroundColor);
}
```

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
TextFragmentAbsorber textFragmentAbsorber;
// 为了精确匹配一个单词，您可以考虑使用正则表达式。
textFragmentAbsorber = new TextFragmentAbsorber(@"\bWord\b", new TextSearchOptions(true));

// 为了在大写或小写中搜索字符串，您可以考虑使用正则表达式。
textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));

// 为了在 PDF 文档中搜索所有字符串（解析所有字符串），请尝试使用以下正则表达式。
textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");

// 查找搜索字符串的匹配项，并获取字符串之后直到换行符的任何内容。
textFragmentAbsorber = new TextFragmentAbsorber(@"(?i)the ((.)*)");

// 请使用以下正则表达式查找正则表达式匹配后的文本。
textFragmentAbsorber = new TextFragmentAbsorber(@"(?<=word).*");

// 为了在 PDF 文档中搜索超链接/URL，请尝试使用以下正则表达式。
textFragmentAbsorber = new TextFragmentAbsorber(@"(http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?");
```


## 基于正则表达式搜索文本并添加超链接

如果您想根据正则表达式在文本短语上添加超链接，首先使用 TextFragmentAbsorber 找到与该特定正则表达式匹配的所有短语，并在这些短语上添加超链接。

要找到短语并在其上添加超链接：

1. 将正则表达式作为参数传递给 TextFragmentAbsorber 构造函数。
2. 创建一个 TextSearchOptions 对象，以指定是否使用正则表达式。
3. 将匹配的短语获取到 TextFragments 中。
4. 循环遍历匹配项以获取其矩形尺寸，将前景色更改为蓝色（可选 - 使其看起来像超链接，并使用 PdfContentEditor 类的 CreateWebLink(..) 方法创建链接）。
5. 使用 Document 对象的 Save 方法保存更新的 PDF。
以下代码片段展示了如何使用正则表达式搜索 PDF 文件中的文本并在匹配项上添加超链接。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();
// 创建吸收器对象以查找输入搜索短语的所有实例
TextFragmentAbsorber absorber = new TextFragmentAbsorber("\\d{4}-\\d{4}");
// 启用正则表达式搜索
absorber.TextSearchOptions = new TextSearchOptions(true);
// 打开文档
PdfContentEditor editor = new PdfContentEditor();
// 绑定源 PDF 文件
editor.BindPdf(dataDir + "SearchRegularExpressionPage.pdf");
// 接受页面的吸收器
editor.Document.Pages[1].Accept(absorber);

int[] dashArray = { };
String[] LEArray = { };
System.Drawing.Color blue = System.Drawing.Color.Blue;

// 循环遍历片段
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Blue;
    System.Drawing.Rectangle rect = new System.Drawing.Rectangle((int)textFragment.Rectangle.LLX,
        (int)Math.Round(textFragment.Rectangle.LLY), (int)Math.Round(textFragment.Rectangle.Width + 2),
        (int)Math.Round(textFragment.Rectangle.Height + 1));
    Enum[] actionName = new Enum[2] { Aspose.Pdf.Annotations.PredefinedAction.Document_AttachFile, Aspose.Pdf.Annotations.PredefinedAction.Document_ExtractPages };
    editor.CreateWebLink(rect, "http:// Www.aspose.com", 1, blue, actionName);
    editor.CreateLine(rect, "", (float)textFragment.Rectangle.LLX + 1, (float)textFragment.Rectangle.LLY - 1,
        (float)textFragment.Rectangle.URX, (float)textFragment.Rectangle.LLY - 1, 1, 1, blue, "S", dashArray, LEArray);
}

dataDir = dataDir + "SearchTextAndAddHyperlink_out.pdf";
editor.Save(dataDir);
editor.Close();
```


## 搜索并在每个文本片段周围绘制矩形

Aspose.PDF for .NET 支持搜索并获取每个字符或文本片段的坐标的功能。因此，为了确保返回每个字符的坐标，我们可以考虑在每个字符周围突出显示（添加矩形）。

对于文本段落，您可以考虑使用正则表达式来确定段落分隔符并在其周围绘制矩形。请查看以下代码片段。以下代码片段获取每个字符的坐标并在每个字符周围创建一个矩形。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document document = new Document(dataDir + "SearchAndGetTextFromAll.pdf");

// 创建 TextAbsorber 对象以查找所有匹配正则表达式的短语

TextFragmentAbsorber textAbsorber = new TextFragmentAbsorber(@"[\S]+");

TextSearchOptions textSearchOptions = new TextSearchOptions(true);

textAbsorber.TextSearchOptions = textSearchOptions;

document.Pages.Accept(textAbsorber);

var editor = new PdfContentEditor(document);

foreach (TextFragment textFragment in textAbsorber.TextFragments)
{
    foreach (TextSegment textSegment in textFragment.Segments)
    {
        DrawBox(editor, textFragment.Page.Number, textSegment, System.Drawing.Color.Red);
    }

}
dataDir = dataDir + "SearchTextAndDrawRectangle_out.pdf";
document.Save(dataDir);
```


## 在 PDF 文档中突出显示每个字符

{{% alert color="primary" %}}

您可以尝试使用 Aspose.PDF 在文档中搜索文本，并在此[链接](https://products.aspose.app/pdf/search)在线获取结果

{{% /alert %}}

Aspose.PDF for .NET 支持搜索并获取每个字符或文本片段坐标的功能。因此，为了确保返回每个字符的坐标，我们可以考虑在每个字符周围添加矩形进行突出显示。以下代码片段获取每个字符的坐标并在每个字符周围创建一个矩形。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

int resolution = 150;

Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(dataDir + "input.pdf");

using (MemoryStream ms = new MemoryStream())
{
    PdfConverter conv = new PdfConverter(pdfDocument);
    conv.Resolution = new Resolution(resolution, resolution);
    conv.GetNextImage(ms, System.Drawing.Imaging.ImageFormat.Png);

    Bitmap bmp = (Bitmap)Bitmap.FromStream(ms);

    using (System.Drawing.Graphics gr = System.Drawing.Graphics.FromImage(bmp))
    {
        float scale = resolution / 72f;
        gr.Transform = new System.Drawing.Drawing2D.Matrix(scale, 0, 0, -scale, 0, bmp.Height);

        for (int i = 0; i < pdfDocument.Pages.Count; i++)
        {
Page page = pdfDocument.Pages[1];
// 创建 TextAbsorber 对象以查找所有单词
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(@"[\S]+");
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;
page.Accept(textFragmentAbsorber);
// 获取提取的文本片段
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;
// 遍历片段
foreach (TextFragment textFragment in textFragmentCollection)
{
    if (i == 0)
    {
        gr.DrawRectangle(
        Pens.Yellow,
        (float)textFragment.Position.XIndent,
        (float)textFragment.Position.YIndent,
        (float)textFragment.Rectangle.Width,
        (float)textFragment.Rectangle.Height);

        for (int segNum = 1; segNum <= textFragment.Segments.Count; segNum++)
        {
TextSegment segment = textFragment.Segments[segNum];

for (int charNum = 1; charNum <= segment.Characters.Count; charNum++)
{
    CharInfo characterInfo = segment.Characters[charNum];

    Aspose.Pdf.Rectangle rect = page.GetPageRect(true);
    Console.WriteLine("TextFragment = " + textFragment.Text + "    Page URY = " + rect.URY +
          "   TextFragment URY = " + textFragment.Rectangle.URY);

    gr.DrawRectangle(
    Pens.Black,
    (float)characterInfo.Rectangle.LLX,
    (float)characterInfo.Rectangle.LLY,
    (float)characterInfo.Rectangle.Width,
    (float)characterInfo.Rectangle.Height);
}

gr.DrawRectangle(
Pens.Green,
(float)segment.Rectangle.LLX,
(float)segment.Rectangle.LLY,
(float)segment.Rectangle.Width,
(float)segment.Rectangle.Height);
        }
    }
}
        }
    }
    dataDir = dataDir + "HighlightCharacterInPDF_out.png";
    bmp.Save(dataDir, System.Drawing.Imaging.ImageFormat.Png);
}
```


## 添加和搜索隐藏文本

有时候，我们想在 PDF 文档中添加隐藏文本，然后搜索隐藏文本并使用其位置进行后处理。为了方便您，Aspose.PDF for .NET 提供了这些功能。您可以在文档生成期间添加隐藏文本。此外，您可以使用 TextFragmentAbsorber 查找隐藏文本。要添加隐藏文本，请为添加的文本设置 TextState.Invisible 为“true”。TextFragmentAbsorber 会找到所有匹配模式的文本（如果指定）。这是无法更改的默认行为。为了验证找到的文本是否实际上是不可见的，可以使用 TextState.Invisible 属性。下面的代码片段展示了如何使用此功能。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

//创建包含隐藏文本的文档
Aspose.Pdf.Document doc = new Aspose.Pdf.Document();
Page page = doc.Pages.Add();
TextFragment frag1 = new TextFragment("This is common text.");
TextFragment frag2 = new TextFragment("This is invisible text.");

//设置文本属性 - 不可见
frag2.TextState.Invisible = true;

page.Paragraphs.Add(frag1);
page.Paragraphs.Add(frag2);
doc.Save(dataDir + "39400_out.pdf");
doc.Dispose();

//搜索文档中的文本
doc = new Aspose.Pdf.Document(dataDir + "39400_out.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber();
absorber.Visit(doc.Pages[1]);

foreach (TextFragment fragment in absorber.TextFragments)
{
    //对片段进行处理
    Console.WriteLine("Text '{0}' on pos {1} invisibility: {2} ",
    fragment.Text, fragment.Position.ToString(), fragment.TextState.Invisible);
}
doc.Dispose();
```


## 使用 .NET Regex 搜索文本

Aspose.PDF for .NET 提供了使用标准 .NET Regex 选项搜索文档的功能。可以使用 TextFragmentAbsorber 来实现这一目的，如下面的代码示例所示。

```csharp
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 创建 Regex 对象以查找所有单词
System.Text.RegularExpressions.Regex regex = new System.Text.RegularExpressions.Regex(@"[\S]+");

// 打开文档
Aspose.Pdf.Document document = new Aspose.Pdf.Document(dataDir + "SearchTextRegex.pdf");

// 获取特定页面
Page page = document.Pages[1];

// 创建 TextAbsorber 对象以查找输入正则表达式的所有实例
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber(regex);
textFragmentAbsorber.TextSearchOptions.IsRegularExpressionUsed = true;

// 接受页面的吸收器
page.Accept(textFragmentAbsorber);

// 获取提取的文本片段
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 遍历文本片段
foreach (TextFragment textFragment in textFragmentCollection)
{
    Console.WriteLine(textFragment.Text);
}
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
    "applicationCategory": "PDF 操作库 for .NET",
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