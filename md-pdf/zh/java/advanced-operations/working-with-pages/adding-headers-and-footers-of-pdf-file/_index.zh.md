---
title: 添加 PDF 页眉和页脚
linktitle: 添加页眉和页脚
type: docs
weight: 70
url: /java/add-headers-and-footers-of-pdf-file/
description: Aspose.PDF for Java 允许您使用 TextStamp 类向 PDF 文件添加页眉和页脚。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

PDF 印章通常用于合同、报告和机密材料，以证明文件已被审阅并标记为“已读”、“合格”或“机密”等。本文将向您展示如何使用 **Aspose.PDF for Java** 向 PDF 文档添加图像印章和文字印章。

如果逐行阅读上面的代码片段，您必须会发现语法和代码逻辑非常易于理解。

## 在 PDF 文件的页眉中添加文字

您可以使用 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 类在 PDF 文件的页眉中添加文字。
 TextStamp 类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加文本，您需要创建一个 Document 对象和一个使用所需属性的 TextStamp 对象。之后，您可以调用 Page 的 AddStamp 方法将文本添加到 PDF 的页眉中。

您需要设置 TopMargin 属性，以便它调整 PDF 页眉区域中的文本。您还需要将 HorizontalAlignment 设置为 Center 和 VerticalAlignment 设置为 Top。

以下代码片段展示了如何使用 Java 在 PDF 文件的页眉中添加文本。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.*;

public class ExampleAddPDFHeaderandFooter {
    // 文档目录的路径。
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void AddingTextInHeaderOfPDFFile() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "TextinHeader.pdf");

        // 创建页眉
        TextStamp textStamp = new TextStamp("Header Text");

        // 设置印章的属性
        textStamp.setTopMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Top);

        // 在所有页面上添加页眉
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }

        // 保存更新后的文档
        pdfDocument.save(_dataDir + "TextinHeader_out.pdf");
    }
```

## 在 PDF 文件的页脚添加文本

您可以使用 TextStamp 类在 PDF 文件的页脚添加文本。TextStamp 类提供了创建基于文本的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页脚添加文本，您需要使用所需属性创建一个 Document 对象和一个 TextStamp 对象。之后，您可以调用 Page 的 AddStamp 方法在 PDF 的页脚添加文本。

以下代码片段向您展示了如何使用 Java 在 PDF 文件的页脚添加文本。

```java
    public static void AddingTextInFooterOfPDFFile() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "TextinFooter.pdf");
        // 创建页脚
        TextStamp textStamp = new TextStamp("Footer Text");
        // 设置印章的属性
        textStamp.setBottomMargin(10);
        textStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        textStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // 在所有页面上添加页脚
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(textStamp);
        }
        _dataDir = _dataDir + "TextinFooter_out.pdf";
        // 保存更新的 PDF 文件
        pdfDocument.save(_dataDir);
    }
```


## 在 PDF 文件的页眉中添加图像

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/imagestamp) 类在 PDF 文件的页眉中添加图像。Image Stamp 类提供了创建基于图像的印章所需的属性，如字体大小、字体样式和字体颜色等。为了在页眉中添加图像，您需要使用所需的属性创建一个 Document 对象和一个 Image Stamp 对象。之后，您可以调用 Page 的 [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) 方法将图像添加到 PDF 的页眉中。

```java
public static void AddingImageInHeaderOfPDFFile() {

// 打开文档
Document pdfDocument = new Document(_dataDir + "ImageInHeader.pdf");

// 创建页眉
ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

// 设置印章的属性
imageStamp.setTopMargin(10);
imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
imageStamp.setVerticalAlignment(VerticalAlignment.Top);
// 在所有页面上添加页眉
for (Page page : pdfDocument.getPages()) {
page.addStamp(imageStamp);
}

_dataDir = _dataDir + "ImageInHeader_out.pdf";

// 保存更新后的 PDF 文件
pdfDocument.save(_dataDir);
}
```


以下代码片段演示了如何使用 Java 在 PDF 文件的页眉中添加图像。

## 在 PDF 文件的页脚中添加图像

您可以使用 Image Stamp 类在 PDF 文件的页脚中添加图像。Image Stamp 类提供了创建基于图像的印章所需的属性，例如字体大小、字体样式和字体颜色等。为了在页脚中添加图像，您需要使用所需属性创建一个 Document 对象和一个 Image Stamp 对象。之后，您可以调用 Page 的 AddStamp 方法将图像添加到 PDF 的页脚中。

{{% alert color="primary" %}}

您需要设置 BottomMargin 属性，以便在 PDF 的页脚区域调整图像。您还需要将 [HorizontalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/HorizontalAlignment) 设置为 `Center` 和 [VerticalAlignment](https://reference.aspose.com/pdf/java/com.aspose.pdf/VerticalAlignment) 设置为 `Bottom`。

{{% /alert %}}

以下代码片段演示了如何使用 Java 在 PDF 文件的页脚中添加图像。

```java
    public static void AddingImageInFooterOfPDFFile() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "ImageInFooter.pdf");

        // 创建页脚
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.jpg");

        // 设置图章的属性
        imageStamp.setBottomMargin(10);
        imageStamp.setHorizontalAlignment(HorizontalAlignment.Center);
        imageStamp.setVerticalAlignment(VerticalAlignment.Bottom);
        // 在所有页面上添加页脚
        for (Page page : pdfDocument.getPages()) {
            page.addStamp(imageStamp);
        }

        _dataDir = _dataDir + "ImageInFooter_out.pdf";

        // 保存更新后的 PDF 文件
        pdfDocument.save(_dataDir);
    }
```

## 在一个 PDF 文件中添加不同的页眉

我们知道可以通过使用 TopMargin 或 Bottom Margin 属性在文档的页眉/页脚部分添加 TextStamp，但有时我们可能需要在单个 PDF 文档中添加多个页眉/页脚。
 **Aspose.PDF for Java** 解释了如何实现这一点。

为了满足这一要求，我们将创建单独的 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象（对象的数量取决于所需的页眉/页脚数量）并将它们添加到 PDF 文档中。我们还可以为单个印章对象指定不同的格式信息。在以下示例中，我们创建了一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和三个 [TextStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextStamp) 对象，然后我们使用 Page 的 [AddStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/class-use/Stamp) 方法将文本添加到 PDF 的页眉部分。以下代码片段向您展示了如何使用 Aspose.PDF for Java 将图像添加到 PDF 文件的页脚中。

```java
public static void AddingDifferentHeadersInOnePDFFile() {

        // 打开源文档
        Document pdfDocument = new Document(_dataDir + "AddingDifferentHeaders.pdf");

        // 创建三个印章
        TextStamp stamp1 = new TextStamp("Header 1");
        TextStamp stamp2 = new TextStamp("Header 2");
        TextStamp stamp3 = new TextStamp("Header 3");

        // 设置印章对齐方式（将印章放在页面顶部，水平居中）
        stamp1.setVerticalAlignment (VerticalAlignment.Top);
        stamp1.setHorizontalAlignment(HorizontalAlignment.Center);
        // 指定字体样式为粗体
        stamp1.getTextState().setFontStyle(FontStyles.Bold);
        // 设置文本前景色信息为红色
        stamp1.getTextState().setForegroundColor(Color.getRed());
        // 指定字体大小为14
        stamp1.getTextState().setFontSize(14);

        // 现在我们需要将第二个印章对象的垂直对齐方式设置为顶部
        stamp2.setVerticalAlignment(VerticalAlignment.Top);
        // 设置印章的水平对齐信息为居中对齐
        stamp2.setHorizontalAlignment(HorizontalAlignment.Center);
        // 设置印章对象的缩放因子
        stamp2.setZoom (10);

        // 设置第三个印章对象的格式
        // 指定印章对象的垂直对齐信息为顶部
        stamp3.setVerticalAlignment(VerticalAlignment.Top);
        // 设置印章对象的水平对齐信息为居中对齐
        stamp3.setHorizontalAlignment (HorizontalAlignment.Center);
        // 设置印章对象的旋转角度
        stamp3.setRotateAngle(35);
        // 设置粉色为印章的背景色
        stamp3.getTextState().setBackgroundColor (Color.getPink());
        
        // 将印章的字体信息更改为 Verdana
        stamp3.getTextState().setFont (FontRepository.findFont("Verdana"));
        // 第一个印章添加到第一页；
        pdfDocument.getPages().get_Item(1).addStamp(stamp1);
        // 第二个印章添加到第二页；
        pdfDocument.getPages().get_Item(2).addStamp(stamp2);
        // 第三个印章添加到第三页。
        pdfDocument.getPages().get_Item(3).addStamp(stamp3);

        _dataDir = _dataDir + "multiheader_out.pdf";

        // 保存更新后的 PDF 文件
        pdfDocument.save(_dataDir);
    }

}
```