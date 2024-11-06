---
title: 使用 C# 从印章中提取文本
type: docs
weight: 60
url: zh/net/extract-text-from-stamps/
description: 学习如何使用 Aspose.PDF for .NET 的特殊功能 - 从印章注释中提取文本
lastmod: "2021-01-30"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 从印章注释中提取文本

Aspose.PDF for NET 允许您从印章注释中提取文本。为了从 PDF 中的印章注释提取文本，可以使用以下步骤。

1. 创建一个 `Document` 类对象
1. 从页面的注释列表中获取所需的 `Annotation`
1. 定义一个新的 `TextAbsorber` 类对象
1. 使用 TextAbsorber 的 visit 方法获取文本

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

```csharp
public static void ExtractText()
{
   Document document = new Document(_dataDir + "ExtractStampText.pdf");
   Annotation item = document.Pages[1].Annotations[1];
   if (item is StampAnnotation annot) {
         TextAbsorber ta = new TextAbsorber();
         XForm ap = annot.Appearance["N"];
         ta.Visit(ap);
         Console.WriteLine(ta.Text);
   }
}
```
当然可以，但请提供需要翻译的文档内容，以便我为您进行翻译。
