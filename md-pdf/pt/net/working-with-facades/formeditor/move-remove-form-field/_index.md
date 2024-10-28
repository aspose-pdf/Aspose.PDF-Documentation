---
title: Move and Remove Form Field
type: docs
weight: 50
url: /net/move-remove-form-field/
description: This section explains how you can move and remove Form Fields with FormEditor Class.
lastmod: "2021-06-05"
draft: false
---


## Move Form Field to a New Location in Existing PDF File

If you want to move a form field to a new location then you can use [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. You only need to provide the field name and new location of this field to the [MoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/movefield) method. You also need to save the updated PDF file using [Save](https://reference.aspose.com/pdf/net/aspose.pdf.facades/form/methods/save/index) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to move a form field in a new location in a PDF file.

```csharp
public static void MoveField()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-05.pdf");
            editor.MoveField("Last Name", 262.56f, 496.75f, 382.28f, 514.03f);
            editor.Save(_dataDir + "Sample-Form-05-mod.pdf");
        }
```

## Delete Form Field from an Existing PDF File 

In order to delete a form field from an existing PDF file, you can use RemoveField method of FormEditor class. This method takes only one argument: field name. You need to create an object of FormEditor class, call [RemoveField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/removefield) method to remove a particular field from the PDF and then call the Save method to save the updated PDF file. The following code snippet shows you how to delete form fields from an existing PDF file.

```csharp
  public static void RemoveFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RemoveField("First Name");
            editor.RemoveField("Last Name");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```

## Rename Form Fields in PDF

Also you can rename your field using [RenameField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/renamefield) method of [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class.

```csharp

        public static void RenameFields()
        {
            var editor = new FormEditor();
            editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
            editor.RenameField("Last Name", "LastName");
            editor.RenameField("First Name", "FirstName");
            editor.Save(_dataDir + "Sample-Form-01-updated.pdf");
        }
```