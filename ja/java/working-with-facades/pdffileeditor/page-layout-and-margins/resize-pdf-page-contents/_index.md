---
title: PDF ページコンテンツのサイズ変更
linktitle: PDF ページコンテンツのサイズ変更
type: docs
weight: 30
url: /ja/java/resize-pdf-page-contents/
description: Java の PdfFileEditor ファサードを使用して、選択した PDF ページのコンテンツのサイズを変更します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java で PDF ドキュメント内の既存ページコンテンツのサイズを変更する
Abstract: Aspose.PDF for Java を使用してページコンテンツのサイズ変更方法を学びます。Java のサンプルでは PdfFileEditor を使用して特定のページを対象にし、新しいコンテンツの幅と高さを適用し、サイズ変更操作が失敗した場合にワークフローを停止します。
---
## PDF ページコンテンツのサイズ変更

Java のサンプルはページ 1 と 3 のコンテンツ領域のサイズを変更し、ブール値の戻り値を確認します。

### 手順

1. 作成する `PdfFileEditor` インスタンス。
2. サイズ変更すべきコンテンツがあるページを選択します。
3. 呼び出し `resizeContents` 対象の幅と高さで。
4. 戻り値を確認し、続行する前に失敗を処理してください。
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
