---
title: 获取文档权限
linktitle: 获取文档权限
type: docs
weight: 10
url: /zh/java/get-document-privileges/
description: 了解如何使用 PdfFileInfo 类在 Java 中检查 PDF 文档权限。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Aspose.PDF for Java 检索 PDF 文档权限
Abstract: 了解如何使用 Aspose.PDF for Java 检索文档权限。Java 示例创建一个 PdfFileInfo 对象，读取其 DocumentPrivilege 设置，并打印打印、复制、修改、批注、填写表单、屏幕阅读器和组装的权限标志。
---
## 获取文档权限

使用 `PdfFileInfo.getDocumentPrivilege()` 检查当前 PDF 允许的操作。

### 步骤

1. 创建一个 `PdfFileInfo` 用于输入 PDF 的对象。
2. 调用 `getDocumentPrivilege()` 检索特权集。
3. 从返回值中读取相关的布尔标志 `DocumentPrivilege` 对象。
4. 关闭 `PdfFileInfo` 实例完成时。

### Java 示例

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
