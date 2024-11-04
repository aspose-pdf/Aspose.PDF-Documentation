---
title: 将 PDF 转换为 PNG
linktitle: 将 PDF 转换为 PNG
type: docs
weight: 20
url: /androidjava/convert-pdf-to-png/
lastmod: "2021-06-05"
description: 本页描述了如何使用 Aspose.PDF for Android via Java 将 PDF 页面转换为 PNG 图像，转换全部和单个页面为 PNG 图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

使用 **Aspose.PDF for Android via Java** 库以便捷的方式将 PDF 页面转换为 <abbr title="Portable Network Graphics">PNG</abbr> 图像。

PngDevice 类允许您将 PDF 页面转换为 PNG 图像。此类提供了一个名为 Process 的方法，允许您将 PDF 文件的特定页面转换为 PNG 图像格式。

## 将 PDF 页面转换为 PNG 图像

要将 PDF 文件中的所有页面转换为 PNG 文件，请遍历各个页面并将每个页面转换为 PNG 格式。以下代码片段显示了如何遍历 PDF 文件的所有页面并将每个页面转换为 PNG 图像。

{{% alert color="primary" %}}

在在线尝试。您可以在此链接 [products.aspose.app/pdf/conversion/pdf-to-png](https://products.aspose.app/pdf/conversion/pdf-to-png) 在线检查 Aspose.PDF 转换的质量并查看结果。

{{% /alert %}}

## 将单个 PDF 页面转换为 PNG 图像

将页面索引作为参数传递给 Process(..) 方法。以下代码片段展示了将 PDF 的第一页转换为 PNG 格式的步骤。

```java
   public void convertPDFtoPNG() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-PNG.png");
        // 创建流对象以保存输出图像
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // 创建 Resolution 对象
            Resolution resolution = new Resolution(300);

            // 使用特定分辨率创建 PngDevice 对象
            PngDevice PngDevice = new PngDevice(resolution);

            // 转换特定页面并将图像保存到流
            PngDevice.process(document.getPages().get_Item(1), imageStream);

            // 关闭流
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }

```


## 将所有 PDF 页面转换为 PNG 图像

Aspose.PDF for Android via Java 向您展示如何将 PDF 文件中的所有页面转换为图像：

1. 循环遍历文件中的所有页面。
1. 单独转换每个页面：
    1. 创建 Document 类的对象以加载 PDF 文档。
    1. 获取要转换的页面。
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

        // 循环遍历 PDF 文件的所有页面
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 创建流对象以保存输出图像
            File file = new File(fileStorage, "PDF-to-PNG"+pageCount+".png");
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
            PngDevice JpegDevice = new PngDevice(resolution);

            // 转换特定页面并将图像保存到流
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


## 将特定的PDF页面转换为PNG图像

Aspose.PDF for Android via Java 向您展示如何将特定页面转换为PNG格式：

```java
public void convertPDFtoPNG_ParticularPageRegion() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        // 获取特定页面区域的矩形
        //x=0,y=0, w=200, h=125;
        Rectangle pageRect = new Rectangle(0, 0, 200, 125);
        // 根据所需页面区域的矩形设置 CropBox 值
        document.getPages().get_Item(1).setCropBox(pageRect);
        // 将裁剪后的文档保存到流中
        ByteArrayOutputStream outStream = new ByteArrayOutputStream();
        document.save(outStream);

        // 从流中打开裁剪后的PDF文档并转换为图像
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 创建Resolution对象
        Resolution resolution = new Resolution(300);
        // 创建具有指定属性的Png设备
        PngDevice PngDevice = new PngDevice(resolution);

        File file = new File(fileStorage, "PDF-to-PNG.png");
        try {
            // 转换特定页面并将图像保存到流中
            PngDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
    }
```