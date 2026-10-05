---
title: "PDF ファイルの復号化"
linktitle: "PDF ファイルの復号化"
type: docs
weight: 20
url: /ja/java/decrypt-pdf-file/
description: PdfFileSecurity ファサードを使用して Java で PDF を復号化する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF のセキュリティ制限を解除する
Abstract: Aspose.PDF for Java を使用して PDF を復号化する方法を学びます。Java のサンプルセットには、直接所有者パスワードの復号化と、例外をスローせずに失敗を処理できる try スタイルの復号化ワークフローが含まれています。
---
## PDF ファイルの復号化

所有者パスワードを持ち、PDF のセキュリティを削除する必要がある場合に、このワークフローを使用します。

### 手順

1. 作成する `PdfFileSecurity` インスタンス。
2. 暗号化されたPDFをバインドする `bindPdf`。
3. 呼び出し `decryptFile` または `tryDecryptFile` 所有者パスワードで。
4. 復号に成功した場合、出力を保存してください。
5. セキュリティオブジェクトを閉じます。

### Java の例

```java
public static void decryptPdfWithOwnerPassword(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    fileSecurity.decryptFile("owner_password");
    fileSecurity.save(outputFile.toString());
    fileSecurity.close();
}

public static void tryDecryptPdfWithoutException(Path inputFile, Path outputFile) {
    PdfFileSecurity fileSecurity = new PdfFileSecurity();
    fileSecurity.bindPdf(inputFile.toString());
    if (fileSecurity.tryDecryptFile("owner_password")) {
        fileSecurity.save(outputFile.toString());
    } else {
        System.out.println("Decryption failed. Check password or document security.");
    }
    fileSecurity.close();
}
```
