```
---
title: Ekstra Anotasi menggunakan C++
linktitle: Ekstra Anotasi
type: docs
weight: 60
url: /id/cpp/extra-annotations/
description: Bagian ini menjelaskan cara menambahkan, mendapatkan, dan menghapus jenis anotasi ekstra dari dokumen PDF Anda.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Cara menambahkan Anotasi Caret ke dalam file PDF yang ada

Anotasi Caret adalah simbol yang menunjukkan pengeditan teks. Anotasi Caret juga merupakan anotasi markup, jadi kelas Caret diturunkan dari kelas Markup dan juga menyediakan fungsi untuk mendapatkan atau mengatur properti Anotasi Caret dan mengatur ulang aliran tampilan Anotasi Caret.

Langkah-langkah dengan mana kita membuat anotasi Caret:

1. Muat file PDF - baru [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1.
``` Buat baru [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) dan atur parameter Caret (Rectangle baru, judul, Subjek, Bendera, warna, lebar, StartingStyle dan EndingStyle). Anotasi ini digunakan untuk menunjukkan penyisipan teks.
1. Buat baru [Caret Annotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.caret_annotation/) dan atur parameter Caret (Rectangle baru, judul, Subjek, Bendera, warna, lebar, StartingStyle dan EndingStyle). Anotasi ini digunakan untuk menunjukkan penggantian teks.
1. Buat baru [StrikeOutAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.strike_out_annotation/) dan atur parameter (Rectangle baru, judul, warna, QuadPoints baru dan titik baru, Subjek, InReplyTo, ReplyType).
1. Setelah itu kita bisa menambahkan anotasi ke halaman.

Cuplikan kode berikut menunjukkan cara menambahkan Caret Annotation ke file PDF:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void MarkupAnnotations::AddCaretAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    // Anotasi ini digunakan untuk menunjukkan penyisipan teks
    auto caretAnnotation1 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(299.988, 713.664, 308.708, 720.769));
    caretAnnotation1->set_Title(u"Pengguna Aspose");
    caretAnnotation1->set_Subject(u"Teks yang disisipkan 1");
    caretAnnotation1->set_Flags(AnnotationFlags::Print);
    caretAnnotation1->set_Color(Color::get_Blue());

    // Anotasi ini digunakan untuk menunjukkan penggantian teks
    auto caretAnnotation2 = MakeObject<CaretAnnotation>(
        document->get_Pages()->idx_get(1),
        new Rectangle(361.246, 727.908, 370.081, 735.107));

    caretAnnotation2->set_Title(u"Pengguna Aspose");
    caretAnnotation2->set_Flags(AnnotationFlags::Print);
    caretAnnotation2->set_Subject(u"Teks yang disisipkan 2");
    caretAnnotation2->set_Color(Color::get_Blue());

    auto strikeOutAnnotation = MakeObject<StrikeOutAnnotation>(
        document->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(318.407, 727.826, 368.916, 740.098));

    strikeOutAnnotation->set_Color(Color::get_Blue());

    strikeOutAnnotation->set_QuadPoints(
        MakeArray<System::SharedPtr<Point>>({
            MakeObject<Point>(321.66, 739.416),
            MakeObject<Point>(365.664, 739.416),
            MakeObject<Point>(321.66, 728.508),
            MakeObject<Point>(365.664, 728.508) }));

    strikeOutAnnotation->set_Subject(u"Dibatalkan");
    strikeOutAnnotation->set_InReplyTo(caretAnnotation2);
    strikeOutAnnotation->set_ReplyType(ReplyType::Group);

    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation1);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(caretAnnotation2);
    document->get_Pages()->idx_get(1)->get_Annotations()->Add(strikeOutAnnotation);

    document->Save(_dataDir + u"sample_caret.pdf");
}
```
### Dapatkan Anotasi Caret

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Caret dalam dokumen PDF

```cpp
void MarkupAnnotations::GetCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Saring anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto ca : caretAnnotations) {
        Console::WriteLine(ca->get_Rect());
    }
}
```

### Hapus Anotasi Caret

Potongan kode berikut menunjukkan cara Menghapus Anotasi Caret dari file PDF.

```cpp

void MarkupAnnotations::DeleteCaretAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_caret.pdf");

    // Saring anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<CaretAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto caretAnnotations = annotationSelector->get_Selected();

    // hapus anotasi
    for (auto ca : caretAnnotations) {
        document->get_Pages()->idx_get(1)->get_Annotations()->Delete(ca);
    }
    document->Save(_dataDir + u"sample_caret_del.pdf");
}
```

## Cara Menambahkan Anotasi Tautan

[Anotasi Tautan](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation) adalah tautan hypertext yang mengarah ke tujuan di tempat lain dalam dokumen atau ke suatu tindakan yang akan dilakukan.

Tautan adalah area persegi panjang yang dapat ditempatkan di mana saja pada halaman. Setiap tautan memiliki tindakan PDF yang sesuai yang terkait dengannya. Tindakan ini dilakukan ketika pengguna mengklik area tautan ini.

Cuplikan kode berikut menunjukkan cara menambahkan Anotasi Tautan ke file PDF menggunakan contoh nomor telepon:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddLinkAnnotation() {
    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);

    // Membuat objek TextFragmentAbsorber untuk menemukan nomor telepon
    auto textFragmentAbsorber = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>("678-555-0103");

    // Menerima absorber hanya untuk halaman pertama
    page->Accept(textFragmentAbsorber);

    auto phoneNumberFragment = textFragmentAbsorber->get_TextFragments()->idx_get(1);

    // Membuat Anotasi Tautan dan menetapkan tindakan untuk memanggil nomor telepon
    auto linkAnnotation = MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, phoneNumberFragment->get_Rectangle());
    linkAnnotation->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("callto:678-555-0103"));

    // Menambahkan anotasi ke halaman
    page->get_Annotations()->Add(linkAnnotation);
    document->Save(_dataDir + u"SimpleResume_mod.pdf");
}
```

### Dapatkan Anotasi Tautan

Silakan coba menggunakan potongan kode berikut untuk Mendapatkan LinkAnnotation dari dokumen PDF.

```cpp
void GetLinkAnnotations() {

    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Saring anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto linkAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto la : linkAnnotations) {

        auto l = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(la);

        // Cetak URL dari setiap Anotasi Tautan
        Console::WriteLine(u"URI: " + System::DynamicCast<Aspose::Pdf::Annotations::GoToURIAction>(l->get_Action())->get_URI());

        auto absorber = MakeObject<TextAbsorber>();
        absorber->get_TextSearchOptions()->set_LimitToPageBounds(true);
        absorber->get_TextSearchOptions()->set_Rectangle(l->get_Rect());
        page->Accept(absorber);

        String extractedText = absorber->get_Text();

        // Cetak teks yang terkait dengan hyperlink
        Console::WriteLine(extractedText);
    }
}
```

### Hapus Anotasi Tautan

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi Tautan dari file PDF. Untuk ini kita perlu menemukan dan menghapus semua anotasi tautan pada halaman pertama. Setelah ini kita akan menyimpan dokumen dengan anotasi yang dihapus.

```cpp
void DeleteLinkAnnotations()
{
    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"SimpleResume_mod.pdf");

    // Saring anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);

    auto lineAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto la : lineAnnotations) {
        page->get_Annotations()->Delete(la);
    }

    // Simpan dokumen dengan anotasi yang dihapus
    document->Save(_dataDir + u"SimpleResume_del.pdf");
}
```

## Menyunting area halaman tertentu dengan Anotasi Penyuntingan menggunakan Aspose.PDF untuk C++

Aspose.PDF untuk C++ mendukung fitur untuk menambahkan serta memanipulasi Anotasi dalam file PDF yang ada. Baru-baru ini beberapa pelanggan kami memposting kebutuhan untuk menyunting (menghapus teks, gambar, dll elemen dari) area halaman tertentu dari dokumen PDF. Untuk memenuhi kebutuhan ini, sebuah kelas bernama RedactionAnnotation disediakan, yang dapat digunakan untuk menyunting area halaman tertentu atau dapat digunakan untuk memanipulasi RedactionAnnotations yang ada dan menyuntingnya (yaitu menyatukan anotasi dan menghapus teks di bawahnya).

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;


void RedactAnnotation::AddRedactionAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Buat instance RedactionAnnotation untuk area halaman tertentu
    auto annot = MakeObject<RedactionAnnotation>(page, MakeObject<Rectangle>(200, 500, 300, 600));
    annot->set_FillColor(Color::get_Green());
    annot->set_BorderColor(Color::get_Yellow());
    annot->set_Color(Color::get_Blue());

    // Teks yang akan dicetak pada anotasi penyuntingan
    annot->set_OverlayText(u"REDACTED");
    annot->set_TextAlignment(HorizontalAlignment::Center);

    // Ulangi teks overlay pada anotasi penyuntingan
    annot->set_Repeat(true);

    // Tambahkan anotasi ke koleksi anotasi halaman pertama
    page->get_Annotations()->Add(annot);

    // Menyatukan anotasi dan menyunting konten halaman (yaitu menghapus teks dan gambar
    // Di bawah anotasi yang disunting)
    annot->Redact();
    document->Save(_dataDir + u"RedactPage_out.pdf");
}
```

## Pendekatan Facades

Aspose.PDF.Facades mendukung kelas [PdfAnnotationEditor](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor/) yang menyediakan fitur untuk memanipulasi Anotasi yang ada di dalam file PDF.

Kelas ini berisi metode bernama [RedactArea(..)](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_annotation_editor#a35ebd333b63b6df2c0c299c7331e3c63) yang menyediakan kemampuan untuk menghapus area halaman tertentu.

```cpp
void RedactAnnotation::AddRedactionAnnotationViaFacades() {

    String _dataDir("C:\\Samples\\");

    auto editor = MakeObject<Aspose::Pdf::Facades::PdfAnnotationEditor>();

    editor->BindPdf(_dataDir + u"sample.pdf");

    // Hapus area halaman tertentu
    editor->RedactArea(1, MakeObject<Rectangle>(100, 100, 20, 70), System::Drawing::Color::get_White());
    editor->BindPdf(_dataDir + u"sample.pdf");
    editor->Save(_dataDir + u"FacadesApproach_out.pdf");
}
```