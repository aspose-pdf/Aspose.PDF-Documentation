---
title: "外部フィールドのコピー"
linktitle: "外部フィールドのコピー"
type: docs
weight: 80
url: /ja/java/copy-outer-field/
description: Aspose.PDF の FormEditor ファサードを使用して、Java で PDF ドキュメント間でフォームフィールドをコピーする方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java で PDF フォームフィールドをドキュメント間でコピーする
Abstract: この記事では、宛先 PDF を作成し、FormEditor ファサードにバインドし、別のドキュメントからフィールドをコピーし、Aspose.PDF for Java を使用して結果を保存する方法を示します。
---
## 別の PDF からフィールドのコピー

1. 少なくとも 1 ページの宛先 PDF を作成してください。
2. 宛先PDFをバインドする `FormEditor` ファサード。
3. 呼び出す `copyOuterField(...)` ソースドキュメントのパス、フィールド名、対象ページ、座標とともに。
4. 更新された宛先文書を保存してください。

```java
public static void copyOuterField(Path inputFile, Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();
        document.save(outputFile.toString());
    }

    FormEditor editor = new FormEditor();
    try {
        editor.bindPdf(outputFile.toString());
        editor.copyOuterField(inputFile.toString(), "First Name", 1, 200, 600);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```
