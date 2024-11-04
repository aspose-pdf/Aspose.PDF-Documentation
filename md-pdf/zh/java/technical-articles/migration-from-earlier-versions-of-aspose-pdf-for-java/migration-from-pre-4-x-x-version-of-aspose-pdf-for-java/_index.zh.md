---
title: 从 Aspose.PDF for Java 旧版 4.x.x 迁移
type: docs
weight: 20
url: /java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Aspose.PDF for Java 的新自动移植版本已经发布，现在这个单一产品支持从头生成 PDF 文档的功能，并提供操作现有 PDF 文档的功能。

{{% /alert %}}

## 产品二进制文件

{{% alert color="primary" %}}

在第一个发布版本 (v4.0.0) 中，我们发布了两个 jar 文件，即 **aspose.pdf-3.3.0.jdk15.jar** 和 **aspose.pdf-new-4.0.0.jar**。

- **aspose.pdf-3.3.0.jdk14.jar**

这个 jar 文件与当前下载模块中标题为 [Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx) 的产品版本相同。今后，我们将此版本称为遗留版 Aspose.PDF for Java。在这个初始版本中，现有的 Aspose.PDF for Java 用户可能不会受到影响，因为他们获得的是相同的版本。然而，不久之后，我们将删除这个单独的 jar 文件，遗留版 Aspose.PDF for Java（4.x.x 之前）的所有类和枚举将会在单一的 aspose.pdf-new-4.x.x.jar 文件的 com.aspose.pdf.generator 包下可用。
- **aspose.pdf-new-4.0.0.jar**
  这个 jar 文件是 Aspose.PDF 从 .NET 到 Java 平台的实际新自动移植版本。
 这个 jar 文件包含了新的文档对象模型 (DOM)，用于创建和操作现有的 PDF 文件，以及当前的 Aspose.PDF.Kit for Java。Aspose.PDF.Kit for Java 的所有类和枚举都被打包在 com.aspose.pdf.facades 包中，并且在 2013 年第三季度，Aspose.PDF.Kit for Java 将被停用。因此，我们鼓励当前的 Aspose.PDF.Kit for Java 客户尝试将他们的代码迁移到新的自动移植版本。

请查看以下博客文章，以获得关于 Java 自动移植的 Aspose.PDF 结构的更多见解。
{{% /alert %}}