---
title: 署名の完全性チェック
linktitle: 署名の完全性チェック
type: docs
weight: 70
url: /ja/java/signature-integrity-checks/
description: "Java で PdfFileSignature ファサードを使用して、署名のカバレッジと完全性を検証する方法を学びます。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF 署名のカバレッジと完全性の検証"
Abstract: "Aspose.PDF for Java を使用して署名の完全性を検査する方法を学びます。現在の Java サンプルセットでは、`verifySignature` を使用して選択した署名を検証し、`coversWholeDocument` を使用して署名が PDF 全体を保護しているかどうかを判断します。"
---
## 署名の完全性のチェック

この記事は、`PdfFileSignatureExamples.java` で公開されているのと同じ検証ワークフローに対応しています。

### 手順

1. 署名済み PDF を `PdfFileSignature` にバインドしてください。
2. ドキュメントから署名名を選択してください。
3. 署名内容を検証するために `verifySignature` を呼び出してください。
4. 文書全体のカバレッジを確認するために `coversWholeDocument` を呼び出してください。
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
