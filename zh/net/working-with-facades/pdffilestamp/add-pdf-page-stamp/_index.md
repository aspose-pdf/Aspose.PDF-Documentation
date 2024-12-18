---
title: 添加PDF页面印章
type: docs
weight: 10
url: /zh/net/add-pdf-page-stamp/
description: 本节解释如何使用PdfFileStamp类与Aspose.PDF Facades协作。
lastmod: "2021-06-05"
draft: false
---

## 在PDF文件的所有页面上添加PDF页面印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在PDF文件的所有页面上添加PDF页面印章。 为了添加PDF页面印章，您首先需要创建[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp)和[Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp)类的对象。 你还需要使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 方法创建 PDF 页面印章。你也可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，如起始位置、旋转、背景等。然后，你可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的所有页面上添加 PDF 页面印章。

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

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的特定页面上添加 PDF 页面印章。 为了添加 PDF 页面印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindPdf](https://reference.aspose.com/pdf/net/aspose.pdf.facades.facade/bindpdf/methods/3) 方法创建 PDF 页面印章。 你可以设置其他属性，比如原点、旋转、背景等。 使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象也是如此。 如您希望在 PDF 文件的特定页面上添加 PDF 页面印章，您还需要设置 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 属性。此属性需要一个包含您希望添加印章的页面编号的整数数组。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示了如何在 PDF 文件的特定页面上添加 PDF 页面印章。

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
            // 添加印章到 PDF 文件
            fileStamp.AddStamp(stamp);

            // 保存更新后的 PDF 文件
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
## 在 PDF 文件中添加页码

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件中添加页码。 为了添加页码，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的对象。 如果您想显示页码，如“第 X 页，共 N 页”，其中 X 是当前页码，N 是 PDF 文件的总页数，那么您首先需要使用 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 类的 [NumberOfpages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/properties/numberofpages) 属性来获取页数。 为了获取当前页码，您可以在文本中任意位置使用 **#** 符号。您可以使用 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类来格式化页码文本。如果您想从特定数字开始页码编号，可以设置 [StartingNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/properties/startingnumber) 属性。当您准备好在文件中添加页码时，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp) 类的 [AddPageNumber](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addpagenumber/methods/7) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示了如何在 PDF 文件中添加页码。

```csharp
 public static void AddPageNumberInPdfFile()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 获取总页数
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // 为页码创建格式化文本
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // 设置第一页的起始编号；您可能希望从 2 或更大的数字开始
            fileStamp.StartingNumber = 1;

            // 添加页码
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```
### 自定义编号样式

PdfFileStamp 类提供了在 PDF 文档内添加页码信息作为印章对象的功能。在此版本之前，该类仅支持 1,2,3,4 作为页码样式。然而，一些客户需要在 PDF 文档内放置页码印章时使用自定义编号样式。为了满足这一要求，引入了 [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) 属性，该属性接受来自 [NumberingStyle](https://reference.aspose.com/pdf/net/aspose.pdf/numberingstyle) 枚举的值。以下是该枚举中提供的值。

- LettersLowercase
- LettersUppercase
- NumeralsArabic
- NumeralsRomanLowercase
- NumeralsRomanUppercase

```csharp
 public static void AddCustomPageNumberInPdfFile()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 获取总页数
            int totalPages = new PdfFileInfo(_dataDir + "sample.pdf").NumberOfPages;

            // 为页码创建格式化文本
            FormattedText formattedText = new FormattedText($"Page # of {totalPages}",
                System.Drawing.Color.AntiqueWhite,
                System.Drawing.Color.Gray,
                FontStyle.TimesBoldItalic,
                EncodingType.Winansi, false, 12);

            // 指定编号样式为罗马数字大写
            fileStamp.NumberingStyle = Aspose.Pdf.NumberingStyle.NumeralsRomanUppercase;

            // 设置第一页的起始编号；您可能希望从 2 或更多开始
            fileStamp.StartingNumber = 1;

            // 添加页码
            fileStamp.AddPageNumber(formattedText, (int)PageNumPosition.PosUpperRight);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "AddPageNumber_out.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```