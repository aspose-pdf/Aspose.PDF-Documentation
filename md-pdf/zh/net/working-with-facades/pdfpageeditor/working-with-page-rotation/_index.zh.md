---
title: 使用页面旋转
type: docs
weight: 10
url: /net/working-with-page-rotation/
description: 本节解释如何使用 PdfPageEditor 类进行页面旋转。
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) 类提供了旋转页面的功能。

{{% /alert %}}

## 使用 PageRotations 旋转页面

要在文档中旋转页面，我们可以使用 [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations)。`PageRotations` 包含页码和旋转度数，键表示页码，键的值表示旋转的度数。

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## 使用旋转旋转页面

我们也可以使用[Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation)属性。旋转必须是0、90、180或270

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