---
title: 创建 PDF 文档
linktitle: 创建
type: docs
weight: 10
url: /java/create-document/
description: 学习如何在 Aspose.PDF for Java 中创建 PDF 文件。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Aspose.PDF for Java** API 允许 Java 应用程序开发人员在他们的应用程序中嵌入 PDF 文档处理功能。它可以用于创建和读取 PDF 文件，而不需要在底层机器上安装任何其他软件。Aspose.PDF for Java 可以用于多种 Java 应用程序类型，例如桌面应用程序、JSP 和 JSF 应用程序。

## 如何使用 Java 创建 PDF 文件

要使用 Java 创建 PDF 文件，可以使用以下步骤。

1. 实例化一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) 对象
2. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page)
3. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) 对象

1. 将 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/textfragment) 添加到页面的 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 集合中
1. 保存生成的 PDF 文档

```java
// 初始化文档对象
Document document = new Document();
 
// 添加页面
Page page = document.getPages().add();
 
// 向新页面添加文本
page.getParagraphs().add(new TextFragment("Hello World!"));
 
// 保存更新的 PDF
document.save("HelloWorld_out.pdf");
```