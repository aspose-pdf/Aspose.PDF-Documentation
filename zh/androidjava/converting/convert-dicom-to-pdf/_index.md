---
title: 将DICOM转换为PDF 
linktitle: 将DICOM转换为PDF
type: docs
weight: 250
url: /zh/androidjava/convert-dicom-to-pdf/
lastmod: "2021-06-05"
description: 使用Aspose.PDF for Android via Java将以DICOM格式保存的医学图像转换为PDF文件。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

<abbr title="Digital Imaging and Communications in Medicine">DICOM</abbr>是一个用于处理、存储、打印和传输医学影像信息的标准。它包括文件格式定义和网络通信协议。

Aspose.PDF for Java允许您将DICOM文件转换为PDF格式，请查看以下代码片段：

1. 将图像加载到流中
1. 初始化[`Document对象`](https://reference.aspose.com/pdf/java/com.aspose.pdf/document)
1. 加载示例DICOM图像文件
1. 保存输出PDF文档

```java
//    将DICOM转换为PDF
    public void convertDICOMtoPDF () {
        // 初始化文档对象
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

        // 加载示例BMP图像文件
        image.setImageStream(inputStream);
        image.setFileType(ImageFileType.Dicom);
        page.getParagraphs().add(image);

        File pdfFileName=new File(fileStorage, "DICOM-to-PDF.pdf");

        // 保存输出文档
        try {
            document.save(pdfFileName.toString());
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```