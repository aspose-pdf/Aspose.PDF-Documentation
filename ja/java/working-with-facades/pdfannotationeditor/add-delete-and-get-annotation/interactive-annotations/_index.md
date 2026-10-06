---
title: Java を使用したインタラクティブ アノテーション
linktitle: インタラクティブ アノテーション
type: docs
weight: 30
url: /ja/java/pdfannotationeditor-class/interactive-annotations/
description: "Java を使用して PDF ドキュメントにリンク アノテーションを追加、検査、削除する方法を学びます。"
lastmod: "2026-10-06"
TechArticle: true
AlternativeHeadline: "Java での インタラクティブ PDF アノテーションの操作"
Abstract: "この記事では、Java を使用して PDF ファイルのインタラクティブ リンク アノテーションを操作する方法を説明します。テキストの位置特定、該当テキスト領域上にリンク アノテーションを作成、既存のリンク アノテーションの読み取り、削除について解説します。"
---
## リンクアノテーションの追加

1. ソース PDF ドキュメントを読み込み、最初のページで対象のテキストを検索してください。
2. 一致したテキスト矩形を使用して `LinkAnnotation` を作成し、宛先 URI を割り当ててください。
3. アノテーションをページに追加し、更新された PDF を保存してください。

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        TextFragment phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);

        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1), phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```
