---
title: 从 PDF C# 中提取文本
linktitle: 从 PDF 中提取文本
type: docs
weight: 10
url: /zh/net/extract-text-from-all-pdf/
description: 本文介绍了使用 Aspose.PDF 在 C# 中从 PDF 文档提取文本的各种方法。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档的所有页面提取文本

从 PDF 文档提取文本是一个常见的需求。在这个示例中，您将看到如何使用 Aspose.PDF for .NET 从 PDF 文档的所有页面提取文本。您需要创建 **TextAbsorber** 类的对象。之后，使用 **Document** 类打开 PDF，并调用 **Pages** 集合的 **Accept** 方法。**TextAbsorber** 类从文档中吸收文本并返回在 **Text** 属性中。以下代码片段显示了如何从 PDF 文档的所有页面提取文本。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// 创建 TextAbsorber 对象以提取文本
TextAbsorber textAbsorber = new TextAbsorber();
// 为所有页面接受吸收器
pdfDocument.Pages.Accept(textAbsorber);
// 获取提取的文本
string extractedText = textAbsorber.Text;
// 创建一个写入器并打开文件
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// 向文件写入一行文本
tw.WriteLine(extractedText);
// 关闭流
tw.Close();
```
在文档对象的特定页面上调用 **Accept** 方法。索引是需要提取文本的特定页面编号。

下面的代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// 创建 TextAbsorber 对象以提取文本
TextAbsorber textAbsorber = new TextAbsorber();
 
// 接受特定页面的吸收器
pdfDocument.Pages[1].Accept(textAbsorber);

// 获取提取的文本
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// 创建一个写入器并打开文件
TextWriter tw = new StreamWriter(dataDir);

// 向文件写入一行文本
tw.WriteLine(extractedText);

// 关闭流
tw.Close();
```
## 使用文本设备从页面提取文本

您可以使用 **TextDevice** 类从 PDF 文件中提取文本。TextDevice 在其实现中使用 TextAbsorber，因此，实际上它们做的事情相同，但 TextDevice 只是为了统一“设备”方法来从页面 ImageDevice、PageDevice 等提取任何内容。TextAbsorber 可以从页面、整个 PDF 或 XForm 提取文本，这使得 TextAbsorber 更通用。

### 从所有页面提取文本

以下步骤和代码片段向您展示如何使用文本设备从 PDF 中提取文本。

1. 使用指定的输入 PDF 文件创建 Document 类的对象
1. 创建 TextDevice 类的对象
1. 使用 TextExtractOptions 类的对象指定提取选项
1. 使用 TextDevice 类的 Process 方法将内容转换为文本
1. 将文本保存到输出文件

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文件路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// 用于保存提取的文本
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // 创建文本设备
        TextDevice textDevice = new TextDevice();

        // 设置文本提取选项 - 设置文本提取模式（Raw 或 Pure）
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // 转换特定页面并将文本保存到流中
        textDevice.Process(pdfPage, textStream);
        // 转换特定页面并将文本保存到流中
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // 关闭内存流
        textStream.Close();

        // 从内存流获取文本
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// 将提取的文本保存在文本文件中
File.WriteAllText(dataDir, builder.ToString());
```
## 从特定页面区域提取文本

**TextAbsorber** 类提供了从 PDF 文档的特定页面或所有页面提取文本的功能。这个类通过 **Text** 属性返回提取的文本。然而，如果我们需要从特定页面区域提取文本，我们可以使用 **TextSearchOptions** 的 **Rectangle** 属性。Rectangle 属性接受一个 Rectangle 对象作为值，使用这个属性，我们可以指定需要提取文本的页面区域。

调用页面的 **Accept** 方法来提取文本。创建 **Document** 和 **TextAbsorber** 类的对象。在 **Document** 对象的个别页面上调用 **Accept** 方法，作为 **Page** 索引。**Index** 是从中需要提取文本的特定页面号。你可以从 **TextAbsorber** 类的 **Text** 属性获取文本。以下代码片段显示了如何从单个页面提取文本。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。
以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// 创建 TextAbsorber 对象以提取文本
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// 接受第一页的吸收器
pdfDocument.Pages[1].Accept(absorber);

// 获取提取的文本
string extractedText = absorber.Text;
// 创建一个写入器并打开文件
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// 向文件写入一行文本
tw.WriteLine(extractedText);
// 关闭流
tw.Close();
```

## 基于列提取文本

PDF 文件可能包含文本、图像、注释、附件、图表等元素，Aspose.PDF for .NET 提供了添加和操作所有这些元素的功能。
PDF 文件可能包括文本、图像、注释、附件、图表等元素，Aspose.PDF for .NET 提供了添加和操作所有这些元素的功能。

以下代码片段也可用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// 打开文档
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // 需要将字体大小至少减小70%
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### 第二种方法 - 使用 ScaleFactor

在这个新版本中，我们还引入了 TextAbsorber 和内部文本格式化机制的几项改进。因此，现在在使用“纯”模式进行文本提取时，您可以指定 ScaleFactor 选项，这可以是从多列 PDF 文档中提取文本的另一种方法，除了上述方法。这个比例因子可以设置为调整用于文本提取期间内部文本格式化机制的网格。指定 ScaleFactor 值在 1 到 0.1 之间（包括 0.1）具有与字体缩小相同的效果。

指定 ScaleFactor 值在 0.1 到 -0.1 之间被视为零值，但它使算法在提取文本期间自动计算所需的比例因子。
指定 ScaleFactor 值在 0.1 到 -0.1 之间被视为零值，但它使算法在自动提取文本时计算所需的缩放因子。

我们建议在处理大量 PDF 文件以提取文本内容时使用自动缩放（ScaleFactor = 0），或者手动设置冗余的网格宽度减小（大约 ScaleFactor = 0.5）。然而，您不必确定具体文件是否需要缩放。如果您为文档设置了不需要的冗余减少网格宽度（该文档不需要这样做），提取的文本内容将保持完全充分。请查看以下代码片段。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// For complete examples and data files, please go to https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// The path to the documents directory.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// Open document
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// 设置缩放因子为 0.5 足以在大多数文件中分割列
// 设置为零可以让算法自动选择缩放因子
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}

请注意，新的 ScaleFactor 与手动减小字体的旧系数之间没有直接对应关系。然而，默认算法会考虑到由于某些内部原因已经减小的字体大小的值。例如，将字体大小从 10 减小到 7 的效果与将缩放因子设置为 5/8（= 0.625）相同。

{{% /alert %}}

## 从 PDF 文档中提取突出显示的文本

在从 PDF 文档中提取文本的各种场景中，您可能需要提取仅突出显示的文本。为了实现此功能，我们在 API 中添加了 TextMarkupAnnotation.GetMarkedText() 和 TextMarkupAnnotation.GetMarkedTextFragments() 方法。您可以通过过滤 TextMarkupAnnotation 并使用上述方法从 PDF 文档中提取突出显示的文本。以下代码片段展示了如何从 PDF 文档中提取突出显示的文本。

以下代码片段还适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。
以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
// 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// 遍历所有注释
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // 过滤 TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // 检索突出显示的文本片段
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // 显示突出显示的文本
            Console.WriteLine(tf.Text);
        }
    }
}
```

## 从 XML 访问文本片段和段元素

有时我们需要在处理从 XML 生成的 PDF 文档时访问 TextFragement 或 TextSegment 项。
有时我们需要在处理从 XML 生成的 PDF 文档时访问 TextFragement 或 TextSegment 项目。

以下代码片段也可以与 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库一起使用。

```csharp
// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
