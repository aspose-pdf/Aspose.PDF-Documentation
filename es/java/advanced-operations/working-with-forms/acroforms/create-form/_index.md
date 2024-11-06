---
title: Crear AcroForms - Crear PDF Rellenable en Java
linktitle: Crear AcroForms
type: docs
weight: 10
url: es/java/create-forms/
description: Esta sección explica cómo crear AcroForms desde cero en sus documentos PDF con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Añadir Campo de Formulario en un Documento PDF

La clase [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) proporciona una colección llamada Form que ayuda a gestionar campos de formulario en un documento PDF.

Para añadir un campo de formulario:

1. Cree el campo de formulario que desea añadir.
2. Llame al método add de la colección [Form](https://reference.aspose.com/pdf/java/com.aspose.pdf/Form).

Este ejemplo muestra cómo añadir un TextBoxField. Puede añadir cualquier campo de formulario utilizando el mismo enfoque:

1. Primero, cree un objeto de campo y establezca sus propiedades.
2. Luego, añada el campo a la colección Form.

### Añadir TextBoxField

Un campo de texto es un elemento de formulario que permite a un destinatario ingresar texto en su formulario.
 Esto se usaría cada vez que desees permitir al usuario la libertad de escribir lo que quieran.

Los siguientes fragmentos de código muestran cómo agregar un TextBoxField a un documento PDF.

```java
public class ExamplesCreateForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void AddingTextBoxField() {

        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Crear un campo
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Text Box");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Agregar campo al documento
        pdfDocument.getForm().add(textBoxField, 1);

        // Guardar PDF modificado
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }
```

## Añadiendo RadioButtonField

Un Botón de Radio se usa comúnmente para preguntas de opción múltiple, en el escenario donde solo se puede seleccionar una respuesta.

Los siguientes fragmentos de código muestran cómo añadir [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) en un documento PDF.

```java
public static void AddingRadioButton() {
        Document pdfDocument = new Document();
        // añadir una página al archivo PDF
        pdfDocument.getPages().add();

        // instanciar el objeto RadioButtonField con el número de página como argumento
        RadioButtonField radio = new RadioButtonField(pdfDocument.getPages().get_Item(1));

        // añadir la primera opción de botón de radio y también especificar su origen usando el objeto Rectangle
        radio.addOption("Test", new Rectangle(20, 720, 40, 740));
        // añadir la segunda opción de botón de radio
        radio.addOption("Test1", new Rectangle(120, 720, 140, 740));
        // añadir el botón de radio al objeto de formulario del objeto Document
        pdfDocument.getForm().add(radio);
        // guardar el archivo PDF
        pdfDocument.save("RadioButtonSample.pdf");

    }
```


El siguiente fragmento de código muestra los pasos para agregar [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField) con tres opciones y colocarlos dentro de celdas de una tabla.

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


## Añadiendo Título al Campo RadioButton

El siguiente fragmento de código muestra cómo añadir un título que estará asociado con [RadioButtonField](https://reference.aspose.com/pdf/java/com.aspose.pdf/RadioButtonField):

```java
public static void AddingCaptionToRadioButtonField() {
        // Cargar formulario PDF de origen
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

                // Crear objeto TextParagraph
                TextParagraph par = new TextParagraph();

                // Establecer posición del párrafo
                par.setPosition(new Position(field0.getRect().getLLX(),
                        field0.getRect().getLLY() + updatedFragment.getTextState().getFontSize()));
                // Especificar modo de ajuste de texto
                par.getFormattingOptions().setWrapMode(TextFormattingOptions.WordWrapMode.ByWords);

                // Añadir nuevo TextFragment al párrafo
                par.appendLine(updatedFragment);

                // Añadir el TextParagraph usando TextBuilder
                TextBuilder textBuilder = new TextBuilder(document.getPages().get_Item(1));
                textBuilder.appendParagraph(par);

                field0.deleteOption("item1");
            }
        }
        document.save(_dataDir + "RadioButtonField_out.pdf");

    }
```


## Añadiendo campo ComboBox

Un Combo Box es un campo de formulario que añadirá un menú desplegable a tu documento.

Los siguientes fragmentos de código muestran cómo añadir un campo [ComboBox](https://reference.aspose.com/pdf/java/com.aspose.pdf/ComboBoxField) en un documento PDF.

```java
public static void AddingComboboxField() {
        // crear objeto Document
        Document doc = new Document();
        // agregar página al objeto documento
        doc.getPages().add();
        // instanciar objeto ComboBox Field
        ComboBoxField combo = new ComboBoxField(doc.getPages().get_Item(1), new Rectangle(100, 600, 150, 616));
        // agregar opción a ComboBox
        combo.addOption("Red");
        combo.addOption("Yellow");
        combo.addOption("Green");
        combo.addOption("Blue");
        // agregar objeto combo box a la colección de campos de formulario del objeto documento
        doc.getForm().add(combo);
        // guardar el documento PDF
        doc.save("ComboBox_Added.pdf");
    }
```

## Añadir Tooltip al Formulario

La clase Document proporciona una colección llamada Form que gestiona los campos de formulario en un documento PDF.
 Para agregar un tooltip a un campo de formulario, use la clase Field AlternateName. Adobe Acrobat utiliza el 'nombre alternativo' como tooltip del campo.

Los fragmentos de código que siguen muestran cómo agregar un tooltip a un campo de formulario con Java.

```java
public static void AddTooltipToFormField() {
        // Cargar formulario PDF fuente
        Document doc = new Document(_dataDir + "AddTooltipToField.pdf");

        // Obtener un campo
        TextBoxField textBoxField = (TextBoxField) doc.getForm().get("textbox1");

        // Establecer el tooltip para el campo de texto
        textBoxField.setAlternateName("Consejo de herramienta del cuadro de texto");

        // Guardar documento modificado
        doc.save("output.pdf");
    }
```