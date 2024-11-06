---
title: Ekstrak Data AcroForm menggunakan C++
linktitle: Ekstrak Data AcroForm
type: docs
weight: 30
url: id/cpp/extract-form/
description: Bagian ini menjelaskan cara mengekstrak formulir dari dokumen PDF Anda dengan Aspose.PDF untuk C++.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Dapatkan Nilai dari semua Bidang Dokumen PDF

Untuk mendapatkan nilai dari semua bidang dalam dokumen PDF, Anda perlu menavigasi melalui semua bidang formulir dan kemudian mendapatkan nilainya menggunakan properti Value. Dapatkan setiap bidang dari koleksi Formulir, dalam tipe bidang dasar yang disebut Field dan akses properti Value-nya.

Cuplikan kode berikut menunjukkan cara mendapatkan nilai dari semua bidang dalam dokumen PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void ExtractDataFromForm()
{
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");

    // Dapatkan nilai dari semua bidang
    for(auto wa : document->get_Form())
    {
        auto formField = System::DynamicCast<Aspose::Pdf::Forms::Field>(wa);

        Console::WriteLine(u"Nama Bidang : {0} ", formField->get_PartialName());
        Console::WriteLine(u"Nilai : {0} ", formField->get_Value());
    }
}
```
```

## Mendapatkan Nilai dari Kolom Individu Dokumen PDF

Properti Nilai kolom formulir memungkinkan Anda untuk mendapatkan nilai dari kolom tertentu. Untuk mendapatkan nilainya, dapatkan kolom formulir dari koleksi Formulir objek Dokumen. Contoh ini memilih sebuah [TextBoxField](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.forms.text_box_field) dan mengambil nilainya menggunakan properti Nilai.

Potongan kode berikut menunjukkan cara mendapatkan nilai dari kolom individu dalam dokumen PDF.

```cpp
void GetValueFromIndividualField(){

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");

    // Dapatkan kolom
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Dapatkan nilai kolom
    Console::WriteLine(u"PartialName : {0} ", textBoxField->get_PartialName());
    Console::WriteLine(u"Value : {0} ", textBoxField->get_Value());
}
```

Untuk mendapatkan URL tombol submit, gunakan baris kode berikut.

```cpp
void GetSubmitButtonURL()
{
    String _dataDir("C:\\Samples\\");

    // Open document
    auto document = MakeObject<Document>(_dataDir + u"GetValueFromField.pdf");
    auto act = System::DynamicCast<Aspose::Pdf::Annotations::SubmitFormAction>(document->get_Form()->idx_get(1)->get_OnActivated());

    if (act != nullptr)
        Console::WriteLine(act->get_Url()->get_Name());
}
```

## Mendapatkan Bidang Formulir dari Wilayah Tertentu dalam File PDF

Terkadang, Anda mungkin tahu di mana dalam dokumen bidang formulir berada, tetapi tidak mengetahui namanya. Sebagai contoh, jika yang Anda miliki hanya skema formulir cetak. Dengan Aspose.PDF untuk C++, ini bukan masalah. Anda dapat menemukan bidang mana yang ada di wilayah tertentu dari file PDF. Untuk mendapatkan bidang formulir dari wilayah tertentu dari file PDF:

1. Buka file PDF menggunakan objek Document.
1. Buat objek persegi panjang untuk mendapatkan bidang di area tersebut
1. Dapatkan formulir dari koleksi Forms dokumen.
1. Tampilkan nama dan nilai Bidang

Cuplikan kode berikut menunjukkan cara mendapatkan bidang formulir di wilayah persegi panjang tertentu dari file PDF.
```

```cpp
void GetFormFieldsFromSpecificRegion()
{
    String _dataDir("C:\\Samples\\");

    // Buka file pdf
    auto document = MakeObject<Aspose::Pdf::Document>(_dataDir + u"GetFieldsFromRegion.pdf");

    // Buat objek persegi untuk mendapatkan field di area tersebut
    auto rectangle = MakeObject<Aspose::Pdf::Rectangle>(35, 30, 500, 500);

    // Dapatkan field di area persegi panjang
    auto fields = document->get_Form()->GetFieldsInRect(rectangle);

    // Tampilkan nama dan nilai Field
    for(auto field : fields)
    {
        // Tampilkan properti penempatan gambar untuk semua penempatan
        Console::WriteLine(u"Nama Field: {0} - Nilai Field: {1}", field->get_FullName(), field->get_Value());
    }
}
```