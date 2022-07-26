---
title: Decorate Form Field in PDF
type: docs
weight: 20
url: /java/decorate-form-field/
description: This section explains how to decorate Form Field in PDF using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Decorate a Particular Form Field in an Existing PDF File

[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) method present in [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class allows you to decorate a particular form field in a PDF file. If you want to decorate a particular field then you need to pass the field name to this method. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) and [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) classes. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) object. Once you have set the attributes, you can call the [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) method and finally save the updated PDF using Save method of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class.
The following code snippet shows you how to decorate a particular form field.

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

## Decorate All Fields of a Particular Type in an Existing PDF File

[decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) method allows you to decorate all the form fields of a particular type in a PDF file at once. If you want to decorate all fields of a particular type then you need to pass the field type to this method. However, before calling this method, you need to create objects of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) and [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) classes. After that, you can set any attributes provided by [FormFieldFacade](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormFieldFacade) object. Once you have set the attributes, you can call the [decorateField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#decorateField--) method and finally save the updated PDF using Save method of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class. The following code snippet shows you how to decorate all the fields of a particular type.


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




