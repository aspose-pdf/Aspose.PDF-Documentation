---
title: "PDF メタデータのクリア"
linktitle: "PDF メタデータのクリア"
type: docs
weight: 10
url: /ja/java/clear-pdf-metadata/
description: "PdfFileInfo ファサードを使用して、Java で PDF メタデータをクリアする方法を学習してください。"
lastmod: "2026-10-06"
draft: false
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Aspose.PDF for Java を使用した PDF メタデータのクリア
Abstract: "Aspose.PDF for Java を使用して PDF メタデータをクリアする方法を学習してください。Java の例では PdfFileInfo を使用し、`clearInfo()` メソッドで保存されたドキュメント情報を削除した後、クリーンアップされた PDF を新しいファイルに保存してください。"
---
## PDF メタデータのクリア

PDF を共有またはアーカイブする前に保存されたドキュメント情報を削除する必要がある場合は、この Workflow を使用してください。

### 手順

1. 入力 PDF の `PdfFileInfo` オブジェクトを作成してください。
2. `clearInfo()` を呼び出して、ドキュメントのメタデータを削除してください。
3. 結果を新しいファイルに保存するには、`save()` を使用してください。
4. `PdfFileInfo` インスタンスを閉じてください。

### Java の例

```java
public static void clearPdfMetadata(Path inputFile, Path outputFile) {
    PdfFileInfo pdfInfo = new PdfFileInfo(inputFile.toString());
    pdfInfo.clearInfo();
    pdfInfo.save(outputFile.toString());
    pdfInfo.close();
}
```
