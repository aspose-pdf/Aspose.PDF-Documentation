---
title: Java を使用したテキストベースの注釈
linktitle: テキスト注釈
type: docs
weight: 10
url: /ja/java/pdfannotationeditor-class/text-based-annotations/
description: "Java を使用して PDF ドキュメント内のテキスト注釈、自由テキスト注釈、取り消し線注釈を追加・検査・削除する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java でのテキスト PDF 注釈の操作"
Abstract: "この記事では、Java を使用して PDF ドキュメント内のテキストベースの注釈を作成・読み取り・削除する方法を説明します。テキスト注釈、自由テキスト注釈、取り消し線注釈について、Java のサンプル実装に基づいて解説します。"
---
## テキスト注釈の追加

1. 入力 PDF を開き、テキスト注釈を配置する対象ページを選択してください。
2. `TextAnnotation` を作成し、その矩形を定義して、タイトル・サブジェクト・フラグ・カラーを設定してください。
3. 注釈をページに追加し、更新されたドキュメントを保存してください。

```java
public static void textAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextAnnotation textAnnotation = new TextAnnotation(
                document.getPages().get_Item(1), new Rectangle(299.988, 613.664, 428.708, 680.769, true));
        textAnnotation.setTitle("Aspose User");
        textAnnotation.setSubject("Inserted text 1");
        textAnnotation.setFlags(AnnotationFlags.Print);
        textAnnotation.setColor(Color.getBlue());

        document.getPages().get_Item(1).getAnnotations().add(textAnnotation, false);
        document.save(outputFile.toString());
    }
}
```

## フリーテキスト注釈の追加

1. ソース PDF を読み込み、対象ページとフリーテキスト注釈の矩形を選択してください。
2. `FreeTextAnnotation` を作成し、デフォルトの外観を初期化して、タイトルと色を設定してください。
3. ページに注釈を追加し、結果を保存してください。

```java
public static void freeTextAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        FreeTextAnnotation freeTextAnnotation = new FreeTextAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(299, 713, 308, 720, true),
                new DefaultAppearance());
        freeTextAnnotation.setTitle("Aspose User");
        freeTextAnnotation.setColor(Color.getLightGreen());

        document.getPages().get_Item(1).getAnnotations().add(freeTextAnnotation);
        document.save(outputFile.toString());
    }
}
```
