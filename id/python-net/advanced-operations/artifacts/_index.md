---
title: Bekerja dengan Artefak di Python via .NET
linktitle: Bekerja dengan Artefak
type: docs
weight: 170
url: /id/python-net/artifacts/
description: Aspose.PDF for Python via .NET memungkinkan Anda menambahkan gambar latar belakang ke halaman PDF, dan memperoleh setiap watermark menggunakan kelas Artifact.
lastmod: "2025-11-13"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan Artefak ke PDF menggunakan Python
Abstract: Artikel ini mengeksplorasi konsep dan penerapan artefak dalam dokumen PDF, khususnya berfokus pada perannya dalam meningkatkan aksesibilitas dan kinerja. Artefak adalah elemen non‑konten, seperti komponen dekoratif atau tata letak, yang tidak menyampaikan makna dokumen. Artikel ini menyoroti penggunaan kelas `Artifact` dalam perpustakaan Aspose.PDF for Python via .NET untuk mengelola elemen‑elemen tersebut, menyediakan properti seperti `custom_type`, `contents`, dan `opacity` untuk penyesuaian detail. Artikel ini juga memperkenalkan kelas terkait untuk menangani jenis artefak tertentu. Contoh praktis menunjukkan operasi seperti mengambil watermark, menambahkan gambar latar belakang, menghitung jenis artefak, dan menerapkan penomoran Bates.
---

Artefak dalam PDF adalah objek grafik atau elemen lain yang bukan bagian dari konten sebenarnya dari dokumen. Mereka biasanya digunakan untuk dekorasi, tata letak, atau tujuan latar belakang. Contoh artefak meliputi header halaman, footer, pemisah, atau gambar yang tidak menyampaikan makna apa pun.

Tujuan artefak dalam PDF adalah memungkinkan perbedaan antara elemen konten dan non‑konten. Hal ini penting untuk aksesibilitas, karena pembaca layar dan teknologi bantuan lainnya dapat mengabaikan artefak dan fokus pada konten yang relevan. Artefak juga dapat meningkatkan kinerja dan kualitas dokumen PDF, karena dapat dihilangkan dari proses pencetakan, pencarian, atau penyalinan.

Untuk membuat sebuah elemen sebagai artefak dalam PDF, Anda perlu menggunakan kelas [Artifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/).
Berisi properti berguna berikut:

- **custom_type** - Mendapatkan nama tipe artefak. Dapat digunakan jika tipe artefak tidak standar.
- **custom_subtype** - Mendapatkan nama subtipe artefak. Dapat digunakan jika subtipe artefak tidak standar.
- **type** - Mendapatkan tipe artefak.
- **subtype** - Mendapatkan subtipe artefak. Jika artefak memiliki subtipe non‑standar, nama subtipe dapat dibaca melalui CustomSubtype.
- **contents** - Mendapatkan koleksi operator internal artefak.
- **form** - Mendapatkan XForm artefak (jika XForm digunakan).
- **rectangle** - Mendapatkan persegi panjang artefak.
- **position** - Mendapatkan atau mengatur posisi artefak. Jika properti ini ditentukan, maka margin dan perataan diabaikan.
- **right_margin** - Margin kanan artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **left_margin** - Margin kiri artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **top_margin** - Margin atas artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **bottom_margin** - Margin bawah artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **artifact_horizontal_alignment** - Perataan horizontal artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **artifact_vertical_alignment** - Perataan vertikal artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **rotation** - Mendapatkan atau mengatur sudut rotasi artefak.
- **text** - Mendapatkan teks artefak.
- **image** - Mendapatkan gambar artefak (jika ada).
- **opacity** - Mendapatkan atau mengatur opasitas artefak. Nilai yang mungkin berada dalam rentang 0..1.
- **lines** - Baris‑baris teks multiline artefak.
- **text_state** - Keadaan teks untuk teks artefak.
- **is_background** - Jika true, Artefak ditempatkan di belakang konten halaman.

Kelas berikut juga mungkin berguna untuk bekerja dengan artefak:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [Bates Numbering](https://reference.aspose.com/pdf/python-net/aspose.pdf/)

Silakan tinjau bagian‑bagian berikut dari artikel:

- [Adding backgrounds](/pdf/python-net/add-backgrounds/) - menambahkan gambar latar belakang ke file PDF Anda dengan Python.
- [Adding Bates Numbering](/pdf/python-net/add-bates-numbering/) - menambahkan Penomoran Bates ke PDF.
- [Adding Watermark](/pdf/python-net/add-watermarks/) - cara menambahkan watermark ke PDF dengan Python.
- [Counting Artifacts](/pdf/python-net/counting-artifacts/) - menghitung Artefak dalam PDF menggunakan Python.

