---
title: 转换 DICOM 为 PDF
linktitle: 转换 DICOM 为 PDF
type: docs
weight: 250
url: /zh/androidjava/convert-dicom-to-pdf/
lastmod: "2026-07-01"
description: 使用 Aspose.PDF for Android via Java 将保存为 DICOM 格式的医学图像转换为 PDF 文件。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr> 是一种用于处理、存储、打印和传输医学影像信息的标准。它包括文件格式定义和网络通信协议。

Aspsoe.PDF for Java 允许您将 DICOM 文件转换为 PDF 格式，请查看下面的代码片段：

1. 将图像加载到流中
1. 初始化 [`Document object`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. 加载示例 DICOM 图像文件
1. 保存输出 PDF 文档

```java
//    Convert DICOM to PDF
    public void convertDICOMtoPDF () {
        // Initialize document object
        document=new Document();

        Page page=document.getPages().add();
        Image image=new Image();

        File imgFileName=new File(fileStorage, "Conversion/bmode.dcm");

        try {
            inputStream=new FileInputStream(imgFileName);
        } catch (FileNotFoundException e) {
            resultMessage.setText(e.getMessage());
            return;
        }

        // Load sample BMP image file
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // Save output document
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```

