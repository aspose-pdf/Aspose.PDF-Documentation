---
title: "PDFにページ区切りの追加"
linktitle: "PDFにページ区切りの追加"
type: docs
weight: 20
url: /ja/java/add-page-breaks-in-pdf/
description: PdfFileEditor ファサードを使用して Java で PDF にページ区切りを挿入します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ドキュメントの固定位置にページ区切りを挿入する
Abstract: Aspose.PDF for Java を使用してページ区切りの追加方法を学びます。Java のサンプルでは PdfFileEditor.PageBreak を使用してページを特定の垂直位置で分割し、結果を新しい PDF として保存します。
---
## PDFにページ区切りの追加

ページを既知の Y 位置で複数のページに分割する必要がある場合は、このワークフローを使用します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 1つまたは複数作成する `PdfFileEditor.PageBreak` ページ番号と改ページ位置を含むエントリ。
3. ページブレーク配列を渡す `addPageBreak`。
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
