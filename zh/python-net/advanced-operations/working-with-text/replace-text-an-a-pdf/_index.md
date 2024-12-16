---
title: 使用Python替换PDF中的文本
linktitle: 替换PDF中的文本
type: docs
weight: 40
url: /zh/python-net/replace-text-in-pdf/
description: 了解通过Aspose.PDF for Python via .NET库替换和删除文本的多种方法。
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "替换PDF中的文本",
    "alternativeHeadline": "在PDF文件中替换和删除文本",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "pdf文档生成",
    "keywords": "pdf, python, 替换文本, 删除文本",
    "wordcount": "302",
    "proficiencyLevel":"初级",
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
    "url": "/python-net/replace-text-in-pdf/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/replace-text-in-pdf/"
    },
    "dateModified": "2024-02-04",
    "description": "了解通过Aspose.PDF for Python via .NET库替换和删除文本的多种方法。"
}
</script>


## 替换PDF文档所有页面中的文本

{{% alert color="primary" %}}

您可以尝试使用 Aspose.PDF 在文档中查找并替换文本，并在此[链接](https://products.aspose.app/pdf/redaction)上在线查看结果

{{% /alert %}}

为了替换PDF文档所有页面中的文本，您首先需要使用 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) 来查找您想要替换的特定短语。之后，您需要遍历所有的 TextFragments 来替换文本并更改任何其他属性。完成这些操作后，您只需使用 Document 对象的 Save 方法保存输出 PDF。以下代码片段向您展示如何替换PDF文档所有页面中的文本。

```python

    import aspose.pdf as ap

    # 打开文档
    document = ap.Document(input_pdf)

    # 创建 TextAbsorber 对象以查找输入搜索短语的所有实例
    absorber = ap.text.TextFragmentAbsorber("format")

    # 接受所有页面的吸收器
    document.pages.accept(absorber)

    # 获取提取的文本片段
    collection = absorber.text_fragments

    # 遍历片段
    for text_fragment in collection:
        # 更新文本和其他属性
        text_fragment.text = "FORMAT"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
        text_fragment.text_state.font_size = 22
        text_fragment.text_state.foreground_color = ap.Color.blue
        text_fragment.text_state.background_color = ap.Color.green

    # 保存文档
    document.save(output_pdf)
```


## 替换特定页面区域的文本

为了替换特定页面区域的文本，首先，我们需要实例化 TextFragmentAbsorber 对象，使用 TextSearchOptions.Rectangle 属性指定页面区域，然后遍历所有的 TextFragments 来替换文本。一旦这些操作完成，我们只需使用 Document 对象的 Save 方法保存输出 PDF。以下代码片段展示了如何替换 PDF 文档所有页面的文本。

```python
// 加载 PDF 文件
Aspose.PDF.Document pdf = new Aspose.PDF.Document("c:/pdftest/programaticallyproducedpdf.pdf");

// 实例化 TextFragment Absorber 对象
Aspose.PDF.Text.TextFragmentAbsorber TextFragmentAbsorberAddress = new Aspose.PDF.Text.TextFragmentAbsorber();

// 在页面边界内搜索文本
TextFragmentAbsorberAddress.TextSearchOptions.LimitToPageBounds = true;

// 为 TextSearch Options 指定页面区域
TextFragmentAbsorberAddress.TextSearchOptions.Rectangle = new Aspose.PDF.Rectangle(100, 100, 200, 200);

// 从 PDF 文件的第一页搜索文本
pdf.Pages[1].Accept(TextFragmentAbsorberAddress);

// 遍历每个 TextFragment
foreach( Aspose.PDF.Text.TextFragment tf in TextFragmentAbsorberAddress.TextFragments)
{
    // 将文本更新为空字符
    tf.Text = "";
}

// 在文本替换后保存更新的 PDF 文件
pdf.Save("c:/pdftest/TextUpdated.pdf");
```


## 根据正则表达式替换文本

如果你想根据正则表达式替换一些短语，你首先需要使用 TextFragmentAbsorber 找到所有匹配该正则表达式的短语。你需要将正则表达式作为参数传递给 TextFragmentAbsorber 构造函数。你还需要创建一个 TextSearchOptions 对象，以指定是否使用正则表达式。一旦在 TextFragments 中获得匹配的短语，你需要遍历它们并根据需要进行更新。最后，你需要使用 Document 对象的 Save 方法保存更新后的 PDF。以下代码片段展示了如何根据正则表达式替换文本。

```python
// 对于完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "SearchRegularExpressionPage.pdf");

// 创建 TextAbsorber 对象以查找所有匹配正则表达式的短语
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // 如 1999-2000

// 设置文本搜索选项以指定正则表达式的使用
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.TextSearchOptions = textSearchOptions;

// 接受单页的吸收器
pdfDocument.Pages[1].Accept(textFragmentAbsorber);

// 获取提取的文本片段
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.TextFragments;

// 遍历片段
foreach (TextFragment textFragment in textFragmentCollection)
{
    // 更新文本和其他属性
    textFragment.Text = "New Phrase";
    // 设置为对象的实例。
    textFragment.TextState.Font = FontRepository.FindFont("Verdana");
    textFragment.TextState.FontSize = 22;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Blue);
    textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.FromRgb(System.Drawing.Color.Green);
}
dataDir = dataDir + "ReplaceTextonRegularExpression_out.pdf";
pdfDocument.Save(dataDir);
```


## 在现有 PDF 文件中替换字体

Aspose.PDF for Python via .NET 支持在 PDF 文档中替换文本的功能。然而，有时您可能只需要替换 PDF 文档中使用的字体。因此，不是替换文本，而是仅替换使用的字体。TextFragmentAbsorber 构造函数的一个重载接受 TextEditOptions 对象作为参数，我们可以使用 TextEditOptions.FontReplace 枚举中的 RemoveUnusedFonts 值来实现我们的要求。以下代码段显示如何替换 PDF 文档中的字体。

```python
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 加载源 PDF 文件
Document pdfDocument = new Document(dataDir + "ReplaceTextPage.pdf");
// 搜索文本片段并将编辑选项设置为删除未使用的字体
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));

// 接受所有页面的吸收器
pdfDocument.Pages.Accept(absorber);
// 遍历所有的 TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    // 如果字体名称是 ArialMT，替换字体名称为 Arial
    if (textFragment.TextState.Font.FontName == "Arial,Bold")
    {
        textFragment.TextState.Font = FontRepository.FindFont("Arial");
    }

}

dataDir = dataDir + "ReplaceFonts_out.pdf";
// 保存更新后的文档
pdfDocument.Save(dataDir);
```


## 文本替换应自动重新排列页面内容

Aspose.PDF for Python via .NET 支持在 PDF 文件内搜索和替换文本的功能。然而，最近一些客户在文本替换过程中遇到了问题，当特定的 TextFragment 被替换为较小的内容时，生成的 PDF 中会显示一些额外的空格，或者在 TextFragment 被替换为较长的字符串时，单词会与现有的页面内容重叠。因此，需要引入一种机制，一旦 PDF 文档中的文本被替换，内容应该重新排列。

为了应对上述情况，Aspose.PDF for Python via .NET 已经得到增强，以便在 PDF 文件内部替换文本时不会出现此类问题。以下代码片段展示了如何在 PDF 文件内替换文本，并且页面内容应自动重新排列。

```python
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 加载源 PDF 文件
Document doc = new Document(dataDir + "ExtractTextPage.pdf");
// 创建带有正则表达式的 TextFragment 吸收器对象
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[TextFragmentAbsorber,companyname,Textbox,50]");
doc.Pages.Accept(textFragmentAbsorber);
// 替换每个 TextFragment
foreach (TextFragment textFragment in textFragmentAbsorber.TextFragments)
{
    // 设置被替换文本片段的字体
    textFragment.TextState.Font = FontRepository.FindFont("Arial");
    // 设置字体大小
    textFragment.TextState.FontSize = 12;
    textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Navy;
    // 用比占位符更长的字符串替换文本
    textFragment.Text = "This is a Larger String for the Testing of this issue";
}
dataDir = dataDir + "RearrangeContentsUsingTextReplacement_out.pdf";
// 保存生成的 PDF
doc.Save(dataDir);
```


## PDF 创建过程中渲染可替换符号

可替换符号是在文本字符串中可以在运行时用相应内容替换的特殊符号。Aspose.PDF 命名空间的新文档对象模型目前支持的可替换符号有 `$P`、`$p`、`\n`、`\r`。 `$p` 和 `$P` 用于在运行时处理页码。`$p` 被替换为当前段落类所在页面的页码。`$P` 被替换为文档中的总页数。当将 `TextFragment` 添加到 PDF 文档的段落集合中时，它不支持文本内的换行。然而，为了添加带有换行的文本，请使用带有 `TextParagraph` 的 `TextFragment`：

- 在 TextFragment 中使用 "\r\n" 或 Environment.NewLine 替代单独的 "\n";
- 创建一个 TextParagraph 对象。它将添加带有分行的文本；
- 使用 TextParagraph.AppendLine 添加 TextFragment；
- 使用 TextBuilder.AppendParagraph 添加 TextParagraph。

```python
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Aspose.Pdf.Document pdfApplicationDoc = new Aspose.Pdf.Document();
Aspose.Pdf.Page applicationFirstPage = (Aspose.Pdf.Page)pdfApplicationDoc.Pages.Add();

// 使用包含所需换行符的文本初始化新的 TextFragment
Aspose.Pdf.Text.TextFragment textFragment = new Aspose.Pdf.Text.TextFragment("Applicant Name: " + Environment.NewLine + " Joe Smoe");

// 如果需要，设置文本片段属性
textFragment.TextState.FontSize = 12;
textFragment.TextState.Font = Aspose.Pdf.Text.FontRepository.FindFont("TimesNewRoman");
textFragment.TextState.BackgroundColor = Aspose.Pdf.Color.LightGray;
textFragment.TextState.ForegroundColor = Aspose.Pdf.Color.Red;

// 创建 TextParagraph 对象
TextParagraph par = new TextParagraph();

// 将新的 TextFragment 添加到段落中
par.AppendLine(textFragment);

// 设置段落位置
par.Position = new Aspose.Pdf.Text.Position(100, 600);

// 创建 TextBuilder 对象
TextBuilder textBuilder = new TextBuilder(applicationFirstPage);
// 使用 TextBuilder 添加 TextParagraph
textBuilder.AppendParagraph(par);

dataDir = dataDir + "RenderingReplaceableSymbols_out.pdf";
pdfApplicationDoc.Save(dataDir);
```


## 页眉/页脚区域中的可替换符号

可替换符号也可以放置在 PDF 文件的页眉/页脚部分。请查看以下代码片段，了解如何在页脚部分添加可替换符号的详细信息。

```python
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

Document doc = new Document();
Page page = doc.Pages.Add();

MarginInfo marginInfo = new MarginInfo();
marginInfo.Top = 90;
marginInfo.Bottom = 50;
marginInfo.Left = 50;
marginInfo.Right = 50;
// 将 marginInfo 实例分配给 sec1.PageInfo 的 Margin 属性
page.PageInfo.Margin = marginInfo;

HeaderFooter hfFirst = new HeaderFooter();
page.Header = hfFirst;
hfFirst.Margin.Left = 50;
hfFirst.Margin.Right = 50;

// 实例化一个文本段落来存储要显示为页眉的内容
TextFragment t1 = new TextFragment("报表标题");
t1.TextState.Font = FontRepository.FindFont("Arial");
t1.TextState.FontSize = 16;
t1.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t1.TextState.FontStyle = FontStyles.Bold;
t1.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t1.TextState.LineSpacing = 5f;
hfFirst.Paragraphs.Add(t1);

TextFragment t2 = new TextFragment("报表名称");
t2.TextState.Font = FontRepository.FindFont("Arial");
t2.TextState.ForegroundColor = Aspose.Pdf.Color.Black;
t2.TextState.HorizontalAlignment = Aspose.Pdf.HorizontalAlignment.Center;
t2.TextState.LineSpacing = 5f;
t2.TextState.FontSize = 12;
hfFirst.Paragraphs.Add(t2);

// 为该部分创建一个 HeaderFooter 对象
HeaderFooter hfFoot = new HeaderFooter();
// 设置 HeaderFooter 对象为奇偶页脚
page.Footer = hfFoot;
hfFoot.Margin.Left = 50;
hfFoot.Margin.Right = 50;

// 添加一个包含当前页码和总页数的文本段落
TextFragment t3 = new TextFragment("生成于测试日期");
TextFragment t4 = new TextFragment("报表名称");
TextFragment t5 = new TextFragment("第 $p 页 共 $P 页");

// 实例化一个表对象
Table tab2 = new Table();

// 将表添加到所需部分的段落集合中
hfFoot.Paragraphs.Add(tab2);

// 设置表的列宽
tab2.ColumnWidths = "165 172 165";

// 在表中创建行，然后在行中创建单元格
Row row3 = tab2.Rows.Add();

row3.Cells.Add();
row3.Cells.Add();
row3.Cells.Add();

// 将文本的垂直对齐设置为居中对齐
row3.Cells[0].Alignment = Aspose.Pdf.HorizontalAlignment.Left;
row3.Cells[1].Alignment = Aspose.Pdf.HorizontalAlignment.Center;
row3.Cells[2].Alignment = Aspose.Pdf.HorizontalAlignment.Right;

row3.Cells[0].Paragraphs.Add(t3);
row3.Cells[1].Paragraphs.Add(t4);
row3.Cells[2].Paragraphs.Add(t5);

// Sec1.Paragraphs.Add(New Text("Aspose.Total for Java 是 Aspose 提供的每个 Java 组件的汇编。它每天编译一次，以确保它包含我们每个 Java 组件的最新版本。 使用 Aspose.Total for Java 开发人员可以创建各种应用程序。 Aspose.Total for Java 是 Aspose 提供的每个 Java 组件的汇编。它每天编译一次，以确保它包含我们每个 Java 组件的最新版本。 使用 Aspose.Total for Java 开发人员可以创建各种应用程序。 Aspose.Total for Java 是 Aspose 提供的每个 Java 组件的汇编。它每天编译一次，以确保它包含我们每个 Java 组件的最新版本。 使用 Aspose.Total for Java 开发人员可以创建各种应用程序。"))
Table table = new Table();

table.ColumnWidths = "33% 33% 34%";
table.DefaultCellPadding = new MarginInfo();
table.DefaultCellPadding.Top = 10;
table.DefaultCellPadding.Bottom = 10;

// 将表添加到所需部分的段落集合中
page.Paragraphs.Add(table);

// 使用 BorderInfo 对象设置默认单元格边框
table.DefaultCellBorder = new BorderInfo(BorderSide.All, 0.1f);

// 使用另一个自定义 BorderInfo 对象设置表边框
table.Border = new BorderInfo(BorderSide.All, 1f);

table.RepeatingRowsCount = 1;

// 在表中创建行，然后在行中创建单元格
Row row1 = table.Rows.Add();

row1.Cells.Add("col1");
row1.Cells.Add("col2");
row1.Cells.Add("col3");
const string CRLF = "\r\n";
for (int i = 0; i <= 10; i++)
{
    Row row = table.Rows.Add();
    row.IsRowBroken = true;
    for (int c = 0; c <= 2; c++)
    {
        Cell c1;
        if (c == 2)
            c1 = row.Cells.Add("Aspose.Total for Java 是 Aspose 提供的每个 Java 组件的汇编。它每天编译一次，以确保它包含我们每个 Java 组件的最新版本。 " + CRLF + "每天编译一次，以确保它包含我们每个 Java 组件的最新版本。 " + CRLF + "使用 Aspose.Total for Java 开发人员可以创建各种应用程序。");
        else
            c1 = row.Cells.Add("item1" + c);
        c1.Margin = new MarginInfo();
        c1.Margin.Left = 30;
        c1.Margin.Top = 10;
        c1.Margin.Bottom = 10;
    }
}

dataDir = dataDir + "ReplaceableSymbolsInHeaderFooter_out.pdf";
doc.Save(dataDir);
```


## 从 PDF 文件中移除未使用的字体

Aspose.PDF for Python via .NET 支持在创建 PDF 文档时嵌入字体的功能，也支持在现有 PDF 文件中嵌入字体。从 Aspose.PDF for Python via .NET 7.3.0 开始，它还允许您从 PDF 文档中移除重复或未使用的字体。

要替换字体，请使用以下方法：

1. 调用 [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber) 类。
1. 调用 TextFragmentAbsorber 类的 TextEditOptions.FontReplace.RemoveUnusedFonts 参数。（这将移除在字体替换过程中变得未使用的字体）。
1. 为每个文本片段单独设置字体。

以下代码片段替换所有文档页面中所有文本片段的字体，并移除未使用的字体。

```python
// 有关完整的示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 加载源 PDF 文件
Document doc = new Document(dataDir + "ReplaceTextPage.pdf");
TextFragmentAbsorber absorber = new TextFragmentAbsorber(new TextEditOptions(TextEditOptions.FontReplace.RemoveUnusedFonts));
doc.Pages.Accept(absorber);

// 遍历所有的 TextFragments
foreach (TextFragment textFragment in absorber.TextFragments)
{
    textFragment.TextState.Font = FontRepository.FindFont("Arial, Bold");
}

dataDir = dataDir + "RemoveUnusedFonts_out.pdf";
// 保存更新后的文档
doc.Save(dataDir);
```


## 从 PDF 文档中删除所有文本

### 使用运算符删除所有文本

在某些文本操作中，您需要从 PDF 文档中删除所有文本，为此，通常需要将找到的文本设为空字符串。关键是更改多个文本片段的文本会引发大量的检查和文本位置调整操作。它们在文本编辑场景中是必不可少的。困难在于您无法确定在循环处理中场景中将删除多少文本片段。

因此，我们建议在从 PDF 页面中删除所有文本的场景中使用另一种方法。请参考以下代码片段，它的工作速度非常快。

```python
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "RemoveAllText.pdf");
// 遍历 PDF 文档的所有页面
for (int i = 1; i <= pdfDocument.Pages.Count; i++)
{
    Page page = pdfDocument.Pages[i];
    OperatorSelector operatorSelector = new OperatorSelector(new Aspose.Pdf.Operators.TextShowOperator());
    // 选择页面上的所有文本
    page.Contents.Accept(operatorSelector);
    // 删除所有文本
    page.Contents.Delete(operatorSelector.Selected);
}
// 保存文档
pdfDocument.Save(dataDir + "RemoveAllText_out.pdf", Aspose.Pdf.SaveFormat.Pdf);
```


<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
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
    "applicationCategory": "PDF 操作库 for Python",
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