---
title: 管理页眉和页脚
type: docs
weight: 40
url: /java/manage-header-and-footer/
description: 本节介绍如何使用 Aspose.PDF Facades 和 PdfFileStamp 类管理页眉和页脚。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件中添加页眉

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件中添加页眉。
 为了添加页眉，首先需要创建一个 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的对象。 您可以使用 [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 类来格式化标题文本。当您准备好在文件中添加标题时，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 方法。您还需要在 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 方法中至少指定上边距。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段演示了如何在 PDF 文件中添加标题。

```java
public static void AddHeader() {
    // 创建 PdfFileStamp 对象
    PdfFileStamp fileStamp = new PdfFileStamp();

    // 打开文档
    fileStamp.bindPdf(_dataDir + "sample.pdf");

    // 创建格式化文本用于页码
    FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.YELLOW,
            java.awt.Color.BLACK, FontStyle.Courier, EncodingType.Winansi, false, 14);

    // 添加标题
    fileStamp.addHeader(formattedText, 20);

    // 保存更新后的 PDF 文件
    fileStamp.save(_dataDir + "AddHeader_out.pdf");

    // 关闭 fileStamp
    fileStamp.close();
}
```

## 在 PDF 文件中添加页脚

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件中添加页脚。
 为了添加页脚，您首先需要创建一个 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的对象。 您可以使用 [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 类格式化页脚文本。准备好在文件中添加页脚后，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 方法。您还需要在 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 方法中至少指定底部边距。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades.PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件中添加页脚。

```java
 public static void AddFooter() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 为页码创建格式化文本
        FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!", java.awt.Color.BLUE,
                java.awt.Color.GRAY, FontStyle.Courier, EncodingType.Winansi, false, 14);

        // 添加页脚
        fileStamp.addFooter(formattedText, 10);

        // 保存更新后的 PDF 文件
        fileStamp.save(_dataDir + "AddFooter_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```

## 在现有 PDF 文件的页眉中添加图像

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的页眉中添加图像。
 为了在页眉中添加图像，首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的对象。之后，需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 方法。您可以将图像传递给 [addHeader](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addHeader-com.aspose.pdf.facades.FormattedText-float-) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码段向您展示如何在 PDF 文件的页眉中添加图像。

```java
public static void AddImageHeader() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // 添加页眉
            fileStamp.addHeader(fs, 10);

            // 保存更新的 PDF 文件
            fileStamp.save(_dataDir + "AddImage-Header_out.pdf");
        } catch (FileNotFoundException e) {

            e.printStackTrace();
        }

        // 关闭 fileStamp
        fileStamp.close();
    }
```

## 在现有 PDF 文件的页脚中添加图像

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的页脚中添加图像。
 为了在页脚中添加图像，首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的对象。之后，需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 方法。可以将图像传递给 [addFooter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addFooter-com.aspose.pdf.facades.FormattedText-float-) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段演示了如何在 PDF 文件的页脚中添加图像。

```java
    public static void AddImageFooter() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");
        FileInputStream fs;
        try {
            fs = new FileInputStream(_dataDir + "aspose-logo.png");
            // 添加页脚
            fileStamp.addFooter(fs, 10);

            // 保存更新后的 PDF 文件
            fileStamp.save(_dataDir + "AddImage-Footer_out.pdf");
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }

        // 关闭 fileStamp
        fileStamp.close();
    }
```