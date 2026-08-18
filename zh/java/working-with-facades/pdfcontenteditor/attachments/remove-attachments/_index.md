---
title: 删除附件
linktitle: 删除附件
type: docs
weight: 50
url: /java/remove-attachments/
description: 了解如何使用 Aspose.PDF 中的 PdfContentEditor 外观从 Java 中的 PDF 中删除所有文档附件。
lastmod: "2026-06-09"
TechArticle: true
AlternativeHeadline: 用Java删除所有PDF附件
Abstract: 本文介绍如何使用 Aspose.PDF for Java 中的 PdfContentEditor 外观绑定 PDF、删除所有文档附件以及保存更新的文件。
---
## 删除所有附件

1. Bind the source PDF to the `PdfContentEditor` facade.
2. Call `deleteAttachments()` to remove every embedded attachment.
3. Save the updated PDF document.

```java
public static void removeAttachments(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.deleteAttachments();
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
