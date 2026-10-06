---
title: PDF ファイルのパスワード変更
linktitle: PDF ファイルのパスワード変更
type: docs
weight: 10
url: /ja/java/change-password/
description: "PdfFileSecurity ファサードを使用して、Java で PDF のパスワードを変更する方法を学習します。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ユーザーおよび所有者パスワードの更新"
Abstract: "Aspose.PDF for Java を使用して PDF のパスワードを変更する方法を学習します。Java のサンプルセットでは、ユーザーおよび所有者パスワードの直接的な変更、セキュリティ設定のリセットを伴うパスワード変更、および成功フラグを返すトライスタイルのパスワード変更ワークフローがカバーされています。"
---
## PDF ファイルのパスワードの変更

`PdfFileSecurity` を使用して、既に保護されている PDF の資格情報をローテーションする場合に利用します。

### 手順

1. `PdfFileSecurity` インスタンスを作成してください。
2. `bindPdf` を使用して保護された PDF にバインドしてください。
3. 特権およびキーサイズもリセットするかどうかに応じて、適切な `changePassword` のオーバーロードを呼び出してください。
4. 更新されたファイルを保存し、セキュリティオブジェクトを閉じてください。

### Java の例

```java
public static void changeUserAndOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void changePasswordAndResetSecurity(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.changePassword("owner_password", "new_user_password", "new_owner_password", privilege, KeySize.x128);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryChangePasswordWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryChangePassword("owner_password", "new_user_password", "new_owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Password change failed. Check owner password or document security.");
    }
    fileSecurity.close();
}
```
