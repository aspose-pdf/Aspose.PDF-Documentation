---
title: 设置PDF文件信息
type: docs
weight: 40
url: /net/set-pdf-file-information/
description: 本节说明如何使用Aspose.PDF Facades设置PDF文件信息。
lastmod: "2021-06-05"
draft: false
---

[PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 类允许您设置PDF文件的特定信息。您需要创建一个 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 类的对象，然后设置不同的文件特定属性，如作者、标题、关键词和创建者等。最后，使用 [PdfFileInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo) 对象的 [SaveNewInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileinfo/savenewinfo/methods/1) 方法保存更新后的PDF文件。

以下代码片段向您展示如何设置PDF文件信息。

```csharp
 public static void SetPdfInfo()
        {
            PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf")
            {
                // 设置PDF信息
                Author = "Aspose",
                Title = "Hello World!",
                Keywords = "Peace and Development",
                Creator = "Aspose"
            };
            // 保存更新后的文件
            fileInfo.SaveNewInfo(_dataDir + "SetFileInfo_out.pdf");
        }
```

## 设置元信息

[SetMetaInfo](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileinfo/methods/setmetainfo) 方法允许您添加任何信息。在我们的示例中，我们添加了一个字段。请查看下一个代码片段：

```csharp
 public static void SetMetaInfo()
        {
            // 创建 PdfFileInfo 对象的实例
            Aspose.Pdf.Facades.PdfFileInfo fInfo = new Aspose.Pdf.Facades.PdfFileInfo(_dataDir + "sample.pdf");

            // 设置新的客户属性作为元信息
            fInfo.SetMetaInfo("Reviewer", "Aspose.PDF user");

            // 保存更新后的文件
            fInfo.SaveNewInfo(_dataDir + "SetMetaInfo_out.pdf");
```