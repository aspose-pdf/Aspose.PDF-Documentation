---
title: 在PDF中以编程方式添加文本水印
linktitle: PDF文件中的文本水印
type: docs
weight: 20
url: /php-java/text-stamps-in-the-pdf-file/
description: 使用TextStamp类通过PHP向PDF文件添加文本水印。
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用Java添加文本水印

Aspose.PDF for PHP via Java 提供了 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类以在PDF文件中添加文本水印。
 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类提供了必要的方法来指定戳记对象的字体大小、字体样式和字体颜色等。为了添加文本戳记，首先需要使用所需的方法创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和一个 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象。之后，您可以调用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类的 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 方法将戳记添加到 PDF 文档中。

下面的代码片段展示了如何在 PDF 文件中添加文本戳记。

```php

    // 打开文档
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();
    // 创建文本戳记
    $textStamp = new TextStamp("Sample Stamp");
    // 设置戳记是否为背景
    $textStamp->setBackground(true);
    // 设置起始坐标
    $textStamp->setXIndent(100);
    $textStamp->setYIndent(100);
    // 旋转戳记
    $textStamp->setRotate((new Rotation())->On90);    
    // 设置文本属性
    $fontRepository = new FontRepository();
    $fontStyles = new FontStyles();
    $textStamp->getTextState()->setFont($fontRepository->findFont("Arial"));
    $textStamp->getTextState()->setFontSize(14);
    $textStamp->getTextState()->setFontStyle($fontStyles->Bold | $fontStyles->Italic);
    $textStamp->getTextState()->setForegroundColor($colors->getGreen());

    // 将戳记添加到特定页面
    $pages->get_Item(1)->addStamp($textStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();
```

## 定义 TextStamp 对象的对齐方式

在 PDF 文档中添加水印是经常需要的功能之一，Aspose.PDF for PHP via Java 完全有能力添加图像和文本水印。[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类提供了在 PDF 文件上添加文本印章的功能。最近有一个需求，需要支持在使用 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象时指定文本对齐的功能。因此，为了满足这个需求，我们在 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类中引入了 setTextAlignment(..) 方法。通过使用此方法，您可以指定水平文本对齐方式。

以下代码片段展示了如何加载现有的 PDF 文档并在其上添加 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 的示例。

```php

    // 打开文档
    $document = new Document($inputFile);        
    $pages = $document->getPages();
    $colors = new Color();

    // 使用示例字符串实例化 FormattedText 对象
    $text = new FormattedText("This");

    // 向 FormattedText 添加新文本行
    $text->addNewLineText("is sample");
    $text->addNewLineText("Center Aligned");
    $text->addNewLineText("TextStamp");
    $text->addNewLineText("Object");
    
    // 创建文本印章
    $textStamp = new TextStamp($text);

    // 将文本印章的水平对齐方式指定为居中对齐
    $textStamp->setHorizontalAlignment((new HorizontalAlignment)->getCenter());
    // 将文本印章的垂直对齐方式指定为居中对齐
    $textStamp->setVerticalAlignment((new VerticalAlignment())->getCenter);
    // 将 TextStamp 的文本水平对齐方式指定为居中对齐
    $textStamp->setTextAlignment((new HorizontalAlignment)->getCenter());
    // 设置印章对象的上边距
    $textStamp->setTopMargin(20);
    
    // 将印章添加到特定页面
    $pages->get_Item(1)->addStamp($textStamp);

    // 保存输出文档
    $document->save($outputFile);
    $document->close();  
```


## 在 PDF 文件中将填充描边文本作为印章

我们已经实现了在文本添加和编辑场景中设置渲染模式。要渲染描边文本，请创建 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) 对象，并将 RenderingMode 设置为 TextRenderingMode.StrokeText，同时为 StrokingColor 属性选择颜色。之后，使用 bindTextState() 方法将 TextState 绑定到印章。

以下代码片段演示了如何添加填充描边文本：

```php

   // 创建 TextState 对象以传输高级属性
    $ts = new TextState();
        
    // 设置描边颜色
    $ts->setStrokingColor((new Color())->getGray());

    // 设置文本渲染模式
    $ts->setRenderingMode(TextRenderingMode::$StrokeText);

    // 加载输入 PDF 文档
    $fileStamp = new PdfFileStamp(new Document($inputFile));

    $stamp = new Stamp();
    $stamp->bindLogo(
        new FormattedText("PAID IN FULL",
            (new Color())->getGray(), "Arial",
            facades_EncodingType::$WinAnsi,
            true, 78));

    // 绑定 TextState
    $stamp->bindTextState($ts);
    
    // 设置 X,Y 原点
    $stamp->setOrigin(100, 100);
    $stamp->setOpacity (5);
    $stamp->setBlendingSpace(BlendingColorSpace::$DeviceRGB);
    $stamp->setRotation (45.0);
    $stamp->setBackground(false);

    // 添加印章
    $fileStamp->addStamp($stamp);
    $fileStamp->save($outputFile);
    $fileStamp->close();
```