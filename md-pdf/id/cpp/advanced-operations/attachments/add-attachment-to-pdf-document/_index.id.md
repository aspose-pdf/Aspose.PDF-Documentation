```
---
title: Menambahkan Lampiran ke Dokumen PDF
linktitle: Menambahkan Lampiran ke Dokumen PDF
type: docs
weight: 10
url: /cpp/add-attachment-to-pdf-document/
description: Halaman ini menjelaskan cara menambahkan lampiran ke file PDF dengan pustaka Aspose.PDF untuk C++
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Lampiran dapat berisi berbagai informasi dan dapat berupa berbagai jenis file. Artikel ini menjelaskan cara menambahkan lampiran ke file PDF.

1. Buat proyek C++ baru.
1. Tambahkan referensi ke Aspose.PDF DLL.
1. Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Buat objek [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) dengan file yang Anda tambahkan, dan deskripsi file.
1.
``` Tambahkan objek [FileSpecification](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.file_specification) ke koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) dari objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document), dengan metode Add dari koleksi tersebut.

Koleksi [EmbeddedFiles](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.embedded_file_collection) berisi semua lampiran dalam file PDF. Cuplikan kode berikut menunjukkan cara menambahkan lampiran dalam dokumen PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void WorkingWithAttachments::AddingAttachment()
{

String _dataDir("C:\\Samples\\");


// Buka dokumen

auto pdfDocument = MakeObject<Document>(_dataDir + u"AddAttachment.pdf");


// Siapkan file baru untuk ditambahkan sebagai lampiran

auto fileSpecification = MakeObject<FileSpecification>(_dataDir + u"test.txt", u"Contoh file teks");


// Tambahkan lampiran ke koleksi lampiran dokumen

pdfDocument->get_EmbeddedFiles()->Add(fileSpecification);


// Simpan output baru

pdfDocument->Save(_dataDir + u"AddAttachment_out.pdf");
}
```