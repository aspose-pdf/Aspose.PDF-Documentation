---
title: 署名管理
linktitle: 署名管理
type: docs
weight: 80
url: /ja/java/signature-management/
description: PdfFileSignature ファサードを使用して、Java で既存の PDF 署名を削除する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF 署名を削除する
Abstract: Aspose.PDF for Java を使用して、署名済み PDF から署名を削除する方法を学びます。現在の Java のサンプルセットでは、名前で既存の署名を削除し、更新されたドキュメントを保存する方法をカバーしています。関連する署名フィールドをクリーンアップする別のサンプルは含まれていません。
---
## 署名の削除

このワークフローは、ドキュメントから既存のデジタル署名を削除する必要がある場合に使用します。

### 手順

1. 作成 `PdfFileSignature` インスタンス化し、署名済みPDFをバインドしてください。
2. 署名コレクションを読み取り、署名名を選択してください。
3. 呼び出す `removeSignature` その名前で。
4. 更新されたファイルを保存し、ファサードオブジェクトを閉じます。

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
