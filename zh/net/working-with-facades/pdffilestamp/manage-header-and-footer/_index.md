---
title: 管理页眉和页脚
type: docs
weight: 40
url: /zh/net/manage-header-and-footer/
description: 本节解释如何使用 Aspose.PDF Facades 的 PdfFileStamp 类管理页眉和页脚。
lastmod: "2021-06-05"
draft: false
---

## 在 PDF 文件中添加页眉

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件中添加页眉。 为了添加页眉，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。 你可以使用 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类来格式化标题文本。准备好在文件中添加标题后，你需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) 类的 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法。你还需要在 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法中至少指定顶部边距。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件中添加标题。

```csharp
 public static void AddHeader()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // 为页码创建格式化文本
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Yellow,
                System.Drawing.Color.Black,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // 添加标题
            fileStamp.AddHeader(formattedText, 10);

            // 保存更新后的 PDF 文件
            fileStamp.Save(_dataDir + "AddHeader_out.pdf");

            // 关闭 fileStamp
            fileStamp.Close();
        }
```
## 在 PDF 文件中添加页脚

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件中添加页脚。 为添加页脚，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。 您可以使用 [FormattedText](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formattedtext) 类来格式化页脚文本。一旦您准备好在文件中添加页脚，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法。您还需要在 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法中至少指定底部边距。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出 PDF 文件。以下代码片段展示了如何在 PDF 文件中添加页脚。

```csharp
 public static void AddFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");

            // Create formatted text for page number
            FormattedText formattedText = new FormattedText("Aspose - Your File Format Experts!",
                System.Drawing.Color.Blue,
                System.Drawing.Color.Gray,
                FontStyle.Courier,
                EncodingType.Winansi, false, 14);

            // Add footer
            fileStamp.AddFooter(formattedText, 10);

            // Save updated PDF file
            fileStamp.Save(_dataDir + "AddFooter_out.pdf");

            // Close fileStamp
            fileStamp.Close();
        }
```
## 在现有 PDF 文件的页眉中添加图像

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件的页眉中添加图像。 为了在页眉中添加图像，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。之后，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/constructors/main) 类的 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法。您可以将图像传递给 [AddHeader](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffilestamp/addheader/methods/4) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段展示了如何在 PDF 文件的页眉中添加图像。

```csharp
public static void AddImageHeader()
        {
            // 创建 PdfFileStamp 对象
            PdfFileStamp fileStamp = new PdfFileStamp();

            // 打开文档
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // 添加页眉
                fileStamp.AddHeader(fs, 10);

                // 保存更新后的 PDF 文件
                fileStamp.Save(_dataDir + "AddImage-Header_out.pdf");
                // 关闭 fileStamp
                fileStamp.Close();
            }
        }
```
## 在现有 PDF 文件的页脚中添加图像

[PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类允许您在 PDF 文件的页脚中添加图像。 为了在页脚添加图像，您首先需要创建 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的对象。之后，您需要调用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法。您可以将图像传递给 [AddFooter](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/methods/addfooter/index) 方法。最后，使用 [PdfFileStamp](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffilestamp/constructors/main) 类的 [Close](https://reference.aspose.com/pdf/net/aspose.pdf.facades/facade/methods/close) 方法保存输出的 PDF 文件。以下代码片段向您展示了如何在 PDF 文件的页脚中添加图像。

```csharp
public static void AddImageFooter()
        {
            // Create PdfFileStamp object
            PdfFileStamp fileStamp = new PdfFileStamp();

            // Open Document
            fileStamp.BindPdf(_dataDir + "sample.pdf");
            using (var fs = new FileStream(_dataDir + "aspose-logo.png", FileMode.Open))
            {
                // Add footer
                fileStamp.AddFooter(fs, 10);

                // Save updated PDF file
                fileStamp.Save(_dataDir + "AddImage-Footer_out.pdf");

                // Close fileStamp
                fileStamp.Close();
            }
        }
```