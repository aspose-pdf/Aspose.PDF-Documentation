---
title: 设置PDF文件信息 - 外观
type: docs
weight: 20
url: /zh/java/set-pdf-information/
description: 本节介绍如何使用Aspose.PDF Facades通过PdfFileInfo类设置PDF文件信息。
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

[PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 类允许您设置PDF文档的特定文件信息。您需要创建一个 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 类的对象，然后设置不同的文件特定属性，如作者、标题、关键词和创建者等。最后，使用 [PdfFileInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo) 对象的 [saveNewInfo(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#saveNewInfo-java.io.OutputStream-) 方法保存更新后的PDF文件。

以下代码片段向您展示如何设置PDF文件信息。

```java
 public static void SetPdfInfo()
    {
        PdfFileInfo fileInfo = new PdfFileInfo(_dataDir + "sample.pdf");
        // 设置PDF信息
        fileInfo.setAuthor("Aspose");
        fileInfo.setTitle ("Hello World!");
        fileInfo.setKeywords("Peace and Development");
        fileInfo.setCreator ("Aspose");
        
        // 保存更新后的文件
        fileInfo.saveNewInfo(_dataDir + "SetfileInfo_out.pdf");
    }
```


## 设置元信息

[setMetaInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfFileInfo#setMetaInfo-java.lang.String-java.lang.String-) 方法允许您添加任何信息。在我们的示例中，我们添加了一个字段。查看下一个代码片段：

```java
   public static void SetMetaInfo()
    {
        // 创建 PdffileInfo 对象的实例
        PdfFileInfo fInfo = new PdfFileInfo(_dataDir + "sample.pdf");
       
        // 设置新的客户属性作为元信息
        fInfo.setMetaInfo("Reviewer", "Aspose.PDF 用户");

        // 保存更新后的文件
        fInfo.saveNewInfo(_dataDir + "SetMetaInfo_out.pdf");

    }
```