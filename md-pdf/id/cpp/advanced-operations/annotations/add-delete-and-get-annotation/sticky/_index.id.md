---
title: PDF Sticky Annotations menggunakan C++
linktitle: Sticky Annotation
type: docs
weight: 50
url: /cpp/sticky-annotations/
description: Topik ini tentang Sticky annotations, sebagai contoh kami menunjukkan Watermark Annotation dalam teks. Ini digunakan untuk merepresentasikan grafik pada halaman. Periksa potongan kode untuk menyelesaikan tugas ini.
lastmod: "2021-11-24"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Tambahkan Watermark Annotation

Sebuah watermark annotation harus digunakan untuk merepresentasikan grafik yang harus dicetak pada ukuran dan posisi tetap di sebuah halaman, terlepas dari dimensi halaman yang dicetak.

Anda dapat menambahkan Teks Watermark menggunakan [WatermarkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.watermark_annotation/) pada posisi spesifik dari halaman PDF. Opasitas dari Watermark juga dapat dikontrol dengan menggunakan properti opasitas.

Silakan periksa potongan kode berikut untuk menambahkan WatermarkAnnotation.

```cpp
 using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Text;
using namespace Aspose::Pdf::Annotations;

void ExampleWatermarkAnnotation::AddWaterMarkAnnotation()
{
    String _dataDir("C:\\Samples\\");

    // Memuat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Buat Annotation
    auto wa = MakeObject<WatermarkAnnotation>(page, MakeObject<Rectangle>(100, 500, 400, 600));

    // Tambahkan anotasi ke dalam koleksi Annotation dari Halaman
    page->get_Annotations()->Add(wa);

    // Buat TextState untuk pengaturan Font
    auto ts = MakeObject<TextState>();

    ts->set_ForegroundColor(Color::get_Blue());
    ts->set_Font(Aspose::Pdf::Text::FontRepository::FindFont(u"Times New Roman"));
    ts->set_FontSize(32);

    // Atur level opasitas dari Teks Annotation
    wa->set_Opacity(0.5);

    // Tambahkan Teks ke Annotation
    wa->SetTextAndState(MakeArray<String>({ u"Aspose.PDF", u"Watermark", u"Demo" }), ts);

    // Simpan Dokumen
    document->Save(_dataDir + u"sample_watermark.pdf");
}
```

## Dapatkan Anotasi Watermark

Silakan coba gunakan potongan kode berikut untuk Mendapatkan Anotasi Watermark dari dokumen PDF.

```cpp
void ExampleWatermarkAnnotation::GetWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filter anotasi menggunakan AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // cetak hasil
    for (auto wa : watermarkAnnotations) {
        Console::WriteLine(wa->get_Rect());
    }
}
```

## Hapus Anotasi Watermark

Silakan coba gunakan potongan kode berikut untuk menghapus Anotasi Watermark dari dokumen PDF.

```cpp
void ExampleWatermarkAnnotation::DeleteWatermarkAnnotation() {

    String _dataDir("C:\\Samples\\");

    // Muat file PDF
    auto document = MakeObject<Document>(_dataDir + u"sample_watermark.pdf");
    auto page = document->get_Pages()->idx_get(1);

    // Filter anotasi menggunakan AnnotationSelector
    auto annotationSelector = MakeObject<AnnotationSelector>(
        MakeObject<WatermarkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(annotationSelector);
    auto watermarkAnnotations = annotationSelector->get_Selected();

    // hapus anotasi
    for (auto wa : watermarkAnnotations) {
        page->get_Annotations()->Delete(wa);
    }
    document->Save(_dataDir + u"sample_watermark_del.pdf");
}
```