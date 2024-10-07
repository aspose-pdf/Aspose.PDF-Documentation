---
title: Bekerja dengan Rotasi Halaman
type: docs
weight: 10
url: /net/working-with-page-rotation/
description: Bagian ini menjelaskan cara bekerja dengan Rotasi Halaman menggunakan Kelas PdfPageEditor.
lastmod: "2021-07-07"
draft: false
---

{{% alert color="primary" %}}

Kelas [PdfPageEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor) menyediakan fasilitas untuk memutar halaman.

{{% /alert %}}

## Memutar halaman menggunakan PageRotations

Untuk memutar halaman dalam dokumen kita dapat menggunakan [PageRotations](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/pagerotations).
`PageRotations` berisi nomor halaman dan derajat rotasi, kunci mewakili nomor halaman, nilai kunci mewakili rotasi dalam derajat.

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

## Memutar halaman menggunakan Rotasi

Kita juga bisa menggunakan properti [Rotation](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfpageeditor/properties/rotation). Rotasi harus 0, 90, 180 atau 270

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