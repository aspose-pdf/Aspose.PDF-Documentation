---
title: Add PDF Form Fields
type: docs
weight: 10
url: /net/add-form-fields/
description: This topic explains how to work with Form Fields with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Add Form Field in an Existing PDF file

In order to add a form field in an existing PDF file, you need to use [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. This method requires you to specify the type of the field you want to add along with the name and location of the field. You need to create an object of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class, use [AddField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfield/index) method to add a new field in the PDF, Also, you can specify a limit on the number of characters in your field with [SetFieldLimit](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/setfieldlimit) and finally use [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method to save the updated PDF file. The following code snippet shows you how to add form field in an existing PDF file.

```csharp
public static void AddField()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.AddField(FieldType.Text, "Country", 1, 232.56f, 496.75f, 352.28f, 514.03f);
    editor.SetFieldLimit("Country", 20);
    editor.Save(dataDir + "Sample-Form-01-mod.pdf");
}
```

## Add Submit Button URL in an Existing PDF File 

[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) method allows you to set the submit button's URL in a PDF file. This is the URL where the data is posted when the submit button is clicked. In our example code, we specify the URL, the name of our field, the page number to which we want to add, and the button placement coordinates.
[AddSubmitBtn](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addsubmitbtn) method required the name of the submit button field and the URL. This method is provided by [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class. The following code snippet shows you how to set submit button URL.

```csharp
public static void AddSubmitBtn()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.AddSubmitBtn("Submit", 1, "Submit", "http://localhost:3000", 232.56f, 466.75f, 352.28f, 484.03f);
    editor.Save(dataDir + "Sample-Form-01-mod.pdf");
}
```

## Add JavaScript for Push Button

[AddFieldScript](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addfieldscript) method allows you to add JavaScript to a push button in a PDF file. This method requires the name of the push button and the JavaScript . This method is provided by [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class. The following code snippet shows you how to set JavaScript to a push button.

```csharp
public static void AddFieldScript()
{
    var editor = new FormEditor();
    editor.BindPdf(dataDir + "Sample-Form-01.pdf");
    editor.AddFieldScript("Last Name", "app.alert(\"Only one last name\",3);");
    editor.Save(dataDir + "Sample-Form-01-mod.pdf");
}
```

