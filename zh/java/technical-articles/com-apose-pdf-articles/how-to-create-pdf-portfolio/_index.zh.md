---
title: 如何创建 PDF 作品集
type: docs
weight: 10
url: /java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

PDF 作品集允许您将来自各种来源的内容（例如，PDF、Word、Excel、JPEG 文件）汇集到一个统一的容器中。原始文件保留其各自的身份，但被组装成一个 PDF 作品集文件。用户可以独立于其他组件文件打开、阅读、编辑和格式化每个组件文件。

Aspose.PDF for Java 允许使用 Document 类创建 PDF 作品集文档。将单个文件加载到 FileSpecification 对象中，并使用 add(...) 方法将它们添加到 Document.Collection 对象中。添加文件后，使用 Document 类的 save(..) 方法生成作品集文档。

{{% /alert %}}

## 代码示例

以下示例使用 Microsoft XPS 文件、Word 文档、PDF 和图像文件创建 PDF 作品集。

**使用 Aspose.PDF 创建的 PDF 作品集**

![todo:图像替代文字](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}