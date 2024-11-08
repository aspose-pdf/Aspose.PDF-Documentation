---
title: Membuat Tautan di File PDF dengan C++
linktitle: Buat Tautan
type: docs
weight: 10
url: /id/cpp/create-links/
description: Bagian ini menjelaskan cara membuat tautan dalam dokumen PDF Anda dengan C++.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Buat Tautan

Dengan menambahkan tautan ke aplikasi ke dalam dokumen, dimungkinkan untuk menautkan ke aplikasi dari dokumen. Ini berguna ketika Anda ingin pembaca mengambil tindakan tertentu pada titik tertentu dalam tutorial, misalnya, atau untuk membuat dokumen yang kaya fitur. Untuk membuat tautan aplikasi:

1. [Buat Objek Dokumen](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Dapatkan [Halaman](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) yang ingin Anda tambahkan tautan.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) menggunakan objek Halaman dan [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Setel atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Juga, setel ke properti Action dari objek [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/).
1. Saat membuat objek [LaunchAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.launch_action/), tentukan aplikasi yang ingin Anda luncurkan.
1. Tambahkan tautan ke properti [Annotations](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.annotations) dari objek Page.
1. Terakhir, simpan PDF yang diperbarui menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara membuat tautan ke aplikasi dalam file PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;

void CreateLink() 
{
    String _dataDir("C:\\Samples\\");
    // Buat instance Document
    auto document = MakeObject<Document>(_dataDir + u"CreateApplicationLink.pdf");

    // Tambahkan halaman ke koleksi halaman dari file PDF
    auto page = document->get_Pages()->idx_get(1);

    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::LaunchAction>(document, _dataDir + u"sample.pdf"));
    page->get_Annotations()->Add(link);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"CreateApplicationLink.pdf");
}
```

### Buat Tautan Dokumen PDF di dalam File PDF

Aspose.PDF untuk C++ memungkinkan Anda menambahkan tautan ke file PDF eksternal sehingga Anda dapat menghubungkan beberapa dokumen bersama. Untuk membuat tautan dokumen PDF:

1. Pertama, buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Kemudian, dapatkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) tertentu yang ingin Anda tambahkan tautannya.
1. Buat objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) menggunakan objek Page dan [Rectangle](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.rectangle).
1. Atur atribut tautan menggunakan objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).
1. Atur properti Action ke objek [GoToRemoteAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_remote_action/).
1.
``` Saat membuat objek GoToRemoteAction, tentukan file PDF yang harus diluncurkan, serta nomor halaman yang harus dibuka.
1. Tambahkan tautan ke koleksi Anotasi objek Page.
1. Simpan PDF yang diperbarui menggunakan metode Save dari objek Document.

Cuplikan kode berikut menunjukkan cara membuat tautan dokumen PDF dalam file PDF.

 ```cpp
void CreatePDFDocumentLink() 
{

    String _dataDir("C:\\Samples\\");
    // Buat instance Document
    auto document = MakeObject<Document>(_dataDir + u"CreateDocumentLink.pdf");

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->idx_get(1);


    auto link = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, MakeObject<Rectangle>(100, 200, 300, 300));
    link->set_Color(Aspose::Pdf::Color::get_Green());

    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToRemoteAction>(_dataDir + u"sample.pdf", 1));
    page->get_Annotations()->Add(link);

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"CreateDocumentLink_out.pdf");
}
```