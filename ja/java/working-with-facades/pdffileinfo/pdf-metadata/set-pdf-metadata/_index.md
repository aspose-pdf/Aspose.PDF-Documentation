---
title: PDF メタデータの設定
linktitle: PDF メタデータの設定
type: docs
weight: 50
url: /ja/java/set-pdf-metadata/
description: PdfFileInfo ファサードを使用して、Java で PDF メタデータを更新する方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF メタデータの更新
Abstract: Aspose.PDF for Java を使用して PDF メタデータを更新する方法を学びます。Java のサンプルでは PdfFileInfo を使用して、subject、title、keywords、creator などの標準メタデータフィールドを設定し、カスタムメタデータエントリを追加して、結果を新しい PDF に保存します。
---
## PDF メタデータの設定

PDF を保存する前に、ドキュメント情報を正規化または強化する必要がある場合は、このワークフローを使用してください。

### 手順

1. 作成する `PdfFileInfo` ソースPDF用のオブジェクト。
2. 更新したい標準メタデータフィールドを設定してください。
3. 任意のカスタムメタデータを追加 `setMetaInfo`。
4. 更新されたドキュメントを保存 `save()`。
5. 閉じる `PdfFileInfo` インスタンス。

### Java の例

```java
public static void setPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.setSubject("Aspose PDF for Java");
    pdfInfo.setTitle("Aspose PDF for Java");
    pdfInfo.setKeywords("Aspose, PDF, Java");
    pdfInfo.setCreator("Aspose Team");
    pdfInfo.setMetaInfo("CustomKey", "CustomValue");
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
