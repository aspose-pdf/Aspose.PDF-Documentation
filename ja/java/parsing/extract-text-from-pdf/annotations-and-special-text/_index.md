---
title: Java を使用した注釈と特殊テキスト
linktitle: 注釈と特殊テキスト
type: docs
weight: 40
url: /ja/java/annotation-and-special-text/
description: Aspose.PDF for Java を使用して、PDF ドキュメント内のスタンプ注釈、ハイライトテキスト、上付きまたは下付きコンテンツからテキストを抽出する方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## ハイライトテキストの抽出

ページの注釈を反復し、マークされたテキストを読み取る `HighlightAnnotation`.

1. ソース PDF を a で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. イテレートする [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) ターゲット上のオブジェクト [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. 各アノテーションが対象かどうかを確認します。 [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) 型付けされたアノテーションクラスにキャストする前に。
1. 各ハイライトアノテーションからマーキングされたテキストを読み取り、コンソールに出力してください。

```java
public static void extractHighlightedText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation instanceof HighlightAnnotation) {
                HighlightAnnotation highlightAnnotation = (HighlightAnnotation) annotation;
                System.out.println(highlightAnnotation.getMarkedText());
            }
        }
    }
}
```

## スタンプ注釈からテキストの抽出

スタンプ注釈から標準外観ストリームを読み取り、それをそのまま渡す `TextAbsorber`.

1. ソース PDF を a で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. イテレートする [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) ターゲット上のオブジェクト [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/)。
1. タイプが ... のアノテーションにフィルタリングする `Stamp`.
1. 作成 [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) そして、スタンプアノテーションの外観辞書から通常の外観エントリを要求してください。
1. 外観を訪問してください。 [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) そして、抽出したテキストを印刷します。

```java
public static void extractStampText(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Stamp) {
                TextAbsorber absorber = new TextAbsorber();
                Object[] xforms = new Object[1];
                if (annotation.getAppearance().tryGetValue("N", xforms) && xforms[0] instanceof XForm) {
                    absorber.visit((XForm) xforms[0]);
                    System.out.println(absorber.getText());
                }
            }
        }
    }
}
```

## 上付き文字と下付き文字のテキストの詳細の抽出

使用 `TextFragmentAbsorber` 各フラグメントで抽出したテキストと、上付きまたは下付きフラグの両方が必要な場合。

1. ソース PDF を a で開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンス。
1. 作成 [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) フラグメントレベルのテキスト分析用。
1. ターゲットを訪問する [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そしてそれを収集する [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) オブジェクト。
1. それらのフラグメントを反復処理し、上付きおよび下付きのフラグと共にテキストを読み取ります。 `fragment.getTextState()`。
1. 抽出した詳細を出力ファイルに書き込んでください。

```java
public static void extractSuperSubDetails(Path inputFile, Path outputFile, int pageNumber) throws Exception {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber absorber = new TextFragmentAbsorber();
        document.getPages().get_Item(pageNumber).accept(absorber);
        StringBuilder details = new StringBuilder();
        for (TextFragment fragment : absorber.getTextFragments()) {
            details.append("Text: '").append(fragment.getText())
                    .append("' | Superscript: ").append(fragment.getTextState().isSuperscript())
                    .append(" | Subscript: ").append(fragment.getTextState().isSubscript())
                    .append(System.lineSeparator());
        }
        Files.writeString(outputFile, details.toString());
    }
}
```
