---
title: 从 PDF 文件提取附件
type: docs
weight: 10
url: zh/java/extract-attachments/
description: 本节介绍如何使用 PdfExtractor 类从 pdf 中提取附件。
lastmod: "2021-06-05"
draft: false
---

在 [com.aspose.pdf.facades](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/package-frame) 的提取功能中，附件提取是主要类别之一。
 这个类别提供了一组方法，这些方法不仅可以帮助提取附件，还提供了可以为您提供附件相关信息的方法，即 [GetAttachmentInfo](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachmentInfo--) 和 [GetAttachName](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachNames--) 方法分别提供附件信息和附件名称。为了提取并获取附件，我们使用 [ExtractAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#extractAttachment--) 和 [GetAttachment](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/PdfExtractor#getAttachment--) 方法。

以下代码片段向您展示了如何使用 PdfExtractor 方法：

```java
  public static void ExtractAttachments() {
        PdfExtractor pdfExtractor = new PdfExtractor();
        pdfExtractor.bindPdf(_dataDir + "sample-attach.pdf");

        // 提取附件
        pdfExtractor.extractAttachment();

        // 获取附件名称
        if (pdfExtractor.getAttachNames().size() > 0) {
            System.out.println("Extracting and storing...");
            // 获取提取的附件
            pdfExtractor.getAttachment(_dataDir);
        }
    }
```