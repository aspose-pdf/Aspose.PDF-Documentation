---
title: Create AcroForm - 在 Java 中创建可填写的 PDF
linktitle: 创建 AcroForm
type: docs
weight: 10
url: /java/create-form/
description: 使用 Aspose.PDF for Java 在 PDF 文档中从头开始创建 AcroForm 字段。
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 使用 Java 在 PDF 文件中创建交互式 AcroForm 字段
Abstract: 本文介绍如何使用 Aspose.PDF for Java 创建 AcroForm 字段。它涵盖交互式 PDF 表单的文本框、多小部件文本字段、单选按钮、组合框、复选框、列表框、签名字段和条形码字段。
---
Aspose.PDF for Java 允许您从头开始创建各种 AcroForm 字段类型。

## 创建文本框字段

当您需要向新的 PDF 表单添加单行文本输入字段时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 使用目标矩形创建一个 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) 并配置其外观。
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

## 创建一个包含多个小部件的文本框字段

当相同的文本字段值应出现在页面上的多个位置时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 为字段小部件定义多个矩形和外观。
1. 创建 [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/)，配置每个小部件，然后保存文档。

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

当表单应让用户从预定义的集合中选择一个选项时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
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

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 创建一个 [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) 并添加其可选选项。
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

当表单需要是非判断选项（例如同意或功能选择）时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 创建一个 [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) 并配置其外观。
1. 将复选框添加到表单并保存输​​出文件。

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

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 创建一个 [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) 并添加可用选项。
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

当文档必须为数字签名保留可见区域时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
1. 在所需的矩形中创建一个 [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/)。
1. 将字段添加到表单并保存输​​出 PDF。

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

当表单应在条形码字段内显示机器可读数据时，请使用此示例。

1. 创建新的 PDF [文档](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) 并添加页面。
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
