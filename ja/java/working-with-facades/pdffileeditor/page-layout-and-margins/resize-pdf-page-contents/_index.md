---
title: PDF ページコンテンツのサイズ変更
linktitle: PDF ページコンテンツのサイズ変更
type: docs
weight: 30
url: /ja/java/resize-pdf-page-contents/
description: Java の PdfFileEditor ファサードを使用して、選択した PDF ページのコンテンツのサイズを変更します。
lastmod: "2026-10-06"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ドキュメント内の既存ページコンテンツのサイズの変更"
Abstract: Aspose.PDF for Java を使用してページコンテンツのサイズ変更方法を学びます。Java のサンプルでは PdfFileEditor を使用して特定のページを対象にし、新しいコンテンツの幅と高さを適用し、サイズ変更操作が失敗した場合にワークフローを停止します。
---
## PDF ページコンテンツのサイズ変更

Java のサンプルはページ 1 と 3 のコンテンツ領域のサイズを変更し、ブール値の戻り値を確認します。

### 手順

1. `PdfFileEditor` インスタンスを作成してください。
2. サイズ変更すべきコンテンツがあるページを選択してください。
3. 対象の幅と高さを指定して `resizeContents` を呼び出してください。
4. 戻り値を確認し、失敗を処理してから続行してください。
5. 更新されたドキュメントを保存してください。

### Java の例

```java
public static void resizePdfPageContents(Path inputFile, Path outputFile) {
    PdfFileEditor pdfEditor = new PdfFileEditor();
    if (!pdfEditor.resizeContents(inputFile.toString(), outputFile.toString(), new int[] {1, 3}, 400, 750)) {
        throw new IllegalStateException("Failed to resize PDF page contents.");
    }
}
```
