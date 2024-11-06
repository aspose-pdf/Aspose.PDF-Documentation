---
title: Extract Table Data from PDF 
linktitle: Extract Table Data
type: docs
weight: 40
url: id/java/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak tabel dari PDF menggunakan Aspose.PDF untuk Java
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Mengekstrak Tabel dari PDF secara Programatis

Mengekstrak tabel dari PDF bukanlah tugas yang sepele karena tabel dapat dibuat dengan berbagai cara.

Aspose.PDF untuk Java memiliki alat untuk memudahkan pengambilan tabel. Untuk mengekstrak data tabel, Anda harus melakukan langkah-langkah berikut:

1. Buka dokumen - instansiasi objek [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document);
1. Buat objek [TableAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/tableabsorber).

1. Tentukan halaman mana yang akan dianalisis dan terapkan [visit](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) ke halaman yang diinginkan. Data tabel akan dipindai, dan hasilnya akan disimpan dalam daftar [AbsorbedTable](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable). Kita dapat mendapatkan daftar ini melalui metode [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--).

2. Untuk mendapatkan data, iterasi melalui `TableList` dan tangani daftar [absorbed rows](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow) dan daftar sel yang diserap. Kita dapat mengakses daftar pertama dengan memanggil metode [getTableList](https://reference.aspose.com/pdf/java/com.aspose.pdf/TableAbsorber#getTableList--) dan daftar kedua dengan memanggil metode [getCellList](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Setiap [AbsorbedCell](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedCell) berisi [TextFragmentCollections](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentCollection). Anda dapat memprosesnya untuk keperluan Anda sendiri.

Contoh berikut menunjukkan ekstraksi tabel dari semua halaman:

```java
public static void Extract_Table() {
    // Muat dokumen PDF sumber        
    String filePath = "/home/aspose/pdf-examples/Samples/sample_table.pdf";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();

    // Pindai halaman
    for (com.aspose.pdf.Page page : pdfDocument.getPages()) {
        absorber.visit(page);
        for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
            System.out.println("Table");
            // Iterasi melalui daftar baris
            for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                // Iterasi melalui daftar sel
                for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                    for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                        StringBuilder sb = new StringBuilder();
                        for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                            sb.append(seg.getText());
                        System.out.print(sb.toString() + "|");
                    }
                }
                System.out.println();
            }
        }
    }
}
```


## Ekstrak tabel di area tertentu pada halaman PDF

Setiap tabel yang diserap memiliki properti [Rectangle](https://reference.aspose.com/pdf/java/com.aspose.pdf/AbsorbedTable#getRectangle--) yang menjelaskan posisi tabel pada halaman.

Jadi, jika Anda perlu mengekstrak tabel yang terletak di wilayah tertentu, Anda harus bekerja dengan koordinat khusus.

Contoh berikut menunjukkan cara mengekstrak tabel yang ditandai dengan Anotasi Persegi:

```java
public static void Extract_Marked_Table() {
    // Memuat dokumen PDF sumber
    String filePath = "<... masukkan jalur ke file pdf di sini ...>";
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);
    com.aspose.pdf.Page page = pdfDocument.getPages().get_Item(1);

    com.aspose.pdf.AnnotationSelector annotationSelector = new com.aspose.pdf.AnnotationSelector(
            new com.aspose.pdf.SquareAnnotation(page, com.aspose.pdf.Rectangle.getTrivial()));

    java.util.List<com.aspose.pdf.Annotation> list = annotationSelector.getSelected();
    if (list.size() == 0) {
        System.out.println("Tabel yang ditandai tidak ditemukan..");
        return;
    }

    com.aspose.pdf.SquareAnnotation squareAnnotation = (com.aspose.pdf.SquareAnnotation) list.get(0);

    com.aspose.pdf.TableAbsorber absorber = new com.aspose.pdf.TableAbsorber();
    absorber.visit(page);

    for (com.aspose.pdf.AbsorbedTable table : absorber.getTableList()) {
        {
            boolean isInRegion = (squareAnnotation.getRect().getLLX() < table.getRectangle().getLLX())
                    && (squareAnnotation.getRect().getLLY() < table.getRectangle().getLLY())
                    && (squareAnnotation.getRect().getURX() > table.getRectangle().getURX())
                    && (squareAnnotation.getRect().getURY() > table.getRectangle().getURY());

            if (isInRegion) {
                for (com.aspose.pdf.AbsorbedRow row : table.getRowList()) {
                    {
                        for (com.aspose.pdf.AbsorbedCell cell : row.getCellList()) {
                            for (com.aspose.pdf.TextFragment fragment : cell.getTextFragments()) {
                                StringBuilder sb = new StringBuilder();
                                for (com.aspose.pdf.TextSegment seg : fragment.getSegments())
                                    sb.append(seg.getText());
                                System.out.print(sb.toString() + "|");
                            }
                        }
                        System.out.println();
                    }
                }
            }
        }
    }
}
```


## Ekstrak Data Tabel dari PDF dan simpan dalam file CSV

Contoh berikut menunjukkan cara mengekstrak tabel dan menyimpannya sebagai file CSV.
Untuk melihat cara mengonversi PDF ke Excel Spreadsheet silakan merujuk ke artikel [Convert PDF to Excel](/pdf/java/convert-pdf-to-excel/).

```java
public static void Extract_Table_Save_CSV()
{
    String filePath = "/home/admin1/pdf-examples/Samples/sample_table.pdf";
    // Muat dokumen PDF
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // Memulai objek ExcelSave Option
    com.aspose.pdf.ExcelSaveOptions excelSave = new com.aspose.pdf.ExcelSaveOptions();
    excelSave.setFormat(com.aspose.pdf.ExcelSaveOptions.ExcelFormat.CSV);

    // Simpan keluaran dalam format XLS
    pdfDocument.save("PDFToXLS_out.xlsx", excelSave);
}
```