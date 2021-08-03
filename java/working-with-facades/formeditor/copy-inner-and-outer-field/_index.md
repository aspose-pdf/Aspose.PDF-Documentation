---
title: Copy Inner and Outer Field
type: docs
weight: 40
url: /java/copy-inner-and-outer-field/
description: This section explains how to copy inner and outer Field with com.aspose.pdf.facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

[copyInnerField](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyInnerField-java.lang.String-java.lang.String-int-) method allows you to copy a field in the same file, at the same coordinates, on the specified page. This method requires the field name which you want to copy, the new field name, and the page number at which the field needs to be copied. [FormEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class provides this method. The following code snippet shows you how to copy the field at the same location in the same file.

```java
    public static void CopyInnerField() {
        FormEditor editor = new FormEditor();
        Document document = new Document(_dataDir + "Sample-Form-01.pdf");
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyInnerField("Last Name", "Last Name 2", 2);
        editor.save(_dataDir + "Sample-Form-01-mod.pdf");
    }
```

## Copy Outer Field in an Existing PDF File

[copyOuterField](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor#copyOuterField-java.lang.String-java.lang.String-) method allows you to copy a form field from an external PDF file and then add it to the input PDF file at the same location and the specified page number. This method requires the PDF file from which the field needs to be copied, the field name, and the page number at which the field needs to be copied. This method is provided by [FormEditor](https://apireference.aspose.com/pdf/java/com.aspose.pdf.facades/FormEditor) class.The following code snippet shows you how to copy a field from an external PDF file.

```java
  public static void CopyOuterField() {
        FormEditor editor = new FormEditor();
        Document document = new Document();
        document.getPages().add();
        editor.bindPdf(document);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
        editor.copyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
        editor.save(_dataDir + "Sample-Form-02-mod.pdf");
    }
```


