---
title: 将 PDF 转换为 DOC
linktitle: 将 PDF 转换为 DOC
type: docs
weight: 70
url: /zh/androidjava/convert-pdf-to-doc/
lastmod: "2026-07-01"
description: 使用 Aspose.PDF for Android via Java，轻松且完全控制地将 PDF 文件转换为 DOC 格式。了解更多关于如何调优 Microsoft Word Doc 文件到 PDF 转换的方式。
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

最受欢迎的功能之一是 PDF 到 Microsoft Word DOC 的转换，这使得内容易于操作。Aspose.PDF for Android via Java 允许您将 PDF 文件转换为 DOC。

**Aspose.PDF for Android via Java** 可以从头创建 PDF 文档，是用于更新、编辑和操作现有 PDF 文档的优秀工具套件。一个重要功能是能够将页面和整个 PDF 文档转换为图像。另一个受欢迎的功能是 PDF 到 Microsoft Word DOC 的转换，这使得内容易于操作。（大多数用户无法编辑 PDF 文档，但可以在 Microsoft Word 中轻松处理表格、文本和图像。）

为简化并易于理解，Aspose.PDF for Android via Java 提供了两行代码即可将源 PDF 文件转换为 DOC 文件。

{{% alert color="primary" %}}

在线尝试。您可以在此链接检查 Aspose.PDF 转换的质量并在线查看结果。 [products.aspose.app/pdf/conversion/pdf-to-doc](https://products.aspose.app/pdf/conversion/pdf-to-doc)

{{% /alert %}}

以下代码片段展示了将 PDF 文件转换为 DOC 格式的过程。

```java
 public void convertPDFtoDOC() {
        // Open the source PDF document
        try {
            document = new Document(inputStream);
        } catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        File docFileName = new File(fileStorage, "PDF-to-Word.doc");

        try {
            // Save the file into MS document format
            document.save(docFileName.toString(), SaveFormat.Doc);
        }
        catch (Exception e) {
            resultMessage.setText(e.getMessage());
            return;
        }
        resultMessage.setText(R.string.success_message);
    }
```


