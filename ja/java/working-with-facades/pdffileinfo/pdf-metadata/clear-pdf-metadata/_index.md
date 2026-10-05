---
title: PDF メタデータをクリア
linktitle: PDF メタデータをクリア
type: docs
weight: 10
url: /ja/java/clear-pdf-metadata/
description: PdfFileInfo ファサードを使用して Java で PDF メタデータをクリアする方法を学びます。
lastmod: "2026-10-05"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF メタデータのクリア
Abstract: Aspose.PDF for Java を使用して PDF メタデータをクリアする方法を学びます。Java の例では PdfFileInfo を使用し、`clearInfo()` で保存されたドキュメント情報を削除し、クリーンアップされた PDF を新しいファイルに保存します。
---
## PDF メタデータをクリア

PDF を共有またはアーカイブする前に保存されたドキュメント情報を削除する必要がある場合は、この Workflow を使用してください。

### 手順

1. 作成 `PdfFileInfo` 入力 PDF のオブジェクト。
2. 呼び出す `clearInfo()` ドキュメントのメタデータを削除するために。
3. 結果を新しいファイルに保存する `save()`。
4. 閉じる `PdfFileInfo` インスタンス。

### Java の例

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
