---
title: Memodifikasi AcroForm
linktitle: Memodifikasi AcroForm
type: docs
weight: 40
url: id/cpp/modifing-form/
description: Memodifikasi formulir dalam file PDF Anda dengan pustaka Aspose.PDF untuk C++. Anda dapat menambah atau menghapus bidang dalam formulir yang ada, mendapatkan dan mengatur batas bidang, dan lain-lain.
lastmod: "2021-12-01"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Mendapatkan atau Mengatur Batas Bidang

Metode FormEditor SetFieldLimit(field, limit) memungkinkan Anda mengatur batas bidang, jumlah maksimum karakter yang dapat dimasukkan ke dalam bidang.

```cpp
void SetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Membuka dokumen
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    textBoxField->set_MaxLen(15);
    document->Save(_dataDir + u"GetValuesFromAllFields.pdf");
}
```

Demikian pula, Aspose.PDF memiliki metode yang mendapatkan batas bidang menggunakan pendekatan DOM. Berikut adalah potongan kode yang menunjukkan langkah-langkahnya.

```cpp
void GetFieldLimitDom() {
    String _dataDir("C:\\Samples\\");
    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"GetValuesFromAllFields.pdf");
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));
    Console::WriteLine(u"Batas: {0}", textBoxField->get_MaxLen());        
}
```

Anda juga dapat mengatur dan mendapatkan nilai yang sama menggunakan namespace *Aspose.PDF.Facades* dengan menggunakan potongan kode berikut.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Forms;

void SetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Menambahkan Field dengan batas
    auto form = MakeObject<Aspose::Pdf::Facades::FormEditor>(_dataDir + u"input.pdf", _dataDir + u"SetFieldLimit_out.pdf");
    form->SetFieldLimit(u"textbox1", 15);
    form->Save();
}
```

```cpp
void GetFieldLimitFacade(){
    String _dataDir("C:\\Samples\\");
    // Menambahkan Field dengan batas
    auto form = MakeObject<Aspose::Pdf::Facades::Form>(_dataDir + u"input.pdf");
    Console::WriteLine(u"Batas: {0}", form->GetFieldLimit(u"textbox1"));
}
```
## Atur Font Kustom untuk Bidang Formulir

Bidang formulir dalam file PDF Adobe dapat dikonfigurasi untuk menggunakan font default tertentu. Pada versi awal Aspose.PDF, hanya 14 font default yang didukung. Rilis selanjutnya memungkinkan pengembang untuk menerapkan font apa pun. Untuk mengatur dan memperbarui font default yang digunakan untuk bidang formulir, gunakan kelas DefaultAppearance (Font font, double size, Color color). Kelas ini dapat ditemukan di bawah namespace Aspose.PDF.InteractiveFeatures. Untuk menggunakan objek ini, gunakan properti DefaultAppearance dari kelas Field.

Cuplikan kode berikut menunjukkan cara mengatur font default untuk bidang formulir PDF.

```cpp
void SetCustomFontForField() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = new Document(_dataDir + u"FormFieldFont14.pdf");

    // Dapatkan bidang formulir tertentu dari dokumen
    auto textBoxField = System::DynamicCast<TextBoxField>(document->get_Form()->idx_get(u"textbox1"));

    // Buat objek font
    auto font = Aspose::Pdf::Text::FontRepository::FindFont(u"ComicSansMS");

    // Atur informasi font untuk bidang formulir

    textBoxField->set_DefaultAppearance(MakeObject<Aspose::Pdf::Annotations::DefaultAppearance>(font, 10, System::Drawing::Color::get_Black()));

    // Simpan dokumen yang diperbarui
    document->Save(_dataDir + u"FormFieldFont14.pdf");
}
```

## Hapus bidang dari formulir yang ada

Semua bidang formulir terdapat dalam koleksi Form dari objek Document. Koleksi ini menyediakan berbagai metode yang mengelola bidang formulir, termasuk metode Delete. Jika Anda ingin menghapus bidang tertentu, berikan nama bidang sebagai parameter ke metode Delete dan kemudian simpan dokumen PDF yang telah diperbarui. Cuplikan kode berikut menunjukkan cara menghapus bidang tertentu dari dokumen PDF.

```cpp
void DeleteFormField() {    
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = new Document(_dataDir + u"DeleteFormField.pdf");

    // Hapus bidang tertentu berdasarkan nama
    document->get_Form()->Delete(u"textbox1");
    
    // Simpan dokumen yang telah dimodifikasi
    document->Save(_dataDir + u"DeleteFormField_out.pdf");
}
```