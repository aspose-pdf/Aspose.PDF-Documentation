---
title: 添加文本和图像印章
type: docs
weight: 20
url: /zh/net/add-text-and-image-stamp/
description: 本节介绍如何使用 Aspose.PDF Facades 中的 PdfFileStamp 类添加文本和图像印章。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件的所有页面上添加文本印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的所有页面上添加文本印章。 为了添加文字印章，首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。 您还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 方法创建文本印章。您还可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，如原点、旋转、背景等。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法将印章添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的所有页面上添加文本印章。

```csharp
 public static void AddTextStampOnAllPagesInPdfFile()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 创建印章
            Stamp stamp = new Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // 将印章添加到 PDF 文件中
            fileStamp.AddStamp(stamp);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "AddTextStamp-All_out.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```
## 在 PDF 文件的特定页面上添加文本印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的特定页面上添加文本印章。 为了添加文本印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。 您还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindLogo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindlogo) 方法来创建文本印章。 你可以设置其他属性，比如origin，rotation，background等。 使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象也是如此。 在您希望在 PDF 文件的特定页面上添加文本印章时，您还需要设置 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 属性。此属性需要一个包含您希望添加印章的页面编号的整数数组。然后，您可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addstamp) 方法在 PDF 文件中添加印章。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的特定页面上添加文本印章。

```csharp
 public static void AddTextStampOnParticularPagesInPdfFile()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 创建印章
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindLogo(new FormattedText("Hello World!", System.Drawing.Color.Blue, System.Drawing.Color.Gray, Aspose.Pdf.Facades.FontStyle.Helvetica, EncodingType.Winansi, true, 14));
            stamp.SetOrigin(10, 400);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // 设置特定页面
            stamp.Pages = new int[] { 2 };

            // 将印章添加到 PDF 文件
            fileStamp.AddStamp(stamp);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "AddTextStamp-Page_out.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```
## 在 PDF 文件的所有页面上添加图像印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的所有页面上添加图像印章。 为了添加图像印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 方法创建图像戳记。你可以使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象设置其他属性，比如起始位置、旋转、背景等。然后，你可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 方法将戳记添加到 PDF 文件中。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的所有页面上添加图像戳记。

```csharp
public static void AddImageStampOnAllPagesInPdfFile()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 创建戳记
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // 设置特定页面
            stamp.Pages = new int[] { 2 };

            // 将戳记添加到 PDF 文件
            fileStamp.AddStamp(stamp);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "AddImageStamp-Page_out.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```
### 控制添加为印章时的图像质量

当将图像添加为印章对象时，您还可以控制图像的质量。为实现此要求，已为 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类添加了 Quality 属性。它表示图像的质量，以百分比表示（有效值为 0..100）。

## 在 PDF 文件的特定页面上添加图像印章

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类允许您在 PDF 文件的特定页面上添加图像印章。 为了添加图像印章，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 和 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的对象。 你还需要使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [BindImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/methods/bindimage/index) 方法创建图像印章。 你可以设置其他属性，如 origin、rotation、background 等。 使用 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 对象也是如此。若要在 PDF 文件的特定页面上添加图像印章，还需要设置 [Stamp](https://reference.aspose.com/pdf/net/aspose.pdf/stamp) 类的 [Pages](https://reference.aspose.com/pdf/net/aspose.pdf.facades/stamp/properties/pages) 属性。此属性需要一个整数数组，其中包含要添加印章的页面编号。然后可以使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [AddStamp](https://reference.aspose.com/pdf/net/aspose.pdf/page/methods/addstamp) 方法在 PDF 文件中添加印章。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出 PDF 文件。以下代码片段展示了如何在 PDF 文件的特定页面上添加图像印章。

```csharp
 public static void AddImageStampOnParticularPagesInPdfFile()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create stamp
            Aspose.Pdf.Facades.Stamp stamp = new Aspose.Pdf.Facades.Stamp();
            stamp.BindImage(_dataDir + "aspose-logo.png");
            stamp.SetOrigin(10, 200);
            stamp.Rotation = 90.0F;
            stamp.IsBackground = true;

            // Add stamp to PDF file
            fileStamp.AddStamp(stamp);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddImageStamp-All_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```