---
title: 将 PDF 转换为 PNG
linktitle: 将 PDF 转换为 PNG
type: docs
weight: 20
url: /zh/androidjava/convert-pdf-to-png/
lastmod: "2026-07-01"
description: 此页面描述了如何使用 Aspose.PDF for Android via Java 将 PDF 页面转换为 PNG 图像，支持将所有页面或单个页面转换为 PNG 图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

使用 **Aspose.PDF for Android via Java** 库将 PDF 页面转换为 <abbr title="Portable Network Graphics">PNG</abbr> 以可访问且便捷的方式呈现图像。

PngDevice 类允许您将 PDF 页面转换为 PNG 图像。该类提供名为 Process 的方法，可将 PDF 文件的特定页面转换为 PNG 图像格式。

## 将 PDF 页面转换为 PNG 图像

要将 PDF 文件中的所有页面转换为 PNG 文件，请遍历各个页面并将每个页面转换为 PNG 格式。以下代码片段演示了如何遍历 PDF 文件的所有页面并将每个页面转换为 PNG 图像。

{{% alert color="primary" %}} 

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png)

{{% /alert %}}

## 将单个 PDF 页面转换为 PNG 图像

将页面索引作为参数传递给 Process(..) 方法。
下面的代码片段展示了将 PDF 的首页转换为 PNG 格式的步骤。

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create PngDevice object with particular resolution
            PngDevice PngDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 将所有 PDF 页面转换为 PNG 图像

Aspose.PDF for Android via Java 向您展示如何将 PDF 文件中的所有页面转换为图像：

1. 遍历文件中的所有页面。
1. 逐个页面单独转换：
    1. 创建 Document 类的对象以加载 PDF 文档。
    1. 获取您想要转换的页面。
    1. 调用 Process 方法将页面转换为 Png。

以下代码片段向您展示如何将所有 PDF 页面转换为 PNG 图像。

```java
 public void convertPDFtoPNG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // Create Resolution object
            Resolution resolution = new Resolution(300);
            // Create JpegDevice object with particular resolution
            PngDevice JpegDevice = new PngDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

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

## 将特定 PDF 页面转换为 PNG 图像

Aspose.PDF for Android via Java 向您展示如何将特定页面转换为 PNG 格式：

```java
public void convertPDFtoPNG_ParticularPageRegion() {
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
        // Create Jpeg device with specified attributes
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // Convert a particular page and save the image to stream
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
