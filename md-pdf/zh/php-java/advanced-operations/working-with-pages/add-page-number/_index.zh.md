---
title: 为 PDF 添加页码
linktitle: 添加页码
type: docs
weight: 100
url: /php-java/add-page-number/
description: Aspose.PDF for PHP via Java 允许您使用 PageNumber Stamp 类向 PDF 文件添加页码。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

所有的文档都必须有页码。页码使读者更容易定位文档的不同部分。
**Aspose.PDF for PHP via Java** 允许您使用 PageNumberStamp 添加页码。

{{% alert color="primary" %}}

在线试用。您可以在此链接 [products.aspose.app/pdf/page-number](https://products.aspose.app/pdf/page-number) 在线检查 Aspose.PDF 转换的质量并查看结果

{{% /alert %}}

您可以使用 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 类在 PDF 文档中添加页码印章。
 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 类提供了创建基于页码的印章的方法，如格式、边距、对齐、起始编号等。要添加页码印章，您需要创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和一个具有所需文本属性的 [PageNumberStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageNumberStamp) 对象。之后，您可以调用 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 方法来将印章添加到 PDF 文件中。您还可以设置页码印章的字体属性。

下面的代码片段展示了如何在 PDF 文件中添加页码。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 创建页码印章
    $pageNumberStamp = new PageNumberStamp();

    // 印章是否为背景
    $Center = (new HorizontalAlignment())->getCenter();
    $pageNumberStamp->setBackground(false);
    $pageNumberStamp->setFormat("Page # of " . $document->getPages()->size());
    $pageNumberStamp->setBottomMargin(10);
    $pageNumberStamp->setHorizontalAlignment($Center);
    $pageNumberStamp->setStartingNumber(1);

    $fontRepository = new FontRepository();
    // 设置文本属性
    $pageNumberStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $pageNumberStamp->getTextState()->setFontSize(14.0);
    $pageNumberStamp->getTextState()->setFontStyle(FontStyles::$Bold);
    $pageNumberStamp->getTextState()->setForegroundColor((new Color())->getAqua());

    // 将印章添加到特定页面
    $document->getPages()->get_Item(1)->addStamp($pageNumberStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```