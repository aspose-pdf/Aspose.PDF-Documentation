---
title: 添加 PDF 页面印章到 PDF
linktitle: PDF 文件中的页面印章
type: docs
weight: 30
url: /java/page-stamps-in-the-pdf-file/
description: 使用 Java 的 PdfPageStamp 类向 PDF 文件添加页面印章。
lastmod: "2021-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 使用 Java 添加页面印章

当您需要应用包含图形、文本、表格的复合印章时，可以使用 [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp)。以下示例展示了如何使用印章来创建类似于使用 Adobe InDesign、Illustrator、Microsoft Word 的信纸。假设我们有一些输入文档，我们想要应用两种带有蓝色和李子色的边框。

```java
public static void AddPageStamp()
{
    String inputFileName = "sample-4pages.pdf";
    String outputFileName = "AddPageStamp_out.pdf";
    String pageStampFileName = "PageStamp.pdf";
    Document document = new Document(_dataDir + inputFileName);

    PdfPageStamp bluePageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 1);
    bluePageStamp.setHeight(800);
    bluePageStamp.setBackground(true);

    PdfPageStamp plumPageStamp = new PdfPageStamp(_dataDir + pageStampFileName, 2);
    plumPageStamp.setHeight(800);
    plumPageStamp.setBackground(true);

    for (int i = 1; i < 5; i++)
    {
        if (i % 2 == 0)
            document.getPages().get_Item(i).addStamp(bluePageStamp);
        else
            document.getPages().get_Item(i).addStamp(plumPageStamp);
    }

    document.save(_dataDir + outputFileName);
}
```