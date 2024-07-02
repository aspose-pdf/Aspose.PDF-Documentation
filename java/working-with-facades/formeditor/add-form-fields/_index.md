---
title: Add PDF Form Fields
type: docs
weight: 10
url: /java/add-form-fields/
description: This topic explains how to work with Form Fields with java/com.aspose.pdf.facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Add Form Field in an Existing PDF file

In order to add a form field in an existing PDF file, you need to use [addField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addField-int-java.lang.String-int-float-float-float-float-) method of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class. This method requires you to specify the type of the field you want to add along with the name and location of the field. You need to create an object of [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class, use [addField](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addField-int-java.lang.String-int-float-float-float-float-) method to add a new field in the PDF, Also, you can specify a limit on the number of characters in your field with [setFieldLimit] (https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#setFieldLimit-java.lang.String-int-) and finally use Save method to save the updated PDF file. The following code snippet shows you how to add form field in an existing PDF file.

```java
    public static void AddField() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
        editor.setFieldLimit("Country", 20);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```

## Add Submit Button URL in an Existing PDF File 

[addSubmitBtn](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addSubmitBtn-java.lang.String-int-java.lang.String-java.lang.String-float-float-float-float-) method allows you to set the submit button's URL in a PDF file. This is the URL where the data is posted when the submit button is clicked. In our example code, we specify the URL, the name of our field, the page number to which we want to add, and the button placement coordinates.
[addSubmitBtn](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addSubmitBtn-java.lang.String-int-java.lang.String-java.lang.String-float-float-float-float-) method required the name of the submit button field and the URL. This method is provided by [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class. The following code snippet shows you how to set submit button URL.

```java
public static void AddSubmitBtn() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```

## Add JavaScript for Push Button

[addFieldScript](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addFieldScript-java.lang.String-java.lang.String-) method allows you to add JavaScript to a push button in a PDF file. This method requires the name of the push button and the JavaScript . This method is provided by [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class. The following code snippet shows you how to set JavaScript to a push button.

```java
  public static void AddFieldScript() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```

