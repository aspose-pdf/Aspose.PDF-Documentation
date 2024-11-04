---
title: Posting AcroForm Data
linktitle: Posting AcroForm
type: docs
weight: 50
url: /cpp/posting-acroform-data/
description: Anda dapat mengimpor dan mengekspor data formulir ke dan dari file XML dengan namespace Aspose.Pdf.Facades di Aspose.PDF untuk C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

{{% alert color="primary" %}}

AcroForm adalah jenis dokumen PDF yang penting. Anda tidak hanya dapat membuat dan mengedit AcroForm menggunakan [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades), tetapi juga mengimpor dan mengekspor data formulir ke dan dari file XML. Namespace Aspose.Pdf.Facades di Aspose.PDF untuk C++ memungkinkan Anda untuk mengimplementasikan fitur lain dari AcroForm, yang membantu Anda mengirim data AcroForm ke halaman web eksternal. Halaman web ini kemudian membaca variabel yang dikirim dan menggunakan data ini untuk pemrosesan lebih lanjut. Fitur ini berguna dalam kasus ketika Anda tidak hanya ingin menyimpan data di file PDF, melainkan ingin mengirimkannya ke server Anda dan kemudian menyimpannya di database dll.
{{% /alert %}}

## Detail implementasi

Dalam artikel ini, kami telah mencoba membuat AcroForm menggunakan [Aspose.Pdf.Facades namespace](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades) dan kelas [FormEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form_editor/). Kami juga telah menambahkan tombol kirim dan menetapkan URL targetnya.

Cuplikan kode berikut menunjukkan kepada Anda cara membuat formulir dan kemudian menerima data yang dikirimkan di halaman web.
```cpp
using namespace System;
using namespace Aspose::Pdf;

void PostingExample() {

    // String _dataDir("C:\\Samples\\");
    // Buat instance dari kelas FormEditor dan hubungkan file pdf input dan output
    auto editor = MakeObject<Aspose::Pdf::Facades::FormEditor>("input.pdf", "output.pdf");

    // Buat bidang AcroForm - Saya hanya membuat dua bidang untuk kesederhanaan
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"firstname", 1, 100, 600, 200, 625);
    editor->AddField(Aspose::Pdf::Facades::FieldType::Text, u"lastname", 1, 100, 550, 200, 575);

    // Tambahkan tombol submit dan setel URL target
    editor->AddSubmitBtn(u"submitbutton", 1, u"Submit", u"http://localhost/csharptesting/show.aspx", 100, 450, 150, 475);

    // Simpan file pdf output
    editor->Save();
}
```