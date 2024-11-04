---
title: 从 PDF 中提取字体
linktitle: 提取字体
type: docs
weight: 30
url: /java/extract-fonts-from-pdf/
description: 如何使用 Aspose.PDF for Java 从 PDF 中提取字体
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

如果您想从 PDF 文档中获取所有字体，可以使用 Document 类中提供的 `Document.IDocumentFontUtilities.getAllFonts()` 方法。请检查以下代码片段以从现有的 PDF 文档中获取所有字体：

```java
public static void Extract_Fonts() throws FileNotFoundException
{
    // 文档目录的路径。
    String filePath = "<... enter file name ...>";
    
    // 加载 PDF 文档
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Font[] fonts = pdfDocument.getFontUtilities().getAllFonts();

    for (com.aspose.pdf.Font font : fonts)
    {
        font.save(new FileOutputStream(font.getFontName()));
    }
}
```