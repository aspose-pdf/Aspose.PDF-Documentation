---
title: 禁用将文件作为嵌入资源添加时的压缩
linktitle: 禁用文件压缩
type: docs
weight: 40
url: zh/java/disable-files-compression-when-adding-as-embedded-resources/
description: 本文解释了如何在将文件添加为嵌入资源时禁用压缩
lastmod: "2021-06-05"
---

[FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 类允许开发人员向 PDF 文档添加附件。默认情况下，附件是压缩的。我们更新了 API，以允许开发人员在将文件作为嵌入资源添加时禁用压缩。这使开发人员对文件的处理方式有更多的控制。

为了允许开发人员控制文件压缩，[setEncoding(..)](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification#setEncoding-int-) 方法已被添加到 [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileSpecification) 类中。
 该属性确定将用于文件压缩的编码。该方法接受来自 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding) 枚举的值。可能的值是 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None 和 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip。

如果将编码设置为 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).None，则附件不被压缩。默认编码是 [FileEncoding](https://reference.aspose.com/pdf/java/com.aspose.pdf/FileEncoding).Zip。

以下代码片段显示了如何将附件添加到 PDF 文档。

```java
    public static void DisableFilesCompressionWhenAddingAsEmbeddedResources() throws IOException{
  // 获取源文件/输入文件的引用
  java.nio.file.Path path = java.nio.file.Paths.get(_dataDir+"input.pdf");
  // 从源文件读取所有内容到字节数组
  byte[] data = java.nio.file.Files.readAllBytes(path);
  // 从字节数组内容创建一个 Stream 对象的实例
  InputStream is = new ByteArrayInputStream(data);
  // 从流实例化 Document 对象
  Document pdfDocument = new Document(is);
  // 设置要添加为附件的新文件
  FileSpecification fileSpecification = new FileSpecification("test.txt", "示例文本文件");
  // 指定编码属性，将其设置为 FileEncoding.None
  fileSpecification.setEncoding(FileEncoding.None);
  // 将附件添加到文档的附件集合中
  pdfDocument.getEmbeddedFiles().add(fileSpecification);
  // 保存新的输出
  pdfDocument.save("output.pdf");
    }
```