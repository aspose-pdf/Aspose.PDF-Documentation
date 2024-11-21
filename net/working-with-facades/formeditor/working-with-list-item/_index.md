---
title: Working with List Item
type: docs
weight: 50
url: /net/working-with-list-item/
description: This section explains how to work with List Item with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Add List Item in an Existing PDF File

[AddListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/addlistitem) method allows you to add an item in a [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield) field. The first argument is the field name and second argument in the field item. You can either pass a single field item or you can pass an array of string contains a list of items. This method is provided by [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to add list items in a PDF file.

```csharp
public static void AddListItem()
{
    var editor = new FormEditor();
    editor.BindPdf(_dataDir + "Sample-Form-01.pdf");
    editor.AddField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
    editor.AddListItem("Country", "USA");
    editor.AddListItem("Country", "Canada");
    editor.AddListItem("Country", "France");
    editor.AddListItem("Country", "Spain");
    editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
}
```

## Delete List Item from an Existing PDF File

[DelListItem](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/dellistitem) method allows you to delete a particular item from the [ListBox](https://reference.aspose.com/pdf/net/aspose.pdf.forms/listboxfield). The first parameter is the field name while second parameter is the item which you want to delete from the list. This method is provided by [FormEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor) class. The following code snippet shows you how to delete a list item from the PDF file.

```csharp
public static void DelListItem()
{
    var editor = new FormEditor();
    editor.BindPdf(_dataDir + "Sample-Form-04.pdf");
    editor.DelListItem("Country", "France");
    editor.Save(_dataDir + "Sample-Form-04-mod.pdf");
}
```
