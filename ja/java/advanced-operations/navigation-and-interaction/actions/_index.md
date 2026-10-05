---
title: "Java での PDF アクションの操作"
linktitle: アクション
type: docs
weight: 20
url: /ja/java/actions/
description: Java を使用して PDF ファイルのドキュメント、ページ、フォーム アクションを追加、更新、削除する方法を学びます。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: "Java での PDF ファイルにドキュメント、ページ、フォーム アクションの追加"
Abstract: "この記事では、Aspose.PDF for Java を使用して PDF 文書のアクションを操作する方法を説明します。印刷やページ ナビゲーション用の名前付きアクション、フォームフィールドの非表示、フォームの送信、JavaScript 起動アクションの割り当て、ページのオープンおよびクローズアクションの追加または削除について取り上げます。"
---
Aspose.PDF for Java を使用すると、ボタン、ドキュメント、ページにアクションを割り当てて、PDF ファイルをインタラクティブにできます。

## 名前付き印刷アクションの追加

ページ上のボタンが印刷コマンドをトリガーする場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象ページを選択してください。
1. [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) を作成し、印刷用に [NamedAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/namedaction/) を割り当ててください。
1. ボタンをフォームに追加し、ドキュメントを保存してください。

```java
public static void addNamedActionPrint(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Page page = document.getPages().get_Item(1);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField printButton = new ButtonField(page, rect);
        printButton.setPartialName("printButton");
        printButton.setValue("Print");
        printButton.getAnnotationActions().setOnReleaseMouseBtn(
                new NamedAction(PredefinedAction.File_Print));

        Border border = new Border(printButton);
        border.setWidth(1);
        printButton.setBorder(border);

        document.getForm().add(printButton, 1);
        document.save(outputFile.toString());
    }
}
```

## 隠しアクションの追加

ボタンがチェックボックスなどのフォーム フィールドのセットを表示または非表示にする必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象のフォーム ウィジェットを収集してください。
1. ボタンを作成し、[HideAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/hideaction/) を割り当ててください。
1. ボタンをフォームに追加し、更新されたドキュメントを保存してください。

```java
public static void addNamedActionHide(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        List<WidgetAnnotation> checkboxes = new ArrayList<>();
        for (WidgetAnnotation field : document.getForm()) {
            if (field instanceof CheckboxField) {
                checkboxes.add(field);
            }
        }

        Rectangle rect = new Rectangle(10, 410, 140, 440, true);
        ButtonField hideButton = new ButtonField(document.getPages().get_Item(1), rect);
        hideButton.setPartialName("HideButton");
        hideButton.setValue("Hide Checkboxes");
        hideButton.getAnnotationActions().setOnReleaseMouseBtn(
                new HideAction(checkboxes.toArray(new WidgetAnnotation[0]), true));

        document.getForm().add(hideButton, 1);
        document.save(outputFile.toString());
    }
}
```

## ページナビゲーションボタンの追加

この例では、ドキュメント全体に最初、前へ、次へ、最後のページボタンを作成します。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 各ページにナビゲーションボタンを作成し、対応する事前定義アクションを割り当ててください。
1. ボタンをフォームに追加し、文書を保存してください。

```java
public static void addNavigationButtons(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        int totalPages = document.getPages().size();

        for (Page page : document.getPages()) {
            ButtonField firstPageButton = new ButtonField(page, new Rectangle(10, 10, 110, 40, true));
            firstPageButton.setPartialName("First Page");
            firstPageButton.setValue("First Page");
            firstPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            firstPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            firstPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            firstPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.FirstPage));
            document.getForm().add(firstPageButton);

            ButtonField previousPageButton = new ButtonField(page, new Rectangle(120, 10, 220, 40, true));
            previousPageButton.setPartialName("Previous Page");
            previousPageButton.setValue("Previous Page");
            previousPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            previousPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            previousPageButton.setReadOnly(document.getPages().indexOf(page) == 1);
            previousPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.PrevPage));
            document.getForm().add(previousPageButton);

            ButtonField nextPageButton = new ButtonField(page, new Rectangle(230, 10, 330, 40, true));
            nextPageButton.setPartialName("Next Page");
            nextPageButton.setValue("Next Page");
            nextPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            nextPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            nextPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            nextPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.NextPage));
            document.getForm().add(nextPageButton);

            ButtonField lastPageButton = new ButtonField(page, new Rectangle(340, 10, 440, 40, true));
            lastPageButton.setPartialName("Last Page");
            lastPageButton.setValue("Last Page");
            lastPageButton.getCharacteristics().setBorder(com.aspose.pdf.Color.getRed());
            lastPageButton.getCharacteristics().setBackground(com.aspose.pdf.Color.getOrange().toRgb());
            lastPageButton.setReadOnly(document.getPages().indexOf(page) == totalPages);
            lastPageButton.getAnnotationActions().setOnReleaseMouseBtn(
                    new NamedAction(PredefinedAction.LastPage));
            document.getForm().add(lastPageButton);
        }

        document.save(outputFile.toString());
    }
}
```

## 送信アクションの追加

ボタンがフォームデータを URL に送信すべき場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) をターゲット URL とフラグとともに作成してください。
1. アクションをボタンフィールドに割り当て、ドキュメントを保存してください。

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        FileSpecification submitUrl = new FileSpecification();
        submitUrl.setFileSystem("URL");
        submitUrl.setName("http://localhost:3000/submit");
        submitAction.setUrl(submitUrl);
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        Rectangle rect = new Rectangle(10, 10, 100, 40, true);
        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), rect);
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getAnnotationActions().setOnReleaseMouseBtn(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```

## ドキュメントレベルの起動アクションの追加

この例では、ドキュメントが開かれたとき、保存されたとき、または印刷されたときに実行される JavaScript アクションを割り当てます。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 必要な [JavascriptAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/javascriptaction/) オブジェクトを、ドキュメントイベント用に作成してください。
1. アクションを割り当てて、ドキュメントを保存してください。

```java
public static void addLaunchActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.setOpenAction(new JavascriptAction("app.launchURL('http://localhost:3000/open');"));
        document.getActions().setBeforeSaving(
                new JavascriptAction("app.launchURL('http://localhost:3000/save');"));
        document.getActions().setBeforePrinting(
                new JavascriptAction("app.launchURL('http://localhost:3000/print');"));

        document.save(outputFile.toString());
    }
}
```

## ページの開閉アクションの追加

特定のページが開くときと閉じるときにアクションをトリガーする必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象ページが存在することを確認してください。
1. ページナビゲーションと JavaScript アクションを作成してください。
1. ページアクションを割り当て、ドキュメントを保存してください。

```java
public static void addPageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        GoToAction action = new GoToAction(page);
        action.setDestination(new XYZExplicitDestination(page, 0, page.getPageInfo().getHeight(), 1));
        page.getActions().setOnOpen(action);
        page.getActions().setOnClose(
                new JavascriptAction("app.launchURL('http://localhost:3000/page/3');"));

        document.save(outputFile.toString());
    }
}
```

## ページアクションの削除

以前に割り当てられたオープンおよびクローズアクションをページからクリアする必要がある場合は、このアプローチを使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開き、対象ページが存在することを確認してください。
1. そのページからすべてのアクションを削除してください。
1. 更新されたドキュメントを保存してください。

```java
public static void removePageActions(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        if (document.getPages().size() < 3) {
            System.out.println("Error: The document does not have at least 3 pages.");
            return;
        }

        Page page = document.getPages().get_Item(3);
        page.getActions().removeActions();

        document.save(outputFile.toString());
    }
}
```
