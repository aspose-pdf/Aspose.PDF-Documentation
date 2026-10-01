---
title: "Memisahkan file PDF menjadi halaman individual dalam PHP"
linktitle: "Memisahkan file PDF menjadi halaman individual dalam PHP"
type: docs
weight: 80
url: /id/java/split-pdf-file-into-individual-pages-in-php/
description: Temukan cara memisahkan dokumen PDF menjadi halaman individual menggunakan PHP dan Aspose.PDF untuk ekstraksi halaman yang efisien.
lastmod: "2026-09-30"
---
## Aspose.PDF - Pisah halaman

Untuk memisahkan dokumen PDF menjadi halaman individual menggunakan **Aspose.PDF Java for PHP**, cukup panggil kelas **SplitAllPages**.

Kode PHP

```php

# Open the target document
$pdf = new Document($dataDir . 'input1.pdf');

# loop through all the pages
$pdf_page = 1;
$total_size = $pdf->getPages()->size();
#for (int pdfPage = 1; pdfPage<= pdfDocument1.getPages().size(); pdfPage++)
while ($pdf_page <= $total_size)

{

    # create a new Document object
    $new_document = new Document();

    # get the page at particular index of Page Collection
    $new_document->getPages()->add($pdf->getPages()->get_Item($pdf_page));

    # save the newly generated PDF file
    $new_document->save($dataDir . "page_#{$pdf_page}.pdf");

    $pdf_page++;

}

print "Split process completed successfully!";

```

**Mengunduh kode yang dapat dijalankan**

Unduh **Split Pages (Aspose.PDF)**В dariВ salah satu situs pengkodean sosial yang disebutkan di bawah:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/blob/master/Plugins/Aspose_Pdf_Java_for_PHP/src/Aspose/Pdf/WorkingWithPages/SplitAllPages.php)
