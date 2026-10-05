---
title: Java を使用した注釈と特殊テキスト
linktitle: 注釈と特殊テキスト
type: docs
weight: 40
url: /ja/java/annotation-and-special-text/
description: Aspose.PDF for Java を使用して、PDF ドキュメント内のスタンプ注釈、ハイライトテキスト、上付きまたは下付きコンテンツからテキストを抽出する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
## ハイライトテキストの抽出

ページの注釈を反復し、マークされたテキストを読み取る `HighlightAnnotation`。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. ターゲットの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 上の [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) オブジェクトを反復処理してください。
1. 各アノテーションが [HighlightAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/highlightannotation/) 型であるかを確認してください。
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

スタンプ注釈から標準外観ストリームを読み取り、それをそのまま `TextAbsorber` に渡します。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. ターゲットの [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) 上の [Annotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotation/) オブジェクトを反復処理してください。
1. 注釈をタイプが `Stamp` のものにフィルタリングしてください。
1. [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textabsorber/) を作成し、スタンプ注釈の外観辞書から通常の外観エントリを要求してください。
1. 外観の [XForm](https://reference.aspose.com/pdf/java/com.aspose.pdf/xform/) を訪問し、抽出したテキストを印刷してください。

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

各フラグメントについて、抽出したテキストと上付きまたは下付きフラグの両方を必要とする場合は、`TextFragmentAbsorber` を使用してください。

1. ソース PDF を [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) インスタンスで開いてください。
1. フラグメントレベルのテキスト分析用に [TextFragmentAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragmentabsorber/) を作成してください。
1. 対象の [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) を訪問し、その [TextFragment](https://reference.aspose.com/pdf/java/com.aspose.pdf/textfragment/) オブジェクトを収集してください。
1. それらのフラグメントを反復処理し、`fragment.getTextState()` から上付きおよび下付きのフラグ付きでテキストを読み取ってください。
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
