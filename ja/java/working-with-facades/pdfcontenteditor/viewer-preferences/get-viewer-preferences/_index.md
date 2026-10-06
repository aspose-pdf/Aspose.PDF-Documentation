---
title: "ビューア設定の取得"
linktitle: "ビューア設定の取得"
type: docs
weight: 10
url: /ja/java/get-viewer-preferences/
description: "Aspose.PDF の PdfContentEditor ファサードを使用して、Java で PDF ドキュメントのビューア設定を読み取る方法を学習します。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: Java で PDF ビューア設定を読み取る
Abstract: この記事では、Aspose.PDF for Java の PdfContentEditor ファサードを使用して PDF をバインドし、現在のビューア設定値を出力する方法を示します。
---
## 現在のビューア設定の取得

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. `getViewerPreference()` を呼び出して現在の値を読み取ってください。
3. 返されたプリファレンスフラグを確認または出力してください。

```java
public static void getViewerPreferences(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        System.out.println("Current viewer preference: " + editor.getViewerPreference());
    } finally {
        editor.close();
    }
}
```
