---
title: 将PDF转换为DOC 
linktitle: 将PDF转换为DOC
type: docs
weight: 70
url: /androidjava/convert-pdf-to-doc/
lastmod: "2021-06-05"
description: 使用Aspose.PDF for Android via Java轻松且完全控制地将PDF文件转换为DOC格式。了解更多关于如何调整Microsoft Word Doc文件到PDF的转换。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

最受欢迎的功能之一是PDF到Microsoft Word DOC的转换，使内容易于操作。Aspose.PDF for Android via Java允许您将PDF文件转换为DOC。

**Aspose.PDF for Android via Java** 可以从头创建PDF文档，是更新、编辑和操作现有PDF文档的优秀工具包。
 一个重要功能是将页面和整个 PDF 文档转换为图像的能力。另一个流行的功能是 PDF 转换为 Microsoft Word DOC，这使得内容易于操作。（大多数用户无法编辑 PDF 文档，但可以轻松处理 Microsoft Word 中的表格、文本和图像。）

为了使事情简单易懂，Aspose.PDF for Android via Java 提供了两行代码，用于将源 PDF 文件转换为 DOC 文件。

{{% alert color="primary" %}}

在线尝试。您可以通过此链接查看 Aspose.PDF 转换的质量并在线查看结果 [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

以下代码片段展示了将 PDF 文件转换为 DOC 格式的过程。

```java
 public void convertPDFtoDOC() {
        // 打开源 PDF 文档
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // 将文件保存为 MS 文档格式
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```