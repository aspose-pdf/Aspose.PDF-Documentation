---
title: "PDF へのページ区切りの追加"
linktitle: "PDF へのページ区切りの追加"
type: docs
weight: 20
url: /ja/java/add-page-breaks-in-pdf/
description: "PdfFileEditor ファサードを使用して、Java で PDF にページ区切りを挿入します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ドキュメントへの固定位置でのページ区切り挿入"
Abstract: "Aspose.PDF for Java を使用してページ区切りを追加する方法を学習します。Java のサンプルでは、PdfFileEditor.PageBreak を使用して、特定の垂直位置でページを分割し、結果を新しい PDF として保存します。"
---
## PDF へのページ区切りの追加

ページを既知の Y 位置で複数のページに分割する必要がある場合は、このワークフローを使用してください。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. 1 つまたは複数の `PdfFileEditor.PageBreak` エントリを、ページ番号と改ページ位置を含めて作成してください。
3. ページブレーク配列を `addPageBreak` に渡してください。
4. 更新された PDF ドキュメントを保存してください。

### Java の例

```java
public static void addPageBreaksInPdf(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    pdfEditor.addPageBreak(inputFile.toString(), outputFile.toString(), new PdfFileEditor.PageBreak[] {
            new PdfFileEditor.PageBreak(1, 400)
    });
}
```
