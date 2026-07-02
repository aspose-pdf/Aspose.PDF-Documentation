---
title: 将 PDF 转换为 BMP
linktitle: 将 PDF 转换为 BMP
type: docs
weight: 40
url: /zh/androidjava/convert-pdf-to-bmp/
lastmod: "2026-07-01"
description: 本文介绍了如何使用 Java 将 PDF 页面转换为 BMP 图像、将所有页面转换为 BMP 图像以及将单个 PDF 页面转换为 BMP 图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

该 [BmpDevice](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice) 类允许您将 PDF 页面转换为 <abbr title="Bitmap Image File">位图</abbr> 图像。此类提供一个名为 [Process](https://reference.aspose.com/pdf/net/aspose.pdf.devices/bmpdevice/methods/process) 它允许您将 PDF 文件的特定页面转换为 Bmp 图像格式。

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp)

{{% /alert %}}

BmpDevice 类允许您将 PDF 页面转换为 BMP 图像。该类提供了一个名为 process(..) 的方法，允许您将 PDF 文件的特定页面转换为 BMP 图像。

## 将 PDF 页面转换为 BMP 图像

将 PDF 页面转换为 BMP 图像的方法：

1. 创建 Document 类的对象，以获取您想要转换的特定页面。
1. 调用 process(..) 方法将页面转换为 BMP。

以下代码片段向您展示如何将特定页面转换为 BMP 图像。

```java
//Convert PDF to BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 将所有 PDF 页面转换为 BMP 图像

要将 PDF 文件的所有页面转换为 BMP 格式，您需要遍历以获取每个单独的页面并将其转换为 BMP 格式。下面的代码片段展示了如何遍历 PDF 文件的所有页面并将其转换为 BMP。

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create BmpDevice object with particular resolution
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // Close the stream
            try {
                imageStream.close();
            } catch (Exception e) {
                resultMessage.setText(e.getMessage());
                return;
            }
        }
        resultMessage.setText(R.string.success_message);
    }
```

## 将特定页面区域转换为图像（DOM）

我们可以使用 Aspose.PDF 的图像设备对象将 PDF 文档转换为不同的图像格式。不过有时需要将特定页面区域转换为图像格式。我们可以通过两步来满足此需求。首先将 PDF 页面裁剪到所需区域，然后使用所需的图像设备对象将其转换为图像。

以下代码片段展示了如何将 PDF 页面转换为图像。

```java
public void convertPDFtoBmp_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // Get rectangle of particular page region
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // set CropBox value as per rectangle of desired page region
        document.getPages().get_Item(1).setCropBox(pageRect);
        // save cropped document into stream
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // open cropped PDF document from stream and convert to image
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // Create Resolution object
        Resolution resolution = new Resolution(300);
        // Create BMP device with specified attributes
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // Convert a particular page and save the image to stream
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```
