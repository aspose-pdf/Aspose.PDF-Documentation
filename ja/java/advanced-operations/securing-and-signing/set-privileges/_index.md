---
title: "Java で PDF ファイルを暗号化および復号化"
linktitle: "PDF ファイルの暗号化および復号化"
type: docs
weight: 70
url: /ja/java/set-privileges-encrypt-and-decrypt-pdf-file/
description: "Java で PDF の権限設定、ファイルの暗号化、保護された PDF の復号化、パスワードの変更方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF の権限を設定し、暗号化の管理"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ファイルを保護する方法を説明します。ユーザー パスワードとオーナー パスワードによるドキュメントの暗号化、権限制限の適用、ファイルの復号化、パスワードの変更、および例外安全でない方法による権限設定の方法をカバーしています。"
---
Aspose.PDF for Java は、PDF のセキュリティ操作を `PdfFileSecurity` ファサードを通じて提供します。

## ユーザー パスワードとオーナー パスワードで PDF の暗号化

1. [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) インスタンスを作成し、ソース PDF ドキュメントにバインドしてください。
1. 例に必要な [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) および [KeySize](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/keysize/) プロパティを設定してください。
1. 更新された PDF ドキュメントを [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) を通じて保存してください。

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

## 特定のアルゴリズムで PDF の暗号化

`encryptPdfWithEncryptionAlgorithm` は `KeySize.x256` と `Algorithm.AES` を組み合わせて、より強力な暗号化設定を適用します。

## 保護された PDF の復号化

1. [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) インスタンスを作成し、ソース PDF ドキュメントにバインドしてください。
1. 保護された文書をオーナーパスワードで復号化してください。
1. 更新された PDF ドキュメントを [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) を通じて保存してください。

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}
```

例のセットには `tryDecryptPdfWithoutException` も含まれており、復号に失敗した場合に例外をスローする代わりに `false` を返します。

## パスワードの変更とセキュリティのリセット

`PdfFileSecurityExamples` クラスでは、以下の操作を示しています。

- `changeUserAndOwnerPassword`：ユーザー パスワードとオーナー パスワードの両方を置き換えます。
- `changePasswordAndResetSecurity`：パスワードを変更し、権限を再適用する操作を 1 ステップで実行します。
- `tryChangePasswordWithoutException`：例外をスローしないパスワード変更フロー用です。

## ドキュメントの権限の設定

印刷やコピーなどの操作を制限するには、次のように行います。

1. [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) インスタンスを作成し、ソース PDF ドキュメントにバインドしてください。
1. [DocumentPrivilege](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/documentprivilege/) 権限または暗号化オプションとして必要な設定を行ってください。
1. サンプルで必要なプロパティを設定してください。
1. 更新された PDF ドキュメントを [PdfFileSecurity](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/pdffilesecurity/) を通じて保存してください。

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
