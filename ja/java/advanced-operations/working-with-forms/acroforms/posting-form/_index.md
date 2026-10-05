---
title: Java を使用して PDF にフォームを投稿する
linktitle: フォームの投稿
type: docs
weight: 75
url: /ja/java/posting-form/
description: Aspose.PDF for Java を使用して PDF AcroForms に送信ボタンと送信アクションを追加します。
lastmod: "2026-10-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Java を使用して PDF ファイルに送信ボタンとフォーム投稿アクションを追加する
Abstract: この記事では、Aspose.PDF for Java を使用して PDF フォームに送信機能を追加する方法を示します。FormEditor を使用した送信ボタンの作成と、SubmitFormAction を使用して送信 URL とフラグをより細かく制御できるカスタムボタンフィールドの構築について説明しています。
---
Aspose.PDF for Java は、facadeベースおよび DOM ベースの送信ボタン作成の両方をサポートしています。

## FormEditor を使用した送信ボタンの追加

1. 作成する [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) ソース PDF ドキュメントのファサード。
1. 構成された送信ボタンオブジェクトを介して追加する [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) ファサード。
1. 更新されたPDFドキュメントを保存してください。

```java
public static void addSubmitButton(Path inputFile, Path outputFile) {
    FormEditor editor = new FormEditor();
    editor.bindPdf(inputFile.toString());
    try {
        editor.addSubmitBtn("submitbutton", 1, "Submit", "http://localhost/testing/show",
                100, 450, 150, 475);
        editor.save(outputFile.toString());
    } finally {
        editor.close();
    }
}
```

## 送信アクションを手動で追加

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 作成する [SubmitFormAction](https://reference.aspose.com/pdf/java/com.aspose.pdf/submitformaction/) および URL [FileSpecification](https://reference.aspose.com/pdf/java/com.aspose.pdf/filespecification/)。
1. 作成する [ButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/buttonfield/) 対象上で [Page](https://reference.aspose.com/pdf/java/com.aspose.pdf/page/) そして送信アクションを割り当てます。
1. 更新された PDF を保存します [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/)。

```java
public static void addSubmitAction(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        SubmitFormAction submitAction = new SubmitFormAction();
        submitAction.setUrl(new FileSpecification("http://localhost:3000/submit"));
        submitAction.setFlags(SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES);

        ButtonField submitButton = new ButtonField(document.getPages().get_Item(1), new Rectangle(10, 10, 100, 40));
        submitButton.setPartialName("SubmitButton");
        submitButton.setValue("Submit");
        submitButton.getPdfActions().add(submitAction);

        document.getForm().add(submitButton, 1);
        document.save(outputFile.toString());
    }
}
```
