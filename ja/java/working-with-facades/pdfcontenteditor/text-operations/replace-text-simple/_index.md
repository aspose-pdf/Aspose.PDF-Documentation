---
title: テキスト置換（シンプル）
linktitle: テキスト置換（シンプル）
type: docs
weight: 10
url: /ja/java/replace-text-simple/
description: "Java で Aspose.PDF の PdfContentEditor ファサードを使用して、PDF ドキュメント全体のテキストを置換する方法について学習してください。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java で PDF のテキストを置換"
Abstract: "この記事では、PDF をバインドし、置換テキストのスコープを設定し、すべての一致するテキストの出現箇所を置換し、更新されたドキュメントを Aspose.PDF for Java の PdfContentEditor ファサードを使用して保存する方法を示します。"
---
## ドキュメント全体のテキストの置換

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. 置換テキストの範囲を `ReplaceAll` に設定してください。
3. 検索テキストと置換テキストを指定して `replaceText(...)` を呼び出してください。
4. 更新された PDF ドキュメントを保存してください。

```java
public static void replaceTextSimple(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("33", "XXXIII ");
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
