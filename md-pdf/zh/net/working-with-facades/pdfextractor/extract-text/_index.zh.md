---
title: 从 PDF 文件中提取文本
type: docs
weight: 30
url: /net/extract-text/
description: 本节说明如何使用 PdfExtractor 类从 pdf 中提取文本。
lastmod: "2021-06-05"
---

在本文中，我们将深入探讨从 PDF 文件中提取文本的细节。所有这些提取功能都在一个地方提供，即 [PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类。我们将了解如何在代码中使用这些功能。

[PdfExtractor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor) 类提供三种类型的提取功能。这三类分别是文本、图像和附件。为了在这三类中进行提取，PdfExtractor 提供了多种方法，这些方法协同工作以提供最终输出。

例如，为了提取文本，您可以使用三种方法，即。 
[ExtractText, GetText, HasNextPageText 和 GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/index)。
``` 现在，为了开始提取文本，首先，你需要调用 [ExtractText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/extracttext/index) 方法；这将从 PDF 文件中提取文本并将其存储到内存中。之后，[GetText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/gettext/index) 方法将获取此提取的文本并将其保存到指定位置的文件中。[HasNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/hasnextpagetext) 帮助你遍历每一页并检查下一页是否有文本。如果它包含一些文本，那么 [GetNextPageText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfextractor/methods/getnextpagetext/index) 将帮助你将单个页面的文本保存到文件中。

```csharp
public static void ExtractText()
{
    bool WholeText = true;
    // 创建 PdfExtractor 类的对象
    PdfExtractor pdfExtractor = new PdfExtractor();

    // 绑定输入的 PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // 提取文本
    pdfExtractor.ExtractText();

    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // 将文本提取到单独的文件中
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```
要提取文本提取模式，请使用以下代码：

```csharp
public static void ExtractTextExtractonMode()
{
    bool WholeText = true;
    // 创建 PdfExtractor 类的对象
    PdfExtractor pdfExtractor = new PdfExtractor();

    // 绑定输入 PDF
    pdfExtractor.BindPdf(_dataDir + "sample.pdf");

    // 提取文本
    // pdfExtractor.ExtractTextMode = 0; //纯模式
    pdfExtractor.ExtractTextMode = 1; //原始模式
    pdfExtractor.ExtractText();


    if (!WholeText)
    {
        pdfExtractor.GetText(_dataDir + "sample.txt");
    }
    else
    {
        // 将文本提取到单独的文件中
        int pageNumber = 1;
        while (pdfExtractor.HasNextPageText())
        {
            pdfExtractor.GetNextPageText($"{_dataDir}\\sample{pageNumber:D3}.txt");
            pageNumber++;
        }
    }
}
```