---
title: 使用 PHP 裁剪 PDF 页面
linktitle: 裁剪页面
type: docs
weight: 80
url: /php-java/crop-pages/
description: 您可以使用 Aspose.PDF for PHP via Java 获取页面属性，例如宽度、高度、出血框、裁剪框和修整框。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取页面属性

PDF 文件中的每一页都有许多属性，例如宽度、高度、出血框、裁剪框和修整框。Aspose.PDF for PHP via Java 允许您访问这些属性。

- **媒体框**：媒体框是最大的页面框。它对应于打印到 PostScript 或 PDF 时选择的页面大小（例如 A4、A5、美国信纸等）。换句话说，媒体框决定了显示或打印 PDF 文档的介质的物理大小。
- **出血框**：如果文档有出血，PDF 也会有一个出血框。
 出血是指超出页面边缘的颜色（或艺术作品）的量。它用于确保当文档被打印并切割到指定尺寸（“修边”）时，墨水会一直延伸到页面边缘。即使页面被错误地裁剪——稍微切偏了裁剪标记——页面上也不会出现白边。
- **裁切框**：裁切框表示文档打印和裁切后的最终尺寸。
- **艺术框**：艺术框是围绕文档中页面实际内容绘制的框。当在其他应用程序中导入 PDF 文档时使用此页面框。
- **裁剪框**：裁剪框是您的 PDF 文档在 Adobe Acrobat 中显示的“页面”大小。在正常视图中，Adobe Acrobat 只显示裁剪框的内容。有关这些属性的详细说明，请阅读 Adobe.Pdf 规范，特别是 10.10.1 页边界。
- **页面矩形**：媒体框和下拉框的交集（通常为可见矩形）。 下面的图片说明了这些属性。  
有关详细信息，请访问[此页面](http://www.enfocus.com/manuals/ReferenceGuide/PP/10/enUS/en-us/concept/c_aa1095731.html)。

下面的代码片段展示了如何裁剪页面：

```php

    // 打开文档
    $document = new Document($inputFile);      

    $page = $document->getPages()->get_Item(1);

    $responseData = $page->getCropBox() . PHP_EOL;
    $responseData = $responseData . $page->getTrimBox() . PHP_EOL;
    $responseData = $responseData . $page->getArtBox() . PHP_EOL;
    $responseData = $responseData . $page->getBleedBox() . PHP_EOL;
    $responseData = $responseData . $page->getMediaBox() . PHP_EOL;

    // 创建新的 Box 矩形
    $newBox = new Rectangle(200, 220, 2170, 1520);

    $page->setCropBox($newBox);
    $page->setTrimBox($newBox);
    $page->setArtBox($newBox);
    $page->setBleedBox($newBox);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```

在这个例子中，我们使用了一个示例文件[这里](crop_page.pdf)。 最初，我们的页面如图1所示。
![图1. 裁剪页面](crop_page.png)

更改后，页面将如图2所示。
![图2. 裁剪页面](crop_page2.png)