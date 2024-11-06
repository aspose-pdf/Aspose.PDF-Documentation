title: Hello World Java Example
linktitle: Hello World Example
type: docs
weight: 40
url: zh/java/hello-world-example/
description: 本页面展示如何使用简单编程创建包含文本的PDF文档 - 使用Aspose.PDF for Java实现Hello World。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Hello World 示例

“Hello World” 示例传统上用于通过一个简单的用例介绍编程语言或软件的特性。

Aspose.PDF for Java API 使 Java 应用程序开发人员能够在他们的应用程序中创建、读取、编辑和操作 PDF 文件。它允许您读取和转换多种不同的文件类型到和从 PDF 文件格式。本文的 Hello World 示例展示了如何使用 Aspose.PDF for Java API 在 Java 中创建 PDF 文件。在您的环境中[安装 Aspose.PDF for Java](/pdf/java/installation/)后，您可以执行以下代码示例以查看 Aspose.PDF API 的工作方式。

以下代码片段遵循这些步骤：

1. 实例化一个 [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/class-use/Document) 对象
1. 向文档对象添加一个 [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/page)
1. 创建一个 [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf.class-use/TextFragment) 对象
1. 将 TextFragment 添加到页面的 [Paragraph](https://reference.aspose.com/pdf/java/com.aspose.pdf/Paragraphs) 集合中
1. 保存生成的 PDF 文档

以下代码片段是一个 Hello World 程序，用于展示 Aspose.PDF for Java API 的工作原理。

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