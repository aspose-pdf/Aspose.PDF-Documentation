---
title: "Java での PDF リンクの抽出"
linktitle: "リンクの抽出"
type: docs
weight: 30
url: /ja/java/extract-links/
description: "Java で PDF 文書からリンクアノテーションとハイパーリンクを抽出する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ファイルからリンクアノテーションと URI ターゲットの抽出"
Abstract: この記事では、Aspose.PDF for Java を使用して PDF 文書からリンクアノテーションを抽出する方法を説明します。ページ上のリンクアノテーションを列挙し、そのページインデックスと矩形を読み取り、GoToURIAction インスタンスから URI ターゲットを抽出する方法を示します。
---
ページ注釈を反復処理し、`AnnotationType.Link` でフィルタリングすることで、PDF リンクを検査できます。

## リンク注釈の抽出

ページ上のリンク注釈の位置とページ情報を取得する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ注釈を反復処理し、リンク注釈をフィルタリングしてください。
1. 一致する各リンクのページインデックスと矩形を読み取ってください。

```java
public static void extractLinkAnnotation(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                System.out.println("Page: " + linkAnnotation.getPageIndex()
                        + ", location: " + linkAnnotation.getRect());
            }
        }
    }
}
```

## ハイパーリンクの宛先の抽出

Web リンク注釈から対象の URI を読み取る必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. アクションが [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) オブジェクトである [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を検索してください。
1. 各ハイパーリンクについて、ページインデックスと URI ターゲットを出力してください。

```java
public static void extractHyperlinks(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link && annotation instanceof LinkAnnotation) {
                LinkAnnotation linkAnnotation = (LinkAnnotation) annotation;
                if (linkAnnotation.getAction() instanceof GoToURIAction) {
                    GoToURIAction action = (GoToURIAction) linkAnnotation.getAction();
                    System.out.println("Page " + linkAnnotation.getPageIndex() + ", URI:" + action.getURI());
                }
            }
        }
    }
}
```
