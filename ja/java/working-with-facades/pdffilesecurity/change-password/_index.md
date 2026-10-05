---
title: PDF ファイルのパスワード変更
linktitle: PDF ファイルのパスワード変更
type: docs
weight: 10
url: /ja/java/change-password/
description: PdfFileSecurity ファサードを使用して、Java で PDF のパスワードを変更する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF のユーザーおよび所有者パスワードを更新する
Abstract: Aspose.PDF for Java を使用して PDF パスワードを変更する方法を学びます。Java のサンプルセットでは、ユーザーおよび所有者パスワードを直接変更する方法、セキュリティ設定をリセットしながらパスワードを変更する方法、成功フラグを返すトライスタイルのパスワード変更ワークフローがカバーされています。
---
## PDF ファイルのパスワードの変更

使用 `PdfFileSecurity` 既に保護されたPDFで資格情報をローテーションする必要があるとき。

### 手順

1. 作成する `PdfFileSecurity` インスタンス。
2. 保護されたPDFにバインドする `bindPdf`。
3. 適切なものを呼び出す `changePassword` オーバーロード、特権とキーサイズもリセットしたいかどうかに応じて。
4. 更新されたファイルを保存し、セキュリティオブジェクトを閉じます。

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
