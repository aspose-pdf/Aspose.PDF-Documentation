---
title: 添加 PDF 页面印章到 PDF 
linktitle: PDF 文件中的页面印章
type: docs
weight: 30
url: /php-java/page-stamps-in-the-pdf-file/
description: 使用 PdfPageStamp 类通过 PHP 向 PDF 文件添加页面印章。
lastmod: "2024-09-10"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## 添加页面印章

当您需要应用包含图形、文本、表格的复合印章时，可以使用 [PdfPageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PdfPageStamp)。以下示例展示了如何使用印章来创建类似于使用 Adobe InDesign、Illustrator、Microsoft Word 的信纸。假设我们有一些输入文档，并且我们想要应用两种颜色的边框，蓝色和李子色。

```php

    // 打开文档
    $document = new Document($inputFile);        
    $bluePageStamp = new PdfPageStamp($inputPageFile, 1);
    $bluePageStamp->setHeight(800);
    $bluePageStamp->setBackground(true);        

    $plumPageStamp = new PdfPageStamp($inputPageFile, 2);
    $plumPageStamp->setHeight(800);
    $plumPageStamp->setBackground(true);

    for ($i = 1; $i < 5; $i++)
    {
        if ($i % 2 == 0)
            $document->getPages()->get_Item($i).addStamp($bluePageStamp);
        else
            $document->getPages()->get_Item($i).addStamp($plumPageStamp);
    }

    // 保存输出文档
    $document->save($outputFile);
    $document->close();  
```