---
title: Manipulasi Tabel di PDF yang Ada
linktitle: Manipulasi Tabel
type: docs
weight: 40
url: id/cpp/manipulate-tables-in-existing-pdf/
description: Bagian ini mencakup berbagai metode untuk modifikasi tabel menggunakan Aspose.PDF untuk C++
lastmod: "2021-11-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Manipulasi tabel di PDF yang ada

Aspose.PDF untuk C++ memungkinkan Anda untuk bekerja dengan cepat dan efisien dengan tabel, yaitu, membuatnya dari awal atau menambahkannya ke dokumen PDF yang ada.

Anda juga mendapatkan kemampuan untuk mengintegrasikan tabel dengan database (DOM) untuk membuat tabel dinamis berdasarkan isi dari database.

Kelas [Aspose.PDF.Text.TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) memungkinkan Anda untuk mencari dan mem-parsing tabel sederhana yang sudah ada di halaman dokumen PDF. Cuplikan kode berikut menunjukkan langkah-langkah untuk memperbarui konten dalam sel tertentu di tabel.

>Headers:

```cpp
#include <system/date_time.h>
#include <system/io/file.h>
#include <system/console.h>
#include <data/data_table.h>
#include <data/data_column_collection.h>
#include <system/type_info.h>

#include <Aspose.PDF.Cpp/Document.h>
#include <Aspose.PDF.Cpp/Page.h>
#include <Aspose.PDF.Cpp/PageCollection.h>
#include <Aspose.PDF.Cpp/Generator/BorderInfo.h>
#include <Aspose.PDF.Cpp/Generator/BorderSide.h>

#include <Aspose.PDF.Cpp/Text/TextFragment.h>
#include <Aspose.PDF.Cpp/Text/TextFragmentCollection.h>

#include <Aspose.PDF.Cpp/Color.h>

#include <Aspose.PDF.Cpp/Table/Table.h>
#include <Aspose.PDF.Cpp/Table/Row.h>
#include <Aspose.PDF.Cpp/Table/Rows.h>
#include <Aspose.PDF.Cpp/Table/Cell.h>
#include <Aspose.PDF.Cpp/Table/Cells.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/TableAbsorber.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedTable.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedRow.h>
#include <Aspose.PDF.Cpp/Text/TableAbsorber/AbsorbedCell.h>
```

>Samples:

```cpp
using namespace System;
using namespace Aspose::Pdf;

#include "Table-Manipulate.h"

void ManipulateTables() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF yang ada
    auto document = MakeObject<Document>(_dataDir + u"input.pdf");

    // Buat objek TableAbsorber untuk menemukan tabel
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Kunjungi halaman pertama dengan absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Dapatkan akses ke tabel pertama di halaman, sel pertama mereka dan fragmen teks di dalamnya
    auto fragment = absorber->get_TableList()->idx_get(0)->get_RowList()->idx_get(0)->get_CellList()->idx_get(0)->get_TextFragments()->idx_get(1);

    // Ubah teks fragmen teks pertama di sel
    fragment->set_Text(u"hi world");
    document->Save(_dataDir + u"ManipulateTable_out.pdf");
}
```

## Ganti Tabel lama dengan yang baru dalam dokumen PDF

Jika Anda perlu menemukan tabel tertentu dan menggantinya dengan yang diinginkan, Anda dapat menggunakan metode Replace() dari Kelas [TableAbsorber](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.text.absorbed_table) untuk melakukannya.

Contoh berikut menunjukkan fungsi untuk mengganti tabel di dalam dokumen PDF:

```cpp
void ReplaceOldTable() {
    String _dataDir("C:\\Samples\\");

    // Muat file PDF yang ada
    auto document = MakeObject<Document>(_dataDir + u"Table_input2.pdf");

    // Buat objek TableAbsorber untuk menemukan tabel
    auto absorber = MakeObject<Aspose::Pdf::Text::TableAbsorber>();

    // Kunjungi halaman pertama dengan absorber
    absorber->Visit(document->get_Pages()->idx_get(1));

    // Dapatkan tabel pertama di halaman
    auto table = absorber->get_TableList()->idx_get(0);

    // Buat tabel baru
    auto newTable = MakeObject<Table>();
    newTable->set_ColumnWidths(u"100 100 100");
    newTable->set_DefaultCellBorder (MakeObject<BorderInfo>(BorderSide::All, 1.0F));

    auto row = newTable->get_Rows()->Add();
    row->get_Cells()->Add(u"Kol 1");
    row->get_Cells()->Add(u"Kol 2");
    row->get_Cells()->Add(u"Kol 3");

    // Gantikan tabel dengan yang baru
    absorber->Replace(document->get_Pages()->idx_get(1), table, newTable);

    // Simpan dokumen
    document->Save(_dataDir + u"TableReplaced_out.pdf");
}
```