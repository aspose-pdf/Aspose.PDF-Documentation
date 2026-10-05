---
title: "既存の PDF ファイルへの特権の設定"
linktitle: "既存の PDF ファイルへの特権の設定"
type: docs
weight: 40
url: /ja/java/set-privileges/
description: "PdfFileSecurity ファサードを使用して、Java で PDF の特権を設定する方法を学びます。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF の権限とアクセス制御の管理"
Abstract: "Aspose.PDF for Java を使用して PDF の権限を制御する方法を学習します。Java のサンプルセットには、パスワードなしで権限を適用する方法、ユーザーおよびオーナーパスワードを使用して権限を適用する方法、および成功フラグを返す try-style の権限更新ワークフローが含まれています。"
---
## 既存の PDF ファイルへの特権の設定

既存の PDF に対してユーザーが実行できる操作を変更する必要がある場合に、このワークフローを使用してください。

### 手順

1. `PdfFileSecurity` インスタンスを作成してください。
2. ソース PDF を `bindPdf` でバインドしてください。
3. `DocumentPrivilege` オブジェクトを作成し、許可されたアクションを設定してください。
4. 適切な `setPrivilege` または `trySetPrivilege` のオーバーロードを呼び出してください。
5. 更新が成功した場合は結果を保存し、その後オブジェクトを閉じてください。

### Java の例

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
