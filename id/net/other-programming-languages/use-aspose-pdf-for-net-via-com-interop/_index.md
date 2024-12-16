---
title: Aspose.PDF for .NET via COM Interop
type: docs
weight: 20
url: /id/net/use-aspose-pdf-for-net-via-com-interop/
---

{{% alert color="primary" %}}

Informasi dalam topik ini berlaku untuk skenario di mana Anda ingin menggunakan [Aspose.PDF for .NET](/pdf/id/net/) melalui COM Interop dalam bahasa pemrograman berikut:

- ASP
- Delphi
- JScript
- Perl
- PHP
- PowerBuilder
- Python
- VBScript
- Visual Basic
- C++

{{% /alert %}}

## Bekerja dengan COM Interop

Aspose.PDF for .NET dieksekusi di bawah kontrol .NET Framework dan ini disebut kode terkelola. Kode yang ditulis dalam semua bahasa di atas berjalan di luar .NET Framework dan ini disebut kode tidak terkelola. Interaksi antara kode tidak terkelola dan Aspose.PDF terjadi melalui fasilitas .NET yang disebut COM Interop.

Objek Aspose.PDF adalah objek .NET, tetapi ketika digunakan melalui COM Interop, mereka muncul sebagai objek COM dalam bahasa pemrograman Anda.
Objek Aspose.PDF adalah objek .NET, tetapi ketika digunakan melalui COM Interop, mereka tampak sebagai objek COM dalam bahasa pemrograman Anda.

{{% alert color="primary" %}}

- Dalam dunia COM kita membedakan antara server COM dan klien COM. Server COM menyimpan kelas COM sementara klien COM meminta instansi kelas dari server COM, yaitu objek COM.
- Klien COM atau aplikasi klien secara sederhana dapat mengetahui isi dari kelas COM atau sama sekali tidak mengetahui tentang metode dan propertinya. Oleh karena itu, aplikasi klien dapat menemukan struktur kelas COM saat kompilasi/pembuatan atau hanya selama eksekusi. Proses "penemuan" ini dikenal sebagai binding dan jadi kita memiliki **binding awal** dan **binding akhir**.
- Singkatnya, kelas COM adalah seperti kotak hitam dan untuk bekerja dengannya diperlukan pustaka tipe, file biner ini memiliki deskripsi metode, properti kelas COM dan bahasa tingkat tinggi mana pun yang mendukung kerja dengan objek COM sering memiliki ekspresi sintaks untuk menambahkan pustaka tipe, misalnya ini adalah [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) dalam C++.
- Secara singkat kelas COM adalah seperti kotak hitam dan untuk bekerja dengannya diperlukan pustaka tipe, file biner ini memiliki deskripsi metode, properti kelas COM dan bahasa tingkat tinggi apa pun yang mendukung kerja dengan objek COM sering memiliki ekspresi sintaks untuk menambahkan pustaka tipe, misalnya ini adalah [**#import**](http://msdn.microsoft.com/en-us/library/8etzzkb6.aspx) dalam C++.
- Pustaka tipe digunakan untuk pengikatan awal.
- Objek COM dapat mengekspos metode dan propertinya dengan dua cara: melalui **antarmuka pengiriman** (dispinterface) dan dalam **vtable** (tabel fungsi virtual)nya.
- Dalam **dispinterface**, setiap metode dan properti diidentifikasi oleh anggota unik; anggota ini adalah pengenal pengiriman fungsi (atau **DispID**).
- **Vtable** hanyalah satu set penunjuk ke fungsi yang didukung oleh antarmuka kelas COM.
- Objek yang mengekspos metodenya melalui kedua antarmuka mendukung **antarmuka ganda**.
- Ada keuntungan untuk kedua jenis pengikatan.
- Ada keuntungan pada kedua jenis pengikatan.
- Mekanisme pengikatan terlambat memiliki keuntungan besar: jika pembuat DLL COM memutuskan untuk merilis versi baru, dengan tata letak antarmuka fungsi yang berbeda, kode apa pun yang memanggil metode tersebut tidak akan crash kecuali jika metode tersebut tidak lagi tersedia; bahkan jika **vtable** berbeda, pengikatan terlambat berhasil menemukan DISPIDs baru dan memanggil metode yang sesuai.
{{% /alert %}}

Berikut adalah topik yang akhirnya perlu Anda kuasai:
{{% alert color="primary" %}}

- Menggunakan objek COM dalam bahasa pemrograman Anda. Lihat dokumentasi bahasa pemrograman Anda dan topik spesifik bahasa lebih lanjut dalam dokumentasi ini.

- Bekerja dengan objek COM yang diungkapkan oleh .NET COM Interop. Lihat [Interoperating With Unmanaged Code](http://msdn.microsoft.com/en-us/library/sd10k43k.aspx) dan [Exposing .NET Framework Components to COM](http://msdn.microsoft.com/en-us/library/zsfww439%28v=vs.110%29.aspx) di MSDN.

- Model objek dokumen Aspose.PDF.
- Model objek dokumen Aspose.PDF.

{{% /alert %}}

## Mendaftarkan Aspose.PDF untuk .NET dengan COM Interop

Anda perlu menginstal Aspose.PDF untuk .NET dan memastikan itu terdaftar dengan COM Interop (memastikan bahwa itu dapat dipanggil dari kode yang tidak dikelola).

{{% alert color="primary" %}}

Untuk mendaftarkan Aspose.PDF untuk .NET untuk COM Interop secara manual:

1. Dari menu **Start**, pilih **All Programs**, kemudian **Microsoft Visual Studio**, **Visual Studio Tools** dan, akhirnya, **Visual Studio Command Prompt**.
1. Masukkan perintah untuk mendaftarkan assembly:
   1. .NET Framework 2.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /codebase
   1. .NET Framework 3.5
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /codebase
   1. .NET Framework 4.0
      regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /codebase

{{% /alert %}}

Perhatikan bahwa /codebase hanya diperlukan jika Aspose.PDF.dll tidak berada di GAC, menggunakan opsi ini membuat regasm menempatkan jalur untuk assembly di registry.
Perhatikan bahwa /codebase hanya diperlukan jika Aspose.PDF.dll tidak ada di GAC, menggunakan opsi ini membuat regasm menempatkan jalur untuk perakitan di registri.

{{% alert color="primary" %}}

regasm.exe adalah alat yang termasuk dalam .NET Framework SDK. Semua alat SDK .NET Framework berada di direktori *\Microsoft .NET\Framework\<VersiFramework>*, misalnya *C:\Windows\Microsoft .NET\Framework\v4.0.30319*. Jika Anda menggunakan Visual Studio .NET:
Dari menu **Start**, pilih **Programs**, diikuti oleh **Microsoft Visual Studio .NET**, kemudian **Visual Studio .NET Tools** dan, akhirnya, **Visual Studio .NET 2003 Command Prompt**.
Ini menjalankan command prompt dengan semua variabel lingkungan yang diperlukan telah diatur.

{{% /alert %}}

### ProgIDs

ProgID adalah singkatan dari "programmatic identifier". Ini adalah nama kelas COM yang digunakan untuk membuat objek. ProgIDs terdiri dari nama perpustakaan "Aspose.PDF" dan nama kelas.

### Type Library

{{% alert color="primary" %}}

Jika bahasa pemrograman Anda (misalnya Visual Basic atau Delphi) memungkinkan Anda untuk merujuk ke perpustakaan tipe COM, maka tambahkan referensi ke Aspose.PDF.tlb dan untuk melihat semua kelas, metode, properti, dan enumerasi Aspose.PDF untuk .NET di Object Browser Anda.
Jika bahasa pemrograman Anda (seperti Visual Basic atau Delphi) memungkinkan Anda untuk merujuk pada pustaka tipe COM, tambahkan referensi ke Aspose.PDF.tlb dan untuk melihat semua kelas, metode, properti, dan enumerasi Aspose.PDF untuk .NET di Penjelajah Objek Anda.

Untuk menghasilkan file TLB:

- .NET Framework 2.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net2.0\Aspose.PDF.tlb" /codebase
- .NET Framework 3.5
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net3.5\Aspose.PDF.tlb" /codebase
- .NET Framework 4.0
  regasm "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.dll" /tlb: "C:\Program Files\Aspose\Aspose.PDF for .NET\bin\net4.0\Aspose.PDF.tlb" /codebase

{{% /alert %}}

## Membuat Objek COM

Pembuatan objek COM serupa dengan pembuatan objek .NET biasa:

```vb

'Instansiasi instance Pdf dengan memanggil konstruktornya yang kosong

Dim pdf
Set pdf = CreateObject("Aspose.PDF.Generator.Pdf")

```
Setelah dibuat, Anda dapat mengakses metode dan properti objek, seolah-olah itu adalah objek COM:

```vb
'Add section to Pdf object
pdf.Sections.Add(pdfsection)
```

Beberapa metode memiliki kelebihan dan akan ditampilkan oleh COM Interop dengan akhiran numerik yang ditambahkan pada mereka, kecuali untuk metode pertama yang tetap tidak berubah. Sebagai contoh, kelebihan metode Pdf.Save menjadi Pdf.Save, Pdf.Save_2, dan seterusnya.

Untuk informasi lebih lanjut, lihat artikel spesifik bahasa selanjutnya dalam dokumentasi ini.

## Membuat Assembly Pembungkus

Jika Anda perlu menggunakan banyak kelas, metode dan properti Aspose.PDF untuk .NET, pertimbangkan untuk membuat assembly pembungkus (menggunakan C# atau bahasa pemrograman .NET lainnya). Assembly pembungkus membantu menghindari penggunaan Aspose.PDF untuk .NET secara langsung dari kode yang tidak terkelola.

Pendekatan yang baik adalah mengembangkan assembly .NET yang merujuk Aspose.PDF untuk .NET dan melakukan semua pekerjaan dengan itu, dan hanya mengekspos satu set minimal kelas dan metode ke kode yang tidak terkelola.
Pendekatan yang baik adalah mengembangkan .NET assembly yang merujuk pada Aspose.PDF untuk .NET dan melakukan semua pekerjaan dengannya, serta hanya mengekspos sejumlah kecil kelas dan metode ke kode yang tidak terkelola.

Mengurangi jumlah kelas dan metode yang perlu Anda panggil melalui COM Interop mempermudah proyek. Menggunakan kelas .NET melalui COM Interop seringkali memerlukan keahlian lanjutan.
