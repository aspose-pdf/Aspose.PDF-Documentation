---
title: Tambahkan latar belakang ke PDF dengan C++
linktitle: Tambahkan latar belakang
type: docs
weight: 110
url: /cpp/add-backgrounds/
descriptions: Tambahkan gambar latar belakang ke file PDF Anda dengan C++. Gunakan objek BackgroundArtifact.
lastmod: "2021-12-03"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Menambahkan latar belakang ke file PDF membantu meningkatkan keterbacaan keseluruhan dokumen. Konten dalam PDF menjadi lebih menarik dan pembaca akan memperhatikan jika Anda memiliki tampilan dokumen yang bagus. Latar belakang juga dapat digunakan untuk menyoroti sorotan dari PDF.

Gambar latar belakang dapat digunakan untuk menambahkan watermark, atau desain halus lainnya, ke dokumen. Dalam Aspose.PDF untuk C++, setiap dokumen PDF adalah kumpulan halaman dan setiap halaman berisi kumpulan artefak. Kelas [BackgroundArtifact](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.background_artifact) dapat digunakan untuk menambahkan gambar latar belakang ke objek halaman.

Cuplikan kode berikut menunjukkan cara menambahkan gambar latar belakang ke halaman PDF menggunakan objek BackgroundArtifact dengan C++.

```cpp
void WorkingWithPages::AddBackgrounds()
{
    String _dataDir("C:\\Samples\\");

    // Buat objek Document baru
    auto document = MakeObject<Document>();

    // Tambahkan halaman baru ke objek dokumen
    auto page = document->get_Pages()->Add();

    // Buat objek Background Artifact
    auto background = MakeObject<BackgroundArtifact>();

    // Tentukan gambar untuk objek backgroundartifact
    background->set_BackgroundImage(System::IO::File::OpenRead(_dataDir + u"background.png"));

    // Tambahkan backgroundartifact ke koleksi artefak halaman
    page->get_Artifacts()->Add(background);

    // Simpan dokumen
    document->Save(_dataDir + u"ImageAsBackground_out.pdf");
}
```