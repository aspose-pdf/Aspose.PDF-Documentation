---
title: 使用 Java 加密和解密 PDF 文件
linktitle: 加密和解密 PDF 文件
type: docs
weight: 70
url: /java/set-privileges-encrypt-and-decrypt-pdf-file/
description: 了解如何在 Java 中设置 PDF 权限、加密文件、解密受保护的 PDF 以及更改密码。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中设置 PDF 权限并管理加密
Abstract: 本文介绍如何使用 Aspose.PDF for Java 保护 PDF 文件。它涵盖使用用户和所有者密码加密文档、应用权限限制、解密文件、更改密码以及使用或不使用异常安全方法设置权限。
---
Aspose.PDF for Java 通过 `PdfFileSecurity` 外观公开 PDF 安全操作。

## 使用用户和所有者密码加密 PDF

1. 创建 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 外观并将其绑定到源 PDF 文档。
1. 配置示例所需的 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 和 [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) 属性。
1. 通过 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 保存更新后的 PDF 文档。

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
```

## 使用特定算法加密 PDF

`encryptPdfWithEncryptionAlgorithm` 使用`KeySize.x256` 和`Algorithm.AES` 来应用更强的加密设置。

## 解密受保护的 PDF

1. 创建 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 外观并将其绑定到源 PDF 文档。
1. 使用所有者密码解密受保护的文档。
1. 通过 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 保存更新后的 PDF 文档。

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

该示例集还包括`tryDecryptPdfWithoutException`，它在解密失败时返回`false`而不是抛出异常。

## 更改密码并重置安全性

`PdfFileSecurityExamples` 类演示：

- `changeUserAndOwnerPassword` 替换两个密码。
- `changePasswordAndResetSecurity` 可一步更改密码并重新应用权限。
- `tryChangePasswordWithoutException` 用于非抛出密码更改流程。

## 设置文档权限

要限制打印和复印等操作：

1. 创建 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 外观并将其绑定到源 PDF 文档。
1. 设置所需的 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 权限或加密选项。
1. 设置示例所需的属性。
1. 通过 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 保存更新后的 PDF 文档。

```java
public static void setPdfPrivilegesWithPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    privilege.setAllowCopy(false);
    fileSecurity.setPrivilege("user_password", "owner_password", privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```
