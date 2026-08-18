---
title: Criar AcroForm - Criar PDF preenchível em Java
linktitle: Criar AcroForm
type: docs
weight: 10
url: /java/create-form/
description: Crie campos AcroForm do zero em documentos PDF usando Aspose.PDF para Java.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Crie campos AcroForm interativos em arquivos PDF com Java
Abstract: Este artigo explica como criar campos AcroForm usando Aspose.PDF para Java. Abrange caixas de texto, campos de texto multi-widget, botões de opção, caixas de combinação, caixas de seleção, caixas de listagem, campos de assinatura e campos de código de barras para formulários PDF interativos.
---
Aspose.PDF para Java permite criar uma ampla variedade de tipos de campos AcroForm do zero.

## Crie um campo de caixa de texto

Use este exemplo quando precisar adicionar um campo de entrada de texto de linha única a um novo formulário PDF.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) com um retângulo alvo e configure sua aparência.
1. Adicione o campo ao formulário e salve o documento.

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

## Crie um campo de caixa de texto com vários widgets

Use este exemplo quando o mesmo valor de campo de texto aparecer em diversas posições na página.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Defina vários retângulos e aparências para os widgets de campo.
1. Crie o [TextBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), configure cada widget e salve o documento.

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

## Crie um campo de botão de opção

Use este exemplo quando o formulário permitir que o usuário escolha uma opção de um conjunto predefinido.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) e adicione as opções necessárias.
1. Adicione o campo ao formulário e salve o PDF.

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

## Crie um campo de caixa de combinação

Use este exemplo quando o usuário precisar escolher um valor em uma lista suspensa.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [ComboBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) e adicione suas opções selecionáveis.
1. Defina a seleção padrão e salve o documento.

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

## Crie um campo de caixa de seleção

Use este exemplo quando o formulário precisar de uma opção verdadeiro ou falso, como consentimento ou seleção de recursos.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [CheckboxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) e configure sua aparência.
1. Adicione a caixa de seleção ao formulário e salve o arquivo de saída.

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

## Crie um campo de caixa de listagem

Use este exemplo quando o formulário exibir diversas opções disponíveis em uma lista visível.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [ListBoxField](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) e adicione as opções disponíveis.
1. Adicione o campo ao formulário e salve o documento.

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

## Crie um campo de assinatura

Use este exemplo quando o documento precisar reservar uma área visível para uma assinatura digital.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [SignatureField](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) no retângulo necessário.
1. Adicione o campo ao formulário e salve o PDF de saída.

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

## Crie um campo de código de barras

Use este exemplo quando o formulário exibir dados legíveis por máquina dentro de um campo de código de barras.

1. Crie um novo [documento] PDF (https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) e adicione uma página.
1. Crie um [BarcodeField](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) e adicione o valor do código de barras.
1. Adicione o campo ao formulário e salve o documento.

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
