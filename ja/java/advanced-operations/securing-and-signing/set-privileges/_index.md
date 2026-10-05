---
title: JavaでPDFファイルを暗号化および復号化
linktitle: PDFファイルを暗号化および復号化
type: docs
weight: 70
url: /ja/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: JavaでPDFの権限設定、ファイルの暗号化、保護されたPDFの復号化、パスワードの変更方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFの権限を設定し、暗号化を管理する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF ファイルを保護する方法を説明します。ユーザー パスワードとオーナー パスワードによるドキュメントの暗号化、権限制限の適用、ファイルの復号化、パスワードの変更、例外安全な方法の有無にかかわらず特権を設定する方法をカバーしています。
---
Aspose.PDF for Java は PDF のセキュリティ操作を介して提供します `PdfFileSecurity` ファサード。

## ユーザー パスワードとオーナー パスワードで PDF の暗号化

1. 作成してバインドする [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ソース PDF ドキュメントへのファサード。
1. 設定 [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) そして [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) 例に必要なプロパティ。
1. 更新された PDF ドキュメントを次の方法で保存する [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/)。

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

## 特定のアルゴリズムでPDFの暗号化

`encryptPdfWithEncryptionAlgorithm` 使用 `KeySize.x256` と一緒に `Algorithm.AES` より強力な暗号化設定を適用するために。

## 保護されたPDFの復号化

1. 作成してバインドする [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ソース PDF ドキュメントへのファサード。
1. 保護された文書をオーナーパスワードで復号します。
1. 更新された PDF ドキュメントを次の方法で保存する [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/)。

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

例のセットには他にも含まれています `tryDecryptPdfWithoutException`、返します `false` 復号に失敗したときに例外を投げる代わりに。

## パスワードを変更し、セキュリティをリセットする

ザ `PdfFileSecurityExamples` クラスは示します:

- `changeUserAndOwnerPassword` 両方のパスワードを置き換える。
- `changePasswordAndResetSecurity` パスワードを変更し、権限を再適用することを1ステップで行う。
- `tryChangePasswordWithoutException` 例外をスローしないパスワード変更フロー用に。

## ドキュメントの権限の設定

印刷やコピーなどの操作を制限するには:

1. 作成してバインドする [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) ソース PDF ドキュメントへのファサード。
1. 必要な設定を行う [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 権限または暗号化オプション。
1. サンプルで必要なプロパティを設定してください。
1. 更新された PDF ドキュメントを次の方法で保存する [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/)。

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
