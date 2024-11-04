---
title: 在PDF中以编程方式添加文字印章
linktitle: 在PDF文件中添加文字印章
type: docs
weight: 20
url: /java/text-stamps-in-the-pdf-file/
description: 使用TextStamp类通过Java向PDF文件添加文字印章。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 使用Java添加文字印章

Aspose.PDF for Java提供了[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp)类，以便在PDF文件中添加文字印章。
 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类提供了必要的方法来指定印章对象的字体大小、字体样式和字体颜色等。为了添加文本印章，首先需要使用所需的方法创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和一个 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象。之后，可以调用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类的 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 方法在 PDF 文档中添加印章。

以下代码片段展示了如何在 PDF 文件中添加文本印章。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;
import com.aspose.pdf.facades.*;
import com.aspose.pdf.facades.Stamp;

public class ExampleStampingImage {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddTextStamp() {
        // 打开文档
        Document pdfDocument = new Document("input.pdf");
        // 创建文本印章
        TextStamp textStamp = new TextStamp("Sample Stamp");
        // 设置印章是否为背景
        textStamp.setBackground(true);
        // 设置起始位置
        textStamp.setXIndent(100);
        textStamp.setYIndent(100);
        // 旋转印章
        textStamp.setRotate(Rotation.on90);
        // 设置文本属性
        textStamp.getTextState().setFont(FontRepository.findFont("Arial"));
        textStamp.getTextState().setFontSize(14.0F);
        textStamp.getTextState().setFontStyle(FontStyles.Bold);
        textStamp.getTextState().setFontStyle(FontStyles.Italic);
        textStamp.getTextState().setForegroundColor(Color.getGreen());
        // 将印章添加到特定页面
        pdfDocument.getPages().get_Item(1).addStamp(textStamp);
        // 保存输出文档
        pdfDocument.save("TextStamp_output.pdf");
    }
```

## 定义 TextStamp 对象的对齐方式

为 PDF 文档添加水印是一个经常被需求的功能，而 Aspose.PDF for Java 完全能够添加图像和文本水印。[TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类提供了在 PDF 文件上添加文本水印的功能。最近有一个需求是支持在使用 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象时指定文本对齐方式。因此，为了满足这一需求，我们在 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类中引入了 setTextAlignment(..) 方法。通过使用此方法，您可以指定水平文本对齐方式。

以下代码片段展示了如何加载现有 PDF 文档并在其上添加 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 的示例。

```java
    public static void DefineAlignmentTextStamp() {
        // 用输入文件实例化 Document 对象
        Document pdfDocument = new Document("input.pdf");
        // 用示例字符串实例化 FormattedText 对象
        FormattedText text = new FormattedText("This");
        
        // 向 FormattedText 添加新文本行
        text.addNewLineText("is sample");
        text.addNewLineText("Center Aligned");
        text.addNewLineText("TextStamp");
        text.addNewLineText("Object");
        // 使用 FormattedText 创建 TextStamp 对象
        TextStamp stamp = new TextStamp(text);
        // 指定文本水印的水平对齐为居中对齐
        stamp.setHorizontalAlignment(HorizontalAlignment.Center);
        // 指定文本水印的垂直对齐为居中对齐
        stamp.setVerticalAlignment(VerticalAlignment.Center);
        // 指定 TextStamp 的文本水平对齐为居中对齐
        stamp.setTextAlignment(HorizontalAlignment.Center);
        // 设置水印对象的上边距
        stamp.setTopMargin(20);
        // 将水印添加到 PDF 文件的所有页面
        pdfDocument.getPages().get_Item(1).addStamp(stamp);
        
        // 保存输出文档
        pdfDocument.save("TextStamp_output.pdf");
    }
```


## 在 PDF 文件中填充描边文本作为印章

我们已经实现了在文本添加和编辑场景中设置渲染模式的功能。要渲染描边文本，请创建 [TextState](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextState) 对象，并将 RenderingMode 设置为 TextRenderingMode.StrokeText，同时为 StrokingColor 属性选择颜色。之后，使用 BindTextState() 方法将 TextState 绑定到印章。

以下代码片段演示了如何添加填充描边文本：

```java
   public static void FillStrokeTextAsStampInPDFFile(){
        // 创建 TextState 对象以传输高级属性
        TextState ts = new TextState();
        
        // 为描边设置颜色
        ts.setStrokingColor(Color.getGray());
        
        // 设置文本渲染模式
        ts.setRenderingMode (TextRenderingMode.StrokeText);
        
        // 加载输入 PDF 文档
        PdfFileStamp fileStamp = new PdfFileStamp(new Document(_dataDir + "input.pdf"));

        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("PAID IN FULL", java.awt.Color.GRAY, "Arial", EncodingType.Winansi, true, 78));

        // 绑定 TextState
        stamp.bindTextState(ts);
        // 设置 X,Y 原点
        stamp.setOrigin(100, 100);
        stamp.setOpacity (5);
        stamp.setBlendingSpace (BlendingColorSpace.DeviceRGB);
        stamp.setRotation (45.0F);
        stamp.setBackground(false);
        // 添加印章
        fileStamp.addStamp(stamp);
        fileStamp.save(_dataDir + "ouput_out.pdf");
        fileStamp.close();
    }
```