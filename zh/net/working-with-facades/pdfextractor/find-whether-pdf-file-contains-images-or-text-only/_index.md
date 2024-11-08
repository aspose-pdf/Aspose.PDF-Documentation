---
title: 找出 PDF 是否包含图像或文本
linktitle: 检查文本和图像的存在
type: docs
weight: 40
url: /zh/net/find-whether-pdf-file-contains-images-or-text-only/
description: 本主题解释如何使用 PdfExtractor 类找出 PDF 文件是否仅包含图像或文本。
lastmod: "2021-06-05"
draft: false
---

## 背景

一个 PDF 文件可以包含文本和图像。有时，用户可能需要找出 PDF 文件是仅包含文本，还是仅包含图像。我们也可以找出它是否同时包含两者或不包含任何内容。

{{% alert color="primary" %}}

以下代码片段向您展示如何满足此要求。

{{% /alert %}}

```csharp
 public static void CheckIfPdfContainsTextOrImages()
{
    // 实例化一个 MemoryStream 对象以保存从文档中提取的文本
    MemoryStream ms = new MemoryStream();
    // 实例化 PdfExtractor 对象
    PdfExtractor extractor = new PdfExtractor();

    // 将输入 PDF 文档绑定到提取器
    extractor.BindPdf(_dataDir + "FilledForm.pdf");
    // 从输入 PDF 文档中提取文本
    extractor.ExtractText();
    // 将提取的文本保存到文本文件
    extractor.GetText(ms);
    // 检查 MemoryStream 的长度是否大于或等于 1

    bool containsText = ms.Length >= 1;

    // 从输入 PDF 文档中提取图像
    extractor.ExtractImage();

    // 在 while 循环中调用 HasNextImage 方法。当图像提取完毕时，循环将退出
    bool containsImage = extractor.HasNextImage();

    // 现在找出这个 PDF 是仅包含文本还是仅包含图像

    if (containsText && !containsImage)
        Console.WriteLine("PDF 仅包含文本");
    else if (!containsText && containsImage)
        Console.WriteLine("PDF 仅包含图像");
    else if (containsText && containsImage)
        Console.WriteLine("PDF 包含文本和图像");
    else if (!containsText && !containsImage)
        Console.WriteLine("PDF 不包含文本和图像");
}
```