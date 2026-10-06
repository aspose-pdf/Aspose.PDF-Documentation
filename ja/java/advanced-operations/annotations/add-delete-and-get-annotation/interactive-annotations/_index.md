---
title: Java を使用したインタラクティブ注釈
linktitle: インタラクティブ注釈
type: docs
weight: 60
url: /ja/java/interactive-annotations/
description: "Aspose.PDF for Java を使用して、PDF ドキュメントにリンク注釈を追加、検査、削除する方法を学んでください。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での インタラクティブな PDF 注釈の操作"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF ファイル内のインタラクティブなリンク注釈を操作する方法を説明します。テキストの検索、マッチしたテキスト領域上にリンク注釈を作成すること、既存のリンク注釈を読み取ること、およびそれらを削除することについて解説します。"
---
このセクションのインタラクティブ注釈は、PDF ビューア内でユーザーの操作に応答するリンクおよびボタンベースのワークフローに焦点を当てています。

## リンクアノテーションの追加

ページ上のテキストにクリック可能なリンクを配置する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象テキストフラグメントを特定し、その長方形の上に [LinkAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/linkannotation/) を作成してください。
1. [GoToURIAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/gotouriaction/) を割り当て、更新されたドキュメントを保存してください。

```java
public static void linkAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("file");
        document.getPages().get_Item(1).accept(textFragmentAbsorber);

        var phoneNumberFragment = textFragmentAbsorber.getTextFragments().get_Item(1);
        LinkAnnotation linkAnnotation = new LinkAnnotation(
                document.getPages().get_Item(1),
                phoneNumberFragment.getRectangle());
        linkAnnotation.setAction(new GoToURIAction("https://www.aspose.com"));

        document.getPages().get_Item(1).getAnnotations().add(linkAnnotation);
        document.save(outputFile.toString());
    }
}
```

## リンク注釈の取得

この例では、ページのアノテーション コレクションをスキャンし、各リンク注釈の位置を報告します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 対象ページのアノテーションを反復処理してください。
1. [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` で注釈をフィルタリングし、それらの矩形を出力してください。

```java
public static void linkGet(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                System.out.println(annotation.getRect());
            }
        }
    }
}
```

## リンク注釈の削除

既存のリンク注釈をページから削除する必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. タイプが [AnnotationType](https://reference.aspose.com/pdf/java/com.aspose.pdf/annotationtype/).`Link` の注釈を収集してください。
1. 収集された注釈を削除し、出力ファイルを保存してください。

```java
public static void linkDelete(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<Annotation> toDelete = new ArrayList<>();
        for (Annotation annotation : document.getPages().get_Item(1).getAnnotations()) {
            if (annotation.getAnnotationType() == AnnotationType.Link) {
                toDelete.add(annotation);
            }
        }
        for (Annotation annotation : toDelete) {
            document.getPages().get_Item(1).getAnnotations().delete(annotation);
        }
        document.save(outputFile.toString());
    }
}
```

## ライン注釈の追加

この例では、矢印スタイル、枠線設定、ポップアップノートを備えたインタラクティブな線アノテーションを作成します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 開始点と終了点を指定して [LineAnnotation](https://reference.aspose.com/pdf/java/com.aspose.pdf/lineannotation/) を作成してください。
1. 外観とポップアップ注釈を設定し、ドキュメントを保存してください。

```java
public static void lineAnnotationAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        LineAnnotation lineAnnotation = new LineAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(550, 93, 562, 439, true),
                new Point(556, 99),
                new Point(556, 443));

        lineAnnotation.setTitle("John Smith");
        lineAnnotation.setColor(Color.getRed());
        lineAnnotation.setStartingStyle(LineEnding.OpenArrow);
        lineAnnotation.setEndingStyle(LineEnding.OpenArrow);

        Border border = new Border(lineAnnotation);
        border.setWidth(3);
        lineAnnotation.setBorder(border);

        PopupAnnotation popup = new PopupAnnotation(
                document.getPages().get_Item(1),
                new Rectangle(842, 124, 1021, 266, true));
        lineAnnotation.setPopup(popup);

        document.getPages().get_Item(1).getAnnotations().add(lineAnnotation);
        document.save(outputFile.toString());
    }
}
```

## ナビゲーションボタンの追加

PDF に前ページと次ページのボタンをインタラクティブなナビゲーション用に含める必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、ドキュメントに必要なページがあることを確認してください。
1. 事前定義されたナビゲーションアクションを持つ [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) コントロールを作成してください。
1. ボタンをフォーム コレクションに追加し、更新されたドキュメントを保存してください。

```java
public static void navigationButtonsAdd(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getPages().add();

        record ButtonConfig(String name, double xPos, PredefinedAction action) {}
        List<ButtonConfig> buttonConfigs = List.of(
                new ButtonConfig("Previous Page", 120.0, PredefinedAction.PrevPage),
                new ButtonConfig("Next Page", 230.0, PredefinedAction.NextPage));

        for (Page page : document.getPages()) {
            for (ButtonConfig config : buttonConfigs) {
                Rectangle rect = new Rectangle(config.xPos(), 10.0, config.xPos() + 100, 40.0, true);
                ButtonField button = new ButtonField(page, rect);
                button.setPartialName(config.name());
                button.setValue(config.name());
                button.getCharacteristics().setBorder(Color.getRed());
                button.getCharacteristics().setBackground(Color.getOrange().toRgb());
                button.getAnnotationActions().setOnReleaseMouseBtn(new NamedAction(config.action()));
                document.getForm().add(button);
            }
        }
        document.save(outputFile.toString());
    }
}
```

## 印刷ボタンの追加

この例では、ユーザーがクリックしたときに印刷コマンドをトリガーするボタンを作成します。

1. 新しい PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を作成し、ページを追加してください。
1. [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) を作成し、印刷の事前定義アクションを割り当ててください。
1. ボタンの枠線と背景を設定し、フォームに追加して、ドキュメントを保存してください。

```java
public static void printButtonAdd(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rect = new Rectangle(72, 748, 164, 768, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setAlternateName("Print current document");
        printButton.setColor(Color.getBlack());
        printButton.setPartialName("printBtn1");
        printButton.setValue("Print Document");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setStyle(BorderStyle.Solid);
        border.setWidth(2);
        printButton.setBorder(border);

        printButton.getCharacteristics().setBorder(Color.getBlue());
        printButton.getCharacteristics().setBackground(Color.getLightBlue().toRgb());

        document.getForm().add(printButton);
        document.save(outputFile.toString());
    }
}
```
