---
title: "Java での PDF リンクの作成"
linktitle: "リンクの作成"
type: docs
weight: 10
url: /ja/java/create-links/
description: "Java で内部リンク、外部リンク、リモート PDF リンクを作成する方法を学びます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF ファイルにリンク注釈の作成"
Abstract: "この記事では、Aspose.PDF for Java を使用してリンク注釈を作成する方法を示します。LinkAnnotation オブジェクトにアクションを添付することで、起動アクション、リモートドキュメントへのナビゲーション、ドキュメント内ページナビゲーション、および URI ベースのウェブリンクをカバーしています。"
---
Aspose.PDF for Java は、`LinkAnnotation` をアクションオブジェクトとともに使用してリンクの動作を定義します。

## 起動アクションリンクの作成

リンク注釈が外部ファイルやターゲットを起動すべき場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象ページを選択してください。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成し、その境界線と色を設定してください。
1. 割り当て [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) して、ドキュメントを保存してください。

```java
public static void createLinkAnnotationLaunchAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        link.setAction(new LaunchAction(document, inputFile.toString()));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## リモートの Go-to リンクの作成

リンクが別の PDF ドキュメント内のページを開く必要がある場合、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページに [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成してください。
1. 割り当て [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) して、出力ファイルを保存してください。

```java
public static void createLinkAnnotationGoToRemoteAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToRemoteAction(inputFile.toString(), 1));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## 内部の go-to リンクの作成

リンクが同じ PDF ドキュメント内の別のページへ移動する必要がある場合、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成し、外観を設定してください。
1. 割り当て [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) して、目的のページへ移動し、ドキュメントを保存してください。

```java
public static void createLinkAnnotationGoToAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        Border border = new Border(link);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        link.setBorder(border);
        link.setColor(Color.getGreen());
        if (document.getPages().size() >= 4) {
            link.setAction(new GoToAction(document.getPages().get_Item(4)));
        } else {
            link.setAction(new GoToAction(document.getPages().get_Item(document.getPages().size())));
        }
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```

## URI リンクの作成

リンクが URI アクションを介して Web リソースを開く必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページ上に [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成してください。
1. [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) を割り当てて、出力ファイルを保存してください。

```java
public static void createLinkAnnotationGoToUriAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        LinkAnnotation link = new LinkAnnotation(page, new Rectangle(10, 580, 120, 600, true));
        link.setColor(Color.getGreen());
        link.setAction(new GoToURIAction("https://docs.aspose.com/pdf/python"));
        page.getAnnotations().add(link);
        document.save(outputFile.toString());
    }
}
```
