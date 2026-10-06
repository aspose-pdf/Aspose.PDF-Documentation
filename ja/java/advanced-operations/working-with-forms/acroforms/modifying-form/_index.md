---
title: AcroForm の変更
linktitle: AcroForm の変更
type: docs
weight: 45
url: /ja/java/modifying-form/
description: "Aspose.PDF for Java を使用して、PDF ドキュメント内の AcroForm フィールドを変更できます。変更内容には、テキストのクリア、制限の設定、フィールドのスタイリング、フィールドの削除が含まれます。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java での PDF フォームフィールドの変更およびカスタマイズ"
Abstract: この記事では、Aspose.PDF for Java を使用して AcroForm コンテンツを変更する方法を説明します。タイプライターフォームリソースからテキストをクリアすること、テキストフィールドの長さ制限を設定および読み取ること、フォームフィールドの Font 外観を変更すること、名前で特定のフィールドを削除することについて解説しています。
---
フォームの保守は、フィールドレベルの編集とフォーム関連ページリソースのクリーンアップの両方を含むことがよくあります。

## 埋め込みフォームリソースのテキストのクリア

フォームオブジェクト自体を削除せずに、タイプライターフォームの内容を空にする必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ページのフォームリソースを反復処理し、タイプライターフォームを検索してください。
1. 吸収されたテキストフラグメントをクリアし、ドキュメントを保存してください。

```java
public static void clearTextInForm(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        for (XForm form : document.getPages().get_Item(1).getResources().getForms()) {
            if ("Typewriter".equals(form.getIT()) && "Form".equals(form.getSubtype())) {
                TextFragmentAbsorber absorber = new TextFragmentAbsorber();
                absorber.visit(form);

                for (TextFragment fragment : absorber.getTextFragments()) {
                    fragment.setText("");
                }
            }
        }
        document.save(outputFile.toString());
    }
}
```

## テキスト フィールドの長さ制限の設定

テキスト フィールドが限定された文字数のみを受け付ける場合は、この例を使用してください。

1. [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/formeditor/) オブジェクトを作成し、ソース PDF にバインドしてください。
1. 対象フィールドの最大長さを設定してください。
1. 更新されたドキュメントを保存してください。

```java
public static void setFieldLimit(Path inputFile, Path outputFile) {
    FormEditor form = new FormEditor();
    form.bindPdf(inputFile.toString());
    try {
        form.setFieldLimit("First Name", 15);
        form.save(outputFile.toString());
    } finally {
        form.close();
    }
}
```

## テキストフィールドの長さ制限の取得

テキストフィールドの現在の最大長さを確認する必要がある場合は、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. フォームコレクションから対象フィールドにアクセスしてください。
1. [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) から制限値を読み取り、出力してください。

```java
public static void getFieldLimit(Path inputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            System.out.println("Limit: " + textBoxField.getMaxLen());
        }
    }
}
```

## Form フィールドのフォントの変更

既存のテキストフィールドに別のフォントまたは外観を使用する必要がある場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. ターゲットの [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) にアクセスし、新しいデフォルトの外観を設定してください。
1. 更新された PDF を保存してください。

```java
public static void setFormFieldFont(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        Field field = document.getForm().getFields()[0];
        if (field instanceof TextBoxField textBoxField) {
            textBoxField.setDefaultAppearance(new DefaultAppearance(
                    FontRepository.findFont("Calibri"), 10, com.aspose.pdf.Color.getBlack().toRgb()));
        }

        document.save(outputFile.toString());
    }
}
```

## 名前でフォームフィールドの削除

特定のフィールドを AcroForm から削除する必要がある場合に、この例を使用してください。

1. ソース PDF の [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) を開いてください。
1. 名前でフォームから対象フィールドを削除してください。
1. 更新されたドキュメントを保存してください。

```java
public static void deleteFormField(Path inputFile, Path outputFile) {
    try (Document document = new Document(inputFile.toString())) {
        document.getForm().delete("First Name");
        document.save(outputFile.toString());
    }
}
```
