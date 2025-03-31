---
title: 将 PDF 转换为 BMP
linktitle: 将 PDF 转换为 BMP
type: docs
weight: 40
url: /zh/androidjava/convert-pdf-to-bmp/
lastmod: "2021-06-05"
description: 本文介绍如何使用 Java 将 PDF 页面转换为 BMP 图像，将所有页面转换为 BMP 图像以及将单个 PDF 页面转换为 BMP 图像。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

[BmpDevice](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/bmpdevice) 类允许您将 PDF 页面转换为<abbr title="Bitmap Image File">BMP</abbr>图像。该类提供了一种名为[Process](https://reference.aspose.com/pdf/zh/net/aspose.pdf.devices/bmpdevice/methods/process)的方法，允许您将 PDF 文件的特定页面转换为 Bmp 图像格式。

{{% alert color="primary" %}}

在线试用。您可以在此链接 [products.aspose.app/pdf/conversion/pdf-to-bmp](https://products.aspose.app/pdf/conversion/pdf-to-bmp) 查看 Aspose.PDF 转换的质量和在线查看结果

{{% /alert %}}

BmpDevice 类允许您将 PDF 页面转换为 BMP 图像。
 这个类提供了一个名为 process(..) 的方法，允许您将 PDF 文件的特定页面转换为 BMP 图像。

## 将 PDF 页面转换为 BMP 图像

要将 PDF 页面转换为 BMP 图像：

1. 创建 Document 类的对象，以获取您要转换的特定页面。
2. 调用 process(..) 方法将页面转换为 BMP。

下面的代码片段向您展示了如何将特定页面转换为 BMP 图像。

```java
// 将 PDF 转换为 BMP
    public void convertPDFtoBMP() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File file = new File(fileStorage, "PDF-to-BMP.bmp");
        // 创建流对象以保存输出图像
        try {
            OutputStream imageStream =
                    new FileOutputStream(file.toString());

            // 创建分辨率对象
            Resolution resolution = new Resolution(300);

            // 使用特定分辨率创建 BmpDevice 对象
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // 转换特定页面并将图像保存到流中
            BmpDevice.process(document.getPages().get_Item(1), imageStream);

            // 关闭流
            imageStream.close();
            resultMessage.setText(file.toString());
        } catch (IOException e) {
            resultMessage.setText(e.getMessage());
        }
    }
```

## 将所有 PDF 页面转换为 BMP 图像

要将 PDF 文件的所有页面转换为 BMP 格式，您需要遍历以获取每个单独的页面并将其转换为 BMP 格式。以下代码片段向您展示了如何遍历 PDF 文件的所有页面并将其转换为 BMP。

```java
public void convertPDFtoBMP_AllPages() {
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // 遍历 PDF 文件的所有页面
        for (int pageCount = 1; pageCount <= document.getPages().size(); pageCount++) {
            // 创建流对象以保存输出图像
            File file = new File(fileStorage, "PDF-to-BMP"+pageCount+".BMP");
            java.io.OutputStream imageStream;
            try {
                imageStream = new java.io.FileOutputStream(file.toString());
            } catch (FileNotFoundException e) {
                resultMessage.setText(e.getMessage());
                return;
            }

            // 创建分辨率对象
            Resolution resolution = new Resolution(300);
            // 创建具有特定分辨率的 BmpDevice 对象
            BmpDevice BmpDevice = new BmpDevice(resolution);

            // 转换特定页面并将图像保存到流
            BmpDevice.process(document.getPages().get_Item(pageCount), imageStream);

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


## 将特定的页面区域转换为图像 (DOM)

我们可以使用 Aspose.PDF 的图像设备对象将 PDF 文档转换为不同的图像格式。然而，有时需要将特定的页面区域转换为图像格式。我们可以通过两个步骤来满足这个需求。首先裁剪 PDF 页面到所需区域，然后使用所需的图像设备对象将其转换为图像。

以下代码片段显示了如何将 PDF 页面转换为图像。

```java
public void convertPDFtoBmp_ParticularPageRegion() {
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

        // 从流中打开裁剪后的 PDF 文档并转换为图像
        document = new Document(new ByteArrayInputStream(outStream.toByteArray()));
        // 创建 Resolution 对象
        Resolution resolution = new Resolution(300);
        // 创建具有指定属性的 BMP 设备
        BmpDevice BmpDevice = new BmpDevice(resolution);

        File file = new File(fileStorage, "PDF-to-BMP.BMP");
        try {
            // 转换特定页面并将图像保存到流中
            BmpDevice.process(document.getPages().get_Item(1), file.toString());
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
        }
        resultMessage.setText(R.string.success_message);
    }
```