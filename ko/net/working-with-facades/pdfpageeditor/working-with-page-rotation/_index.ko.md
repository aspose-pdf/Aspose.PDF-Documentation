---
title: 페이지 회전 작업
type: docs
weight: 10
url: /net/working-with-page-rotation/
description: 이 섹션은 PdfPageEditor 클래스를 사용하여 페이지 회전 작업을 설명합니다.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 클래스는 페이지를 회전하는 기능을 제공합니다.

{{% /alert %}}

## PageRotations를 사용하여 페이지 회전

문서에서 페이지를 회전하려면 [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations)를 사용할 수 있습니다.
`PageRotations`는 페이지 번호와 회전 각도를 포함하며, 키는 페이지 번호를 나타내고, 키의 값은 회전 각도를 나타냅니다.

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```
```

## Rotation을 사용하여 페이지 회전

우리는 또한 [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation) 속성을 사용할 수 있습니다. 회전은 0, 90, 180 또는 270이어야 합니다.

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