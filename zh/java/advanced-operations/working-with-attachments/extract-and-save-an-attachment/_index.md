---
title: 提取并保存附件
linktitle: 提取并保存附件
type: docs
weight: 20
url: /zh/java/extract-and-save-an-attachment/
description: Aspose.PDF for Java 允许您从 PDF 文档中获取所有附件。此外，您还可以从文档中获取单个附件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## 从 PDF 文档获取附件

使用 Aspose.PDF，可以从 PDF 文档中获取所有附件。这在您希望将文档与 PDF 分开保存时很有用，或者当您需要从 PDF 中去除附件时。

以下代码片段展示了如何从 PDF 文档中获取所有附件。

```java
   public static void GetAttachmentsFromPDFDocument() {
// 打开文档
Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 获取特定的嵌入文件
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // 获取文件属性
  System.out.printf("Name: - " + fileSpecification.getName());
  System.out.printf("\nDescription: - " + fileSpecification.getDescription());
  System.out.printf("\nMime Type: - " + fileSpecification.getMIMEType());
  // 从 PDF 文件中获取附件
  try {
   InputStream input = fileSpecification.getContents();
   File file = new File(fileSpecification.getName());
   // 为 pdf 中的文件创建路径
   file.getParentFile().mkdirs();
   // 从 pdf 中创建并提取文件
   java.io.FileOutputStream output = new java.io.FileOutputStream(fileSpecification.getName(), true);
   byte[] buffer = new byte[4096];
   int n = 0;
   while (-1 != (n = input.read(buffer)))
    output.write(buffer, 0, n);
   // 关闭 InputStream 对象
   input.close();
   output.close();
  } catch (IOException e) {
   e.printStackTrace();
  }
  // 关闭 Document 对象
  pdfDocument.dispose();
        
    }

```


## 获取附件信息

如[从 PDF 文档获取附件](/pdf/zh/java/get-attachments-from-a-pdf-document/)中所述，附件信息保存在[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)对象中，与其他附件一起收集在[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document)对象的EmbeddedFiles集合中。

[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification)对象提供获取附件信息的方法，例如：

- getName() – 获取文件名。
- [getDescription()](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#getDescription--) – 获取文件描述。
- getMIMEType() – 获取文件的 MIME 类型。
- getParams() – 文件参数的信息，例如 CheckSum、CreationDate、ModDate 和 Size。

要获取这些参数，首先确保 getParams() 方法不返回 null。

可以使用 for 循环遍历 EmbeddedFiles 集合中的所有附件，或者通过指定其索引值获取单个附件。
 以下代码片段展示了如何获取有关特定附件的信息。

```java
    public static void GetAttachmentInformation() {
  // 打开文档
  Document pdfDocument = new Document(_dataDir+"input.pdf");
  // 获取特定的嵌入文件
  FileSpecification fileSpecification = pdfDocument.getEmbeddedFiles().get_Item(1);
  // 获取文件属性
  System.out.println("Name:-" + fileSpecification.getName());
  System.out.println("Description:- " + fileSpecification.getDescription());
  System.out.println("Mime Type:-" + fileSpecification.getMIMEType());
  // 检查参数对象是否包含参数
  if (fileSpecification.getParams() != null) {
   System.out.println("CheckSum:- " + fileSpecification.getParams().getCheckSum());
   System.out.println("Creation Date:- " + fileSpecification.getParams().getCreationDate());
   System.out.println("Modification Date:- " + fileSpecification.getParams().getModDate());
   System.out.println("Size:- " + fileSpecification.getParams().getSize());
  } 
```