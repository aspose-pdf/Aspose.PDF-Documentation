---
title: テキスト置換（シンプル）
linktitle: テキスト置換（シンプル）
type: docs
weight: 10
url: /ja/java/replace-text-simple/
description: JavaでAspose.PDFのPdfContentEditorファサードを使用してPDFドキュメント全体のテキストを置換する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: JavaでPDFのテキストを置換
Abstract: この記事では、PDFをバインドし、置換テキストのスコープを設定し、すべての一致するテキストの出現箇所を置換し、更新されたドキュメントをAspose.PDF for JavaのPdfContentEditorファサードを使用して保存する方法を示します。
---
## ドキュメント全体のテキストの置換

1. ソース PDF をバインドする `PdfContentEditor` ファサード。
2. 置換テキストの範囲を設定 `ReplaceAll`。
3. 呼び出す `replaceText(...)` 検索テキストと置換テキストで。
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
