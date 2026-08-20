---
title: Создать AcroForm - Создать заполняемый PDF на Java
linktitle: Создать AcroForm
type: docs
weight: 10
url: /ru/java/create-form/
description: Создайте поля AcroForm с нуля в PDF‑документах с использованием Aspose.PDF for Java.
lastmod: "2026-08-19"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Создайте интерактивные поля AcroForm в PDF‑файлах с помощью Java.
Abstract: В этой статье объясняется, как создавать поля AcroForm с использованием Aspose.PDF for Java. Рассматриваются текстовые поля, мультивиджетные текстовые поля, переключатели, выпадающие списки, флажки, списки, поля подписи и поля штрихкода для интерактивных PDF‑форм.
---
Aspose.PDF for Java позволяет создавать широкий спектр типов полей AcroForm с нуля.

## Создайте текстовое поле

Используйте этот пример, когда вам нужно добавить однострочное текстовое поле ввода в новую форму PDF.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [ТекстовоеПоле](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) с целевым прямоугольником и настройте его внешний вид.
1. Добавьте поле в форму и сохраните документ.

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

## Создайте текстовое поле с несколькими виджетами

Используйте этот пример, когда значение одного и того же текстового поля должно отображаться в нескольких местах на странице.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Определите несколько прямоугольников и внешних видов для виджетов полей.
1. Создайте [ТекстовоеПоле](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), настройте каждый виджет и сохраните документ.

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

## Создайте поле радиокнопки

Используйте этот пример, когда форма должна позволять пользователю выбрать одну опцию из предопределённого набора.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [Поле радиокнопки](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) и добавьте необходимые опции.
1. Добавьте поле в Form и сохраните PDF.

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

## Создайте поле комбобокса

Используйте этот пример, когда пользователю нужно выбрать одно значение из выпадающего списка.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [Поле комбобокса](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) и добавить его варианты выбора.
1. Установите выбор по умолчанию и сохраните документ.

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

## Создайте поле флажка

Используйте этот пример, когда в форме требуется параметр «да/нет», например, согласие или выбор функции.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [Поле флажка](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) и настройте его внешний вид.
1. Добавьте флажок в форму и сохраните выходной файл.

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

## Создайте поле списка

Используйте этот пример, когда форма должна отображать несколько доступных вариантов в видимом списке.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [Поле списка](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) и добавить доступные варианты.
1. Добавьте поле в форму и сохраните документ.

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

## Создайте поле подписи

Используйте этот пример, когда документ должен зарезервировать видимую область для цифровой подписи.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [ПолеПодписи](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) в требуемом прямоугольнике.
1. Добавьте поле в форму и сохраните выходной PDF.

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

## Создайте поле штрихкода

Используйте этот пример, когда форма должна отображать машиночитаемые данные в поле штрихкода.

1. Создайте новый PDF [Документ](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) и добавить страницу.
1. Создайте [Поле штрих‑кода](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) и добавить значение штрихкода.
1. Добавьте поле в форму и сохраните документ.

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


