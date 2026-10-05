---
title: PDF 認証
linktitle: PDF 認証
type: docs
weight: 30
url: /ja/java/pdf-certification/
description: PdfFileSignature と DocMDPSignature を使用して、Java で PDF 文書を認証する方法を学びましょう。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で DocMDP 権限を使用して PDF 文書を認証する
Abstract: Aspose.PDF for Java を使用して PDF 文書を認証する方法を学びます。Java の例では、PdfFileSignature と DocMDPSignature および DocMDPAccessPermissions を組み合わせて、フォーム入力と署名のために文書を認証し、その他の変更は制限します。
---
## PDF 文書を認証する

署名後も文書を信頼できる状態に保ちつつ、定義された種類の変更を許可したい場合に認証を使用します。

### 手順

1. `PdfFileSignature` のインスタンスを作成してソースPDFをバインドしてください。
2. ビルドする `PKCS7` 証明書と証明書パスワードを使用した署名オブジェクト。
3. その署名を…でラップする `DocMDPSignature` 必要なものと共に `DocMDPAccessPermissions` 値。
4. 呼び出す `certify` 対象ページ、署名メタデータ、表示領域、そしてMDP署名とともに。
5. 認証済み PDF を保存し、ファサードオブジェクトを閉じます。

### Java の例

```java
public static void certifyPdfWithMdpSignature(Path inputFile, Path certificateFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        DocMDPSignature signature = new DocMDPSignature(
                createPkcs7(certificateFile, "Certified for form filling and signing"),
                DocMDPAccessPermissions.FillingInForms);
        pdfSignature.certify(1, "Certified for form filling and signing", "security@example.com", "New York, USA", true, signatureRectangle(), signature);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```
