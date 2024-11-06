---
title: Rellenar AcroForms
linktitle: Rellenar AcroForms
type: docs
weight: 20
url: es/java/fill-form/
description: Esta sección explica cómo rellenar un campo de formulario en un documento PDF con Aspose.PDF para Java.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Los documentos PDF son maravillosos y realmente el tipo de archivo preferido para crear Formularios.

Aspose.PDF para Java te permite rellenar un campo de formulario, obtener el campo de la colección de Form del objeto Document.

Veamos el siguiente ejemplo de cómo resolver esta tarea:

```java
public class ExamplesFillForm {

    private static String _dataDir = "/home/aspose/pdf-examples/Samples/Forms/";

    public static void FillFormFieldPDFDocument() {
        // Abrir documento
        Document pdfDocument = new Document(_dataDir + "TextField.pdf");
        Page page = pdfDocument.getPages().get_Item(1);
        // Crear un campo
        TextBoxField textBoxField = new TextBoxField(page, new Rectangle(100, 200, 300, 300));
        textBoxField.setPartialName("textbox1");
        textBoxField.setValue("Cuadro de Texto");

        // TextBoxField.Border = new Border(
        Border border = new Border(textBoxField);
        border.setWidth(5);
        border.setDash(new Dash(1, 1));
        textBoxField.setBorder(border);

        textBoxField.setColor(Color.getGreen());

        // Añadir campo al documento
        pdfDocument.getForm().add(textBoxField, 1);

        // Guardar PDF modificado
        pdfDocument.save(_dataDir + "TextBox_out.pdf");

    }

    
}
```