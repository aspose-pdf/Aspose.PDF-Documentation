---
title: Java を使用したマークアップ注釈
linktitle: マークアップ注釈
type: docs
weight: 20
url: /ja/java/pdfannotationeditor-class/markup-annotations/
description: Java を使用して PDF ドキュメントにハイライト、下線、波線、取り消し線の注釈を追加、検査、削除する方法を学びます。
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイルのマークアップ注釈の操作"
Abstract: "この記事では、Java を使用して PDF ドキュメント内のテキストマークアップ注釈を作成、検査、および削除する方法について説明します。リポジトリの Java サンプルに基づき、ハイライト、下線、波線、取り消し線の注釈を取り上げています。"
---
## ハイライト、下線、波線、または取り消し線の注釈の追加

1. 入力 PDF を開き、マークアップ注釈が表示されるページ領域を選択してください。
2. 必要な注釈タイプを作成し、メタデータや視覚プロパティを構成してください。
3. 注釈をページコレクションに追加し、ドキュメントを保存してください。

```java
public static void addTextHighlightAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        HighlightAnnotation highlightAnnotation = new HighlightAnnotation(
                document.getPages().get_Item(1), new Rectangle(300, 750, 320, 770, true));
        document.getPages().get_Item(1).getAnnotations().add(highlightAnnotation);
        document.save(outputFile.toString());
    }
}
```

```java
public static void addTextUnderlineAnnotation(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        UnderlineAnnotation underlineAnnotation = new UnderlineAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 713.664, 308.708, 720.769, true));
        underlineAnnotation.setTitle("Aspose User");
        underlineAnnotation.setSubject("Inserted Underline 1");
        underlineAnnotation.setFlags(AnnotationFlags.Print);
        underlineAnnotation.setColor(Color.getBlue());
        document.getPages().get_Item(1).getAnnotations().add(underlineAnnotation);
        document.save(outputFile.toString());
    }
}
```
