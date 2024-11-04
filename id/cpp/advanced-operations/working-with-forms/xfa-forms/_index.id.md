---
title: Bekerja dengan Formulir XFA menggunakan C++
linktitle: Formulir XFA
type: docs
weight: 20
url: /cpp/xfa-forms/
description: Aspose.PDF untuk API C++ memungkinkan Anda bekerja dengan XFA dan bidang XFA Acroform dalam dokumen PDF. Aspose.PDF.Facades.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Formulir XFA adalah Arsitektur Formulir XML, keluarga spesifikasi XML berpemilik yang diusulkan dan dikembangkan oleh JetForm untuk meningkatkan penanganan formulir web. Ini juga dapat digunakan dalam file PDF mulai dari spesifikasi PDF 1.5.

Isi bidang XFA dengan kelas [Form](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.form/) oleh [Aspose.Pdf.Facades](https://reference.aspose.com/pdf/cpp/namespace/aspose.pdf.facades).

## Isi bidang XFA

Cuplikan kode berikut menunjukkan cara mengisi bidang dalam formulir XFA.

```cpp
using namespace System;
using namespace System::Collections::Generic;

using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void FillXFA() {
    String _dataDir("C:\\Samples\\");

    // Muat formulir XFA
    auto document = MakeObject<Document>(_dataDir + u"FillXFAFields.pdf");

    // Dapatkan nama-nama bidang formulir XFA
    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Tetapkan nilai bidang

    document->get_Form()->get_XFA()->idx_set(names->idx_get(0),u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(1),u"Field 1");

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```
```

## Convert XFA to AcroForm

{{% alert color="primary" %}}

Coba online
Anda dapat memeriksa kualitas konversi Aspose.PDF dan melihat hasilnya secara online di tautan ini: [products.aspose.app/pdf/xfa/acroform](https://products.aspose.app/pdf/xfa/acroform)

{{% /alert %}}

Formulir dinamis didasarkan pada spesifikasi XML yang dikenal sebagai XFA, “XML Forms Architecture”. Informasi tentang formulir tersebut (sejauh menyangkut PDF) sangat samar – ini menentukan bahwa bidang-bidang ada, dengan properti-properti, dan kejadian-kejadian JavaScript, tetapi tidak menentukan rendering apa pun.

Saat ini, PDF mendukung dua metode berbeda untuk mengintegrasikan data dan formulir PDF:

- AcroForms (juga dikenal sebagai formulir Acrobat), diperkenalkan dan disertakan dalam spesifikasi format PDF 1.2.
- Adobe XML Forms Architecture (XFA) forms, diperkenalkan dalam spesifikasi format PDF 1.5 sebagai fitur opsional (Spesifikasi XFA tidak disertakan dalam spesifikasi PDF, hanya dirujuk.)

Kami tidak dapat mengekstrak atau memanipulasi halaman dari Formulir XFA, karena konten formulir tersebut dihasilkan saat runtime (selama tampilan formulir XFA) di dalam aplikasi yang mencoba menampilkan atau merender formulir XFA. Aspose.PDF memiliki fitur yang memungkinkan pengembang untuk mengonversi formulir XFA ke AcroForms standar.

```cpp
void ConvertXFAtoAcroForms() {

    String _dataDir("C:\\Samples\\");

    // Muat formulir XFA
    auto document = MakeObject<Document>(_dataDir + u"DynamicXFAToAcroForm.pdf");

    // Atur tipe bidang formulir sebagai AcroForm standar
    document->get_Form()->set_Type(Aspose::Pdf::Forms::FormType::Standard);

    // Simpan PDF hasil
    document->Save(_dataDir + u"Standard_AcroForm_out.pdf");
}
```

## Dapatkan properti bidang XFA

Untuk mengakses properti bidang, pertama gunakan Document.Form.XFA.Teamplate untuk mengakses template bidang. Cuplikan kode berikut menunjukkan langkah-langkah mendapatkan koordinat X dan Y dari bidang formulir XFA.

```cpp
void GetXFAProprties() {

    String _dataDir("C:\\Samples\\");
    // Muat formulir XFA
    auto document = MakeObject<Document>(_dataDir + u"GetXFAProperties.pdf");

    auto names = document->get_Form()->get_XFA()->get_FieldNames();

    // Atur nilai bidang
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 0");
    document->get_Form()->get_XFA()->idx_set(names->idx_get(0), u"Field 1");

    // Dapatkan posisi bidang
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"x")->get_Value());

    // Dapatkan posisi bidang
    Console::WriteLine(document->get_Form()->get_XFA()->GetFieldTemplate(names[0])->get_Attributes()->idx_get(u"y")->get_Value());

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"Filled_XFA_out.pdf");
}
```