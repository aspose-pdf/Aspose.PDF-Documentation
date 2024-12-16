---
title: Membagi File PDF menjadi Halaman Individu dalam PHP
type: docs
weight: 80
url: /id/java/split-pdf-file-into-individual-pages-in-php/
lastmod: "2021-06-05"
---

## Aspose.PDF - Membagi Halaman

Untuk membagi dokumen PDF menjadi halaman individu menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **SplitAllPages**.

Kode PHP

```php

# Buka dokumen target
$pdf = new Document($dataDir . 'input1.pdf');

# loop melalui semua halaman
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # buat objek Dokumen baru
    $new_document = new Document();

    # dapatkan halaman pada indeks tertentu dari Koleksi Halaman
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # simpan file PDF yang baru dihasilkan
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Proses pemisahan selesai dengan sukses!";

```

**Unduh Kode Berjalan**

Unduh **Membagi Halaman (Aspose.PDF)** dari salah satu situs sosial coding yang disebutkan di bawah ini:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)