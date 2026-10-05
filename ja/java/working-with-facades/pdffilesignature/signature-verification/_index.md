---
title: 署名検証
linktitle: 署名検証
type: docs
weight: 90
url: /ja/java/signature-verification/
description: PdfFileSignature ファサードを使用して、Java で PDF 署名を検証する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF 署名を検証する
Abstract: Aspose.PDF for Java を使用して PDF 署名を検証する方法を学びます。Java のサンプルは、利用可能な最初の署名を選択し、署名を検証し、文書全体をカバーしているかどうかをチェックします。
---
## PDF 署名の検証

既存の署名済み PDF に対して迅速な検証を行う必要がある場合は、このワークフローを使用してください。

### 手順

1. 作成 `PdfFileSignature` インスタンスを作成し、署名されたPDFをバインドしてください。
2. 検査したい署名名を選択してください。
3. 呼び出し `verifySignature` 署名を検証するために。
4. 呼び出し `coversWholeDocument` カバレッジを確認するために。
5. ファサードオブジェクトを閉じます。

### Javaの例

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
