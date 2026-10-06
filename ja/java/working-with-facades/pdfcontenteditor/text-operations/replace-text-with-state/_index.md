---
title: "ステートでテキストの置換"
linktitle: "ステートでテキストの置換"
type: docs
weight: 20
url: /ja/java/replace-text-with-state/
description: Aspose.PDF の PdfContentEditor ファサードを使用して、Java でカスタム書式設定によるテキスト置換の方法を学びましょう。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での カスタム書式設定を使用して PDF のテキストの置換"
Abstract: 本記事では、PDF をバインドし、カスタム TextState を設定し、該当するすべてのテキストを置換し、更新されたドキュメントを Aspose.PDF for Java の PdfContentEditor ファサードを使用して保存する方法を示します。
---
## カスタム TextState でテキストの置換

1. ソース PDF を `PdfContentEditor` ファサードにバインドしてください。
2. 必要なカラーとフォントサイズで `TextState` を作成して構成してください。
3. 置換テキストのスコープを `ReplaceAll` に設定してください。
4. `replaceText(...)` を呼び出し、検索テキスト、置換テキスト、および設定済みの `TextState` を渡してください。
5. 更新された PDF ドキュメントを保存してください。

```java
public static void replaceTextWithState(Path inputFile, Path outputFile) {
    PdfContentEditor editor = new PdfContentEditor();
    try {
        editor.bindPdf(inputFile.toString());
        TextState textState = new TextState();
        textState.setForegroundColor(com.aspose.pdf.Color.getBlue());
        textState.setFontSize(14);
        editor.getReplaceTextStrategy().setReplaceScope(ReplaceTextStrategy.Scope.ReplaceAll);
        editor.replaceText("software", "SOFTWARE", textState);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
