---
title: Visual Studio Export GridView To PDF Control
type: docs
weight: 10
url: /id/net/visual-studio-export-gridview-to-pdf-control/
---

## Pendahuluan

Kontrol Ekspor GridView ke Pdf adalah kontrol server ASP.NET yang memungkinkan ekspor konten GridView ke dalam dokumen Pdf menggunakan [Aspose.PDF](http://www.aspose.com/.net/pdf-component.aspx). Ini menambahkan tombol **Ekspor ke Pdf** di atas kontrol GridView. Dengan mengklik tombol tersebut, konten kontrol GridView secara dinamis diekspor ke dokumen Pdf dan kemudian secara otomatis mengunduh file yang diekspor ke lokasi disk yang dipilih oleh pengguna hanya dalam beberapa detik.

### Fitur Modul

Versi awal kontrol ini menyediakan fitur-fitur berikut:

- Dapatkan salinan offline dari konten GridView online favorit Anda untuk diedit, dibagikan dan dicetak dalam dokumen Pdf yang sangat populer.
- Diwarisi dari kontrol GridView ASP.NET default dan oleh karena itu memiliki semua fitur dan propertinya.
- Berfungsi dengan semua versi .NET mulai dari .NET 2.0.
- Kemampuan untuk menyesuaikan/melokalkan teks tombol Ekspor.
- Kemampuan untuk menyesuaikan/melokalkan teks tombol Ekspor.
- Opsi untuk Mengekspor dalam mode Lanskap jika konten GridView lebih lebar dan tidak muat dalam mode Potret default
- Terapkan tampilan dan nuansa tema Anda sendiri pada tombol Ekspor menggunakan css.
- Opsi untuk menambahkan judul kustom di bagian atas dokumen yang diekspor
- Opsi untuk menyimpan setiap dokumen yang diekspor di server di jalur disk yang dapat dikonfigurasi
- Opsi untuk mengekspor halaman saat ini atau semua halaman ketika paging diaktifkan

## Persyaratan Sistem dan Platform yang Didukung

### Persyaratan Sistem

Kontrol Ekspor GridView Ke Pdf untuk Visual Studio dapat digunakan di sistem apa pun yang memiliki IIS dan .NET framework 2.0 atau lebih tinggi terinstal.

### Platform yang Didukung

Kontrol Ekspor GridView Ke Pdf untuk Visual Studio didukung dari semua versi ASP.NET yang berjalan pada .NET framework 2.0 atau lebih tinggi. Anda dapat menggunakan salah satu versi Visual Studio berikut untuk menggunakan kontrol ini dalam aplikasi ASP.NET Anda

- Visual Studio 2005
- Visual Studio 2008
- Visual Studio 2010
- Visual Studio 2012
- Visual Studio 2013

## Mengunduh
## Mengunduh

Anda dapat mengunduh Export GridView To Pdf Control dari salah satu lokasi berikut

- [CodePlex](https://asposevs.codeplex.com/releases/view/617022)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/releases/tag/AsposeExportGridViewToPdfControl_1.0)

## Memasang

Sangat sederhana dan mudah untuk memasang Export GridView To Pdf Control, silakan ikuti langkah-langkah sederhana ini

### **Untuk Visual Studio 2010, 2012 dan 2013**

1. Ekstrak file zip yang telah diunduh yaitu Aspose.PDF.GridViewExport_1.0.zip
2. Klik dua kali file VSIX Aspose.PDF.GridViewExport.vsix
3. Akan muncul dialog yang menunjukkan versi Visual Studio yang tersedia dan didukung yang terinstal di mesin Anda
4. Pilih yang ingin Anda tambahkan Export GridView To Pdf Control ke.
5. Klik Pasang

Anda akan mendapatkan dialog keberhasilan setelah pemasangan selesai.

**Catatan:** Pastikan untuk me-restart Visual Studio agar perubahan dapat berlaku.

### **Untuk Visual Studio 2005, 2008 dan edisi Express**

Silakan ikuti langkah-langkah ini untuk mengintegrasikan Export GridView To Pdf Control di Visual Studio untuk drag and drop yang mudah seperti kontrol ASP.NET lainnya
Silakan ikuti langkah-langkah ini untuk mengintegrasikan kontrol Ekspor GridView Ke Pdf di Visual Studio untuk tarik dan lepas seperti kontrol ASP.NET lainnya

1. Ekstrak file zip yang telah diunduh yaitu Aspose.PDF.GridViewExport.NET2.0_1.0.zip
1. Pastikan untuk menjalankan Visual Studio sebagai Administrator

Pada menu Alat, klik Pilih Item Kotak Alat.

1. Klik Telusuri.
   Kotak dialog Buka muncul.
1. Telusuri ke folder yang telah diekstrak dan pilih Aspose.PDF.GridViewExport.dll
1. Klik OK.

Ketika Anda membuka kontrol aspx atau ascx di Toolbox sisi kiri, Anda akan melihat ExportGridViewToPdf di bawah Tab Umum

![todo:image_alt_text](visual-studio-export-gridview-to-pdf-control_2.png)

## Menggunakan

Setelah terinstal, sangat mudah untuk mulai menggunakan kontrol ini di aplikasi ASP.NET Anda

|**Untuk kerangka kerja .NET 4.0 dan di atasnya**|**Untuk kerangka kerja .NET 2.0 dan di atasnya**|** |
| :- | :- | :- |
|Untuk aplikasi yang berjalan dalam kerangka kerja .NET 4.0 dan di atasnya di Visual Studio 2010 dan di atasnya, Anda seharusnya melihat kontrol **ExportGridViewToPdf** di Tab **Aspose** di Toolbar seperti yang ditunjukkan di bawah ini.
|Untuk aplikasi yang berjalan di .NET framework 4.0 dan di atasnya di Visual Studio 2010 dan di atasnya, Anda seharusnya melihat kontrol **ExportGridViewToPdf** di Tab **Aspose** di Toolbar seperti yang ditunjukkan di bawah ini.

### Menambahkan kontrol ExportGridViewToPdf secara manual

Jika Anda mengalami masalah menggunakan metode di atas yang menggunakan Visual Studio Toolbox, Anda dapat secara manual menambahkan kontrol ini ke aplikasi ASP.NET Anda yang berjalan di .NET framework yang lebih besar dari 2.0

1. Jika Anda menggunakan Visual Studio pastikan untuk Menjalankannya sebagai Administrator
1. Tambahkan referensi ke **Aspose.PDF.GridViewExport.dll** yang tersedia dalam paket unduhan yang telah diekstrak di proyek ASP.NET Anda atau aplikasi web. Pastikan aplikasi web/Visual Studio Anda memiliki akses penuh ke folder ini, jika tidak Anda mungkin mendapatkan pengecualian Akses ditolak.
1. Tambahkan baris ini ke bagian atas halaman, kontrol atau MasterPage

```csharp
 <%@ Register assembly="Aspose.PDF.GridViewExport" namespace="Aspose.PDF.GridViewExport" tagprefix="aspose" %>
```
```csharp
 <aspose:ExportGridViewToPdf ID="ExportGridViewToPdf1" runat="server"></aspose:ExportGridViewToPdf>
```

### FAQs

Pertanyaan umum dan masalah yang mungkin Anda hadapi saat menggunakan Control ini

<div class="schema-faq-code" itemscope="" itemtype="https://schema.org/FAQPage">
    <div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
        <h3 itemprop="name" class="faq-q">1. Saya tidak dapat melihat kontrol ExportGridViewToPdf di Toolbox</h3>
        <div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
             <div itemprop="text" class="faq-a">
               <p><strong>Visual Studio 2010 dan lebih tinggi</strong></p>
<ol><li>Pastikan Anda telah menginstal kontrol ini menggunakan file ekstensi VSIX yang ditemukan dalam paket yang diunduh. Untuk memverifikasi, pergi ke Tools -&gt; Extension and Updates. Di bawah Installed Anda seharusnya melihat 'Aspose Export Export GridView To Pdf Control'. Jika tidak terlihat, silakan coba menginstal ulang</li>
<li>Pastikan aplikasi web Anda berjalan di .NET framework 4.0 atau lebih tinggi, untuk versi .NET framework yang lebih rendah, silakan periksa metode alternatif di atas.</li>
<li>Pastikan aplikasi web Anda berjalan di .NET framework 4.0 atau lebih tinggi, untuk versi .NET framework yang lebih rendah silahkan cek metode alternatif di atas.
Versi Lama dari Visual Studio</li>
<li>Pastikan Anda telah menambahkan kontrol ini ke Toolbox Anda secara manual sesuai dengan instruksi di atas.</li></ol>
</div>
</div>
</div>

<div itemscope="" itemprop="mainEntity" itemtype="https://schema.org/Question" class="faq-question">
<h3 itemprop="name" class="faq-q">2. Saya mendapatkan kesalahan 'Akses ditolak' saat menjalankan aplikasi</h3>
<div itemscope="" itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
<div itemprop="text" class="faq-a">
<ol>
<li>Jika Anda mengalami masalah ini pada produksi maka pastikan Anda menyalin kedua Aspose.PDF.dll dan Aspose.PDF.GridViewExport.dll ke folder bin Anda.</li>
<li>Jika Anda menggunakan Visual Studio pastikan untuk menjalankannya sebagai Administrator meskipun Anda sudah login sebagai administrator.</li>

<li>Jika Anda menggunakan Visual Studio pastikan untuk menjalankannya sebagai Administrator meskipun Anda sudah login sebagai administrator.</li>
</ol>
</div>
</div>
</div>
</div>

### **Properti Kontrol Aspose .NET Export GridView Ke Pdf**

Properti berikut ini tersedia untuk dikonfigurasi dan menggunakan fitur menarik yang disediakan oleh kontrol ini

|**Nama Properti**|**Tipe**|**Contoh/Nilai yang mungkin**|**Deskripsi**|
| :- | :- | :- | :- |
|ExportButtonText|string|Export to Pdf|Anda dapat menggunakan properti ini untuk menggantikan teks default yang ada|
|ExportButtonCssClass|string|btn btn-primary|Kelas Css yang diterapkan pada div luar dari tombol ekspor. Untuk menerapkan css pada tombol Anda dapat menggunakan .yourClass input|
|ExportInLandscape|bool|true or false|Jika benar ini mengubah orientasi dokumen keluaran menjadi landscape. Default adalah Portrait|
| | | | |
|ExportFileHeading|string|GridView Export Example Report|Anda dapat menggunakan tag html untuk menambahkan gaya pada heading Anda|
|ExportOutputPathOnServer|string|c:/temp|Jalur Disk lokal output di server di mana salinan ekspor secara otomatis disimpan.|
```
|ExportOutputPathOnServer|string|c:/temp|Lokal output Disk path di server tempat salinan ekspor secara otomatis disimpan.
|ExportDataSource|object|allRowsDataTable|Menetapkan objek dari mana kontrol pengikat data ini mengambil daftar item data-nya. Objek tersebut harus memiliki semua data yang perlu diekspor. Properti ini digunakan bersamaan dengan properti DataSource normal dan berguna ketika paging kustom diaktifkan dan halaman saat ini hanya mengambil baris yang akan ditampilkan di layar.
|LicenseFilePath|string| |Lokal path di server untuk file lisensi. Sebagai contoh c:/inetpub/Aspose.PDF.lic|

Sebuah contoh dari Ekspor GridView ke kontrol Pdf dengan semua properti yang digunakan ditunjukkan di bawah ini

```csharp
<aspose:ExportGridViewToPdf Width="800px" ID="ExportGridViewToPdf1" ExportButtonText="Ekspor ke Pdf"
    CssClass="table table-hover table-bordered" ExportButtonCssClass="myClass" ExportOutputFormat="Doc"
    ExportInLandscape="true" ExportOutputPathOnServer="c:\\temp" ExportFileHeading="<h4>Laporan Contoh</h4>"
    OnPageIndexChanging="ExportGridViewToPdf1_PageIndexChanging" PageSize="5" AllowPaging="True"
    LicenseFilePath="c:\\inetpub\\Aspose.PDF.lic"
    runat="server" CellPadding="4" ForeColor="#333333" GridLines="Both">
</aspose:ExportGridViewToPdf>
```
## Video Demo

Silakan periksa [video](https://www.youtube.com/watch?v=WNJ7T8u4JlM) di bawah ini untuk melihat modul dalam aksi.

### Dukungan

Sejak hari-hari pertama Aspose, kami tahu bahwa hanya memberikan produk yang baik kepada pelanggan kami tidak akan cukup. Kami juga perlu memberikan layanan yang baik. Kami adalah pengembang juga dan memahami betapa frustrasinya ketika masalah teknis atau keanehan dalam perangkat lunak menghentikan Anda dari melakukan apa yang perlu Anda lakukan. Kami di sini untuk menyelesaikan masalah, bukan menciptakannya.

Inilah mengapa kami menawarkan dukungan gratis. Siapa pun yang menggunakan produk kami, apakah mereka telah membelinya atau menggunakan evaluasi, pantas mendapatkan perhatian dan penghormatan penuh dari kami.

Anda dapat mencatat masalah atau saran terkait Pdf ini menggunakan platform berikut

- [CodePlex](https://asposevs.codeplex.com/workitem/list/basic)
- [Visual Studio Gallery - Q and A](https://visualstudiogallery.msdn.microsoft.com/fb8b9944-cfe5-44a9-8aa7-c785d32d1066)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/issues)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)
- [Microsoft Developer Network - Q and A](https://code.msdn.microsoft.com/Aspose-NET-Export-GridView-caddbb6d/view/Discussions#content)

### Perluas dan Berkontribusi

Aspose .NET Export GridView ke Pdf untuk Visual Studio bersifat open source dan kode sumbernya tersedia di situs web coding sosial utama yang tercantum di bawah ini. Pengembang didorong untuk mengunduh kode sumber dan memperluas fungsionalitas sesuai dengan kebutuhan mereka sendiri.

#### Kode Sumber

Anda dapat mendapatkan kode sumber terbaru dari salah satu lokasi berikut

- [CodePlex](https://asposevs.codeplex.com/SourceControl/latest#Aspose.PDF.GridViewExport/)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-.NET/tree/master/Plugins/Visual%20Studio/Aspose.PDF.GridViewExport)

#### Cara mengonfigurasi kode sumber

Anda perlu memiliki yang berikut ini terpasang untuk membuka dan memperluas kode sumber

- Visual Studio 2010

Silakan ikuti langkah-langkah sederhana ini untuk memulai

1. Unduh/Clone kode sumber.
1.
1.
1. Telusuri ke kode sumber terbaru yang telah Anda unduh dan buka **Aspose.PDF.GridViewExport.sln**

#### Tinjauan Kode Sumber

Terdapat tiga proyek dalam solusi tersebut

- Aspose.PDF.GridViewExport - Berisi paket VSIX dan Server Pdf untuk .NET 4.0.
- Aspose.PDF.GridViewExport_DotNet_2.0 - GridView Pdf yang diperluas untuk .NET 2.0
- Aspose.PDF.GridViewExport.Website - Proyek web untuk menguji GridView Pdf yang dapat diekspor ke Word
