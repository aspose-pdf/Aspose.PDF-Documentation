---
title: Crear AcroForm - Crear PDF rellenable en Java
linktitle: Crear AcroForm
type: docs
weight: 10
url: /es/java/create-form/
description: Cree campos AcroForm desde cero en documentos PDF usando Aspose.PDF for Java.
lastmod: "2026-09-03"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Cree campos AcroForm interactivos en archivos PDF con Java
Abstract: Este artículo explica cómo crear campos AcroForm usando Aspose.PDF for Java. Cubre cuadros de texto, campos de texto multi-widget, botones de opción, cuadros combinados, casillas de verificación, listas desplegables, campos de firma y campos de código de barras para formularios PDF interactivos.
---
Aspose.PDF for Java le permite crear una amplia gama de tipos de campo AcroForm desde cero.

## Crear un campo de cuadro de texto

Utilice este ejemplo cuando necesite agregar un campo de entrada de texto de una sola línea a un nuevo formulario PDF.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Campo de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/) con un rectángulo de destino y configure su apariencia.
1. Agregue el campo al Form y guarde el documento.

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

## Crear un campo de cuadro de texto con múltiples widgets

Utilice este ejemplo cuando el mismo valor del campo de texto deba aparecer en varias posiciones de la página.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Defina varios rectángulos y apariencias para los widgets de campo.
1. Crear el [Campo de texto](https://reference.aspose.com/pdf/java/com.aspose.pdf/textboxfield/), configure cada widget y guarde el documento.

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

## Crear un campo de botón de opción

Utilice este ejemplo cuando el formulario deba permitir al usuario elegir una opción de un conjunto predefinido.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Campo de botón de opción](https://reference.aspose.com/pdf/java/com.aspose.pdf/radiobuttonfield/) y agregue las opciones requeridas.
1. Agregue el campo al Form y guarde el PDF.

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

## Crear un campo de cuadro combinado

Utilice este ejemplo cuando el usuario deba seleccionar un valor de una lista desplegable.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [CampoComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/comboboxfield/) y agregue sus opciones seleccionables.
1. Establezca la selección predeterminada y guarde el documento.

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

## Crear un campo de casilla de verificación

Utilice este ejemplo cuando el formulario necesite una opción verdadero/falso, como consentimiento o selección de funciones.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Campo de casilla de verificación](https://reference.aspose.com/pdf/java/com.aspose.pdf/checkboxfield/) y configure su apariencia.
1. Añade la casilla de verificación al formulario y guarda el archivo de salida.

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

## Crear un campo de lista

Utilice este ejemplo cuando el formulario debe mostrar múltiples opciones disponibles en una lista visible.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Campo de lista](https://reference.aspose.com/pdf/java/com.aspose.pdf/listboxfield/) y agregue las opciones disponibles.
1. Agregue el campo al Form y guarde el documento.

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

## Crear un campo de firma

Utilice este ejemplo cuando el documento debe reservar un área visible para una firma digital.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Campo de firma](https://reference.aspose.com/pdf/java/com.aspose.pdf/signaturefield/) en el rectángulo requerido.
1. Agrega el campo al formulario y guarda el PDF de salida.

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

## Crear un campo de código de barras

Utilice este ejemplo cuando el formulario deba mostrar datos legibles por máquina dentro de un campo de código de barras.

1. Crear un nuevo PDF [Documento](https://reference.aspose.com/pdf/java/com.aspose.pdf/document/) y agrega una página.
1. Crear un [Campo de código de barras](https://reference.aspose.com/pdf/java/com.aspose.pdf/barcodefield/) y añada el valor del código de barras.
1. Agregue el campo al Form y guarde el documento.

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
