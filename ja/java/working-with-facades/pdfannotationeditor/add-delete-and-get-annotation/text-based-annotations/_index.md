---
title: Java を使用したテキストベースの注釈
linktitle: テキスト注釈
type: docs
weight: 10
url: /ja/java/pdfannotationeditor-class/text-based-annotations/
description: Java を使用して PDF ドキュメント内のテキスト、自由テキスト、取り消し線注釈を追加、検査、削除する方法を学びます。
lastmod: "2026-10-05"
TechArticle: true
AlternativeHeadline: Java でテキスト PDF 注釈を操作する
Abstract: この記事では、Java を使用して PDF ドキュメント内のテキストベースの注釈を作成、読み取り、削除する方法を説明します。テキスト注釈、自由テキスト注釈、取り消し線注釈を、Java のサンプル実装に基づいてカバーしています。
---
## テキスト注釈の追加

1. 入力 PDF を開き、テキスト注釈を配置すべきページを対象にしてください。
2. 作成する `TextAnnotation`, その矩形を定義し、タイトル、サブジェクト、フラグ、カラーを設定してください。
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

1. ソースPDFを読み込み、対象ページとフリーテキストノートの矩形を選択してください。
2. 作成する `FreeTextAnnotation`, デフォルトの外観を初期化し、タイトルと色を設定してください。
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
