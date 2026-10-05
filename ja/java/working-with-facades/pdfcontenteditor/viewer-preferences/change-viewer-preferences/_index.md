---
title: ビューア設定の変更
linktitle: ビューア設定の変更
type: docs
weight: 20
url: /ja/java/change-viewer-preferences/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF ドキュメントのビューア設定を変更する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF ビューア設定を変更する
Abstract: この記事では、PDF をバインドし、現在のビューア設定値を変更し、更新されたドキュメントを Aspose.PDF for Java の PdfContentEditor ファサードを使用して保存する方法を示します。
---
## ビューア設定の変更

1. ソースPDFをバインドする `PdfContentEditor` ファサード。
2. 現在のビューア設定値を読み取ります。
3. 希望する追加フラグと組み合わせ、その結果を渡す `changeViewerPreference(...)`.
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
