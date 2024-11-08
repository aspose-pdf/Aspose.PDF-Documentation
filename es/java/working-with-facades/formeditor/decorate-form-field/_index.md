---
title: Decorar Campo de Formulario en PDF
type: docs
weight: 20
url: /es/java/decorate-form-field/
description: Esta sección explica cómo decorar un campo de formulario en PDF usando la clase FormEditor.
lastmod: "2021-06-05"
draft: false
---

## Decorar un Campo de Formulario Particular en un Archivo PDF Existente

El método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) presente en la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) permite decorar un campo de formulario particular en un archivo PDF.
 Si desea decorar un campo en particular, entonces necesita pasar el nombre del campo a este método. Sin embargo, antes de llamar a este método, necesita crear objetos de las clases [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) y [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Después de eso, puede establecer cualquier atributo proporcionado por el objeto [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Una vez que haya establecido los atributos, puede llamar al método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) y finalmente guardar el PDF actualizado usando el método Save de la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor).
El siguiente fragmento de código le muestra cómo decorar un campo de formulario en particular.

```java
public static void DecorateField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade cityDecoration = new FormFieldFacade();
        cityDecoration.setFont(FontStyle.Courier);
        cityDecoration.setFontSize(12);
        cityDecoration.setBorderColor(Color.BLACK);
        cityDecoration.setBorderWidth(2);

        editor.setFacade(cityDecoration);
        editor.decorateField("City");
        editor.save(_dataDir + "Sample-Form-02.pdf");
    }
```

## Decorar Todos los Campos de un Tipo Particular en un Archivo PDF Existente

El método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) permite decorar todos los campos de formulario de un tipo particular en un archivo PDF de una vez.
 Si deseas decorar todos los campos de un tipo particular, entonces necesitas pasar el tipo de campo a este método. Sin embargo, antes de llamar a este método, necesitas crear objetos de las clases [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) y [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Después de eso, puedes establecer cualquier atributo proporcionado por el objeto [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade). Una vez que hayas establecido los atributos, puedes llamar al método [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) y finalmente guardar el PDF actualizado usando el método Save de la clase [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor). El siguiente fragmento de código te muestra cómo decorar todos los campos de un tipo particular.

```java
   public static void DecorateFields() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");

        FormFieldFacade textFieldDecoration = new FormFieldFacade();
        textFieldDecoration.setAlignment(FormFieldFacade.ALIGN_CENTER);

        editor.setFacade(textFieldDecoration);
        editor.decorateField(FieldType.Text);
        editor.save(_dataDir + "Sample-Form-01-align-text.pdf");
    }
```