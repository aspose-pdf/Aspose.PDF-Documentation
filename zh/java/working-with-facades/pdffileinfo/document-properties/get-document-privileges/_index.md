---
title: 获取文档权限
linktitle: 获取文档权限
type: docs
weight: 10
url: /java/get-document-privileges/
description: 了解如何使用 PdfFileInfo 外观在 Java 中检查 PDF 文档权限。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 检索 PDF 文档权限
Abstract: 了解如何使用 Aspose.PDF for Java 检索文档权限。 Java 示例创建一个 PdfFileInfo 对象，读取其 DocumentPrivilege 设置，并打印打印、复制、修改、注释、表单填写、屏幕阅读器和汇编的权限标志。
---
## 获取文档权限

使用`PdfFileInfo.getDocumentPrivilege()`检查当前PDF允许哪些操作。

### 步骤

1. 为输入 PDF 创建一个 `PdfFileInfo` 对象。
2. Call `getDocumentPrivilege()` to retrieve the privilege set.
3. 从返回的`DocumentPrivilege`对象中读取相关的布尔标志。
4. 完成后关闭`PdfFileInfo`实例。

### Java示例

```java
public static void getDocumentPrivileges(Path inputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    DocumentPrivilege privileges = pdfInfo.getDocumentPrivilege();

    System.out.println("Document Privileges:");
    System.out.println("  Can Print: " + privileges.isAllowPrint());
    System.out.println("  Can Degraded Print: " + privileges.isAllowDegradedPrinting());
    System.out.println("  Can Copy: " + privileges.isAllowCopy());
    System.out.println("  Can Modify Contents: " + privileges.isAllowModifyContents());
    System.out.println("  Can Modify Annotations: " + privileges.isAllowModifyAnnotations());
    System.out.println("  Can Fill In: " + privileges.isAllowFillIn());
    System.out.println("  Can Screen Readers: " + privileges.isAllowScreenReaders());
    System.out.println("  Can Assembly: " + privileges.isAllowAssembly());
    pdfInfo.close();
}
```
