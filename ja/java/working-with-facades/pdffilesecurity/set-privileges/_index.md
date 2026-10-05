---
title: "既存のPDFファイルへの特権の設定"
linktitle: "既存のPDFファイルへの特権の設定"
type: docs
weight: 40
url: /ja/java/set-privileges/
description: PdfFileSecurityファサードを使用してJavaでPDFの特権を設定する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFの権限とアクセス制御を管理する
Abstract: Aspose.PDF for Javaを使用してPDF権限を制御する方法を学びます。Javaのサンプルセットには、パスワードなしで特権を適用する方法、ユーザーおよびオーナーパスワードを使用して特権を適用する方法、そして成功フラグを返す try-style 特権更新ワークフローが含まれています。
---
## 既存のPDFファイルへの特権の設定

既存のPDFでユーザーができることを変更する必要がある場合に、このワークフローを使用します。

### 手順

1. 作成する `PdfFileSecurity` インスタンス。
2. ソースPDFをバインドする `bindPdf`。
3. `DocumentPrivilege` オブジェクトを作成し、許可されたアクションを設定してください。
4. 適切なものを呼び出す `setPrivilege` または `trySetPrivilege` オーバーロード。
5. 更新が成功した場合は結果を保存し、その後オブジェクトを閉じます。

### Javaの例

```java
public static void setPdfPrivilegesWithoutPasswords(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    fileSecurity.setPrivilege(privilege);
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

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

public static void trySetPdfPrivilegesWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    DocumentPrivilege privilege = DocumentPrivilege.getForbidAll();
    privilege.setAllowPrint(true);
    if (fileSecurity.trySetPrivilege("user_password", "owner_password", privilege)) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Setting privileges failed. Check passwords or document state.");
    }
    fileSecurity.close();
}
```
