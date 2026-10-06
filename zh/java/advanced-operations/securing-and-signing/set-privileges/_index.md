---
title: 在 Java 中加密和解密 PDF 文件
linktitle: 加密和解密 PDF 文件
type: docs
weight: 70
url: /zh/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: 了解如何在 Java 中设置 PDF 权限、加密文件、解密受保护的 PDF，以及更改密码。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 在 Java 中设置 PDF 权限并管理加密
Abstract: 本文介绍了如何使用 Aspose.PDF for Java 对 PDF 文件进行安全保护。内容包括使用用户密码和所有者密码对文档加密、应用权限限制、解密文件、更改密码，以及在是否使用异常安全方法的情况下设置权限。
---
Aspose.PDF for Java 通过以下方式公开 PDF 安全操作 `PdfFileSecurity` 立面。

## 使用用户密码和所有者密码加密 PDF

1. 创建并绑定该 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 源 PDF 文档的外观层。
1. 配置 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 和 [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) 示例所需的属性。
1. 通过保存更新的 PDF 文档 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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

`encryptPdfWithEncryptionAlgorithm` 使用 `KeySize.x256` 一起 `Algorithm.AES` 以应用更强的加密设置。

## 解密受保护的 PDF

1. 创建并绑定该 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 源 PDF 文档的外观层。
1. 使用所有者密码解密受保护的文档。
1. 通过保存更新的 PDF 文档 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

示例集还包括 `tryDecryptPdfWithoutException`，返回 `false` 而不是在解密失败时抛出异常。

## 更改密码并重置安全性

该 `PdfFileSecurityExamples` 类演示:

- `changeUserAndOwnerPassword` 替换两个密码。
- `changePasswordAndResetSecurity` 一次性更改密码并重新应用权限。
- `tryChangePasswordWithoutException` 用于不抛出异常的密码更改流程。

## 设置文档权限

以限制打印和复制等操作：

1. 创建并绑定该 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) 源 PDF 文档的外观层。
1. 设置所需的 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 权限或加密选项。
1. 设置示例所需的属性。
1. 通过保存更新的 PDF 文档 [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/).

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
