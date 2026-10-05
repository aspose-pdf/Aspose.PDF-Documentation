---
title: PDFを先頭から分割
linktitle: PDFを先頭から分割
type: docs
weight: 10
url: /ja/java/split-pdf-from-beginning/
description: JavaでPdfFileEditorファサードを使用してPDFを先頭から分割します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFの最初のページを新しいドキュメントに抽出する
Abstract: Aspose.PDF for Java を使用して、PDFを先頭から分割する方法を学びましょう。Java のサンプルでは PdfFileEditor を使用してドキュメントの最初の 3 ページを取得し、別々の PDF として保存します。
---
## PDFを先頭から分割

Java のサンプルはソースドキュメントから最初の3ページを抽出します。

### 手順

1. 作成 `PdfFileEditor` インスタンス。
2. 呼び出し `splitFromFirst` ソースファイル、保持するページ数、出力ファイルとともに。
3. 新しい PDF ドキュメントを保存してください。

```java
public static void splitPdfFromBeginning(Path inputFile, Path outputFile) {
    PdfFileEditor pdfFileEditor = new PdfFileEditor();
    pdfFileEditor.splitFromFirst(inputFile.toString(), 3, outputFile.toString());
}
```
