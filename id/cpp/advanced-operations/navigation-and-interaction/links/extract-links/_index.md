```
---
title: Ekstrak Tautan dari File PDF
linktitle: Ekstrak Tautan
type: docs
weight: 30
url: id/cpp/extract-links/
description: Ekstrak tautan dari PDF dengan C#. Topik ini menjelaskan bagaimana cara mengekstrak tautan menggunakan kelas AnnotationSelector.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Ekstrak Tautan dari File PDF

Tautan diwakili sebagai anotasi dalam file PDF, jadi untuk mengekstrak tautan, ekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/).

1. Buat objek [Document](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.document).
1. Dapatkan [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) yang ingin Anda ekstrak tautannya.
1.
``` Gunakan kelas [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) untuk mengekstrak semua objek [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) dari halaman yang ditentukan.
1. Lepaskan objek [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/) ke metode Accept dari objek Page.
1. Dapatkan semua anotasi tautan yang dipilih ke dalam objek IList menggunakan properti Selected dari objek [AnnotationSelector](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.annotation_selector/).

Cuplikan kode berikut menunjukkan kepada Anda cara mengekstrak tautan dari file PDF.

```cpp
void ExtractLinksFromThePDFFile() {
   
    // Memuat file PDF
    String _dataDir("C:\\Samples\\");

    // Membuat instance Dokumen
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Menambahkan halaman ke koleksi halaman dari file PDF
    auto page = document->get_Pages()->idx_get(1);


    auto selector = MakeObject<Aspose::Pdf::Annotations::AnnotationSelector>(MakeObject<Aspose::Pdf::Annotations::LinkAnnotation>(page, Rectangle::get_Trivial()));
    page->Accept(selector);
    auto list = selector->get_Selected();
    for (auto annot : list)
    {
        Console::WriteLine(u"Annotation located: {0}", annot->get_Rect());
    }
}
```