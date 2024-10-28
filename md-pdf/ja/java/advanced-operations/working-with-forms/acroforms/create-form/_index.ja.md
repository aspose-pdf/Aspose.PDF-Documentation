---
title: AcroFormsを作成する - Javaで記入可能なPDFを作成する
linktitle: AcroFormsを作成する
type: docs
weight: 10
url: /java/create-forms/
description: このセクションでは、Aspose.PDF for Javaを使用してPDFドキュメントにAcroFormsをゼロから作成する方法を説明します。
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## PDFドキュメントにフォームフィールドを追加する

[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) クラスは、PDFドキュメント内のフォームフィールドを管理するのに役立つFormという名前のコレクションを提供します。

フォームフィールドを追加するには：

1. 追加したいフォームフィールドを作成します。
2. [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form) コレクションのaddメソッドを呼び出します。

この例では、TextBoxFieldを追加する方法を示しています。同じアプローチで任意のフォームフィールドを追加できます：

1. まず、フィールドオブジェクトを作成し、そのプロパティを設定します。
2. 次に、フィールドをFormコレクションに追加します。

### TextBoxFieldの追加

テキストフィールドは、受信者がフォームにテキストを入力できるフォーム要素です。
 これは、ユーザーが自由に入力できるようにしたいときに使用されます。

以下のコードスニペットは、PDFドキュメントにTextBoxFieldを追加する方法を示しています。

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // ドキュメントを開く
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // フィールドを作成する
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("テキストボックス");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // ドキュメントにフィールドを追加する
        pdfDocument.getForm().add(textBoxField, 1);

        // 変更されたPDFを保存
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## RadioButtonFieldの追加

ラジオボタンは、複数の選択肢がある質問で、一つだけの回答が選べる場合に最も一般的に使用されます。

次のコードスニペットは、PDFドキュメントに[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)を追加する方法を示しています。

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // PDFファイルにページを追加
        pdfDocument.getPages().add();

        // ページ番号を引数としてRadioButtonFieldオブジェクトをインスタンス化
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // 最初のラジオボタンオプションを追加し、Rectangleオブジェクトを使用してその起点を指定
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // 2番目のラジオボタンオプションを追加
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // ラジオボタンをDocumentオブジェクトのformオブジェクトに追加
        pdfDocument.getForm().add(radio);
        // PDFファイルを保存
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


次のコードスニペットは、3つのオプションを持つ[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)を追加し、それらをテーブルセル内に配置する手順を示しています。

```java
public static void AddingRadioButtonAdvanced() {
        Document doc = new Document();
        Page page = doc.getPages().add();
        Table table = new Table();
        table.setColumnWidths("120 120 120");
        page.getParagraphs().add(table);
        Row r1 = table.getRows().add();
        Cell c1 = r1.getCells().add();
        Cell c2 = r1.getCells().add();
        Cell c3 = r1.getCells().add();

        RadioButtonField rf = new RadioButtonField(page);
        rf.setPartialName("radio");
        doc.getForm().add(rf, 1);

        RadioButtonOptionField opt1 = new RadioButtonOptionField();
        RadioButtonOptionField opt2 = new RadioButtonOptionField();
        RadioButtonOptionField opt3 = new RadioButtonOptionField();

        opt1.setOptionName("Item1");
        opt2.setOptionName("Item2");
        opt3.setOptionName("Item3");

        opt1.setWidth(15);
        opt1.setHeight(15);
        opt2.setWidth(15);
        opt2.setHeight(15);
        opt3.setWidth(15);
        opt3.setHeight(15);

        rf.add(opt1);
        rf.add(opt2);
        rf.add(opt3);

        opt1.setBorder(new Border(opt1));
        opt1.getBorder().setWidth(1);
        opt1.getBorder().setStyle(BorderStyle.Solid);
        opt1.getCharacteristics().setBorder(Color.getBlack());
        opt1.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt1.setCaption(new TextFragment("Item1"));
        opt2.setBorder(new Border(opt2));
        opt2.getBorder().setWidth(1);
        opt2.getBorder().setStyle(BorderStyle.Solid);
        opt2.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt2.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt2.setCaption(new TextFragment("Item2"));
        opt3.setBorder(new Border(opt3));
        opt3.getBorder().setWidth(1);
        opt3.getBorder().setStyle(BorderStyle.Solid);
        opt3.getCharacteristics().setBorder(java.awt.Color.BLACK);
        opt3.getDefaultAppearance().setTextColor(java.awt.Color.RED);
        opt3.setCaption(new TextFragment("Item3"));
        c1.getParagraphs().add(opt1);
        c2.getParagraphs().add(opt2);
        c3.getParagraphs().add(opt3);

        doc.save("RadioButtonField.pdf");
    }
```


## RadioButtonFieldにキャプションを追加する

以下のコードスニペットは、[RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField)に関連付けられるキャプションを追加する方法を示しています:

```java
public static void AddingCaptionToRadioButtonField() {
        // ソースPDFフォームを読み込む
        com.aspose.pdf.facades.Form form1 = new com.aspose.pdf.facades.Form(_dataDir + "RadioButtonField.pdf");
        Document document = new Document(_dataDir + "RadioButtonField.pdf");
        for (String item : form1.getFieldNames()) {
            System.out.println(item.toString());
            if (item.contains("radio1")) {
                RadioButtonField field0 = (RadioButtonField) document.getForm().get(item);
                RadioButtonOptionField fieldoption = new RadioButtonOptionField();
                fieldoption.setOptionName("Yes");
                fieldoption.setPartialName("Yesname");

                var updatedFragment = new TextFragment("test123");
                updatedFragment.getTextState().setFont(FontRepository.findFont("Arial"));
                updatedFragment.getTextState().setFontSize(10);
                updatedFragment.getTextState().setLineSpacing(6.32f);

                // TextParagraphオブジェクトを作成
                TextParagraph par = new TextParagraph();

                // 段落の位置を設定
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // ワードラッピングモードを指定
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // 新しいTextFragmentを段落に追加
                par.appendLine(updatedFragment);

                // TextBuilderを使用してTextParagraphを追加
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## コンボボックスフィールドの追加

コンボボックスは、ドキュメントにドロップダウンメニューを追加するフォームフィールドです。

次のコードスニペットは、PDFドキュメントに[コンボボックス](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField)フィールドを追加する方法を示しています。

```java
public static void AddingComboboxField() {
        // Documentオブジェクトを作成
        Document doc = new Document();
        // ドキュメントオブジェクトにページを追加
        doc.getPages().add();
        // コンボボックスフィールドオブジェクトをインスタンス化
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // コンボボックスにオプションを追加
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // コンボボックスオブジェクトをドキュメントオブジェクトのフォームフィールドコレクションに追加
        doc.getForm().add(combo);
        // PDFドキュメントを保存
        doc.save("ComboBox_Added.pdf");
    }
```

## フォームにツールチップを追加

Documentクラスは、PDFドキュメント内のフォームフィールドを管理するFormというコレクションを提供します。
 フォームフィールドにツールチップを追加するには、FieldクラスのAlternateNameを使用します。Adobe Acrobatは「代替名」をフィールドツールチップとして使用します。

以下のコードスニペットは、Javaでフォームフィールドにツールチップを追加する方法を示しています。

```java
public static void AddTooltipToFormField() {
        // ソースPDFフォームを読み込む
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // フィールドを取得する
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // テキストフィールドのツールチップを設定する
        textBoxField.setAlternateName("テキストボックスのツールチップ");

        // 変更されたドキュメントを保存する
        doc.save("output.pdf");
    }
```