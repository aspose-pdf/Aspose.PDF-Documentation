---
title: Ekstrak Data Tabel dari PDF 
linktitle: Ekstrak Data Tabel
type: docs
weight: 40
url: id/php-java/extract-data-from-table-in-pdf/
description: Pelajari cara mengekstrak tabel dari PDF menggunakan Aspose.PDF untuk PHP
lastmod: "2021-05-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Ekstrak Tabel dari PDF secara programatik

Mengekstrak tabel dari PDF bukanlah tugas yang sepele karena tabel dapat dibuat dengan berbagai cara.

Aspose.PDF untuk PHP via Java memiliki alat untuk memudahkan pengambilan tabel. Untuk mengekstrak data tabel, Anda harus melakukan langkah-langkah berikut:

1. Buka dokumen PDF - buat objek [Document](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/Document);
1. Buat objek TableAbsorber [TableAbsorber](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/tableabsorber) untuk mengekstrak tabel dari dokumen.
1. Iterasi melalui setiap halaman dokumen.

1. Tentukan halaman mana yang akan dianalisis dan terapkan [visit](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#visit-com.aspose.pdf.Page-) pada halaman yang diinginkan. Data tabel akan dipindai, dan hasilnya akan disimpan dalam daftar [AbsorbedTable](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedTable). Kita bisa mendapatkan daftar ini melalui metode [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--).

1. Untuk mendapatkan data, iterasi melalui `TableList` dan tangani daftar [absorbed rows](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow) dan daftar sel yang diserap. Kita dapat mengakses daftar pertama dengan memanggil metode [getTableList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TableAbsorber#getTableList--) dan ke yang kedua dengan memanggil [getCellList](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedRow#getCellList--).

1. Setiap [AbsorbedCell](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/AbsorbedCell) berisi [TextFragmentCollections](https://reference.aspose.com/pdf/php-java/com.aspose.pdf/TextFragmentCollection). Anda dapat memprosesnya untuk tujuan Anda sendiri.

Contoh berikut menunjukkan ekstraksi tabel dari semua halaman:

```php

$document = new Document($inputFile);
$tableAbsorber = new TableAbsorber();


for ($pageIndex = 1; $pageIndex <= java_values($pages->size()); $pageIndex++) {
    $page = $pages->get_Item($pageIndex);
    $tableAbsorber->visit($page);
    $tableList = $tableAbsorber->getTableList();
    $tableIterator = $tableList->iterator();

    while (java_values($tableIterator->hasNext())) {
        $table = $tableIterator->next();
        $tableRowList = $table->getRowList();
        $tableRowListIterator = $tableRowList->iterator();

        while (java_values($tableRowListIterator->hasNext())) {
            $row = $tableRowListIterator->next();
            $cellList = $row->getCellList();
            $cellListIterator = $cellList->iterator();

            // Iterasi melalui setiap sel dalam baris.
            while (java_values($cellListIterator->hasNext())) {
                $cell = $cellListIterator->next();
                $fragmentList = $cell->getTextFragments();

                // Iterasi melalui setiap fragmen teks dalam sel.
                for ($fragmentIndex = 1; $fragmentIndex <= java_values($fragmentList->size()); $fragmentIndex++) {
                    $fragment = $fragmentList->get_Item($fragmentIndex);
                    $segments = $fragment->getSegments();

                    // Iterasi melalui setiap segmen dalam fragmen teks.
                    for ($segmentIndex = 1; $segmentIndex <= java_values($segments->size()); $segmentIndex++) {
                        $segment = $segments->get_Item($segmentIndex);
                        $responseData .= $segment->getText();
                    }
                }
                $responseData .= "|";
            }
            $responseData .= PHP_EOL;
        }
    }
}

// Simpan data tabel ke file output.
file_put_contents($outputFile, $responseData);

// Tutup dokumen PDF.
$document->close();
```


## Ekstrak Data Tabel dari PDF dan simpan ke file CSV

Contoh berikut menunjukkan cara mengekstrak tabel dan menyimpannya sebagai file CSV.
Untuk melihat cara mengonversi PDF ke Spreadsheet Excel silakan merujuk ke artikel [Konversi PDF ke Excel](/pdf/php-java/convert-pdf-to-excel/).

```php

    // Muat dokumen PDF input menggunakan kelas Document.
    $document = new Document($inputFile);

    // Buat instance dari kelas ExcelSaveOptions untuk menentukan opsi penyimpanan.
    $saveOption = new ExcelSaveOptions();

    // Atur format output ke CSV.
    $saveOption->setFormat(ExcelSaveOptions_ExcelFormat::$CSV);

    // Simpan dokumen PDF sebagai file Excel menggunakan opsi penyimpanan yang ditentukan.
    $document->save($outputFile, $saveOption);
```