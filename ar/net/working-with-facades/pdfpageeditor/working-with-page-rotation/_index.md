---
title: العمل مع تدوير الصفحات
type: docs
weight: 10
url: ar/net/working-with-page-rotation/
description: يشرح هذا القسم كيفية العمل مع تدوير الصفحات باستخدام فئة PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

يوفر فصل [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) إمكانية تدوير الصفحة.

{{% /alert %}}

## تدوير الصفحة باستخدام PageRotations

لتدوير الصفحات في المستند يمكننا استخدام [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` يحتوي على رقم الصفحة ودرجة التدوير، المفتاح يمثل رقم الصفحة، وقيمة المفتاح تمثل التدوير بالدرجات.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## تدوير الصفحة باستخدام التدوير

يمكننا أيضًا استخدام خاصية [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). يجب أن يكون التدوير 0، 90، 180 أو 270

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