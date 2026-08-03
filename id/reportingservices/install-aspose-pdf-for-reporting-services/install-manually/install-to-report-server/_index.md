---
title: Instal ke Server Laporan
linktitle: Install to Report Server
type: docs
weight: 10
url: /reportingservices/install-to-report-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Anda hanya perlu mengikuti langkah-langkah ini jika Anda menginstal Aspose.PDF untuk Layanan Pelaporan secara manual, tidak menggunakan penginstal MSI. Penginstal MSI melakukan semua tindakan instalasi dan registrasi yang diperlukan secara otomatis.

{{% /alert %}}

Pada langkah-langkah berikut, Anda perlu menyalin dan memodifikasi file di direktori tempat Layanan Pelaporan Microsoft SQL Server diinstal. Perakitan SSRS 2016 terletak di direktori \Bin\SSRS2016 paket zip; perakitan SSRS 2017 terletak di direktori \Bin\SSRS2017; perakitan SSRS 2019 terletak di direktori \Bin\SSRS2019; perakitan SSRS 2022 terletak di direktori \Bin\SSRS2022; rakitan Server Laporan Power BI terletak di direktori \Bin\PowerBI.

**Langkah 1.** Temukan direktori instalasi Server Laporan. Direktori akar untuk Microsoft SQL Server biasanya C:\Program Files\Microsoft SQL Server. Proses lebih lanjut sedikit berbeda untuk Layanan Pelaporan 2016, Layanan Pelaporan 2017 dan yang lebih baru, dan Server Laporan Power BI:

- Report Server 2016 secara default diinstal di direktori C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Jika Anda menggunakan instans dengan nama khusus dan bukan instans default, jalur defaultnya adalah C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 dan yang lebih baru secara default diinstal di direktori C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Server Laporan Power BI secara default diinstal di direktori C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

Dalam teks berikut, direktori instalasi Layanan Pelaporan (salah satu jalur yang disebutkan di atas) akan dirujuk sebagai `<Instance>`.

**Langkah 2.** Salin Aspose.Pdf.ReportingServices.dll untuk versi SSRS yang sesuai ke folder `<Instance>\bin`.

**Langkah 3.** Daftarkan Aspose.PDF untuk Layanan Pelaporan sebagai ekstensi rendering. Buka file `<Instance>\rsreportserver.config` dan tambahkan baris berikut ke dalam elemen `<Render>`:

## Contoh

```xml
<Render>
...
<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>
</Render>
```

**Langkah 4.** Berikan Aspose.PDF untuk Layanan Pelaporan dengan izin untuk mengeksekusi. Buka file `<Instance>\rssrvpolicy.config` dan tambahkan teks berikut sebagai item terakhir di elemen kedua di luar `<CodeGroup>` yang seharusnya `<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):`

## Contoh

```xml

 <CodeGroup>
...

<CodeGroup>
...

<!--Start here.-->

<CodeGroup class="UnionCodeGroup" version="1" PermissionSetName="FullTrust"

Name="Aspose.Pdf_for_Reporting_Services" Description="This code group grants full trust to the AP4SSRS assembly.">

<IMembershipCondition class="StrongNameMembershipCondition" version="1" PublicKeyBlob="00240000048000009400000006020000002400005253413100040000010001005542e99cecd28842dad186257b2c7b6ae9b5947e51e0b17b4ac6d8cecd3e01c4d20658c5e4ea1b9a6c8f854b2d796c4fde740dac65e834167758cff283eed1be5c9a812022b015a902e0b97d4e95569eb8c0971834744e633d9cb4c4a6d8eda03c12f486e13a1a0cb1aa101ad94943236384cbbf5c679944b994de9546e493bf " />

</CodeGroup>

<!--End here. -->

</CodeGroup>

</CodeGroup>
```

**Langkah 5.** Verifikasi bahwa Aspose.PDF untuk Layanan Pelaporan berhasil diinstal. Buka portal web Layanan Pelaporan dan periksa daftar format ekspor yang tersedia untuk laporan. Anda dapat meluncurkan portal web dengan memulai browser web dan mengetikkan URL portal web Layanan Pelaporan di bilah alamat (secara default adalah http://@@KEEP_0@@/reports/). Pilih salah satu laporan yang tersedia di portal web Anda dan tarik daftar tarik-turun Ekspor. Anda akan melihat daftar format ekspor termasuk yang disediakan oleh ekstensi Aspose.PDF untuk Layanan Pelaporan. Pilih PDF melalui item Aspose.PDF.

![Install to report server](install-to-report-server_1.png)

Klik item yang dipilih. Ini akan menghasilkan laporan dalam format yang dipilih, mengirimkannya ke klien, dan, tergantung pada pengaturan browser web Anda, menampilkan dialog Simpan File untuk memilih tempat menyimpan laporan yang diekspor, atau secara otomatis mengunduh file ke folder Unduhan Anda.

Selamat, Anda telah berhasil menginstal Aspose.PDF untuk Layanan Pelaporan dan mengekspor laporan sebagai dokumen PDF!


