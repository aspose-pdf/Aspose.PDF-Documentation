---
title: Copy Inner and Outer Field
type: docs
weight: 60
url: /net/copy-inner-and-outer-field/
description: This section explains how to copy Inner and Outer Field with Aspose.PDF Facades using FormEditor Class.
lastmod: "2021-06-05"
draft: false
---

[CopyInnerField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyinnerfield/index) method allows you to copy a field in the same file, at the same coordinates, on the specified page. This method requires the field name which you want to copy, the new field name, and the page number at which the field needs to be copied. [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class provides this method. The following code snippet shows you how to copy the field at the same location in the same file.

```csharp
public static void CopyInnerField()
{
    var editor = new FormEditor();
    var document = new Aspose.Pdf.Document(_dataDir + "Sample-Form-01.pdf");
    document.Pages.Add();
    editor.BindPdf(document);
    editor.CopyInnerField("Last Name", "Last Name 2", 2);
    editor.Save(_dataDir + "Sample-Form-01-mod.pdf");
}
```

## Copy Outer Field in an Existing PDF File

[CopyOuterField](https://reference.aspose.com/pdf/net/aspose.pdf.facades/formeditor/methods/copyouterfield/index) method allows you to copy a form field from an external PDF file and then add it to the input PDF file at the same location and the specified page number. This method requires the PDF file from which the field needs to be copied, the field name, and the page number at which the field needs to be copied. This method is provided by [FormEditor](https://reference.aspose.com/html/net/aspose.html.forms/formeditor) class.The following code snippet shows you how to copy a field from an external PDF file.

```csharp
public static void CopyOuterField()
{
    var editor = new FormEditor();
    var document = new Aspose.Pdf.Document();
    document.Pages.Add();
    editor.BindPdf(document);
    editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "First Name", 1);
    editor.CopyOuterField(_dataDir + "Sample-Form-01.pdf", "Last Name", 1);
    editor.Save(_dataDir + "Sample-Form-02-mod.pdf");
}
```


