---
title: 加密 PDF 文件
linktitle: 加密 PDF 文件
type: docs
weight: 30
url: /zh/java/encrypt-pdf-file/
description: 了解如何在 Java 中使用 PdfFileSecurity 类加密 PDF 并配置权限。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中加密 PDF 文件并定义用户权限
Abstract: 了解如何使用 Aspose.PDF for Java 加密 PDF。此 Java 示例集涵盖基于密码的加密（带受限权限）、侧重权限的加密以及使用 256 位密钥大小的基于 AES 的加密。
---
## 加密 PDF 文件

当需要使用密码和权限规则保护 PDF 时，使用 `PdfFileSecurity`。

### 步骤

1. 创建一个 `PdfFileSecurity` 实例。
2. 将源 PDF 绑定到 `bindPdf`。
3. 构建一个 `DocumentPrivilege` 匹配允许的操作的对象。
4. 根据所需的密钥大小和算法，调用相应的 `encryptFile` 重载。
5. 保存已加密的文件并关闭对象。

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
