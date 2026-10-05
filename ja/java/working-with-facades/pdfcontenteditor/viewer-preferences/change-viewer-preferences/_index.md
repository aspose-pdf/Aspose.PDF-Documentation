---
title: ビューア設定の変更
linktitle: ビューア設定の変更
type: docs
weight: 20
url: /ja/java/change-viewer-preferences/
description: "Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF ドキュメントのビューア設定を変更する方法を学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF ビューア設定の変更"
Abstract: "この記事では、PDF をバインドし、現在のビューア設定値を変更し、更新されたドキュメントを Aspose.PDF for Java の PdfContentEditor ファサードを使用して保存する方法を説明します。"
---
## ビューア設定の変更

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. 現在のビューア設定値を読み取ってください。
3. 希望する追加フラグと組み合わせ、その結果を `changeViewerPreference(...)` に渡してください。
4. 更新された PDF ドキュメントを保存してください。

```java
public static void changeViewerPreferences(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.changeViewerPreference(editor.getViewerPreference() | 1);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
