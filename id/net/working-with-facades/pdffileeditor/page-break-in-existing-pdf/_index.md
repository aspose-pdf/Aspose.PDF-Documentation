---
title: Page Break in existing PDF
type: docs
weight: 30
url: id/net/page-break-in-existing-pdf/
description: Bagian ini menjelaskan cara memecah halaman dalam PDF yang ada menggunakan kelas PdfFileEditor.
lastmod: "2021-06-05"
draft: false
---

Sebagai tata letak default, konten di dalam file PDF ditambahkan dalam tata letak Kiri-Atas ke Kanan-Bawah. Setelah konten melebihi batas margin bawah halaman, pemisahan halaman terjadi. Namun, Anda mungkin menemui persyaratan untuk menyisipkan pemisahan halaman tergantung pada kebutuhan. Metode bernama AddPageBreak(...) ditambahkan dalam kelas [PdfFileEditor](https://reference.aspose.com/pdf/net/aspose.pdf.facades/pdffileeditor) untuk memenuhi persyaratan ini.

1. [public void AddPageBreak(Document src, Document dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/1) [public void AddPageBreak(string src, string dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/addpagebreak/methods/2)
1. [public void AddPageBreak(Stream src, Stream dest, PageBreak[] pageBreaks)](https://reference.aspose.com/pdf/net/aspose.pdf.facades.pdffileeditor/methods/addpagebreak)

- src adalah dokumen sumber/jalur ke dokumen/aliran dengan dokumen sumber
- dest adalah dokumen tujuan/jalur tempat dokumen akan disimpan/aliran tempat dokumen akan disimpan
- PageBreak adalah array dari objek page break. Ini memiliki dua properti: indeks halaman tempat page break harus ditempatkan dan posisi vertikal dari page break pada halaman.

## Contoh 1 (Tambah page break)

```csharp
public static void PageBrakeExample01()
{
    // Membuat instance Dokumen
    Document doc = new Document(_dataDir + "Sample-Document-01.pdf");
    // Membuat instance Dokumen kosong
    Document dest = new Document();
    // Membuat objek PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(doc, dest, new PdfFileEditor.PageBreak[]
    {
        new PdfFileEditor.PageBreak(1, 450)
    });
    // Simpan file hasil
    dest.Save(_dataDir + "PageBreak_out.pdf");
}
```
## Contoh 2

```csharp
public static void PageBrakeExample02()
{
    // Buat objek PdfFileEditor
    PdfFileEditor fileEditor = new PdfFileEditor();

    fileEditor.AddPageBreak(_dataDir + "Sample-Document-02.pdf",
        _dataDir + "PageBreakWithDestPath_out.pdf",
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
}
```

## Contoh 3

```csharp
public static void PageBrakeExample03()
{
    Stream src = new FileStream(_dataDir + "Sample-Document-03.pdf", FileMode.Open, FileAccess.Read);
    Stream dest = new FileStream(_dataDir + "PageBreakWithStream_out.pdf", FileMode.Create, FileAccess.ReadWrite);
    PdfFileEditor fileEditor = new PdfFileEditor();
    fileEditor.AddPageBreak(src, dest,
        new PdfFileEditor.PageBreak[]
        {
            new PdfFileEditor.PageBreak(1, 450)
        });
    dest.Close();
    src.Close();
}
```