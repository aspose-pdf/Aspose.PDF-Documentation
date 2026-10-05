---
title: "スタンプの一覧表示"
linktitle: "スタンプの一覧表示"
type: docs
weight: 20
url: /ja/java/list-stamps/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java でページ上のゴムスタンプを一覧表示する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での PDF のゴムスタンプ一覧表示"
Abstract: この記事では、PDF をバインドし、ページ上のスタンプを取得し、Aspose.PDF for Java の PdfContentEditor ファサードを使用して結果のコレクションを検査する方法を示します。
---
## ページ上のスタンプの一覧表示

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. `getStamps(pageNumber)` を呼び出して、対象ページのスタンプを取得してください。
3. 結果の `StampInfo[]` コレクションを検柼してください。

```java
public static void listStamps(Path inputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        StampInfo[] stamps = editor.getStamps(1);
        System.out.println("Stamps on page 1: " + stamps.length);
    } finally {
        editor.close();
    }
}
```
