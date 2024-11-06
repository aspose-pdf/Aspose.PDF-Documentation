---
title: 从 PDF C# 中提取图像
linktitle: 从 PDF 提取图像
type: docs
weight: 20
url: zh/net/extract-images-from-the-pdf-file/
description: 使用 Aspose.PDF for .NET 在 C# 中从 PDF 提取图像部分
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

图像保存在每个页面的 [Resources](https://reference.aspose.com/pdf/net/aspose.pdf/resources) 集合的 [Images](https://reference.aspose.com/pdf/net/aspose.pdf/resources/properties/images) 集合中。要提取特定页面，然后使用图像的特定索引从 Images 集合中获取图像。

图像索引返回一个 [XImage](https://reference.aspose.com/pdf/net/aspose.pdf/ximage) 对象。该对象提供了一个 Save 方法，可以用来保存提取的图像。以下代码片段显示了如何从 PDF 文件中提取图像。

以下代码片段也适用于 [Aspose.PDF.Drawing](/pdf/net/drawing/) 库。

 ```csharp
 // 完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
 ```

// 有关完整示例和数据文件，请访问 https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// 文档目录的路径。
string dataDir = RunExamples.GetDataDir_AsposePdf_Images();

// 打开文档
Document pdfDocument = new Document(dataDir+ "ExtractImages.pdf");

// 提取特定图片
XImage xImage = pdfDocument.Pages[1].Resources.Images[1];

FileStream outputImage = new FileStream(dataDir + "output.jpg", FileMode.Create);

// 保存输出图片
xImage.Save(outputImage, ImageFormat.Jpeg);
outputImage.Close();

dataDir = dataDir + "ExtractImages_out.pdf";

// 保存更新后的PDF文件
pdfDocument.Save(dataDir);
```

