---
title: 添加 PDF 页眉和页脚 
linktitle: 添加 PDF 页眉和页脚
type: docs
weight: 70
url: /php-java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for PHP via Java 允许您使用 TextStamp 类为 PDF 文件添加页眉和页脚。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 印章通常用于合同、报告和限制性材料，以证明文档已被审核并标记为“已读”、“合格”或“机密”等。本文将向您展示如何使用 **Aspose.PDF for PHP via Java** 向 PDF 文档添加图像印章和文字印章。

如果您逐行阅读上述代码片段，您会发现语法和代码逻辑非常容易理解。

## 在 PDF 文件的页眉中添加文本

您可以使用 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类在 PDF 文件的页眉中添加文本。
 TextStamp 类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加文本，您需要使用所需属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 AddStamp 方法在 PDF 的页眉中添加文本。

您需要设置 TopMargin 属性，以便它调整 PDF 页眉区域中的文本。您还需要将 HorizontalAlignment 设置为 Center，并将 VerticalAlignment 设置为 Top。

以下代码片段向您展示如何使用 PHP 在 PDF 文件的页眉中添加文本。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 创建页眉
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // 设置印章的属性
    $textStamp->setTopMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // 在第一页添加页脚
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```

## 在 PDF 文件的页脚添加文本

您可以使用 TextStamp 类在 PDF 文件的页脚添加文本。TextStamp 类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚添加文本，您需要创建一个 Document 对象和一个使用所需属性的 TextStamp 对象。之后，您可以调用页面的 addStamp 方法在 PDF 的页脚添加文本。

以下代码片段向您展示了如何使用 PHP 在 PDF 文件的页脚添加文本。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 创建页眉
    $textStamp = new TextStamp("Header Text");
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // 设置印章的属性
    $textStamp->setBottomMargin(10);
    $textStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $textStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // 在第一页添加页脚
    $page = $pages->get_Item(1);
    $page->addStamp($textStamp);
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```


## 在 PDF 文件的页眉中添加图像

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) 类在 PDF 文件的页眉中添加图像。Image Stamp 类提供了创建基于图像的图章所需的属性，例如字体大小、字体样式和字体颜色等。为了在页眉中添加图像，您需要使用所需属性创建一个 Document 对象和一个 Image Stamp 对象。之后，您可以调用 Page 的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) 方法将图像添加到 PDF 的页眉中。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 创建页脚
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // 设置图章的属性
    $imageStamp->setTopMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Top);

    $pages = $document->getPages();

    // 将页脚添加到第一页
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```


以下代码片段展示了如何使用 PHP 在 PDF 文件的页眉中添加图像。

## 在 PDF 文件的页脚中添加图像

您可以使用 Image Stamp 类在 PDF 文件的页脚中添加图像。Image Stamp 类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚中添加图像，您需要使用所需的属性创建一个 Document 对象和一个 Image Stamp 对象。之后，您可以调用 Page 的 AddStamp 方法在 PDF 的页脚中添加图像。

{{% alert color="primary" %}}

您需要设置 BottomMargin 属性，以便调整图像在 PDF 的页脚区域。您还需要将 [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) 设置为 `Center`，并将 [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) 设置为 `Bottom`。

{{% /alert %}}

以下代码片段展示了如何使用 PHP 在 PDF 文件的页脚中添加图像。

```php

    // 打开文档
    $document = new Document($inputFile);
    
    // 创建页脚
    $imageStamp = new ImageStamp($inputImage);
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();

    // 设置图章的属性
    $imageStamp->setBottomMargin(10);
    $imageStamp->setHorizontalAlignment($horizontalAlignment->Center);
    $imageStamp->setVerticalAlignment($verticalAlignment->Bottom);

    $pages = $document->getPages();

    // 添加页脚到第一页
    $page = $pages->get_Item(1);
    $page->addStamp($imageStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```

## 在一个 PDF 文件中添加不同的页眉

我们知道可以通过使用 TopMargin 或 Bottom Margin 属性在文档的页眉/页脚部分添加 TextStamp，但有时我们可能需要在一个 PDF 文档中添加多个页眉/页脚。**Aspose.PDF for PHP via Java** 解释了如何做到这一点。

为了实现这一要求，我们将创建单独的 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象（对象的数量取决于所需的页眉/页脚数量），并将它们添加到 PDF 文档中。

 我们还可以为单独的印章对象指定不同的格式信息。在以下示例中，我们创建了 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和三个 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象，然后我们使用页面的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) 方法将文本添加到 PDF 的页眉部分。以下代码片段向您展示了如何使用 Aspose.PDF for PHP via Java 在 PDF 文件的页脚添加图像。

```php

    // 打开文档
    $document = new Document($inputFile);

    // 创建三个印章
    $stamp1 = new TextStamp("Header 1");
    $stamp2 = new TextStamp("Header 2");
    $stamp3 = new TextStamp("Header 3");
    
    $horizontalAlignment = new HorizontalAlignment();
    $verticalAlignment = new VerticalAlignment();
    $fontStyles = new FontStyles();

    // 设置印章对齐方式（将印章放在页面顶部，水平居中）
    $stamp1->setVerticalAlignment ($verticalAlignment->Top);
    $stamp1->setHorizontalAlignment($horizontalAlignment->Center);

    // 指定字体样式为粗体
    $stamp1->getTextState()->setFontStyle($fontStyles->Bold);
    // 设置文本前景色信息为红色
    $stamp1->getTextState()->setForegroundColor((new Color())->getRed());
    // 指定字体大小为 14
    $stamp1->getTextState()->setFontSize(14);

    // 现在我们需要将第二个印章对象的垂直对齐方式设置为顶部
    $stamp2->setVerticalAlignment($verticalAlignment->Top);
    // 将印章的水平对齐信息设置为居中对齐
    $stamp2->setHorizontalAlignment($horizontalAlignment->Center);
    // 设置印章对象的缩放因子
    $stamp2->setZoom(10);

    // 设置第三个印章对象的格式
    // 指定印章对象的垂直对齐信息为顶部
    $stamp3->setVerticalAlignment($verticalAlignment->Top);
    // 将印章对象的水平对齐信息设置为居中对齐
    $stamp3->setHorizontalAlignment ($horizontalAlignment->Center);
    // 设置印章对象的旋转角度
    $stamp3->setRotateAngle(35);
    // 将印章的背景色设置为粉色
    $stamp3->getTextState()->setBackgroundColor ((new Color())->getPink());  
    // 将印章的字体信息更改为 Verdana
    $stamp3->getTextState()->setFont ((new FontRepository())->findFont("Verdana"));

    // 第一个印章添加在第一页;
    $document->getPages()->get_Item(1)->addStamp($stamp1);
    // 第二个印章添加在第二页;
    $document->getPages()->get_Item(2)->addStamp($stamp2);
    // 第三个印章添加在第三页。
    $document->getPages()->get_Item(3)->addStamp($stamp3);
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```