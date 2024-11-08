---
title: ページ回転の操作
type: docs
weight: 10
url: /ja/net/working-with-page-rotation/
description: このセクションでは、PdfPageEditorクラスを使用してページ回転を操作する方法を説明します。
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

[PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) クラスは、ページを回転させる機能を提供します。

{{% /alert %}}

## PageRotationsを使用してページを回転する

ドキュメント内のページを回転させるには、[PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations) を使用できます。
`PageRotations` はページ番号と回転角度を含み、キーはページ番号を表し、キーの値は度数での回転を表します。

```csharp
public static void RotatePages1()
{
    var editor = new PdfPageEditor();
    editor.BindPdf(_dataDir + "sample.pdf");

    editor.PageRotations = new System.Collections.Generic.Dictionary<int, int> { { 1, 90 }, { 2, 180 }, { 3,270 } };

    editor.Save(_dataDir + "sample-rotate-a.pdf");
}
```

## Rotationを使用してページを回転

[Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation)プロパティを使用することもできます。回転は0、90、180または270でなければなりません。

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