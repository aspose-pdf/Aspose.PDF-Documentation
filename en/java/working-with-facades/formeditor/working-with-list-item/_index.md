---
title: Working with List Item
type: docs
weight: 30
url: /java/working-with-list-item/
description: This section explains how to work with List Item with com.aspose.pdf.facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

## Add List Item in an Existing PDF File

[addListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#addListItem-java.lang.String-java.lang.String-) method allows you to add an item in a ListBox field. The first argument is the field name and second argument in the field item. You can either pass a single field item or you can pass an array of string contains a list of items. This method is provided by [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class. The following code snippet shows you how to add list items in a PDF file.

```java
public static void AddListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-01.pdf");
        editor.addField(FieldType.ListBox, "Country", 1, 232.56f, 476.75f, 352.28f, 514.03f);
        editor.addListItem("Country", "USA");
        editor.addListItem("Country", "Canada");
        editor.addListItem("Country", "France");
        editor.addListItem("Country", "Spain");
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```

## Delete List Item from an Existing PDF File

[delListItem](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#delListItem-java.lang.String-java.lang.String-) method allows you to delete a particular item from the ListBox The first parameter is the field name while second parameter is the item which you want to delete from the list. This method is provided by [FormEditor](https://reference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class. The following code snippet shows you how to delete a list item from the PDF file.

```java
    public static void DelListItem() {
        FormEditor editor = new FormEditor();
        editor.bindPdf(_dataDir + "Sample-Form-04.pdf");
        // -----
        editor.delListItem("Country", "France");
        // -----
        editor.save(_dataDir + "Sample-Form-04-mod.pdf");
    }
```
