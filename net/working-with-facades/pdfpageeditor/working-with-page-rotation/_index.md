---
title: Working with Page Rotation
type: docs
weight: 10
url: /net/working-with-page-rotation/
description: This section explains how to work with Page Rotation using PdfPageEditor Class.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

[PdfPageEditor](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) class provides the facility to rotate a page.

{{% /alert %}}

## Rotate page using PageRotations

To rotate pages in document we can use [PageRotations](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` contains the page number and rotation degree, the key represents the page number, the value of key represents the rotation in degrees.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## Rotate page using Rotation

We can also use [Rotation](https://apireference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation) propety. The rotation must be 0, 90, 180 or 270

```csharp
public static void RotatePages2()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.ProcessPages = new int[] { 1, 3 };
    editor.Rotation = 90;

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

