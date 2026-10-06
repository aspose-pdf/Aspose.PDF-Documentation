---
title: 解密 PDF 文件
linktitle: 解密 PDF 文件
type: docs
weight: 20
url: /zh/java/decrypt-pdf-file/
description: 了解如何在 Java 中使用 PdfFileSecurity 类解密 PDF。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 删除 PDF 安全限制
Abstract: 了解如何使用 Aspose.PDF for Java 解密 PDF。Java 示例集包括直接的所有者密码解密以及一种 try-style 解密工作流，帮助您在不抛出异常的情况下处理失败。
---
## 解密 PDF 文件

当您拥有所有者密码且需要从 PDF 中移除安全限制时，请使用此工作流。

### 步骤

1. 创建一个 `PdfFileSecurity` 实例。
2. 将加密的 PDF 绑定到 `bindPdf`。
3. 调用 `decryptFile` 或 `tryDecryptFile` 使用所有者密码。
4. 如果解密成功，保存输出。
5. 关闭安全对象。

### Java 示例

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
