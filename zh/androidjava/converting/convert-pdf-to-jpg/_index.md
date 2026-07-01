---
title: 将 PDF 转换为 JPG
linktitle: 将 PDF 转换为 JPG
type: docs
weight: 10
url: /zh/androidjava/convert-pdf-to-jpg/
description:  本页描述了如何将 PDF 页面转换为 JPEG 图像，使用 Aspose.PDF for Android via Java 将所有页面和单个页面转换为 JPEG 图像。
lastmod: "2026-07-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将 PDF 页面转换为 JPG 图像

JpegDevice 类允许您将 PDF 页面转换为 JPEG 图像。该类提供了一个名为 process(..) 的方法，可将 PDF 文件的特定页面转换为 JPEG 图像。

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。  [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## 将单个 PDF 页面转换为 JPG 图像

Aspose.PDF for Android via Java 允许您将单页转换为 Jpeg 格式。

要将仅一页转换为 JPEG 图像：

1. 创建 Document 类的对象以获取您想要转换的页面。
1. 调用 process(..) 方法将页面转换为 JPEG 图像。

以下代码片段展示了将 PDF 的第一页转换为 Jpeg 格式的步骤。

```java
public void convertPDFtoJPEG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        // Create stream object to save the output image
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // Create Resolution object
            Resolution resolution = new Resolution(300);

            // Create JpegDevice object with particular resolution
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // Close the stream
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```

## 将所有 PDF 页面转换为 JPG 图像

Aspose.PDF for Android via Java 允许您将 PDF 文件中的所有页面转换为图像：

1. 遍历文件中的所有页面。
1. 逐个页面单独转换：
    - 创建 Document 类的对象以加载 PDF 文档。
    - 获取您想要转换的页面。
    - 调用 Process 方法将页面转换为 Jpeg。

下面的代码片段展示了如何将所有 PDF 页面转换为 Jpeg 图像。

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Loop through all the pages of PDF file
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // Create stream object to save the output image
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
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
            JpegDevice JpegDevice = new JpegDevice(resolution);

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

## 将特定的 PDF 页面转换为 JPG 图像

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
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
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // Convert a particular page and save the image to stream
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```
