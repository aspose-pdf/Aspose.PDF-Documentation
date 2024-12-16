---
title: 从PDF中提取上标和下标文本
linktitle: 提取上标和下标
type: docs
weight: 30
url: /zh/net/extract-superscripts-subscripts-from-pdf/
description: 本文介绍了使用Aspose.PDF在C#中从PDF提取上标和下标文本的各种方法。
lastmod: "2022-10-07"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 提取上标和下标文本

从PDF文档中提取文本是一件常见的事情。然而，在这样的文本中，当提取时，其中包含的**上标和下标**，这些通常用于技术文档和文章，可能不会显示。上标或下标是放置在常规文本行下方或上方的字符、数字或字母。它通常比文本的其余部分小。

**下标和上标**最常用于公式、数学表达式和化学化合物的规格中。
**下标和上标**通常用于公式、数学表达式和化学化合物的规格说明中。
在最新的版本更新中，**Aspose.PDF for .NET**库增加了从PDF提取上标和下标文本的支持。

使用**TextFragmentAbsorber**类，您可以对找到的文本做任何事情，即，您可以简单地使用整个文本。尝试以下代码片段：

以下代码片段也可以与[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库一起使用。

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            writer.WriteLine(absorber.Text);
        }
```

或者单独使用**TextFragments**并对它们进行各种操作，例如按坐标或大小排序。

以下代码片段也可以与[Aspose.PDF.Drawing](/pdf/zh/net/drawing/)库一起使用。
以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/zh/net/drawing/) 库。

```csharp
    Document doc = new Document(GetInputPath("test1.pdf"));
    TextFragmentAbsorber absorber = new TextFragmentAbsorber();
    doc.Pages[1].Accept(absorber);
        using (StreamWriter writer = new StreamWriter(GetOutputPath("output.txt")))
        {
            foreach (var textFragment in absorber.TextFragments)
            {
                writer.Write(textFragment.Text);
            }
        }
```
