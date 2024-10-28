---
title: 使用PDF文件元数据
linktitle: PDF文件元数据
type: docs
weight: 140
url: /java/pdf-file-metadata/
description: 本节解释如何获取PDF文件信息，如何从PDF文件获取XMP元数据，设置PDF文件信息。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 获取PDF文件信息

要获取有关PDF文件的特定信息，首先使用[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)类的[getInfo()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getInfo--)方法获取[DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo)对象。一旦检索到[DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo)对象，就可以获取各个属性的值。

以下代码片段展示了如何设置PDF文件信息。

```java
public class ExampleMetadata {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Metadata/";

    public static void GetPDFFileInformation() {
        // 创建一个新的PDF文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");
        // 获取文档信息
        DocumentInfo docInfo = pdfDocument.getInfo();
        // 显示文档信息
        System.out.println("作者: " + docInfo.getAuthor());
        System.out.println("创建日期: " + docInfo.getCreationDate());
        System.out.println("关键词: " + docInfo.getKeywords());
        System.out.println("修改日期: " + docInfo.getModDate());
        System.out.println("主题: " + docInfo.getSubject());
        System.out.println("标题: " + docInfo.getTitle());
    }
```


## 设置 PDF 文件信息

Aspose.PDF for Java 允许您为 PDF 设置特定于文件的信息，例如作者、创建日期、主题和标题。

要设置此信息：

1. 创建一个 [DocumentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf/DocumentInfo) 对象。
1. 设置属性的值。
1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 类的 [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) 方法保存更新后的文档。

{{% alert color="primary" %}}

请注意，您不能对 **Producer** 和 **Creator** 字段设置值，因为 Aspose.PDF for Java x.x.x 将显示在这些字段中。

{{% /alert %}}

以下代码片段向您展示如何设置 PDF 文件信息。

```java
 public static void SetPDFFileInformation() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 指定文档信息
        DocumentInfo docInfo = new DocumentInfo(pdfDocument);

        docInfo.setAuthor("Aspose");
        docInfo.setCreationDate(new java.util.Date());
        docInfo.setKeywords("Aspose.Pdf, DOM, API");
        docInfo.setModDate(new java.util.Date());
        docInfo.setSubject("PDF 信息");
        docInfo.setTitle("设置 PDF 文档信息");

        // 保存输出文档
        pdfDocument.save(_dataDir + "SetFileInfo_out.pdf");
    }
```


## 从 PDF 文件获取 XMP 元数据

Aspose.PDF for Java 允许您访问 PDF 文件的 XMP 元数据。

要获取 PDF 文件的元数据，

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象并打开输入的 PDF 文件。
1. 使用 [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) 属性来获取元数据。

以下代码片段向您展示了如何从 PDF 文件中获取元数据。

```java
   public static void GetXMPMetadata() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");

        System.out.println("xmp:CreateDate: " + pdfDocument.getMetadata().get_Item("xmp:CreateDate"));
        System.out.println("xmp:Nickname: " + pdfDocument.getMetadata().get_Item("xmp:Nickname"));
        System.out.println("xmp:CustomProperty: " + pdfDocument.getMetadata().get_Item("xmp:CustomProperty"));

    }
```

## 在 PDF 文件中设置 XMP 元数据

Aspose.PDF for Java 允许您在 PDF 文件中设置元数据。
 设置元数据：

1. 创建一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象。
1. 使用 [getMetadata()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#getMetadata--) 属性设置元数据值。
1. 使用 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象的 [save()](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document#save-com.aspose.ms.System.IO.FileStream-) 方法保存更新后的文档。

以下代码片段展示了如何在 PDF 文件中设置元数据。

```java
    public static void SetXMPMetadata() {

        // 打开文档
        Document pdfDocument = new Document(_dataDir + "sample.pdf");

        // 设置属性
        pdfDocument.getMetadata().set_Item("xmp:CreateDate", new XmpValue(new java.util.Date()));
        pdfDocument.getMetadata().set_Item("xmp:Nickname", new XmpValue("Nickname"));
        pdfDocument.getMetadata().set_Item("xmp:CustomProperty", new XmpValue("Custom Value"));

        // 保存文档
        pdfDocument.save(_dataDir + "SetXMPMetadata.pdf");
    }
```

## 插入带前缀的元数据

一些开发人员需要创建一个带有前缀的新元数据命名空间。以下代码片段展示了如何插入带前缀的元数据。

```java
    public static void InsertMetadataWithPrefix() {
        // 打开文档
        Document pdfDocument = new Document(_dataDir + "SetXMPMetadata.pdf");
        pdfDocument.getMetadata().registerNamespaceUri("adc", "http://tempuri.org/adc/1.0");
        pdfDocument.getMetadata().set_Item("adc:format", new XmpValue("application/pdf"));
        pdfDocument.getMetadata().set_Item("adc:title", new XmpValue("alternative title"));        
        // 保存文档
        pdfDocument.save(_dataDir + "SetPrefixMetadata_out.pdf");
    }
}
```