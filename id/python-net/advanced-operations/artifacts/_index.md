---
title: Artefak PDF dengan Python
linktitle: Artefak PDF
type: docs
weight: 170
url: /id/python-net/artifacts/
description: Tambah, periksa, dan hapus artefak PDF dalam Python, termasuk latar belakang, tanda air, header, footer, dan penomoran Bates.
lastmod: "2026-11-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Artefak PDF dengan Python
Abstract: Temukan panduan untuk menambahkan dan menghapus artefak PDF, memeriksa detail tanda air, dan menghitung artefak pagination berdasarkan subtipe dengan Aspose.PDF for Python via .NET.
---

Artefak PDF menandai elemen halaman seperti latar belakang dekoratif, header dan footer yang berjalan, serta tanda air. Pada PDF yang ditandai, teknologi bantu dapat melewati artefak dan fokus pada konten bermakna dokumen.

## Memilih panduan

### Menambahkan artefak

- [Menambahkan latar belakang](/pdf/id/python-net/add-backgrounds/)
- [Menambahkan tanda air](/pdf/id/python-net/add-watermarks/)
- [Menambahkan penomoran Bates](/pdf/id/python-net/add-bates-numbering/)
- [Menambahkan header dan footer](/pdf/id/python-net/artifacts-header-footer/)

### Memeriksa artefak

- [Menghitung artefak paginasi](/pdf/id/python-net/counting-artifacts/)
- [Mengekstrak detail tanda air](/pdf/id/python-net/extract-watermarks/)

### Menghapus artefak

- [Menghapus latar belakang](/pdf/id/python-net/remove-backgrounds/)
- [Menghapus tanda air](/pdf/id/python-net/remove-watermarks/)
- [Menghapus penomoran Bates](/pdf/id/python-net/remove-bates-numbering/)
- [Menghapus header dan footer](/pdf/id/python-net/remove-headers-footers/)

## API artefak

Properti `artifacts` mengembalikan koleksi [`ArtifactCollection`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifactcollection/) pada halaman. Kelas [`Artifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/artifact/) menyediakan properti yang digunakan bersama oleh kelas khusus [`BackgroundArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/backgroundartifact/), [`WatermarkArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/watermarkartifact/), [`HeaderArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerartifact/), [`FooterArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/footerartifact/), dan [`BatesNArtifact`](https://reference.aspose.com/pdf/python-net/aspose.pdf/batesnartifact/).

| Tugas | Properti |
| --- | --- |
| Identifikasi artefak | Gunakan `type` dan `subtype` untuk klasifikasi standar dan `custom_type` dan `custom_subtype` untuk nama khusus. |
| Periksa isinya | Gunakan `text`, `image`, dan `lines` untuk teks dan gambar, atau `contents` dan `form` untuk operator PDF dan XForm yang terkait. |
| Posisikan di halaman | Gunakan `rectangle` untuk memeriksa batasnya. Set `position` untuk penempatan eksplisit atau penggunaan `left_margin`, `right_margin`, `top_margin`, `bottom_margin`, `artifact_horizontal_alignment`, dan `artifact_vertical_alignment`. Posisi eksplisit menggantikan margin dan perataan. |
| Kendalikan penampilannya | Gunakan `rotation`, `opacity` (dari 0 hingga 1), dan `text_state`. Set `is_background` menempatkan artefak di belakang konten halaman. |
