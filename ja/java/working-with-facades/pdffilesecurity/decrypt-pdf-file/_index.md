---
title: "PDF ファイルの復号化"
linktitle: "PDF ファイルの復号化"
type: docs
weight: 20
url: /ja/java/decrypt-pdf-file/
description: "PdfFileSecurity ファサードを使用して、Java で PDF を復号化する方法を学習します。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF のセキュリティ制限の解除"
Abstract: "Aspose.PDF for Java を使用して PDF を復号化する方法を学習します。Java のサンプルセットには、所有者パスワードによる直接的な復号化と、例外をスローせずに失敗を処理できる try スタイルの復号化ワークフローが含まれています。"
---
## PDF ファイルの復号化

所有者パスワードを所持しており、PDF のセキュリティを解除する必要がある場合に、このワークフローを使用してください。

### 手順

1. `PdfFileSecurity` インスタンスを作成してください。
2. 暗号化された PDF を `bindPdf` でバインドしてください。
3. 所有者パスワードを指定して `decryptFile` または `tryDecryptFile` を呼び出してください。
4. 復号に成功した場合は、出力を保存してください。
5. セキュリティオブジェクトを閉じてください。

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
