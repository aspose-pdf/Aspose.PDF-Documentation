---
title: Ekstrak Data dari Tabel dalam PDF dengan C#
linktitle: Ekstrak Data dari Tabel
type: docs
weight: 40
url: id/net/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak tabel dari PDF menggunakan Aspose.PDF untuk .NET dalam C#
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Tabel dari PDF secara programatik

Mengekstrak tabel dari PDF bukan tugas yang sederhana karena tabel dapat dibuat dengan berbagai cara.

Aspose.PDF untuk .NET memiliki alat untuk memudahkan pengambilan tabel. Untuk mengekstrak data tabel Anda harus melakukan langkah-langkah berikut:

1. Buka dokumen - instansiasi objek [Document](https://reference.aspose.com/pdf/net/aspose.pdf/document);
1. Buat objek [TableAbsorber](https://reference.aspose.com/pdf/net/aspose.pdf.text/tableabsorber).
1. `TableList` adalah daftar dari [AbsorbedTable](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable). Untuk mendapatkan data, iterasi melalui `TableList` dan tangani [RowList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rowlist) dan [CellList](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedrow/properties/celllist)
1. Setiap [AbsorbedCell](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell) berisi koleksi [TextFragments](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedcell/properties/textfragments). Anda dapat memprosesnya untuk tujuan Anda sendiri.

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

Contoh berikut menunjukkan ekstraksi tabel dari semua halaman:

```csharp
public static void Extract_Table()
{
    // Muat dokumen PDF sumber
    var filePath="<... masukkan jalur ke file pdf di sini ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);                       
    foreach (var page in pdfDocument.Pages)
    {
        Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
        absorber.Visit(page);
        foreach (AbsorbedTable table in absorber.TableList)
        {
            Console.WriteLine("Table");
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {                                 
                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                            sb.Append(seg.Text);
                        Console.Write($"{sb.ToString()}|");
                    }                           
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Ekstrak tabel di area tertentu pada halaman PDF

Setiap tabel yang terserap memiliki properti [Rectangle](https://reference.aspose.com/pdf/net/aspose.pdf.text/absorbedtable/properties/rectangle) yang mendeskripsikan posisi tabel di halaman.

Jadi, jika Anda perlu mengekstrak tabel yang berada di wilayah tertentu, Anda harus bekerja dengan koordinat tertentu.

Potongan kode berikut juga bekerja dengan pustaka [Aspose.PDF.Drawing](/pdf/net/drawing/).

Contoh berikut menunjukkan cara mengekstrak tabel yang ditandai dengan Anotasi Kotak:

```csharp
public static void Extract_Marked_Table()
{
    // Memuat dokumen PDF sumber
    var filePath="<... masukkan jalur ke file pdf di sini ...>";
    Aspose.Pdf.Document pdfDocument = new Aspose.Pdf.Document(filePath);  
    var page = pdfDocument.Pages[1];
    var squareAnnotation =
        page.Annotations.FirstOrDefault(ann => ann.AnnotationType == Annotations.AnnotationType.Square)
        as Annotations.SquareAnnotation;


    Aspose.Pdf.Text.TableAbsorber absorber = new Aspose.Pdf.Text.TableAbsorber();
    absorber.Visit(page);

    foreach (AbsorbedTable table in absorber.TableList)
    {
        var isInRegion = (squareAnnotation.Rect.LLX < table.Rectangle.LLX) &&
        (squareAnnotation.Rect.LLY < table.Rectangle.LLY) &&
        (squareAnnotation.Rect.URX > table.Rectangle.URX) &&
        (squareAnnotation.Rect.URY > table.Rectangle.URY);

        if (isInRegion)
        {
            foreach (AbsorbedRow row in table.RowList)
            {
                foreach (AbsorbedCell cell in row.CellList)
                {

                    foreach (TextFragment fragment in cell.TextFragments)
                    {
                        var sb = new StringBuilder();
                        foreach (TextSegment seg in fragment.Segments)
                        {
                            sb.Append(seg.Text);
                        }
                        var text = sb.ToString();
                        Console.Write($"{text}|");
                    }
                }
                Console.WriteLine();
            }
        }
    }
}
```
## Ekstrak Data Tabel dari PDF dan simpan dalam file CSV

Contoh berikut menunjukkan cara mengekstrak tabel dan menyimpannya sebagai file CSV.
Untuk melihat cara mengonversi PDF ke Spreadsheet Excel, silakan lihat artikel [Konversi PDF ke Excel](/pdf/net/convert-pdf-to-excel/).

Potongan kode berikut juga bekerja dengan perpustakaan [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
public static void Extract_Table_Save_CSV()
{
    // Untuk contoh lengkap dan file data, silakan kunjungi https://github.com/aspose-pdf/Aspose.PDF-for-.NET

    // Muat dokumen PDF
    Document pdfDocument = new Document(_dataDir + "input.pdf");

    // Instansiasi objek opsi ExcelSave
    ExcelSaveOptions excelSave = new ExcelSaveOptions { Format = ExcelSaveOptions.ExcelFormat.CSV };

    // Simpan output dalam format XLS
    pdfDocument.Save("PDFToXLS_out.xlsx", excelSave);
}
```
