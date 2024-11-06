---
title: Bekerja dengan Artefak di C++
linktitle: Bekerja dengan Artefak
type: docs
weight: 110
url: id/cpp/artifacts/
description: Halaman ini menjelaskan cara bekerja dengan kelas Artifact menggunakan Aspose.PDF untuk C++. Cuplikan kode menunjukkan cara menambahkan gambar latar belakang ke halaman PDF dan cara mendapatkan setiap watermark pada halaman pertama dari file PDF.
lastmod: "2021-11-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## Bagaimana cara mendapatkan Watermark di PDF?

**Apa itu artefak dalam PDF?**

Menurut referensi PDF / UA ISO, konten yang tidak penting atau tidak muncul di latar belakang tidak membawa informasi yang relevan, harus diberi label sebagai artefak sehingga teknologi bantu dapat mengabaikannya.
Jika artefak tidak dapat diidentifikasi dalam program untuk dibuat, ini harus dilakukan secara manual menggunakan Aspose.PDF untuk C++.

Kelas [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) berisi properti berikut:


- **Artifact.Type** – mendapatkan tipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilai termasuk Background, Layout, Page, Pagination dan Undefined).
- **Artifact.Subtype** – mendapatkan subtipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilai termasuk Latar Belakang, Footer, Header, Tidak Terdefinisi, Tanda Air).

{{% alert color="primary" %}}

Harap dicatat bahwa tanda air yang dibuat dengan Adobe Acrobat memiliki tipe Pagination dan subtipe Tanda Air.

{{% /alert %}}

- **Artifact.Contents** – Mendapatkan koleksi operator internal artefak. Tipe yang didukung adalah System.Collections.ICollection.
- **Artifact.Form** – Mendapatkan XForm artefak (jika XForm digunakan). Artefak tanda air, header, dan footer mengandung XForm yang menunjukkan semua isi artefak.
- **Artifact.Image** – Mendapatkan gambar artefak (jika gambar ada, jika tidak null).
- **Artifact.Text** – Mendapatkan teks artefak.
- **Artifact.Rectangle** – Mendapatkan posisi artefak pada halaman.
- **Artifact.Rotation** – Mendapatkan rotasi artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).
- **Artifact.Opacity** – Mendapatkan opasitas artefak. Nilai yang mungkin berada dalam rentang 0...1, di mana 1 sepenuhnya buram.

Sebagai contoh bekerja dengan artefak dalam file PDF, mari kita ambil watermark.

Watermark yang dibuat dengan dukungan Adobe Acrobat disebut sebagai artefak (sebagaimana dijelaskan dalam 14.8.2.2 Present Content and PDF Specification Artifacts). Untuk bekerja dengan artefak, Aspose.PDF berisi 2 kelas:
[Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Untuk mendapatkan semua artefak pada halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) memiliki properti Artifacts. Topik ini menunjukkan cara bekerja dengan artefak Watermark dalam file PDF.

Cuplikan kode berikut menunjukkan cara mendapatkan setiap watermark pada halaman pertama file PDF dengan C++:

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;
void Artifacts::SetWatermark() {
    String _dataDir("C:\\Samples\\");

    auto document = MakeObject<Document>(_dataDir + u"sample.pdf");
    auto artifact = MakeObject<WatermarkArtifact>();
    String text(u"WATERMARK");    
    artifact->set_Text(text);
    artifact->get_TextState()->set_ForegroundColor(Color::get_Blue());
    artifact->get_TextState()->set_FontSize(72);
    artifact->set_ArtifactHorizontalAlignment(HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment(VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);
    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);
    document->Save(_dataDir + u"watermark.pdf");
}
```
Background images dapat digunakan untuk menambahkan watermark atau desain eksklusif ke dokumen PDF. Aspose.PDF untuk C++ menggunakan kelas [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) untuk menambahkan gambar latar belakang ke objek halaman.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF dengan objek BackgroundArtifact:

```cpp
void Artifacts::SetBackground() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto pdfDocument = MakeObject<Document>();

    // Tambahkan objek MakeObject<page ke dokumen
    auto page = pdfDocument->get_Pages()->Add();

    // Buat objek Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Tentukan gambar untuk objek backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Tambahkan BackgroundArtifact ke koleksi artifacts pada halaman
    page->get_Artifacts()->Add(background);

    // Simpan PDF yang telah dimodifikasi
    pdfDocument->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```

### Contoh Pemrograman: Mendapatkan Tanda Air

Cuplikan kode berikut menunjukkan cara mendapatkan setiap tanda air pada halaman pertama file PDF.

```cpp
void Artifacts::GettingWatermarks() {
    
    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    // Iterasi dan dapatkan sub-tipe, teks, dan lokasi artefak
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        Console::WriteLine(u"{0} {1} {2}", artifact->get_Subtype(), 
            artifact->get_Text(), artifact->get_Rectangle());
    }

}
```

### Contoh Pemrograman: Menghitung Artefak dari Jenis Tertentu

Untuk menghitung jumlah total artefak dari jenis tertentu (misalnya, jumlah total tanda air), gunakan kode berikut:

```cpp
void Artifacts::CountingArtifacts() {

    String _dataDir("C:\\Samples\\");

    // Buka dokumen
    auto pdfDocument = MakeObject<Document>(_dataDir + u"watermark_new.pdf");
    int count = 0;
    for (auto artifact : pdfDocument->get_Pages()->idx_get(1)->get_Artifacts())
    {
        // Jika tipe artefak adalah tanda air, tingkatkan penghitung
        if (artifact->get_Subtype() == Artifact::ArtifactSubtype::Watermark) count++;
    }
    Console::WriteLine(u"Page contains {0} watermarks", count);
}
```