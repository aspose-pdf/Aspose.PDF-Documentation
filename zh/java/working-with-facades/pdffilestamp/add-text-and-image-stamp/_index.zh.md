---
title: 添加文本和图像印章
type: docs
weight: 20
url: /java/add-text-and-image-stamp/
description: 本节解释如何使用 PdfFileStamp 类在 com.aspose.pdf.facades 中添加文本和图像印章。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件的所有页面上添加文本印章

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的所有页面上添加文本印章。
 为了添加文本印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 和 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 BindLogo 方法来创建文本印章。你可以使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 对象设置其他属性，如起始点、旋转、背景等。然后，你可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的所有页面上添加文本印章。

```java
 public static void AddTextStampOnAllPagesInPdfFile() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 创建印章
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 将印章添加到 PDF 文件中
        fileStamp.addStamp(stamp);

        // 保存更新后的 PDF 文件
        fileStamp.save(_dataDir + "AddTextStamp-All_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```

## 在 PDF 文件的特定页面添加文本印章

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的特定页面上添加文本印章。
 为了添加文本印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 和 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 方法创建文本印章。 You can set other attributes like origin, rotation, background etc.  
您可以设置其他属性，如原点、旋转、背景等。 使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 对象也是如此。 当你想在PDF文件的特定页面上添加文字印章时，你还需要设置 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) 属性。这个属性需要一个包含你想添加印章的页面号码的整数数组。然后，你可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 方法在PDF文件中添加印章。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的PDF文件。下面的代码片段展示了如何在PDF文件的特定页面上添加文字印章。

```java
 public static void AddTextStampOnParticularPagesInPdfFile() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 创建印章
        Stamp stamp = new Stamp();
        stamp.bindLogo(new FormattedText("Hello World!", java.awt.Color.BLUE, java.awt.Color.GRAY, FontStyle.Helvetica,
                EncodingType.Winansi, true, 14));
        stamp.setOrigin(10, 400);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 设置特定页面
        stamp.setPages(new int[] { 2 });

        // 将印章添加到PDF文件
        fileStamp.addStamp(stamp);

        // 保存更新后的PDF文件
        fileStamp.save(_dataDir + "AddTextStamp-Page_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```

## 在 PDF 文件的所有页面上添加图像印记

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的所有页面上添加图像印记。
 为了添加图像印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 和 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 方法创建图像印章。你可以使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 对象设置其他属性，如起点、旋转、背景等。然后，你可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的所有页面上添加图像印章。

```java
public static void AddImageStampOnParticularPagesInPdfFile() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 创建印章
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 将印章添加到 PDF 文件
        fileStamp.addStamp(stamp);

        // 保存更新的 PDF 文件
        fileStamp.save(_dataDir + "AddImageStamp-All_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```

### 控制作为印章添加时的图像质量

在将图像作为印章对象添加时，您还可以控制图像的质量。为了实现这一要求，[Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类增加了 Quality 属性。它表示图像的质量百分比（有效值为0..100）。

## 在 PDF 文件的特定页面上添加图像印章

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的特定页面上添加图像印章。
 为了添加图像印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 和 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 方法来创建图像印章。 你可以设置其他属性，比如原点、旋转、背景等。 using [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 对象也是如此。 当你想在 PDF 文件的特定页面上添加图像印章时，你还需要设置 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) 属性。这个属性需要一个包含你想要添加印章的页面编号的整数数组。然后，你可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 方法在 PDF 文件中添加印章。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的特定页面上添加图像印章。

```java
  public static void AddImageStampOnAllPagesInPdfFile() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 创建印章
        Stamp stamp = new Stamp();
        stamp.bindImage(_dataDir + "aspose-logo.png");
        stamp.setOrigin(10, 200);
        stamp.setRotation(90.0F);
        stamp.setBackground(true);

        // 设置特定页面
        stamp.setPages(new int[] { 2 });

        // 将印章添加到 PDF 文件
        fileStamp.addStamp(stamp);

        // 保存更新的 PDF 文件
        fileStamp.save(_dataDir + "AddImageStamp-Page_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```