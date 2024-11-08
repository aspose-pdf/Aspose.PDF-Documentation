---
title: 在PDF中以编程方式添加图片水印
linktitle: PDF文件中的图片水印
type: docs
weight: 10
url: /zh/java/image-stamps-in-pdf-page/
description: 使用Aspose.PDF for Java库中的ImageStamp类在PDF文档中添加图片水印。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 在PDF文件中添加图片水印

您可以使用 [ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类在PDF文档中添加图片作为水印。[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类提供了指定高度、宽度和透明度等的方法。

要添加图片水印：

1. 使用所需属性创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象和一个 ImageStamp 对象。

1. 调用 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page) 类的 [addStamp(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page#addStamp-com.aspose.pdf.Stamp-) 方法将印章添加到 PDF 中。

以下代码片段展示了如何在 PDF 文件中添加图片印章。

```java
public static void AddImageStampInPDFFile() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // 创建图片印章
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setBackground(true);
        imageStamp.setXIndent(100);
        imageStamp.setYIndent(100);
        imageStamp.setHeight(48);
        imageStamp.setWidth(225);
        imageStamp.setRotate(Rotation.on270);
        imageStamp.setOpacity(0.5);

        // 将印章添加到特定页面
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        // 保存输出文档
        pdfDocument.save(_dataDir + "AddImageStamp_out.pdf");

    }
```


## 控制添加印章时的图像质量

[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类允许您在 PDF 文档中添加图像作为印章。它还允许您在将图像作为水印添加到 PDF 文件时控制图像质量。为此，[ImageStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/ImageStamp) 类中添加了一个名为 setQuality(...) 的方法。在 com.aspose.pdf.facades 包的 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf/Stamp) 类中也可以找到类似的方法。

以下代码片段演示了如何在 PDF 文件中添加印章时控制图像质量。

```java
 public static void ControlImageQualityWhenAddingStamp() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "AddImageStamp.pdf");

        // 创建图像印章
        ImageStamp imageStamp = new ImageStamp(_dataDir + "aspose-logo.png");
        imageStamp.setQuality(10);
        pdfDocument.getPages().get_Item(1).addStamp(imageStamp);

        pdfDocument.save(_dataDir + "ControlImageQuality_out.pdf");
    }
```


## 将图像印章作为浮动框中的背景

Aspose.PDF API 允许您在浮动框中添加图像印章作为背景。FloatingBox 类的 BackgroundImage 属性可用于为浮动框设置背景图像印章，如以下代码示例所示。

```java
public static void ImageStampAsBackgroundInFloatingBox() {
        // 实例化 Document 对象
        Document doc = new Document();
        // 向 PDF 文档添加页面
        Page page = doc.getPages().add();

        // 创建 FloatingBox 对象
        FloatingBox aBox = new FloatingBox(200, 100);

        // 设置 FloatingBox 的左位置
        aBox.setLeft(40);
        // 设置 FloatingBox 的顶部位置
        aBox.setTop(80);
        // 设置 FloatingBox 的水平对齐方式
        aBox.setHorizontalAlignment(HorizontalAlignment.Center);
        // 向 FloatingBox 的段落集合中添加文本片段
        aBox.getParagraphs().add(new TextFragment("main text"));
        // 设置 FloatingBox 的边框
        aBox.setBorder(new BorderInfo(BorderSide.All, Color.getRed()));

        // 添加背景图像
        Image img = new Image();
        img.setFile(_dataDir + "aspose-logo.png");
        aBox.setBackgroundImage(img);

        // 设置 FloatingBox 的背景颜色
        aBox.setBackgroundColor(Color.getYellow());

        // 将 FloatingBox 添加到页面对象的段落集合中
        page.getParagraphs().add(aBox);
        // 保存 PDF 文档
        doc.save(_dataDir + "AddImageStampAsBackgroundInFloatingBox_out.pdf");
    }
}
```