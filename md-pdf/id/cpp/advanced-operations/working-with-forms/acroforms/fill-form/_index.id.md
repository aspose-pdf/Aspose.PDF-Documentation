---
title: Isi AcroForm
linktitle: Isi AcroForm
type: docs
weight: 20
url: /cpp/fill-form/
description: Bagian ini menjelaskan cara mengisi bidang formulir dalam dokumen PDF dengan Aspose.PDF untuk C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Dokumen PDF adalah yang terbaik, dan benar-benar jenis file yang disukai, untuk membuat Formulir.

Topik ini menjelaskan cara mengisi formulir PDF menggunakan Aspose.PDF untuk C++.

Aspose.PDF untuk C++ memungkinkan Anda untuk mengisi bidang formulir, mendapatkan bidang dari koleksi Formulir objek Dokumen.

Mari kita lihat contoh berikut bagaimana menyelesaikan tugas ini:

```cpp
using namespace System;
using namespace Aspose::Pdf;

void FillAcroform()
{
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"FillFormField.pdf");

    // Dapatkan bidang
    auto textBoxField = System::DynamicCast<Aspose::Pdf::Forms::TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Ubah nilai bidang
    textBoxField->set_Value(u"Nilai yang akan diisi di bidang");

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"FillFormField_out.pdf");

}
```