---
title: 署名の完全性チェック
linktitle: 署名の完全性チェック
type: docs
weight: 70
url: /ja/java/signature-integrity-checks/
description: JavaでPdfFileSignatureファサードを使用して、署名のカバレッジと完全性を検証する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDF署名のカバレッジと完全性を検証する
Abstract: Aspose.PDF for Javaを使用して署名の完全性を検査する方法を学びます。現在のJavaサンプルセットでは、`verifySignature`を使用して選択した署名を検証し、`coversWholeDocument`を使用して署名がPDF全体を保護しているかどうかを判断します。
---
## 署名の完全性をチェックする

この記事は、同じ検証ワークフローにマッピングされます `PdfFileSignatureExamples.java`.

### 手順

1. 署名済みPDFを結合する `PdfFileSignature`。
2. ドキュメントから署名名を選択してください。
3. 呼び出し `verifySignature` 署名内容を検証するために。
4. 呼び出し `coversWholeDocument` 文書全体のカバレッジを確認するために
5. ファサードオブジェクトを閉じます。

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
