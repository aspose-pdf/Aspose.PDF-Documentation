---
title: Bekerja dengan Artefak PDF di Python
linktitle: Bekerja dengan Artefak
type: docs
weight: 170
url: /id/python-net/artifacts/
description: Pelajari cara bekerja dengan artefak PDF di Python untuk menambahkan latar belakang, tanda air, dan penomoran Bates serta menghitung jenis-jenis artefak dengan Aspose.PDF for Python via .NET.
lastmod: "2026-06-12"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Tambahkan artefak latar belakang, tanda air, dan penomoran Bates di Python
Abstract: Artikel ini menjelaskan cara bekerja dengan artefak PDF di Aspose.PDF for Python via .NET. Pelajari apa itu artefak, mengapa mereka penting untuk aksesibilitas dan tata letak dokumen, serta cara menambahkan gambar latar belakang, menerapkan tanda air, menambahkan penomoran Bates, dan memeriksa jenis-jenis artefak dalam file PDF dengan Python.
---

Artefak dalam PDF adalah objek grafik atau elemen lain yang bukan bagian dari konten aktual dokumen. Mereka biasanya digunakan untuk dekorasi, tata letak, atau keperluan latar belakang. Contoh artefak meliputi header halaman, footer, pemisah, atau gambar yang tidak menyampaikan makna apa pun.

Tujuan dari artefak dalam PDF adalah memungkinkan perbedaan antara elemen konten dan non‑konten. Ini penting untuk aksesibilitas, karena pembaca layar dan teknologi bantuan lainnya dapat mengabaikan artefak dan fokus pada konten yang relevan. Artefak juga dapat meningkatkan kinerja dan kualitas dokumen PDF, karena dapat dihilangkan dari pencetakan, pencarian, atau penyalinan.

Gunakan bagian ini ketika Anda perlu membuat atau memeriksa elemen PDF non‑konten dalam Python, seperti latar belakang dokumen, watermark halaman, dan tanda penomoran Bates. Panduan berikut menunjukkan alur kerja artefak utama yang didukung oleh Aspose.PDF for Python via .NET.

Untuk membuat elemen sebagai artefak dalam PDF, Anda perlu menggunakan [Artefak](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) kelas.
Ia berisi properti berguna berikut:

- **custom_type** - Mendapatkan nama jenis artefak. Dapat digunakan jika jenis artefak tidak standar.
- **custom_subtype** - Mendapatkan nama subtipe artefak. Dapat digunakan bila subtipe artefak bukan subtipe standar.
- **type** - Mendapatkan tipe artefak.
- **subtype** - Mendapatkan subtipe artefak. Jika artefak memiliki subtipe non-standar, nama subtipe dapat dibaca melalui CustomSubtype.
- **contents** - Mendapatkan koleksi operator internal artefak.
- **form** - Mendapatkan XForm dari artefak (jika XForm digunakan).
- **rectangle** - Mendapatkan persegi panjang artefak.
- **position** - Mendapatkan atau mengatur posisi artefak. Jika properti ini ditentukan, maka margin dan perataan diabaikan.
- **right_margin** - Margin kanan artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **left_margin** - Margin kiri artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **top_margin** - Margin atas artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **bottom_margin** - Margin bawah artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **artifact_horizontal_alignment** - Perataan horizontal artefak. Jika posisi ditentukan secara eksplisit (pada properti Position) nilai ini diabaikan.
- **artifact_vertical_alignment** - Penjajaran vertikal artefak. Jika posisi ditentukan secara eksplisit (dalam properti Position) nilai ini diabaikan.
- **rotation** - Mendapatkan atau mengatur sudut rotasi artefak.
- **text** - Mendapatkan teks artefak.
- **image** - Mendapatkan gambar artefak (jika ada).
- **opacity** - Mendapatkan atau mengatur opasitas artefak. Nilai yang mungkin berada dalam rentang 0..1.
- **lines** - Baris-baris artefak teks multiline.
- **text_state** - Status teks untuk teks artefak.
- **is_background** - Jika true Artefak ditempatkan di belakang konten halaman.

Kelas berikut mungkin juga berguna untuk bekerja dengan artefak:

- [ArtifactCollection](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/)
- [BackgroundArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/)
- [HeaderArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/)
- [FooterArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/)
- [WatermarkArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/)
- [BatesNArtifact](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/)

## Alur Kerja Artefak yang Dibahas dalam Bagian Ini

Silakan tinjau bagian-bagian berikut dari artikel:

- [Menambahkan latar belakang](/pdf/id/python-net/add-backgrounds/) - tambahkan gambar latar belakang ke file PDF Anda dengan Python.
- [Menambahkan Penomoran Bates](/pdf/id/python-net/add-bates-numbering/) - tambahkan Penomoran Bates ke PDF.
- [Menambahkan Tanda Air](/pdf/id/python-net/add-watermarks/) - cara menambahkan watermark ke PDF dengan Python.
- [Menghitung Artefak](/pdf/id/python-net/counting-artifacts/) - menghitung Artifacts dalam PDF menggunakan Python.
- [Kelola Header dan Footer PDF](/pdf/id/python-net/artifacts-header-footer/) - mengelola header dan footer dalam dokumen PDF.

Tutorial ini berguna ketika Anda perlu mengelola elemen PDF dekoratif atau struktural tanpa mengubah aliran konten utama dokumen.
