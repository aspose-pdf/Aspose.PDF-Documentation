---
title: Bekerja dengan Gambar menggunakan PdfContentEditor
type: docs
weight: 50
url: /net/working-with-images-in-pdf
description: Bagian ini menjelaskan bagaimana menambahkan dan menghapus Gambar dengan Aspose.PDF Facades menggunakan Kelas PdfContentEditor.
lastmod: "2021-06-24"
---

## Hapus Gambar dari Halaman Tertentu di PDF (Facades)

Untuk menghapus gambar dari halaman tertentu, Anda perlu memanggil metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) dengan parameter pageNumber dan index. Parameter indeks mewakili array bilangan bulat – indeks dari gambar yang akan dihapus. Pertama-tama, Anda perlu membuat objek dari kelas [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) dan kemudian memanggil metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1). Setelah itu, Anda dapat menyimpan file PDF yang diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Cuplikan kode berikut menunjukkan cara menghapus gambar dari halaman tertentu dari PDF.

```csharp
public static void DeleteImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage(2, new[] { 2 });
    editor.Save(_dataDir + "PdfContentEditorDemo10.pdf");
}
```

## Hapus Semua Gambar dari File PDF (Facades)

Semua gambar dapat dihapus dari file PDF menggunakan metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) dari [PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor). Hubungi metode [DeleteImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdfcontenteditor/deleteimage/methods/1) – overload tanpa parameter – untuk menghapus semua gambar, dan kemudian simpan file PDF yang telah diperbarui menggunakan metode [Save](https://reference.aspose.com/pdf/net/aspose.pdf/document/methods/save/index).

Cuplikan kode berikut menunjukkan kepada Anda cara menghapus semua gambar dari file PDF.

```csharp
public static void DeleteImages()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample.pdf"));
    editor.DeleteImage();
    editor.Save(_dataDir + "PdfContentEditorDemo11.pdf");
}
```

## Ganti Gambar dalam File PDF (Facades)

[PdfContentEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor) memungkinkan Anda mengganti gambar dalam file PDF, panggil untuk ini metode [ReplaceImage](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdfcontenteditor/methods/replaceimage), dan simpan hasilnya.

```csharp
public static void ReplaceImage()
{
    PdfContentEditor editor = new PdfContentEditor(new Document(_dataDir + "sample_cats_dogs.pdf"));
    editor.ReplaceImage(2, 4, @"C:\Samples\Facades\PdfContentEditor\cat04.jpg");
    editor.Save(_dataDir + "PdfContentEditorDemo12.pdf");
}
```