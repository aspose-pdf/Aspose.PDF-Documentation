---
title: Tambahkan tanda air ke PDF menggunakan C++
linktitle: Tambahkan tanda air
type: docs
weight: 90
url: /cpp/add-watermarks/
description: Artikel ini menjelaskan fitur bekerja dengan artefak dan mendapatkan tanda air dalam PDF secara programatis menggunakan C++.
lastmod: "2021-12-08"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

Tanda air adalah gambar transparan yang biasanya berisi logo atau segel untuk mengidentifikasi siapa yang membuat dokumen atau gambar tersebut.

**Aspose.PDF for C++** memungkinkan penambahan tanda air ke dokumen PDF Anda menggunakan kelas Artifact. Silakan periksa artikel ini untuk menyelesaikan tugas Anda.

Tanda air yang dibuat dengan Adobe Acrobat disebut artefak (seperti yang dijelaskan dalam 14.8.2.2 Real Content and Artifacts dari spesifikasi PDF). Untuk bekerja dengan artefak, Aspose.PDF memiliki dua kelas: [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) dan [ArtifactCollection](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact_collection).

Untuk mendapatkan semua artefak pada halaman tertentu, kelas [Page](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.page) memiliki properti Artifacts. ```
Topik ini menjelaskan cara bekerja dengan artefak dalam file PDF.

## Bekerja dengan Artefak

Kelas [Artifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.artifact) mengandung properti berikut:

**Artifact.Type** – mendapatkan tipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactType di mana nilainya termasuk Background, Layout, Page, Pagination, dan Undefined).
**Artifact.Subtype** – mendapatkan subtipe artefak (mendukung nilai dari enumerasi Artifact.ArtifactSubtype di mana nilainya termasuk Background, Footer, Header, Undefined, Watermark).

{{% alert color="primary" %}}

Harap dicatat bahwa watermark yang dibuat dengan Adobe Acrobat memiliki tipe Pagination dan subtipe Watermark.

{{% /alert %}}

**Artifact.Contents** – Mendapatkan koleksi operator internal artefak. Jenis yang didukung adalah System.Collections.ICollection.
**Artifact.Form** – Mendapatkan XForm artefak (jika XForm digunakan). Artefak watermark, header, dan footer mengandung XForm yang menunjukkan semua isi artefak.

**Artifact.Image** – Mendapatkan gambar artefak (jika ada gambar, jika tidak maka null).
```**Artifact.Text** – Mendapatkan teks dari sebuah artefak.  
**Artifact.Rectangle** – Mendapatkan posisi sebuah artefak di halaman.  
**Artifact.Rotation** – Mendapatkan rotasi sebuah artefak (dalam derajat, nilai positif menunjukkan rotasi berlawanan arah jarum jam).  
**Artifact.Opacity** – Mendapatkan opasitas sebuah artefak. Nilai yang mungkin berada dalam rentang 0…1, di mana 1 sepenuhnya buram.  

## Contoh Pemrograman: Cara Menambahkan Watermark Pada File PDF

Cuplikan kode berikut menunjukkan cara mendapatkan setiap watermark di halaman pertama file PDF dengan C++.

```cpp
void GettingWatermarks() {

    String _dataDir("C:\\Samples\\");
    String inputFileName("watermark.pdf");
    String outputFileName("watermark_out.pdf");

    auto document = MakeObject<Document>(_dataDir + inputFileName);

    auto artifact = MakeObject<WatermarkArtifact>();
    auto textState = MakeObject<TextState>();
    textState->set_FontSize(72);
    textState->set_ForegroundColor(Color::get_Blue());
    textState->set_Font(FontRepository::FindFont(u"Courier"));
    artifact->SetTextAndState(u"WATERMARK", textState);
    artifact->set_ArtifactHorizontalAlignment (HorizontalAlignment::Center);
    artifact->set_ArtifactVerticalAlignment (VerticalAlignment::Center);
    artifact->set_Rotation(45);
    artifact->set_Opacity(0.5);
    artifact->set_IsBackground(true);

    document->get_Pages()->idx_get(1)->get_Artifacts()->Add(artifact);

    document->Save(_dataDir + outputFileName);
}
```