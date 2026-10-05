---
title: "Java での PDFリンクの作成"
linktitle: "リンクの作成"
type: docs
weight: 10
url: /ja/java/create-links/
description: Javaで内部リンク、外部リンク、リモートPDFリンクの作成方法を学びます。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: JavaでPDFファイルにリンク注釈を作成する
Abstract: この記事では、Aspose.PDF for Java を使用してリンク注釈を作成する方法を示します。LinkAnnotation objectsにアクションを添付することで、起動アクション、リモートドキュメントへのナビゲーション、ドキュメント内ページナビゲーション、および URI ベースのウェブリンクをカバーしています。
---
Aspose.PDF for Java は使用します `LinkAnnotation` リンクの動作を定義するアクションオブジェクトとともに。

## 起動アクションリンクの作成

リンク注釈が外部ファイルやターゲットを起動すべき場合にこの例を使用します。

1. ソース PDF を開く [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 対象ページを選択してください。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成し、その境界線と色を設定してください。
1. 割り当て [LaunchAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/launchaction/) そして文書を保存してください。

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

リンクが別の PDF ドキュメント内のページを開くべき場合に、この例を使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) 対象ページで。
1. 割り当て [GoToRemoteAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoremoteaction/) および出力ファイルを保存してください。

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

この例は、リンクが同じ PDF ドキュメント内の別のページへ移動する必要がある場合に使用します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成し、外観を設定してください。
1. 割り当て [GoToAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotoaction/) 目的のページへ移動し、ドキュメントを保存してください。

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

リンクが URI アクションを介して Web リソースを開く必要がある場合はこの例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) ページ上で。
1. 割り当て [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) および出力ファイルを保存してください。

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
