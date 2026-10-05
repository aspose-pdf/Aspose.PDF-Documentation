---
title: "PDF ドキュメントへの署名"
linktitle: "PDF ドキュメントへの署名"
type: docs
weight: 10
url: /ja/java/pdf-signing/
description: "PdfFileSignature ファサードを使用して、Java で PDF ドキュメントに署名する方法を学びます。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java でのデジタル署名による PDF ドキュメントへの署名"
Abstract: Aspose.PDF for Java を使用して PDF ドキュメントに署名する方法を学びます。Java のサンプルセットでは、設定された証明書パスとパスワードを使用した署名、および理由、連絡先情報、場所、権限などの署名メタデータを含む明示的な PKCS7 署名オブジェクトを使用した署名をカバーしています。
---
## PDF ドキュメントへの署名

`PdfFileSignature` を使用して、PDF に可視デジタル署名を適用します。

### 手順

1. `PdfFileSignature` インスタンスを作成し、ソース PDF をバインドしてください。
2. 証明書をロードするには、`setCertificate` メソッドを使用するか、`PKCS7` オブジェクトを作成してください。
3. 対象ページ、表示設定、署名矩形、および署名データを引数として `sign` メソッドを呼び出してください。
4. 署名された PDF を保存し、Facade オブジェクトを閉じてください。

### Java の例

```java
public static void signPdfWithCertificateObject(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.sign(1, false, signatureRectangle(), createPkcs7(certificateFile, "Document approval"));
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}

public static void signPdfWithBasicParameters(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        pdfSignature.setCertificate(certificateFile.toString(), CERTIFICATE_PASSWORD);
        pdfSignature.sign(1, "Document approval", "qa@example.com", "New York, USA", false, signatureRectangle());
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
