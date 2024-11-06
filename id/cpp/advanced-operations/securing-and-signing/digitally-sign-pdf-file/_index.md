---
title: Cara menandatangani PDF secara digital
linktitle: Tanda tangan PDF secara digital
type: docs
weight: 10
url: id/cpp/digitally-sign-pdf-file/
description: Menandatangani dokumen PDF secara digital menggunakan C++. Verifikasi, atau validasi PDF yang telah ditandatangani secara digital menggunakan C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Menandatangani PDF dengan tanda tangan digital

Anda dapat menandatangani dokumen PDF untuk mengonfirmasi isinya, atau Anda dapat menyetujui dokumen dengan Aspose.PDF.

Aspose.PDF untuk C++ mendukung fitur untuk menandatangani file PDF secara digital menggunakan kelas SignatureField. Anda juga dapat mengesahkan file PDF dengan Sertifikat PKCS12. Sesuatu yang mirip dengan [Menambahkan Tanda Tangan dan Keamanan di Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

Gunakan kelas [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) untuk menandatangani PDF Anda.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// String untuk nama jalur.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Gunakan PKCS7/PKCS7Detached
























// objek

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// Simpan file PDF keluaran

signature->Save(outFile);
}
```

## Tambahkan stempel waktu ke tanda tangan digital

### Cara menandatangani PDF secara digital dengan stempel waktu

Aspose.PDF untuk C++ mendukung penandatanganan digital PDF dengan server stempel waktu atau layanan Web.

Stempel waktu digunakan untuk menunjukkan tanggal dan waktu ketika Anda menandatangani dokumen. Pemberian stempel waktu yang andal membuktikan bahwa konten PDF Anda ada pada titik waktu tertentu dan belum berubah sejak saat itu.

Gunakan kelas [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) untuk menambahkan stempel waktu terpercaya ke tanda tangan digital atau dokumen.

Silakan lihat potongan kode berikut yang memperoleh stempel waktu dan menambahkannya ke dokumen PDF:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// String untuk nama path.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // Pengguna/Kata Sandi dapat
























// diabaikan

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// Buat salah satu dari tiga jenis tanda tangan

signature->Sign(1, u"Alasan Tanda Tangan", u"Kontak", u"Lokasi", true, rect, pkcs);

// Simpan file PDF keluaran

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```