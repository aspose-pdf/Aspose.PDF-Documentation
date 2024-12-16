---
title: Ekstrak Data dari Tabel di PDF
linktitle: Ekstrak Data dari Tabel
type: docs
weight: 40
url: /id/cpp/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak tabel dari PDF menggunakan Aspose.PDF untuk C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Tabel dari PDF secara programatis

Karena PDF adalah format yang paling umum untuk bertukar dokumen, mari kita pertimbangkan sebuah dokumen dengan beberapa kumpulan data yang memerlukan analisis. Dalam artikel ini, kami akan menjelaskan ekstraksi tabel dari PDF.

**Aspose.PDF untuk C++** menyediakan alat yang dibutuhkan pengembang untuk mengekstrak data dari tabel dalam dokumen PDF.

Contoh ini menunjukkan penggunaan Kelas [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber) untuk mengambil data tabel dari tabel dalam file PDF.

Contoh berikut menunjukkan ekstraksi tabel dari semua halaman:

```cpp
void ExtractTable() {
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    // Pindai halaman
    for (auto page : document->get_Pages()) {
        absorber->Visit(page);
        for (auto table : absorber->get_TableList()) {
        std::cout << "Table" << std::endl;
        // Iterasi melalui daftar baris
        for (auto row : table->get_RowList()) {
            // Iterasi melalui daftar sel
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Ekstrak tabel di area tertentu pada halaman PDF

Setiap tabel yang diserap memiliki properti [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle/) yang menggambarkan posisi tabel pada halaman.

Jadi, jika Anda perlu mengekstrak tabel yang terletak di wilayah tertentu, Anda harus bekerja dengan koordinat spesifik.

Contoh berikut menunjukkan cara mengekstrak tabel yang ditandai dengan Square Annotation:

```cpp
void ExtractMarkedTable()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama path
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-table.pdf");


    auto document = MakeObject<Document>(_dataDir + infilename);
    auto absorber = MakeObject<TableAbsorber>();

    auto page = document->get_Pages()->idx_get(1);
    auto sqa = MakeObject<Aspose::Pdf::Annotations::SquareAnnotation>(page, Rectangle::get_Trivial());
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(sqa);


    auto list = annotationSelector->get_Selected();
    if (list->get_Count() == 0) {
        std::cerr << "Tabel yang ditandai tidak ditemukan.." << std::endl;
        return;
    }

    auto squareAnnotation = System::DynamicCast<Aspose::Pdf::Annotations::SquareAnnotation>(list->idx_get(1));

    absorber->Visit(page);

    for (auto table : absorber->get_TableList())
    {
        auto isInRegion =
        (squareAnnotation->get_Rect()->get_LLX() < table->get_Rectangle()->get_LLX()) &&
        (squareAnnotation->get_Rect()->get_LLY() < table->get_Rectangle()->get_LLY()) &&
        (squareAnnotation->get_Rect()->get_URX() > table->get_Rectangle()->get_URX()) &&
        (squareAnnotation->get_Rect()->get_URY() > table->get_Rectangle()->get_URY());

        if (isInRegion)
        {
        for (auto row : table->get_RowList()) {
            // Iterasi melalui daftar sel
            for (auto cell : row->get_CellList()) {
                String sb;
                for (auto fragment : cell->get_TextFragments()) {
                sb += fragment->get_Text();
                }
                std::cout << sb << "|";
            }
            std::cout << std::endl;
        }
        }
    }
    std::clog << __func__ << ": Finish" << std::endl;
}
```

## Ekstrak Data Tabel dari PDF dan simpan dalam file CSV

Contoh berikut menunjukkan cara mengekstrak tabel dan menyimpannya sebagai file CSV. Untuk melihat cara mengonversi PDF ke Spreadsheet Excel, silakan merujuk ke artikel [Convert PDF to Excel](/pdf/id/cpp/convert-pdf-to-excel/).

```cpp
void ExtractTableSaveCSV()
{
    std::clog << __func__ << ": Start" << std::endl;
    // String untuk nama jalur
    String _dataDir("C:\\Samples\\Parsing\\");

    // String untuk nama file
    String infilename("sample-table.pdf");
    String outfilename("PDFToXLS_out.csv");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + infilename);

    // Instansiasi objek ExcelSave Option
    auto excelSave = MakeObject<ExcelSaveOptions>();
    excelSave->set_Format(ExcelSaveOptions::ExcelFormat::CSV);

    // Simpan output dalam format XLS
    document->Save(_dataDir + outfilename, excelSave);
    std::clog << __func__ << ": Finish" << std::endl;
}
```