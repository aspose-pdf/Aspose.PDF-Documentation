---
title: Mengamankan dan menandatangani PDF dalam Rust
linktitle: Mengamankan dan menandatangani PDF
type: docs
weight: 50
url: /id/rust-cpp/securing-and-signing/
description: Bagian ini menjelaskan fitur penggunaan tanda tangan dan mengamankan dokumen PDF Anda menggunakan Rust
lastmod: "2026-07-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Bagian ini memberikan panduan komprehensif untuk bekerja dengan dokumen PDF yang diamankan menggunakan Aspose.PDF for Rust via C++. Ini menjelaskan cara melindungi file PDF dengan kata sandi, mengelola izin akses, dan membuka atau membuka kunci dokumen yang terenkripsi secara aman dalam Rust.

Artikel ini menjelaskan tugas-tugas PDF umum yang terkait keamanan, termasuk mengenkripsi PDF dengan algoritma kriptografi modern, mendekripsi file yang dilindungi kata sandi, dan mengontrol akses pengguna melalui flag izin. Anda juga akan belajar cara memeriksa pengaturan izin yang ada dan membuka dokumen yang diamankan menggunakan kredensial pemilik untuk pemrosesan lebih lanjut.

Anda akan belajar cara membuat dokumen PDF, menerapkan perlindungan kriptografi modern menggunakan enkripsi berbasis AES, dan mengontrol kemampuan pengguna seperti mencetak, mengedit konten, dan mengisi formulir. Artikel ini juga menunjukkan cara membuka PDF yang dilindungi kata sandi menggunakan kredensial pemilik dan mendekripsinya untuk menghasilkan dokumen tanpa pembatasan yang cocok untuk pemrosesan lebih lanjut.

- [Enkripsi dan File PDF](/pdf/id/rust-cpp/encrypt-pdf/)
- [Dekripsi File PDF](/pdf/id/rust-cpp/decrypt-pdf/)
- [Dapatkan Izin](/pdf/id/rust-cpp/get-permissions/)
- [Atur izin](/pdf/id/rust-cpp/set_permissions/)
- [Buka PDF yang dilindungi kata sandi](/pdf/id/rust-cpp/open-password-protected-pdf/)

Untuk mengerjakan Set Permissions dan Get Permissions, silakan merujuk ke tabel PDF Permissions Reference. Yang mencantumkan flag izin yang tersedia yang dapat diterapkan pada dokumen PDF untuk mengontrol bagaimana pengguna akhir berinteraksi dengannya.

## Referensi Izin PDF

| **Izin** | **Deskripsi** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | Izinkan mencetak |
| Permissions::MODIFY_CONTENT | Izinkan memodifikasi konten (kecuali formulir/anotasi) |
| Permissions::EXTRACT_CONTENT | Izinkan menyalin/mengambil teks dan grafik |
| Permissions::MODIFY_TEXT_ANNOTATIONS | Izinkan menambahkan/memodifikasi anotasi teks |
| Permissions::FILL_FORM | Izinkan mengisi formulir interaktif |
| Permissions::EKSTRAK_KONTEN_DENGAN_DISABILITAS | Izinkan ekstraksi konten untuk aksesibilitas |
| Permissions::MERAKIT_DOKUMEN | Izinkan menyisipkan/memutar/menghapus halaman atau mengubah struktur |
| Permissions::KUALITAS_PENCETAKAN | Izinkan pencetakan berkualitas tinggi / setia |
