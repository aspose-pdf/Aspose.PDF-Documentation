---
title: Batasan API
type: docs
weight: 70
url: /net/api-limitations/
---

## **Xsl Fo ke Pdf**
Berikut adalah masalah yang diketahui dari dukungan XSL-FO.

- SVG tidak didukung
## **Informasi pembuat PDF**
- Harap dicatat bahwa Anda tidak dapat mengatur nilai untuk bidang **Aplikasi** dan **Produsen**, karena Aspose Ltd. dan Aspose.PDF untuk .NET x.x.x akan ditampilkan pada bidang tersebut
## **Lainnya**
Berikut adalah beberapa masalah lain yang diketahui.

- Pdf/X tidak didukung.
- Formulir XFA dinamis tidak didukung: Karena halamannya dibuat/ditampilkan pada saat memuat PDF, di Adobe Acrobat/Reader. Jadi kita tidak bisa mengekstrak dan menyimpan halaman virtual atau beberapa halaman tersebut. Sebagai gantinya, kami (dan Adobe Acrobat) hanya dapat mengekstrak satu halaman nyata yang hanya berisi pesan kesalahan.
- Simbol khusus $p dan $P tidak akan berfungsi jika tidak diakhiri dengan karakter kosong.
- Konversi HTML ke PDF :- HTML adalah bahasa yang sangat luas dan dengan setiap rilis baru Aspose.PDF untuk .NET, kami berusaha sebaik mungkin untuk memberikan versi konversi HTML ke PDF yang lebih baik & kuat (*dengan mendukung semua jenis HTML*) namun karena ada banyak file HTML dengan sifat/struktur dan kompleksitas yang berbeda, kadang komponen kami mengalami beberapa masalah dalam hal pemformatan saat merender konten HTML ke format PDF dan ini biasanya terjadi saat menggunakan dokumen dengan struktur yang kompleks.
- Konversi HTML ke PDF :- HTML adalah bahasa yang sangat luas dan dengan setiap rilis baru Aspose.PDF untuk .NET, kami berusaha sebaik mungkin untuk menghadirkan versi yang lebih baik dan lebih kuat dari konversi HTML ke PDF (*dengan mendukung semua jenis HTML*) tetapi karena ada banyak file HTML dengan berbagai sifat/struktur dan kompleksitas, kadang-kadang komponen kami mengalami beberapa masalah dalam hal pemformatan saat merender konten HTML ke format PDF dan ini biasanya terjadi saat menggunakan dokumen dengan struktur yang kompleks.
- Penyisipan font tidak didukung di MS Word untuk Macintosh dan juga harap dicatat bahwa di MS Word untuk Windows, ini hanya terbatas pada font TrueType. Oleh karena itu, ketika melihat file word (DOC) yang dihasilkan sebagai hasil dari konversi PDF ke DOC melalui Aspose.PDF untuk .NET, font yang disisipkan diganti ketika melihat file-file tersebut di MS Word di MAC OS. Untuk detail lebih lanjut, silakan lihat di [macsupportcentral](http://www.macsupportcentral.com/2012/05/embed-fonts-microsoft-office-word-files/).
