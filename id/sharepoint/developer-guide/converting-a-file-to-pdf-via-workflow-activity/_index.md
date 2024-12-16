---
title: Mengonversi File ke PDF melalui Aktivitas Alur Kerja
type: docs
weight: 50
url: /id/sharepoint/converting-a-file-to-pdf-via-workflow-activity/
lastmod: "2020-12-16"
description: API SharePoint PDF dapat digunakan dalam alur kerja SharePoint yang mengonversi dokumen ke PDF.
---

{{% alert color="primary" %}}

Dukungan untuk alur kerja adalah fungsi utama dari Microsoft Office SharePoint Server. Alur kerja membantu mengotomatisasi pergerakan dokumen sesuai dengan logika bisnis dan menyederhanakan biaya dan waktu pengorganisasian dokumen. Artikel ini menunjukkan cara menggunakan Aspose.PDF untuk SharePoint dalam alur kerja yang mengonversi dokumen ke PDF.

{{% /alert %}}

## **Menyiapkan Alur Kerja**

Contoh ini membuat alur kerja yang mengonversi item baru di perpustakaan dokumen ke format PDF dan menyimpannya di perpustakaan dokumen lain. Contoh ini menggunakan perpustakaan **Dokumen Pribadi** sebagai perpustakaan sumber dan sub-folder **Pdf** di perpustakaan **Dokumen Bersama** sebagai perpustakaan tujuan.

Aspose.PDF untuk SharePoint mendukung konversi file HTML, teks, dan gambar.

### **Merancang Alur Kerja menggunakan SharePoint Designer**

1. Buka **SharePoint Designer** dan hubungkan ke situs di mana alur kerja akan diterapkan.
2. Pilih **Workflows** dari **objek situs** dan kemudian buka **List Workflow**.
3. Pilih perpustakaan **Personal Documents** untuk membuat dan melampirkan alur kerja daftar baru ke perpustakaan dokumen.

   **Memilih Personal Documents dari menu**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_1.png)

4. Buat dan lampirkan alur kerja daftar ke perpustakaan **Personal Documents** dengan mengetikkan nama dan deskripsi alur kerja.
5. Klik **OK** untuk menyelesaikan langkah ini.

   **Membuat alur kerja daftar**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_2.png)

Editor langkah alur kerja muncul. Ini digunakan untuk mendefinisikan kondisi dan tindakan untuk alur kerja. Sekarang tambahkan tindakan untuk mengonversi dokumen baru ke PDF tanpa syarat apa pun, dari **Aspose Actions**.
1. Pilih tindakan **Convert file to PDF via Aspose.PDF** dari menu **Action**.

   **Memilih dan melakukan tindakan**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_3.png)


1. Konfigurasikan parameter tindakan:
   1. Atur parameter **this folder** ke folder tujuan.
   1. Biarkan parameter tindakan lainnya sebagai nilai default atau atur menggunakan jendela properti tindakan. Nilai default untuk parameter **Overwrite** adalah false.

      **Editor Alur Kerja**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_4.png)



**Mengatur pustaka tujuan**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_5.png)



**Mengatur properti**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_6.png)




1. Dari menu **Workflow**, pilih **Workflow Settings**.
1. Pilih **start workflow automatically when a new item created** dan hapus opsi lainnya dari **Start Options**.

   **Mengatur opsi mulai**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_7.png)

Desain alur kerja selesai.

1. Simpan dan publikasikan alur kerja untuk menerapkannya di situs SharePoint.

### **Uji Alur Kerja**

Untuk menguji alur kerja:

1. Buka situs SharePoint dan unggah dokumen baru ke pustaka dokumen **Dokumen Pribadi**.
   Aspose.PDF untuk SharePoint mendukung konversi dari file HTML, file teks, dan gambar (JPG, PNG, GIF, TIFF, dan BMP*) ke PDF. Alur kerja dikonfigurasi untuk mulai secara otomatis ketika item baru dibuat, jadi file diproses secara otomatis.
1. Segarkan browser.
   Status alur kerja muncul di kolom alur kerja, **Alur Kerja Aspose.PDF** dalam kasus ini.

   **Menambahkan dokumen ke pustaka sumber**

![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_8.png)

1. Buka pustaka dokumen tujuan untuk melihat dokumen yang telah dikonversi. **Dokumen Bersama/Pdf** adalah jalur dalam contoh ini.

   **Pustaka tujuan**
![todo:image_alt_text](converting-a-file-to-pdf-via-workflow-activity_9.png)

Untuk mengonversi file ke PDF melalui aktivitas alur kerja, ikuti langkah-langkah berikut:

1. **Buka Alur Kerja**: Navigasikan ke modul Alur Kerja di dalam aplikasi Anda.

2. **Tambahkan Aktivitas Baru**: Klik tombol untuk menambahkan aktivitas baru ke alur kerja Anda.

3. **Pilih Konversi ke PDF**: Dari daftar aktivitas yang tersedia, pilih "Konversi ke PDF".

4. **Konfigurasi Aktivitas**: 
   - **Masukan File**: Tentukan file yang ingin Anda konversi.
   - **Nama File Keluaran**: Berikan nama untuk file PDF yang akan dihasilkan.

5. **Simpan dan Jalankan Alur Kerja**: Setelah Anda mengatur semua parameter, simpan alur kerja dan jalankan untuk melihat hasilnya.

```python
# Contoh kode untuk mengonversi file ke PDF
def convert_to_pdf(file_input, output_filename):
    # Logika konversi file
    pass
```

6. **Verifikasi Hasil**: Setelah alur kerja selesai, periksa direktori keluaran untuk memastikan file PDF telah dibuat dengan benar.

Dengan mengikuti langkah-langkah di atas, Anda dapat dengan mudah mengonversi file ke format PDF menggunakan aktivitas alur kerja.