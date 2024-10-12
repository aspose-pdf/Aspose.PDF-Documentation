---
title: Update Links in PDF 
linktitle: Update Links
type: docs
weight: 20
url: /cpp/update-links/
description: Memperbarui tautan dalam PDF secara programatis dengan Aspose.PDF untuk C++. Panduan ini tentang cara memperbarui tautan dalam file PDF.
lastmod: "2022-01-31"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Memperbarui Tautan dalam File PDF

Seperti yang dibahas dalam Menambahkan Hyperlink dalam File PDF, kelas [LinkAnnotation](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.link_annotation/) memungkinkan untuk menambahkan tautan dalam file PDF. Ada juga kelas serupa yang digunakan untuk mendapatkan tautan yang ada dari dalam file PDF. Gunakan ini jika Anda perlu memperbarui tautan yang ada. Untuk memperbarui tautan yang ada:

1. Muat file PDF.
1. Pergi ke halaman tertentu dalam file PDF.
1. Tentukan tujuan tautan menggunakan properti Destination dari objek [GoToAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_action).
1. Halaman tujuan ditentukan menggunakan konstruktor [XYZExplicitDestination](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.x_y_z_explicit_destination).

### Mengatur Target Tautan ke Halaman di Dokumen yang Sama

Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan mengatur targetnya ke halaman kedua dari dokumen.

```cpp
void SetLinkTargetToAPageInTheSameDocument()
{
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modifikasi tautan: ubah tujuan tautan
    auto goToAction = System::DynamicCast<Aspose::Pdf::Annotations::GoToAction>(link->get_Action());

    // Tentukan tujuan untuk objek tautan
    // Mewakili tujuan eksplisit yang menampilkan halaman dengan koordinat (kiri, atas) diposisikan di sudut kiri atas
    // jendela dan isi halaman diperbesar oleh faktor zoom.
    // Parameter pertama adalah nomor halaman tujuan.
    // Yang kedua adalah koordinat kiri
    // Yang ketiga adalah koordinat atas
    // Argumen keempat adalah faktor zoom saat menampilkan halaman masing-masing. Menggunakan 2 berarti halaman akan ditampilkan dalam zoom 200%
    goToAction->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(1, 1, 2, 2));

    // Simpan dokumen dengan tautan yang diperbarui
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```
### Setel Tujuan Tautan ke Alamat Web

Untuk memperbarui hyperlink sehingga mengarah ke alamat web, buat objek [GoToURIAction](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.annotations.go_to_u_r_i_action) dan berikan ke properti Action dari LinkAnnotation. Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan menetapkan targetnya ke alamat web.

```cpp
void SetLinkDestinationToWebAddress() 
{
    // Muat file PDF
    String _dataDir("C:\\Samples\\");
    // Buat instance Dokumen
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->idx_get(1);
    auto link = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Ubah tautan: ubah aksi tautan dan setel target sebagai alamat web
    link->set_Action(MakeObject<Aspose::Pdf::Annotations::GoToURIAction>("www.aspose.com"));

    // Simpan dokumen dengan tautan yang diperbarui
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Tetapkan Target Tautan ke File PDF Lain

Cuplikan kode berikut menunjukkan cara memperbarui tautan dalam file PDF dan menetapkan targetnya ke file PDF lain.

```cpp
void SetLinkTargetToAnotherPDFFile()
{
    // Muat file PDF
    String _dataDir("C:\\Samples\\");
    // Buat instansi Dokumen
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->idx_get(1);
    auto linkAnnot = System::DynamicCast<Aspose::Pdf::Annotations::LinkAnnotation>(page->get_Annotations()->idx_get(1));

    // Modifikasi tautan: ubah aksi tautan dan tetapkan target sebagai alamat web
    auto goToR = System::DynamicCast<Aspose::Pdf::Annotations::GoToRemoteAction>(linkAnnot->get_Action());
    // Baris selanjutnya memperbarui destinasi, tidak memperbarui file
    goToR->set_Destination(MakeObject<Aspose::Pdf::Annotations::XYZExplicitDestination>(2, 0, 0, 1.5));
    // Baris selanjutnya memperbarui file
    goToR->set_File(MakeObject<FileSpecification>(_dataDir + u"input.pdf"));

    // Simpan dokumen dengan tautan yang diperbarui
    document->Save(_dataDir + u"UpdateLinks_out.pdf");
}
```

### Perbarui Warna Teks LinkAnnotation

Link anotasi tidak mengandung teks. Sebaliknya, teks ditempatkan dalam isi halaman di bawah anotasi. Oleh karena itu, untuk mengubah warna teks, gantilah warna teks halaman alih-alih mencoba mengubah warna anotasi. Cuplikan kode berikut menunjukkan cara memperbarui warna link anotasi dalam file PDF.

```cpp
void UpdateLinkAnnotationTextColor() 
{
    // Muat file PDF
    String _dataDir("C:\\Samples\\");

    // Buat instansi Dokumen
    auto document = MakeObject<Document>(_dataDir + u"UpdateLinks.pdf");

    // Tambahkan halaman ke koleksi halaman file PDF
    auto page = document->get_Pages()->idx_get(1);

    for (auto annotation : page->get_Annotations())
    {
        if (annotation->get_AnnotationType() == Aspose::Pdf::Annotations::AnnotationType::Link)
        {
            // Cari teks di bawah anotasi
            auto ta = MakeObject<Aspose::Pdf::Text::TextFragmentAbsorber>();
            auto rect = annotation->get_Rect();
            rect->set_LLX(rect->get_LLX() - 10);
            rect->set_LLY(rect->get_LLY() - 10);
            rect->set_URX(rect->get_URX() + 10);
            rect->set_URY(rect->get_URY() + 10);

            ta->set_TextSearchOptions(MakeObject<Aspose::Pdf::Text::TextSearchOptions>(rect));
            ta->Visit(page);
            // Ubah warna teks.
            for (auto tf : ta->get_TextFragments())
            {
                tf->get_TextState()->set_ForegroundColor(Color::get_Red());
            }
        }

    }
    // Simpan dokumen dengan link yang diperbarui
    document->Save(_dataDir + u"UpdateLinkTextColor_out.pdf");
}
```