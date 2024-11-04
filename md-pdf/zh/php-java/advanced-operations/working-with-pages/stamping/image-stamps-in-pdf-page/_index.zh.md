---
title: 在PDF中以编程方式添加图像印章 
linktitle: PDF文件中的图像印章
type: docs
weight: 10
url: /php-java/image-stamps-in-pdf-page/
description: 使用ImageStamp类通过Aspose.PDF for PHP via Java库在PDF文档中添加图像印章。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在PDF文件中添加图像印章

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类在PDF文档中添加图像作为印章。[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类提供了指定高度、宽度和不透明度等的方法。

要添加图像印章：

1. 使用所需属性创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和一个 ImageStamp 对象。

1. 调用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类的 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 方法，将图章添加到 PDF 中。

以下代码片段展示了如何在 PDF 文件中添加图像图章。

```php

    // 打开文档
    $document = new Document($inputFile);        
    $pages = $document->getPages();
  
    // 创建图像图章
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setBackground(true);
    $imageStamp->setXIndent(100);
    $imageStamp->setYIndent(100);
    $imageStamp->setHeight(48);
    $imageStamp->setWidth(225);
    $imageStamp->setRotate((new Rotation())->getOn270());
    $imageStamp->setOpacity(0.5);

    // 将图章添加到特定页面
    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close()
```

## 控制添加图章时的图像质量

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类允许您在 PDF 文档中添加图像作为图章。
 它还允许您在将图像作为水印添加到 PDF 文件时控制图像质量。为此，已在 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类中添加了一个名为 setQuality(...) 的方法。在 com.aspose.pdf.facades 包的 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) 类中也可以找到类似的方法。

以下代码片段展示了如何在 PDF 文件中添加印章时控制图像质量。

```php

    // 打开文档
    $document = new Document($inputFile);        
    $pages = $document->getPages();

    // 创建图像印章
    $imageStamp = new ImageStamp($inputImageFile);
    $imageStamp->setQuality(10);

    $document->getPages()->get_Item(1)->addStamp($imageStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();        
```

## 浮动框中的图像印章作为背景

Aspose.PDF API 允许您在浮动框中将图像印章作为背景添加。 FloatingBox 类的 BackgroundImage 属性可以用来为浮动框设置背景图章，如以下代码示例所示。

此代码片段演示了创建 PDF 文档并向其中添加 FloatingBox 的过程。FloatingBox 包含一个文本片段、一个边框、一个背景图片和一个背景颜色。生成的文档随后保存到输出文件。

```php

    // 打开文档
    $document = new Document($inputFile);
    $colors = new Color();
    $pages = $document->getPages();

    // 向 PDF 文档添加页面
    $page = $pages->add();

    // 创建 FloatingBox 对象
    $aBox = new FloatingBox(200, 100);

    // 设置 FloatingBox 的左侧位置
    $aBox->setLeft(40);

    // 设置 FloatingBox 的顶部位置
    $aBox->setTop(80);

    // 设置 FloatingBox 的水平对齐
    $aBox->setHorizontalAlignment((new HorizontalAlignment())->getCenter());

    // 向 FloatingBox 的段落集合中添加文本片段
    $aBox->getParagraphs()->add(new TextFragment("主文本"));

    // 设置 FloatingBox 的边框
    $aBox->setBorder(new BorderInfo(BorderSide::$All, $colors->getRed()));

    // 添加背景图片
    $img = new Image();
    $img->setFile($inputImageFile);
    $aBox->setBackgroundImage($img);

    // 设置 FloatingBox 的背景颜色
    $aBox->setBackgroundColor($colors->getYellow());

    // 将 FloatingBox 添加到页面对象的段落集合中
    $page->getParagraphs()->add($aBox);
    
    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```