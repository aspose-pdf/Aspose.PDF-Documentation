---
title: 将PDF转换为JPG
linktitle: 将PDF转换为JPG
type: docs
weight: 10
url: /zh/androidjava/convert-pdf-to-jpg/
description: 本页介绍如何使用Aspose.PDF for Android via Java将PDF页面转换为JPEG图像，将所有页面和单个页面转换为JPEG图像。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 将PDF页面转换为JPG图像

JpegDevice类允许您将PDF页面转换为JPEG图像。该类提供了一个名为process(..)的方法，它允许您将PDF文件的特定页面转换为JPEG图像。

{{% alert color="primary" %}}

在线试用。您可以通过此链接在线查看Aspose.PDF转换的质量和结果 [products.aspose.app/pdf/conversion/pdf-to-jpg](https://products.aspose.app/pdf/conversion/pdf-to-jpg)

{{% /alert %}}


## 将单个PDF页面转换为JPG图像

Aspose.PDF for Android via Java允许您将单个页面转换为Jpeg格式。

要将仅一个页面转换为JPEG图像：

1. 创建一个 Document 类的对象以获取要转换的页面。
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
        // 创建流对象以保存输出图像
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // 创建 Resolution 对象
            Resolution resolution = new Resolution(300);

            // 创建具有特定分辨率的 JpegDevice 对象
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // 转换特定页面并将图像保存到流
            JpegDevice.process(document.getPages().get_Item(1), imageStream);

            // 关闭流
            imageStream.close();

            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```


## 将所有 PDF 页面转换为 JPG 图像

通过 Java 的 Aspose.PDF for Android 允许您将 PDF 文件中的所有页面转换为图像：

1. 循环遍历文件中的所有页面。
1. 单独转换每个页面：
    - 创建一个 Document 类的对象来加载 PDF 文档。
    - 获取您要转换的页面。
    - 调用 Process 方法将页面转换为 Jpeg。

下面的代码片段向您展示如何将所有 PDF 页面转换为 Jpeg 图像。

```java
public void convertPDFtoJPEG_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 循环遍历 PDF 文件的所有页面
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 创建流对象以保存输出图像
            File file = new File(fileStorage, "PDF-to-JPEG"+pageCount+".jpeg");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // 创建 Resolution 对象
            Resolution resolution = new Resolution(300);
            // 创建具有特定分辨率的 JpegDevice 对象
            JpegDevice JpegDevice = new JpegDevice(resolution);

            // 转换特定页面并将图像保存到流中
            JpegDevice.process(document.getPages().get_Item(pageCount), imageStream);

            // 关闭流
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


## 将特定的PDF页面转换为JPG图像

```java
   public void convertPDFtoJPEG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 获取特定页面区域的矩形
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // 根据所需页面区域的矩形设置CropBox值
        document.getPages().get_Item(1).setCropBox(pageRect);
        // 将裁剪后的文档保存到流中
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // 从流中打开裁剪后的PDF文档并转换为图像
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 创建Resolution对象
        Resolution resolution = new Resolution(300);
        // 创建具有指定属性的Jpeg设备
        JpegDevice JpegDevice = new JpegDevice(resolution);

        File file = new File(fileStorage, "PDF-to-JPEG.jpeg");
        try {
            // 转换特定页面并将图像保存到流中
            JpegDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```