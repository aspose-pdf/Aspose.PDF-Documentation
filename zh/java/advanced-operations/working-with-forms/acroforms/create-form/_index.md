---
title: 创建 AcroForm - 在 Java 中创建可填写的 PDF
linktitle: 创建 AcroForm
type: docs
weight: 10
url: /zh/java/create-form/
description: 使用 Aspose.PDF for Java 从头创建 PDF 文档中的 AcroForm 字段。
lastmod: "2026-10-06"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中创建交互式 AcroForm 字段
Abstract: 本文解释了如何使用 Aspose.PDF for Java 创建 AcroForm 字段。内容涵盖文本框、多部件文本字段、单选按钮、下拉框、复选框、列表框、签名字段和条形码字段，用于交互式 PDF 表单。
aliases:
    - "/zh/java/create-forms/"
---
Aspose.PDF for Java 让您能够从头创建各种 AcroForm 字段类型。

## 创建一个文本框字段

在需要向新 PDF 表单添加单行文本输入字段时使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个带有目标矩形的 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)，并配置其外观。
1. 将字段添加到表单并保存文档。

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

## 创建一个带有多个小部件的文本框字段

当同一文本字段值应出现在页面的多个位置时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 为字段小部件定义多个矩形和外观。
1. 创建 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), 配置每个小部件，并保存文档。

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

## 创建单选按钮字段

当表单应让用户从预定义集合中选择一个选项时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个 [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) 并添加所需的选项。
1. 将字段添加到表单并保存 PDF。

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

## 创建组合框字段

当用户应从下拉列表中选择一个值时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个 [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) 并添加其可选择的选项。
1. 设置默认选择并保存文档。

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

## 创建复选框字段

在表单需要真/假选项（例如同意或功能选择）时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个 [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) 并配置其外观。
1. 在表单中添加复选框并保存输出文件。

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

## 创建列表框字段

当表单应在可见列表中显示多个可用选项时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个 [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) 并添加可用的选项。
1. 将字段添加到表单并保存文档。

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

## 创建签名字段

当文档需要为数字签名预留可见区域时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) 在所需的矩形中。
1. 将字段添加到表单并保存输出 PDF。

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

## 创建条形码字段

当表单应在条形码字段中显示机器可读数据时，请使用此示例。

1. 创建一个新的 PDF [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加一页。
1. 创建一个 [BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) 并添加条形码值。
1. 将字段添加到表单并保存文档。

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
