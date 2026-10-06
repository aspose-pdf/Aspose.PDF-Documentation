---
title: 署名管理
linktitle: 署名管理
type: docs
weight: 80
url: /ja/java/signature-management/
description: PdfFileSignature ファサードを使用して、Java で既存の PDF 署名を削除する方法を学びます。
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF 署名の削除"
Abstract: "Aspose.PDF for Java を使用して、署名済み PDF から署名を削除する方法を学習します。現在の Java サンプルセットでは、名前で既存の署名を削除し、更新されたドキュメントを保存する方法をカバーしています。関連する署名フィールドをクリーンアップする別のサンプルは含まれていません。"
---
## 署名の削除

このワークフローは、ドキュメントから既存のデジタル署名を削除する必要がある場合に使用します。

### 手順

1. `PdfFileSignature` インスタンスを作成し、署名済み PDF をバインドしてください。
2. 署名コレクションを読み取り、署名名を選択してください。
3. その名前で `removeSignature` を呼び出してください。
4. 更新されたファイルを保存し、ファサードオブジェクトを閉じてください。

### Java の例

```java
public static void removeSignature(Path inputFile, Path outputFile) {
    PdfFileSignature pdfSignature = new PdfFileSignature();
    try {
        pdfSignature.bindPdf(inputFile.toString());
        SignatureName signatureName = pdfSignature.getSignatureNames().get_Item(0);
        pdfSignature.removeSignature(signatureName);
        pdfSignature.save(outputFile.toString());
    } finally {
        pdfSignature.close();
    }
}
```

現在の Java サンプルセットには、署名を削除した後に関連する署名フィールドを削除するための個別のメソッドは含まれていません。
