---
title: 从 PDF 文档生成缩略图
linktitle: 生成缩略图
type: docs
weight: 100
url: /java/generate-thumbnail-images-from-pdf-documents/
description: 本节介绍如何使用 Aspose.PDF for Java 从 PDF 文档生成缩略图。
lastmod: "2021-06-05"
---

## Aspose.PDF for Java 方法

Aspose.PDF for Java 提供了广泛支持处理 PDF 文档的功能。它还支持将 PDF 文档的页面转换为多种图像格式。上述功能可以通过 Aspose.PDF for Java 轻松实现。

Aspose.PDF 具有明显的优势：

- 您不需要在系统上安装 Adobe Acrobat 即可处理 PDF 文件。
- 使用 Aspose.PDF for Java 比 Acrobat Automation 更简单易懂。

如果我们需要将 PDF 页面转换为 JPEG，[com.aspose.pdf.devices](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/package-frame) 命名空间提供了一个名为 [JpegDevice](https://reference.aspose.com/pdf/java/com.aspose.pdf.devices/JpegDevice) 的类，用于将 PDF 页面呈现为 JPEG 图像。
 请查看以下代码片段。

```java
package com.aspose.pdf.examples;

import com.aspose.pdf.Document;
import com.aspose.pdf.devices.JpegDevice;
import com.aspose.pdf.devices.Resolution;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class ExampleGenerateThumbnails {
    private static String _dataDir = "/home/admin1/pdf-examples/Samples/";

    public static void GenerateThumbnails() throws IOException {
        // 检索特定目录中所有 PDF 文件的名称
        List<String> fileEntries = null;
        try {
            fileEntries = Files.list(Paths.get(_dataDir)).filter(Files::isRegularFile)
                    .filter(path -> path.toString().endsWith(".pdf")).map(path -> path.toString())
                    .collect(Collectors.toList());

        } catch (IOException e) {
            // 读取目录时出错
        }

        // 遍历数组中的所有文件条目
        for (int counter = 0; counter < fileEntries.size(); counter++) {
            // 打开文档
            Document pdfDocument = new Document(fileEntries.get(counter));

            for (int pageCount = 1; pageCount <= 4; pageCount++) {
                FileOutputStream imageStream = new FileOutputStream(
                        _dataDir + "\\Thumbnails" + counter + "_" + pageCount + ".jpg");
                // 创建分辨率对象
                Resolution resolution = new Resolution(300);
                JpegDevice jpegDevice = new JpegDevice(45, 59, resolution, 100);
                // 转换特定页面并将图像保存到流中
                jpegDevice.process(pdfDocument.getPages().get_Item(pageCount), imageStream);
                // 关闭流
                imageStream.close();
            }
        }

    }
}
```