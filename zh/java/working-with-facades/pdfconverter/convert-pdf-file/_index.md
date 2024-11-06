---
title: 转换PDF文件
type: docs
weight: 20
url: zh/java/convert-pdf-file/
description: 本节解释如何使用PdfConverter类通过Aspose.PDF Facades转换PDF文件。
lastmod: "2021-06-05"
draft: false
---

## 将PDF页面转换为不同的图像格式 (Facades)

为了将PDF页面转换为不同的图像格式，您需要创建一个[PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter)对象，并使用[bindPdf](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#bindPdf-java.lang.String-)方法打开PDF文件。

之后，您需要调用[doConvert](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#doConvert--)方法进行初始化任务。
 然后，您可以使用 [hasNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#hasNextImage--) 和 [getNextImage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#getNextImage-java.io.OutputStream-) 方法遍历所有页面。getNextImage 方法允许您创建特定页面的图像。您还需要将 ImageType 传递给此方法，以便创建特定类型的图像，例如 JPEG、GIF 或 PNG 等。

最后，调用 [PdfConverter](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter) 类的 close 方法。

以下代码片段向您展示了如何将 PDF 页面转换为图像。

```java
public static void ConvertPdfPagesToImages01() {
        // 创建 PdfConverter 对象
        PdfConverter converter = new PdfConverter();

        // 绑定输入 pdf 文件
        converter.bindPdf(_dataDir + "Sample-Document-01.pdf");

        // 初始化转换过程
        converter.doConvert();
        
        int count=0;

        // 检查页面是否存在，然后一个一个地转换为图像
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // 关闭 PdfConverter 对象
        converter.close();
    }
```

在下一个代码片段中，我们将展示如何更改一些参数。使用 [setCoordinateType](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setCoordinateType-int-) 我们设置框架 [CropBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCoordinateType#CropBox)。此外，我们可以更改 [setResolution](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setResolution-com.aspose.pdf.devices.Resolution-) 指定每英寸的点数。接下来是 [setFormPresentationMode](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setFormPresentationMode-int-) - 表单呈现模式。然后我们指示 [setStartPage](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfConverter#setStartPage-int-) 设置转换开始的页面编号。我们还可以通过设置范围指定最后一页。

```java
public static void ConvertPdfPagesToImages02()
    {
        // 创建 PdfConverter 对象
        PdfConverter converter = new PdfConverter();

        // 绑定输入 pdf 文件
        converter.bindPdf(_dataDir + "sample.pdf");

        // 初始化转换过程
        converter.doConvert();
        converter.setCoordinateType(PageCoordinateType.CropBox);
        converter.setResolution (new Resolution(600));
        converter.setFormPresentationMode(FormPresentationMode.Editor);
        converter.setStartPage(2);
        int count=0;
        // 检查页面是否存在，然后逐一转换为图像
        while (converter.hasNextImage())
            converter.getNextImage(_dataDir + "page" + count + "_out.jpg", ImageType.getJpeg());
        // 关闭 PdfConverter 对象
        converter.close();
    }
```