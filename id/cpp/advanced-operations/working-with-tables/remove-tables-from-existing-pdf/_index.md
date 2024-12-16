---
title: Hapus Tabel dari PDF yang Ada
linktitle: Hapus Tabel
type: docs
weight: 50
url: /id/cpp/remove-tables-from-existing-pdf/
description: Bagian ini menjelaskan cara menghapus Tabel dari dokumen PDF.
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Aspose.PDF for C++ memungkinkan Anda untuk menyisipkan dan membuat Tabel di dalam dokumen PDF saat sedang dibuat dari awal atau Anda juga dapat menambahkan objek tabel dalam dokumen PDF yang ada. Tetapi Anda mungkin memiliki kebutuhan untuk [Memanipulasi Tabel di PDF yang Ada](https://docs.aspose.com/pdf/cpp/manipulate-tables-in-existing-pdf/) di mana Anda dapat memperbarui konten dalam sel tabel yang ada. Juga, Anda mungkin menemui kebutuhan untuk menghapus objek tabel dari dokumen PDF yang ada.

Untuk menghapus tabel, kita perlu menggunakan kelas [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) untuk mendapatkan tabel di PDF yang ada dan kemudian memanggil metode 'Remove'.

## Hapus Tabel dari dokumen PDF

Kami telah menambahkan fungsi baru yaitu.
``` [Remove](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.table_absorber#ace39006d8f44c9cb776ee26281a1cbb3) ke Kelas TableAbsorber yang ada untuk menghapus tabel dari dokumen PDF. Setelah absorber berhasil menemukan tabel pada halaman, ia menjadi mampu untuk menghapusnya. Silakan periksa potongan kode berikut yang menunjukkan cara menghapus tabel dari dokumen PDF:

>Headers:

```cpp
#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void RemoveTable() {

    String _dataDir("C:\\Samples\\");

    // Memuat dokumen PDF sumber
    auto document = MakeObject<Document>(_dataDir + u"Table_input.pdf");

    // Membuat objek TableAbsorber untuk menemukan tabel
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Mengunjungi halaman pertama dengan absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Mendapatkan tabel pertama pada halaman
    auto table = absorber->get_TableList()->idx_get(0);

    // Menghapus tabel
    absorber->Remove(table);

    // Menyimpan PDF
    document->Save(_dataDir + u"Table_out.pdf");
}
```
## Hapus Beberapa Tabel dari Dokumen PDF

Beberapa tugas akan berhubungan dengan bekerja dengan beberapa tabel dalam satu dokumen pdf. Dan Anda akan perlu menghapus beberapa tabel dari situ. Untuk menghapus beberapa tabel dari dokumen PDF, gunakan potongan kode berikut:

```cpp
void RemoveMultipleTables() {

    String _dataDir("C:\\Samples\\");

    // Muat dokumen PDF yang ada
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Buat objek TableAbsorber untuk menemukan tabel
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Kunjungi halaman pertama dengan absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Dapatkan salinan koleksi tabel
    auto tables = absorber->get_TableList();


    // Loop melalui salinan koleksi dan menghapus tabel
    for(auto table : tables)
    absorber->Remove(table);

    // Simpan dokumen
    document->Save(_dataDir + u"Table2_out.pdf");
}
```

{{% alert color="primary" %}}

Harap diperhatikan bahwa menghapus atau mengganti tabel mengubah koleksi TableList. Therefore, in case removing/replacing tables in a loop the copying of TableList collection is essential.

{{% /alert %}}