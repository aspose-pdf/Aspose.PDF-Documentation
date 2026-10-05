---
title: "AcroForm の作成 - Java で記入可能な PDF の作成"
linktitle: "AcroForm の作成"
type: docs
weight: 10
url: /ja/java/create-form/
description: "Aspose.PDF for Java を使用して、PDF ドキュメントにゼロから AcroForm フィールドを作成します。"
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "Java を使用して PDF ファイルにインタラクティブな AcroForm フィールドの作成"
Abstract: "この記事では、Aspose.PDF for Java を使用して AcroForm フィールドを作成する方法について説明します。テキストボックス、マルチウィジェットテキストフィールド、ラジオボタン、コンボボックス、チェックボックス、リストボックス、署名フィールド、バーコードフィールドなどのインタラクティブな PDF フォームをカバーしています。"
---
Aspose.PDF for Java では、最初から幅広い種類の AcroForm フィールドタイプを作成できます。

## テキストボックスフィールドの作成

新しい PDF フォームに単一行のテキスト入力フィールドを追加する必要がある場合は、この例を使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. 対象の矩形を指定して [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) を作成し、外観を設定してください。
1. フィールドをフォームに追加して、ドキュメントを保存してください。

```java
public static void addTextBoxField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle rectangle = new Rectangle(10, 600, 110, 620, true);
        TextBoxField textBoxField = new TextBoxField(page, rectangle);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");
        textBoxField.setDefaultAppearance(new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()));

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField, 1);
        document.save(outputFile.toString());
    }
}
```

## 複数のウィジェットを持つテキストボックスフィールドの作成

同じテキストフィールドの値がページ上の複数の位置に表示される場合は、この例を使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. フィールドウィジェットのために複数の矩形と外観を定義してください。
1. [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) を作成し、各ウィジェットを構成して、ドキュメントを保存してください。

```java
public static void addTextBoxFieldNt(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        Rectangle[] rects = {
                new Rectangle(10, 600, 110, 620, true),
                new Rectangle(10, 630, 110, 650, true),
                new Rectangle(10, 660, 110, 680, true)
        };

        DefaultAppearance[] defaultAppearances = {
                new DefaultAppearance("Arial", 10, Color.getDarkBlue().toRgb()),
                new DefaultAppearance("Helvetica", 12, Color.getDarkGreen().toRgb()),
                new DefaultAppearance(FontRepository.findFont("Calibri"), 14, Color.getDarkMagenta().toRgb())
        };

        TextBoxField textBoxField = new TextBoxField(page, rects);
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Some text");

        int index = 0;
        for (WidgetAnnotation widget : textBoxField) {
            widget.setDefaultAppearance(defaultAppearances[index]);
            index++;
        }

        Border border = new Border(textBoxField);
        border.setWidth(1);
        border.setStyle(BorderStyle.Dashed);
        border.setDash(new Dash(3, 3));
        textBoxField.setBorder(border);

        textBoxField.getCharacteristics().setBorder(Color.getRed());
        textBoxField.getCharacteristics().setBackground(Color.getYellow().toRgb());

        document.getForm().add(textBoxField);
        document.save(outputFile.toString());
    }
}
```

## ラジオボタンフィールドの作成

この例は、フォームがユーザーに事前定義されたセットから1つのオプションを選択させる場合に使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) を作成し、必要なオプションを追加してください。
1. フィールドをフォームに追加し、PDF を保存してください。

```java
public static void addRadioButton(Path outputFile) {
    try (Document document = new Document()) {
        document.getPages().add();

        RadioButtonField radio = new RadioButtonField(document.getPages().get_Item(1));
        radio.addOption("Option 1", new Rectangle(100, 640, 120, 680, true));
        radio.addOption("Option 2", new Rectangle(140, 640, 160, 680, true));

        document.getForm().add(radio);
        document.save(outputFile.toString());
    }
}
```

## コンボボックスフィールドの作成

ユーザーがドロップダウンリストから1つの値を選択すべき場合に、この例を使用します。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) を作成し、その選択可能なオプションを追加してください。
1. デフォルトの選択を設定し、ドキュメントを保存してください。

```java
public static void addComboBox(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ComboBoxField combo = new ComboBoxField(page, new Rectangle(100, 640, 150, 656, true));
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        combo.setSelected(3);

        document.getForm().add(combo);
        document.save(outputFile.toString());
    }
}
```

## チェックボックス フィールドの作成

フォームが同意や機能選択などの真偽オプションを必要とする場合は、この例を使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) を作成し、その外観を設定してください。
1. チェックボックスをフォームに追加し、出力ファイルを保存してください。

```java
public static void addCheckboxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        CheckboxField checkbox = new CheckboxField(page, new Rectangle(50, 620, 100, 650, true));
        checkbox.getCharacteristics().setBackground(Color.getAqua().toRgb());
        checkbox.setStyle(BoxStyle.Circle);

        document.getForm().add(checkbox);
        document.save(outputFile.toString());
    }
}
```

## リストボックス フィールドの作成

フォームに複数の利用可能な選択肢を可視リストで表示する必要がある場合は、この例を使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) を作成し、利用可能なオプションを追加してください。
1. フィールドをフォームに追加して、ドキュメントを保存してください。

```java
public static void addListBoxFieldToPdf(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        ListBoxField listBox = new ListBoxField(page, new Rectangle(50, 650, 100, 700, true));
        listBox.setPartialName("list");
        listBox.addOption("Red");
        listBox.addOption("Green");
        listBox.addOption("Blue");

        document.getForm().add(listBox);
        document.save(outputFile.toString());
    }
}
```

## 署名フィールドの作成

ドキュメントがデジタル署名用に可視領域を確保する必要がある場合は、この例を使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) を必要な矩形内で作成してください。
1. フィールドをフォームに追加して、出力 PDF を保存してください。

```java
public static void addSignatureField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        SignatureField signatureField = new SignatureField(page, new Rectangle(100, 700, 200, 800, true));
        signatureField.setPartialName("Signature1");
        document.getForm().add(signatureField);
        document.save(outputFile.toString());
    }
}
```

## バーコードフィールドの作成

フォームがバーコードフィールド内に機械可読データを表示すべき場合は、この例を使用してください。

1. 新しい PDF を作成し、[Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) にページを追加してください。
1. [BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) を作成し、バーコードの値を追加してください。
1. フィールドをフォームに追加して、ドキュメントを保存してください。

```java
public static void addBarcodeField(Path outputFile) {
    try (Document document = new Document()) {
        Page page = document.getPages().add();

        BarcodeField barcode = new BarcodeField(page, new Rectangle(100, 700, 200, 740, true));
        barcode.setPartialName("Barcode1");
        barcode.addBarcode("1234567890");
        document.getForm().add(barcode);
        document.save(outputFile.toString());
    }
}
```
