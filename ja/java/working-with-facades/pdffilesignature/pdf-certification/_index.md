---
title: PDF 認証
linktitle: PDF 認証
type: docs
weight: 30
url: /ja/java/pdf-certification/
description: PdfFileSignature と DocMDPSignature を使用して、Java で PDF 文書を認証する方法を学びましょう。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での DocMDP 権限を使用して PDF 文書の認証"
Abstract: "Aspose.PDF for Java を使用して PDF 文書を認証する方法を学びます。Java の例では、PdfFileSignature と DocMDPSignature および DocMDPAccessPermissions を組み合わせて、フォーム入力と署名のために文書を認証し、その他の変更を制限します。"
---
## PDF 文書の認証

署名後も文書を信頼できる状態に保ちつつ、定義された種類の変更を許可したい場合に、認証を使用します。

### 手順

1. `PdfFileSignature` のインスタンスを作成し、ソース PDF をバインドしてください。
2. `PKCS7` 証明書と証明書パスワードを使用して署名オブジェクトをビルドしてください。
3. その署名を、必要な `DocMDPAccessPermissions` 値とともに `DocMDPSignature` でラップしてください。
4. `certify` メソッドを、対象ページ、署名メタデータ、表示領域、および MDP 署名を引数として呼び出してください。
5. 認証済み PDF を保存し、ファサードオブジェクトを閉じてください。

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
