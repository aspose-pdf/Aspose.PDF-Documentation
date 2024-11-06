---
title: 保存 PDF 文档
linktitle: 保存
type: docs
weight: 30
url: zh/java/save-pdf-document/
description: 学习如何使用 Aspose.PDF for Java 库保存 PDF 文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 保存 PDF 文档到文件系统

您可以使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 Save 方法将创建或操作的 PDF 文档保存到文件系统。
如果您不提供格式类型（选项），则文档将以 Aspose.PDF v.1.7 (*.pdf) 格式保存。

```java
package com.aspose.pdf.examples;


import java.io.FileOutputStream;

import java.nio.file.Path;
import java.nio.file.Paths;
import com.aspose.pdf.*;

public final class BasicOperationsSave {

    private BasicOperationsSave() {
    }

    private static Path _dataDir = Paths.get("/home/admin1/pdf-examples/Samples");

    public static void main(String[] args) {
        SaveDocument();
        SaveDocumentStream();
        SaveDocumentAsPDFx();
    }

    public static void SaveDocument() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // 进行一些操作，例如添加新空白页
        pdfDocument.getPages().add();
        pdfDocument.save(modifiedFileName);
    }
```


## 保存 PDF 文档到流

您还可以使用 Save 方法的重载将创建或操作的 PDF 文档保存到流中。

```java
public static void SaveDocumentStream() {
        String originalFileName = _dataDir + "/SimpleResume.pdf";
        String modifiedFileName = _dataDir + "/SimpleResumeModified.pdf";

        Document pdfDocument = new Document(originalFileName);
        // 进行一些操作，例如添加新的空白页
        pdfDocument.getPages().add();
        try {
            pdfDocument.save(new FileOutputStream(modifiedFileName));
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }

```

## 在 Web 应用程序中保存 PDF 文档

要在 Web 应用程序中保存文档，您可以使用上面提出的方法。此外，[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类具有重载方法 Save。
```java
    // @RequestMapping(value = "/files/{file_name}", method = RequestMethod.GET)
    // public void getFile(@PathVariable("file_name") String fileName, HttpServletResponse response) {
    //     try {
    //         response.setContentType("application/pdf");
    //         // 将您的文件作为 InputStream 获取
    //         InputStream is = new FileInputStream(_dataDir + fileName);
    //         // 将其复制到响应的 OutputStream
    //         org.apache.commons.io.IOUtils.copy(is, response.getOutputStream());
    //         response.flushBuffer();
    //     } catch (IOException ex) {
    //         log.info("Error writing file to output stream. Filename was '{}'", fileName, ex);
    //         throw new RuntimeException("IOError writing file to output stream");
    //     }
    // }
```


有关更详细的解释，请参阅[展示]()部分。

## 保存为 PDF/A 或 PDF/X 格式

PDF/A 是用于电子文档归档和长期保存的可移植文档格式 (PDF) 的 ISO 标准化版本。PDF/A 与 PDF 的区别在于它禁止不适合长期归档的功能，如字体链接（相对于字体嵌入）和加密。PDF/A 查看器的 ISO 要求包括颜色管理指南、嵌入字体支持和用于阅读嵌入注释的用户界面。

PDF/X 是 PDF ISO 标准的一个子集。PDF/X 的目的是促进图形交换，因此它具有一系列不适用于标准 PDF 文件的打印相关要求。

在这两种情况下，保存方法用于存储文档，而文档必须使用转换方法进行准备。

```java
public static void SaveDocumentAsPDFx() {
        Document pdfDocument = new Document("../../../Samples/SimpleResume.pdf");
        pdfDocument.getPages().add();
        pdfDocument.convert(new PdfFormatConversionOptions(PdfFormat.PDF_X_3));
        pdfDocument.save("../../../Samples/SimpleResume_X3.pdf");
    }

}
```