---
title: "PDF ファイルの暗号化"
linktitle: "PDF ファイルの暗号化"
type: docs
weight: 30
url: /ja/java/encrypt-pdf-file/
description: Java の PdfFileSecurity ファサードを使用して、PDF の暗号化方法と権限設定方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF ファイルを暗号化し、ユーザー権限を定義する
Abstract: Aspose.PDF for Java を使用して PDF を暗号化する方法を学びます。Java のサンプルセットでは、制限付き権限を伴うパスワードベースの暗号化、権限に焦点を当てた暗号化、そして 256 ビットキーサイズの AES ベース暗号化がカバーされています。
---
## PDF ファイルの暗号化

使用 `PdfFileSecurity` PDF をパスワードと権限ルールで保護する必要があるとき。

### 手順

1. 作成する `PdfFileSecurity` インスタンス。
2. ソースPDFをバインドする `bindPdf`。
3. ビルドする `DocumentPrivilege` 許可されたアクションに一致するオブジェクト。
4. 適切なものを呼び出す `encryptFile` 必要なキーサイズとアルゴリズムのオーバーロード。
5. 保護されたファイルを保存し、オブジェクトを閉じます。

### Javaの例

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
