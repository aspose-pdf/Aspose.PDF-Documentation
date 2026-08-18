---
title: 加密 PDF 文件
linktitle: 加密 PDF 文件
type: docs
weight: 30
url: /java/encrypt-pdf-file/
description: 了解如何使用 PdfFileSecurity 外观加密 PDF 并在 Java 中配置权限。
lastmod: "2026-06-09"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在Java中加密PDF文件并定义用户权限
Abstract: 了解如何使用 Aspose.PDF for Java 加密 PDF。 Java 示例集涵盖具有受限权限的基于密码的加密、以权限为中心的加密以及具有 256 位密钥大小的基于 AES 的加密。
---
## 加密 PDF 文件

当您需要使用密码和权限规则保护 PDF 时，请使用`PdfFileSecurity`。

### 步骤

1. 创建一个 `PdfFileSecurity` 实例。
2. 使用 `bindPdf` 绑定源 PDF。
3. 构建一个与允许的操作匹配的 `DocumentPrivilege` 对象。
4. 根据您需要的密钥大小和算法调用适当的 `encryptFile` 重载。
5. 保存受保护的文件并关闭对象。

### Java 示例

```java
public static void encryptPdfWithUserOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithPermissions(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getAllowAll();
    privilege.setAllowPrint(false);
    privilege.setAllowCopy(false);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void encryptPdfWithEncryptionAlgorithm(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.encryptFile("user_password", "owner_password", privilege, KeySize.x256, Algorithm.AES);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
