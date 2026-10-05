---
title: 署名検証
linktitle: 署名検証
type: docs
weight: 90
url: /ja/java/signature-verification/
description: "PdfFileSignature ファサードを使用して、Java で PDF 署名を検証する方法を学習します。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF 署名の検証"
Abstract: "Aspose.PDF for Java を使用して PDF 署名を検証する方法を学びます。Java のサンプルでは、利用可能な最初の署名を選択し、署名を検証したうえで、文書全体をカバーしているかどうかを確認します。"
---
## PDF 署名の検証

既存の署名済み PDF に対して迅速な検証を行う必要がある場合は、このワークフローを使用してください。

### 手順

1. `PdfFileSignature` インスタンスを作成し、署名された PDF をバインドしてください。
2. 検査したい署名名を選択してください。
3. `verifySignature` を呼び出して署名を検証してください。
4. `coversWholeDocument` を呼び出してカバレッジを確認してください。
5. ファサードオブジェクトを閉じてください。

### Java の例

```java
public static void verifyPdfSignature(Path inputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        System.out.println("Signature '" + signatureName + "' is valid: " + pdfSignature.verifySignature(signatureName));
        System.out.println("Signature covers whole document: " + pdfSignature.coversWholeDocument(signatureName));
    } finally {
        pdfSignature.close();
    }
}
```
