---
title: 解密PDF文件
linktitle: 解密PDF文件
type: docs
weight: 20
url: /java/decrypt-pdf-file/
description: 了解如何使用 PdfFileSecurity 外观在 Java 中解密 PDF。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 消除 PDF 安全限制
Abstract: 了解如何使用 Aspose.PDF for Java 解密 PDF。 Java 示例集包括直接所有者密码解密和尝试式解密工作流程，使您可以在不引发异常的情况下处理失败。
---
## 解密PDF文件

当您拥有所有者密码并需要从 PDF 中删除安全性时，请使用此工作流程。

### 步骤

1. 创建一个 `PdfFileSecurity` 实例。
2. 使用`bindPdf`绑定加密的PDF。
3. 使用所有者密码调用 `decryptFile` 或 `tryDecryptFile`。
4. 如果解密成功，则保存输出。
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
