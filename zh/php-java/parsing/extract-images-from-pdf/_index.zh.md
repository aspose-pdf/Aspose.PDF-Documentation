---
title: 从PDF中提取图像
linktitle: 提取图像
type: docs
weight: 20
url: /php-java/extract-images-from-the-pdf-file/
description: 如何使用 Aspose.PDF for PHP 从 PDF 中提取部分图像
lastmod: "2024-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

PDF 文档中的每一页都包含资源（图像、表单和字体）。我们可以通过调用[getResources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#getResources--)方法来访问这些资源。[Resources](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources)类包含[XImageCollection](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImageCollection)，我们可以通过调用[getImages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Resources#getImages--)方法来获取图像列表。

因此，要从页面中提取图像，我们需要获取对页面的引用，然后是页面资源，最后是图像集合。
我们可以通过索引来提取特定图像。

图像的索引返回一个[XImage](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage)对象。
该对象提供了一个 [save](https://reference.aspose.com/pdf/java/com.aspose.pdf/XImage#save-java.io.OutputStream-) 方法，可用于保存提取的图像。以下代码片段显示了如何从 PDF 文件中提取图像。

```php

    // 加载 PDF 文档
    $document = new Document($inputFile);

    // 获取文档的第一页
    $page = $document->getPages()->get_Item(1);

    // 获取页面上的图像集合
    $xImageCollection = $page->getResources()->getImages();

    // 从集合中获取第一张图像
    $xImage = $xImageCollection->get_Item(1);

    // 创建一个新的 FileOutputStream 对象以保存图像
    $outputImage = new java("java.io.FileOutputStream", $outputFile);

    // 将图像保存到输出文件
    $xImage->save($outputImage);

    // 关闭输出图像文件
    $outputImage->close();
```