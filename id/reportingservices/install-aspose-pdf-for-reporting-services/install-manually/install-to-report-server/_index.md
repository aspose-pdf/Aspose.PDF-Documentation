---
title: Instal ke Report Server
linktitle: Instal ke Report Server
type: docs
weight: 10
url: /id/reportingservices/install-to-report-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

Anda hanya perlu mengikuti langkah-langkah ini jika Anda menginstal Aspose.PDF for Reporting Services secara manual, tidak menggunakan installer MSI. Installer MSI melakukan semua tindakan instalasi dan pendaftaran yang diperlukan secara otomatis.

{{% /alert %}}

Dalam langkah-langkah berikut, Anda perlu menyalin dan memodifikasi file di direktori tempat Microsoft SQL Server Reporting Services diinstal. Assembly SSRS 2016 terletak di direktori \Bin\SSRS2016 dalam paket zip; assembly SSRS 2017 terletak di direktori \Bin\SSRS2017; assembly SSRS 2019 terletak di direktori \Bin\SSRS2019; assembly SSRS 2022 terletak di direktori \Bin\SSRS2022; assembly Power BI Report Server terletak di direktori \Bin\PowerBI. 

{{% alert color="primary" %}}

**Step 1.** Temukan direktori instalasi Report Server. Direktori root untuk Microsoft SQL Server biasanya C:\Program Files\Microsoft SQL Server. Proses selanjutnya sedikit berbeda untuk Reporting Services 2016, Reporting Services 2017 dan yang lebih baru, serta Power BI Report Server:

- Report Server 2016 secara default diinstal di direktori C:\Program Files\Microsoft SQL Server\MSRS13.MSSQLSERVER\Reporting Services\ReportServer. Jika Anda menggunakan instance dengan nama khusus selain yang default, jalur default akan menjadi C:\Program Files\Microsoft SQL Server\MSRS13.[SSRSInstanceName]\Reporting Services\ReportServer
- Report Server 2017 dan versi selanjutnya secara default diinstal di direktori C:\Program Files\Microsoft SQL Server Reporting Services\SSRS\ReportServer.
- Power BI Report Server secara default diinstal di direktori C:\Program Files\Microsoft Power BI Report Server\PBIRS\ReportServer.

Dalam teks berikut, direktori instalasi Reporting Services (salah satu jalur yang disebutkan di atas) akan dirujuk sebagai ```<Instance>```.
{{% /alert %}}

{{% alert color="primary" %}}
**Langkah 2.** Salin Aspose.Pdf.ReportingServices.dll untuk versi SSRS yang sesuai ke ```<Instance>```folder \bin.
{{% /alert %}}

{{% alert color="primary" %}}
**Langkah 3.** Daftarkan Aspose.Pdf untuk Reporting Services sebagai ekstensi rendering. Buka ```<Instance>```\rsreportserver.config file dan tambahkan baris berikut ke dalam ```<Render>``` elemen:
{{% /alert %}}

**Contoh**

{{< highlight csharp >}}

 <Render>
...
<!--Start here.-->

<Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices"/>

</Render>

{{< /highlight >}}

{{% alert color="primary" %}}
**Step 4.** Sediakan Aspose.Pdf for Reporting Services dengan izin untuk dijalankan. Buka file ```<Instance>```\rssrvpolicy.config dan tambahkan teks berikut sebagai item terakhir dalam elemen ```<CodeGroup>``` kedua dari luar (yang seharusnya ```<CodeGroup class="FirstMatchCodeGroup" version="1" PermissionSetName="Execution" Description="This code group grants MyComputer code Execution permission. ">):```):
{{% /alert %}}

**Contoh**

{{< highlight csharp >}}

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

{{< /highlight >}}

{{% alert color="primary" %}}
**Langkah 5.** Verifikasi bahwa Aspose.Pdf for Reporting Services telah diinstal dengan sukses. Buka portal web Reporting Services dan periksa daftar format ekspor yang tersedia untuk sebuah laporan. Anda dapat meluncurkan portal web dengan memulai peramban web dan mengetikkan URL portal web Reporting Services di bilah alamat (secara default adalah http://```<Reporting_Services_server_name>```/reports/). Pilih salah satu laporan yang tersedia di portal web Anda dan tarik daftar dropdown Export. Anda harus melihat daftar format ekspor termasuk yang disediakan oleh ekstensi Aspose.Pdf for Reporting Services. Pilih item PDF via Aspose.PDF.

 
{{% /alert %}}

![todo:image_alt_text](install-to-report-server_1.png)

Klik item yang dipilih. Itu akan menghasilkan laporan dalam format yang dipilih, mengirimkannya ke klien, dan, tergantung pada pengaturan peramban web Anda, baik menampilkan dialog Simpan File untuk memilih tempat menyimpan laporan yang diekspor, atau secara otomatis mengunduh file ke folder Unduhan Anda.

{{% alert color="primary" %}}
Selamat, Anda telah berhasil menginstal Aspose.Pdf for Reporting Services dan mengekspor laporan sebagai dokumen PDF!
{{% /alert %}}





