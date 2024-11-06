---
title: 添加 PDF 页面印章
type: docs
weight: 10
url: zh/java/add-pdf-page-stamp/
description: 本节解释了如何使用 PdfFileStamp 类与 Aspose.PDF Facades 一起工作。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件的所有页面上添加 PDF 页面印章

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的所有页面上添加 PDF 页面印章。
 In order to add PDF page stamp, you first need to create objects of [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) and [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) classes.

为了添加 PDF 页面印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 和 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的对象。 您还需要使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 方法来创建 PDF 页面印章。您可以使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 对象设置其他属性，如位置、旋转、背景等。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的所有页面上添加 PDF 页面印章。

```csharp
public static void AddPageStampOnAllPages()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 创建印章
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // 将印章添加到 PDF 文件
            fileStamp.AddStamp(stamp);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```

## 在 PDF 文件的特定页面上添加 PDF 页面印章

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件的特定页面上添加 PDF 页面印章。
 为了添加 PDF 页面印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 和 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 类的 [bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#bindPdf-java.lang.String-int-) 方法创建 PDF 页面印章。 你可以设置其他属性，比如起始点、旋转、背景等。 使用 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 对象也是如此。 如需在 PDF 文件的特定页面上添加 PDF 页面印章，还需要设置 [Stamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp#setPages-int:A-) 类的 [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/Stamp) 属性。此属性需要一个包含要添加印章的页面号码的整数数组。然后，可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#addStamp-com.aspose.pdf.facades.Stamp-) 类的 [addStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 方法在 PDF 文件中添加印章。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp#close--) 类的 [close](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 方法保存输出 PDF 文件。下面的代码片段展示了如何在 PDF 文件的特定页面上添加 PDF 页面印章。

```csharp
public static void AddPageStampOnCertainPages()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 创建印章
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindPdf(_dataDir + "pagestamp.pdf", 1);
            stamp.SetOrigin(20, 20);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;
            stamp.Pages = new[] { 1, 3 };
            // 将印章添加到 PDF 文件
            fileStamp.AddStamp(stamp);

            // 保存更新的 PDF 文件
            fileStamp.Save(_dataDir + "PageStampOnAllPages.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }

        // 添加 PDF 页码
        public enum PageNumPosition
        {
            PosBottomMiddle, PosBottomRight, PosUpperRight, PosSidesRight, PosUpperMiddle, PosBottomLeft, PosSidesLeft, PosUpperLeft
        }
```

## 在 PDF 文件中添加页码 (facades)

[PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类允许您在 PDF 文件中添加页码。
 为了添加页码，您首先需要创建一个 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的对象。 如果您想显示页码为“第 X 页，共 N 页”，其中 X 是当前页码，N 是 PDF 文件的总页数，那么首先需要使用 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 类的 getNumberOfpages 属性获取页数。为了获取当前页码，您可以在文本中任何地方使用 **#** 符号。您可以使用 [FormattedText](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormattedText) 类格式化页码文本。如果您想从特定编号开始页码，可以设置 setStartingNumber 属性。当您准备好在文件中添加页码时，需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 addPageNumber 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类的 Save 方法保存输出的 PDF 文件。

以下代码片段向您展示了如何在 PDF 文件中添加页码。
```java
 public static void AddPageNumberInPdfFile() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 获取总页数
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // 为页码创建格式化文本
        FormattedText formattedText = new FormattedText("第 # 页 共 " + totalPages + " 页", java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // 设置第一页的起始编号；您可能希望从 2 或更多开始
        fileStamp.setStartingNumber(1);

        // 添加页码
        fileStamp.addPageNumber(formattedText, (int) PageNumPosition.PosUpperRight.ordinal());

        // 保存更新的 PDF 文件
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```


### 自定义编号样式

The [PdfFileStamp](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileStamp) 类提供了在 PDF 文档中添加页码信息作为印章对象的功能。在此版本之前，该类仅支持 1,2,3,4 作为页码样式。然而，一些客户要求在 PDF 文档中放置页码印章时使用自定义编号样式。为了满足这一需求，引入了 [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) 属性，该属性接受来自 [NumberingStyle](https://reference.aspose.com/pdf/java/com.aspose.pdf/numberingstyle) 枚举的值。该枚举中提供的值如下所示。

```java
 public static void AddCustomPageNumberInPdfFile() {
        // 创建 PdfFileStamp 对象
        PdfFileStamp fileStamp = new PdfFileStamp();

        // 打开文档
        fileStamp.bindPdf(_dataDir + "sample.pdf");

        // 获取总页数
        int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").getNumberOfPages();

        // 为页码创建格式化文本
        FormattedText formattedText = new FormattedText("Page # of " + totalPages, java.awt.Color.WHITE,
                java.awt.Color.GRAY, FontStyle.TimesBoldItalic, EncodingType.Winansi, false, 12);

        // 指定编号样式为罗马数字大写
        fileStamp.setNumberingStyle(NumberingStyle.NumeralsRomanUppercase);

        // 设置第一页的起始编号；您可能希望从 2 或更多开始
        fileStamp.setStartingNumber(1);

        // 添加页码
        fileStamp.addPageNumber(formattedText, PageNumPosition.PosUpperRight.ordinal());

        // 保存更新后的 PDF 文件
        fileStamp.save(_dataDir + "AddPageNumber_out.pdf");

        // 关闭 fileStamp
        fileStamp.close();
    }
```