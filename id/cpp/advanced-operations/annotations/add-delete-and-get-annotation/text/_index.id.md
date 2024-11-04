---
title: PDF Text Annotation
Texttitle: Text Annotation
type: docs
weight: 10
url: /cpp/text-annotation/
description: Aspose.PDF untuk C++ memungkinkan Anda untuk Menambah, Mendapatkan, dan Menghapus Anotasi Teks dari dokumen PDF Anda.
lastmod: "2021-11-24"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## Cara menambahkan Anotasi Teks ke dalam file PDF yang ada

Anotasi Teks adalah anotasi yang terhubung ke lokasi tertentu dalam dokumen PDF. Ketika ditutup, anotasi ditampilkan sebagai ikon; ketika dibuka, harus menampilkan jendela pop-up yang berisi teks catatan dalam font dan ukuran yang dipilih oleh pembaca.

Anotasi terkandung dalam koleksi [Annotations](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation) dari Halaman tertentu. Koleksi ini hanya berisi anotasi untuk halaman individu tersebut; setiap halaman memiliki koleksi Anotasinya sendiri.

Untuk menambahkan anotasi ke halaman tertentu, tambahkan ke koleksi Anotasi halaman tersebut dengan metode [Add](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_collection#a1f7bf6c38fe2f97904a3575f5241d6c9).


1. Pertama, buat anotasi yang ingin Anda tambahkan ke PDF.
1. Kemudian buka PDF masukan.
1. Tambahkan anotasi ke koleksi Anotasi objek [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page).

Cuplikan kode berikut menunjukkan cara menambahkan anotasi pada halaman PDF.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;

void AddTextAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Load the PDF file
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");

    auto page = document->get_Pages()->idx_get(1);
    auto rect = MakeObject<Rectangle>(200, 750, 400, 790);
    auto textAnnotation = MakeObject<Aspose::Pdf::Annotations::TextAnnotation>(page, rect);

    textAnnotation->set_Title(u"Aspose User");
    textAnnotation->set_Subject(u"Sample Subject");
    textAnnotation->set_State(Aspose::Pdf::Annotations::AnnotationState::Accepted);
    textAnnotation->set_Contents(u"Sample contents for the annotation");
    textAnnotation->set_Open(true);
    textAnnotation->set_Icon(Aspose::Pdf::Annotations::TextIcon::Circle);

    auto border = MakeObject<Aspose::Pdf::Annotations::Border>(textAnnotation);
    border->set_Width(5);
    border->set_Dash(MakeObject<Aspose::Pdf::Annotations::Dash>(1, 1));
    textAnnotation->set_Border(border);
    textAnnotation->set_Rect(rect);

    page->get_Annotations()->Add(textAnnotation);
    document->Save(_dataDir + u"sample_textannot.pdf");
}
```
```

## Dapatkan Anotasi Teks

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Teks dalam dokumen PDF:

```cpp
void GetTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filter anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto fa : textAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

## Hapus Anotasi Teks dari file PDF

Potongan kode berikut menunjukkan cara Menghapus Anotasi Teks dari file PDF.

```cpp
void DeleteTextAnnotation() {

    String _dataDir("C:\\Samples\\");
    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_textannot.pdf");

    // Filter anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);
    auto annotationSelector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(
        MakeObject<Aspose::Pdf::Annotations::LineAnnotation>(page, Rectangle::get_Trivial(), Point::get_Trivial(), Point::get_Trivial()));
    page->Accept(annotationSelector);
    auto textAnnotations = annotationSelector->get_Selected();

    // hapus anotasi
    for (auto fa : textAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_textannot_del.pdf");
}
```

## Cara Menambahkan (atau Membuat) Anotasi Teks Bebas Baru

Anotasi teks bebas menampilkan teks langsung pada halaman. Dalam cuplikan berikut, kami menambahkan anotasi teks bebas di atas kemunculan pertama string.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void FreeTextAnnotations::AddFreeTextAnnotationDemo()
{
    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    auto defaultAppearance = MakeObject<DefaultAppearance>();
    defaultAppearance->set_FontName(u"Helvetica");
    defaultAppearance->set_FontSize(12);
    defaultAppearance->set_TextColor(System::Drawing::Color::get_Blue());

    auto freeTextAnnotation = MakeObject<FreeTextAnnotation>(page, new Rectangle(300.0, 770.0, 400.0, 790.0), defaultAppearance);

    freeTextAnnotation->set_RichText(u"Demo Teks Bebas");
    page->get_Annotations()->Add(freeTextAnnotation);
    document->Save(_dataDir + u"sample_freetext.pdf");
}
```

## Get FreeText Annotation

Silakan coba gunakan cuplikan kode berikut untuk Mendapatkan Anotasi Teks dalam dokumen PDF:

```cpp
void FreeTextAnnotations::GetFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Memfilter anotasi menggunakan AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // mencetak hasil
    for (auto fa : freeTextAnnotations) {
        Console::WriteLine(fa->get_Rect());
    }
}
```

### Membuat Anotasi Teks Bebas Tidak Terlihat

Terkadang, perlu untuk membuat watermark yang tidak terlihat dalam dokumen saat melihatnya tetapi harus terlihat saat dokumen dicetak. Gunakan bendera anotasi untuk tujuan ini. Cuplikan kode berikut menunjukkan caranya.

```cpp
void FreeTextAnnotations::MakeFreeTextAnnotationInvisble() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto doc = MakeObject<Document>(_dataDir + u"input.pdf");

    auto annotation = new FreeTextAnnotation(doc->get_Pages()->idx_get(1),
        MakeObject<Rectangle>(50, 600, 250, 650),
        MakeObject<DefaultAppearance>(u"Helvetica", 16,
            System::Drawing::Color::get_Red()));
    annotation->set_Contents(u"ABCDEFG");
    annotation->get_Characteristics()->set_Border(System::Drawing::Color::get_Red());
    annotation->set_Flags (AnnotationFlags::Print | AnnotationFlags::NoView);
    doc->get_Pages()->idx_get(1)->get_Annotations()->Add(annotation);

    // Simpan file keluaran
    doc->Save(_dataDir + u"InvisibleAnnotation_out.pdf");
}
```

## Hapus Anotasi FreeText

Cuplikan kode berikut menunjukkan cara Menghapus Anotasi FreeText dari file PDF.

```cpp
void FreeTextAnnotations::DeleteFreeTextAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_freetext.pdf");

    // Saring anotasi menggunakan AnnotationSelector
    auto page = document->get_Pages()->idx_get(1);

    auto annotationSelector = MakeObject<AnnotationSelector>(
        new FreeTextAnnotation(page, Rectangle::get_Trivial(), new DefaultAppearance()));
    page->Accept(annotationSelector);
    auto freeTextAnnotations = annotationSelector->get_Selected();

    // hapus anotasi
    for (auto fa : freeTextAnnotations) {
        page->get_Annotations()->Delete(fa);
    }
    document->Save(_dataDir + u"sample_freetext_del.pdf");
}
```