---
title: "Java での PDF リンクの更新"
linktitle: "リンクの更新"
type: docs
weight: 20
url: /ja/java/update-links/
description: "Java で PDF リンクの外観と宛先を更新する方法を学習してください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用した PDF ファイルのリンク注釈の外観とウェブ宛先の更新"
Abstract: "この記事では、Aspose.PDF for Java を使用して既存のリンク注釈を更新する方法を示します。例では、リンクでカバーされたテキストの色を変更すること、リンク注釈の色を更新すること、およびウェブリンクの対象 URI を置き換えることをデモンストレーションしています。"
---
既存のリンクは、ページ上でリンク注釈を見つけ、その外観またはアクションのいずれかを更新することで編集できます。

## リンク付きテキストの色の更新

リンク注釈でカバーされたテキスト領域の色を変更する必要がある場合にこの例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. リンク注釈を検索し、各注釈領域からテキスト検索矩形を作成してください。
1. 一致したテキストフラグメントの色を変更し、文書を保存してください。

```java
public static void linkAnnotationUpdateTextColor(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                Rectangle rect = annotation.getRect();
                rect.setLLX(rect.getLLX() - 2);
                rect.setLLY(rect.getLLY() - 2);
                rect.setURX(rect.getURX() + 2);
                rect.setURY(rect.getURY() + 2);
                absorber.setTextSearchOptions(new TextSearchOptions(rect));
                absorber.visit(document.getPages().get_Item(1));
                for (TextFragment textFragment : absorber.getTextFragments()) {
                    textFragment.getTextState().setForegroundColor(Color.getRed());
                }
            }
        }

        document.save(outputFile.toString());
    }
}
```

## リンク枠の色の更新

既存のリンク注釈の表示色を変更する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ注釈を反復処理し、[LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) オブジェクトをフィルタリングしてください。
1. リンク注釈の色を更新し、ドキュメントを保存してください。

```java
public static void linkAnnotationUpdateBorder(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                linkAnnotation.setColor(Color.getRed());
            }
        }

        document.save(outputFile.toString());
    }
}
```

## Web リンクの宛先の更新

既存の Web リンクを新しい URI に変更する場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. アクションが [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) であるリンク注釈を検索してください。
1. URI を新しいものに置き換え、更新されたドキュメントを保存してください。

```java
public static void linkAnnotationUpdateWebDestination(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    action.setURI("https://www.aspose.com");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```
