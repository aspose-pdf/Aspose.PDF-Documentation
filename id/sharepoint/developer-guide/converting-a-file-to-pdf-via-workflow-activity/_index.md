---
title: Mengonversi File ke PDF melalui Aktivitas Alur Kerja
linktitle: Mengonversi File ke PDF melalui Aktivitas Alur Kerja
type: docs
weight: 50
url: /id/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-08-07"
description: API PDF SharePoint dapat digunakan dalam alur kerja SharePoint yang mengonversi dokumen ke PDF.
---

{{% alert color="primary" %}}

Pendukung alur kerja adalah fungsi utama Microsoft Office SharePoint Server. Alur kerja membantu mengotomatisasi pergerakan dokumen sesuai logika bisnis dan menyederhanakan biaya serta waktu organisasi dokumen. Artikel ini menunjukkan cara menggunakan Aspose.PDF for SharePoint dalam alur kerja yang mengonversi dokumen ke PDF.

{{% /alert %}}

## Menyiapkan Alur Kerja

Contoh ini membuat alur kerja yang mengonversi setiap item baru dalam perpustakaan dokumen ke format PDF dan menyimpannya di perpustakaan dokumen lain. Contoh ini menggunakan perpustakaan **Personal Documents** sebagai perpustakaan sumber dan subfolder **Pdf** dalam perpustakaan **Shared Documents** sebagai perpustakaan tujuan.

Aspose.PDF for SharePoint mendukung konversi file HTML, teks, dan gambar.

### Rancang Alur Kerja menggunakan SharePoint Designer

1. Buka **SharePoint Designer** dan hubungkan ke situs tempat alur kerja akan diterapkan.
1. Pilih **Workflows** dari **site objects** dan kemudian buka **List Workflow**.
1. Pilih perpustakaan **Personal Documents** untuk membuat dan melampirkan alur kerja daftar baru ke perpustakaan dokumen.

   **Memilih Dokumen Pribadi dari menu**

![Mengonversi file ke PDF via Workflow Activity_1](converting-a-file-to-pdf-via-workflow-activity_1.png)

1. Buat dan lampirkan alur kerja daftar ke pustaka **Personal Documents** dengan mengetikkan nama alur kerja dan deskripsi.
1. Klik **OK** untuk menyelesaikan langkah ini.

   **Membuat alur kerja daftar**

![Mengonversi file ke PDF via Workflow Activity_2](converting-a-file-to-pdf-via-workflow-activity_2.png)

Editor langkah alur kerja muncul. Ini digunakan untuk mendefinisikan kondisi dan tindakan untuk alur kerja. Sekarang tambahkan tindakan untuk mengonversi dokumen baru ke PDF tanpa kondisi apa pun, dari **Aspose Actions**.

1. Pilih tindakan **Convert file to PDF via Aspose.PDF** dari menu **Action**.

   **Memilih tindakan**

![Mengonversi file ke PDF melalui Workflow Activity_3](converting-a-file-to-pdf-via-workflow-activity_3.png)

1. Konfigurasikan parameter tindakan:
   1. Setel parameter **this folder** ke folder tujuan.
   1. Baik biarkan parameter aksi lainnya dengan nilai default atau atur menggunakan jendela properti aksi. Nilai default untuk parameter **Overwrite** adalah false.

      **Editor Alur Kerja**

![Mengonversi file ke PDF via Workflow Activity_4](converting-a-file-to-pdf-via-workflow-activity_4.png)

**Mengatur perpustakaan tujuan**

![Mengonversi file ke PDF via Workflow Activity_5](converting-a-file-to-pdf-via-workflow-activity_5.png)

**Mengatur properti**

![Mengonversi file ke PDF melalui Aktivitas Workflow_6](converting-a-file-to-pdf-via-workflow-activity_6.png)

1. Dari menu **Workflow**, pilih **Workflow Settings**.
1. Pilih **start workflow automatically when a new item created** dan hapus opsi lain dari **Start Options**.

   **Setting the start options**

![Mengonversi file ke PDF melalui Aktivitas Workflow_7](converting-a-file-to-pdf-via-workflow-activity_7.png)

Desain workflow selesai.

1. Simpan dan publikasikan alur kerja untuk menerapkannya di situs SharePoint.

### Uji alur kerja

Untuk menguji alur kerja:

1. Buka situs SharePoint dan unggah dokumen baru ke perpustakaan dokumen **Personal Documents**.
   Aspose.PDF for SharePoint mendukung konversi dari file HTML, file teks, dan gambar (JPG, PNG, GIF, TIFF dan BMP*) ke PDF. Alur kerja dikonfigurasi untuk mulai secara otomatis ketika item baru dibuat, sehingga file diproses secara otomatis.
1. Segarkan browser.
   Status alur kerja muncul di kolom alur kerja, **Aspose.PDF Workflow** dalam kasus ini.

   **Menambahkan dokumen ke perpustakaan sumber**

![Mengonversi file ke PDF melalui Workflow Activity_8](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Buka perpustakaan dokumen tujuan untuk melihat dokumen yang dikonversi. **Shared Documents/Pdf** adalah jalur dalam contoh ini.

   **Perpustakaan tujuan**

![Mengonversi file ke PDF melalui Workflow Activity_9](converting-a-file-to-pdf-via-workflow-activity_9.png)
