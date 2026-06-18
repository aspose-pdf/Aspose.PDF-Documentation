---
title: Mengonversi File ke PDF melalui Aktivitas Alur Kerja
linktitle: Mengonversi File ke PDF melalui Aktivitas Alur Kerja
type: docs
weight: 50
url: /id/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2026-06-18"
description: API PDF SharePoint dapat digunakan dalam alur kerja SharePoint yang mengonversi dokumen ke PDF.
---

{{% alert color="primary" %}}

Dukungan untuk alur kerja merupakan fungsi utama dari Microsoft Office SharePoint Server. Alur kerja membantu mengotomatiskan pergerakan dokumen sesuai logika bisnis dan menyederhanakan biaya serta waktu organisasi dokumen. Artikel ini menunjukkan cara menggunakan Aspose.PDF for SharePoint dalam alur kerja yang mengonversi dokumen ke PDF.

{{% /alert %}}
## **Menyiapkan Alur Kerja**

Contoh ini membuat alur kerja yang mengonversi setiap item baru dalam pustaka dokumen ke format PDF dan menyimpannya di pustaka dokumen lain. Contoh ini menggunakan pustaka **Personal Documents** sebagai pustaka sumber dan subfolder **Pdf** dalam pustaka **Shared Documents** sebagai pustaka tujuan.

Aspose.PDF for SharePoint mendukung konversi file HTML, teks, dan gambar.

### **Rancang Alur Kerja menggunakan SharePoint Designer**

1. Buka **SharePoint Designer** dan hubungkan ke situs tempat alur kerja akan diterapkan.
1. Pilih **Workflows** dari **site objects** dan kemudian buka **List Workflow**.
1. Pilih pustaka **Personal Documents** untuk membuat dan melampirkan alur kerja daftar baru ke pustaka dokumen.

   **Memilih Personal Documents dari menu**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)


1. Buat dan lampirkan alur kerja daftar ke pustaka **Personal Documents** dengan mengetikkan nama alur kerja dan deskripsi.
1. Klik **OK** untuk menyelesaikan langkah ini.

   **Membuat alur kerja daftar**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)



Editor langkah alur kerja muncul. Ini digunakan untuk menentukan kondisi dan tindakan untuk alur kerja. Sekarang tambahkan tindakan untuk mengonversi dokumen baru ke PDF tanpa kondisi apa pun, dari **Aspose Actions**.

1. Pilih tindakan **Convert file to PDF via Aspose.PDF** dari menu **Action**.

   **Memilih tindakan**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. Konfigurasikan parameter tindakan:
   1. Atur parameter **folder ini** ke folder tujuan.
   1. Biarkan parameter aksi lainnya dengan nilai default atau ubah menggunakan jendela properti aksi. Nilai default untuk parameter **Overwrite** adalah false.

      **Editor Alur Kerja**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**Mengatur perpustakaan tujuan**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**Mengatur properti**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. Dari menu **Workflow**, pilih **Pengaturan Workflow**.
1. Pilih **memulai alur kerja secara otomatis ketika item baru dibuat** dan hapus opsi lain dari **Opsi Mulai**.

   **Pengaturan opsi mulai**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)



Desain alur kerja selesai.

1. Simpan dan publikasikan alur kerja untuk menerapkannya di situs SharePoint.

### **Uji Alur Kerja**

Untuk menguji alur kerja:

1. Buka situs SharePoint dan unggah dokumen baru ke perpustakaan dokumen **Personal Documents**.
   Aspose.PDF for SharePoint mendukung konversi dari file HTML, file teks, dan gambar (JPG, PNG, GIF, TIFF, dan BMP*) ke PDF. Workflow dikonfigurasi untuk dimulai secara otomatis ketika item baru dibuat, sehingga file diproses secara otomatis.
1. Segarkan browser.
   Status workflow muncul di kolom workflow, **Aspose.PDF Workflow** dalam kasus ini.

   **Menambahkan dokumen ke perpustakaan sumber**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)




1. Buka perpustakaan dokumen tujuan untuk melihat dokumen yang telah dikonversi. **Shared Documents/Pdf** adalah jalur dalam contoh ini.

   **Perpustakaan tujuan**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

