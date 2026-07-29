---
title: Pengaturan Keamanan
linktitle: Pengaturan Keamanan
type: docs
weight: 30
url: /id/reportingservices/security-setting/
lastmod: "2026-07-29"
---

{{% alert color="primary" %}}

Keamanan selalu menjadi isu paling penting di setiap bidang, baik itu perlindungan jaringan maupun dokumen PDF. Dokumen dibuat aman untuk banyak alasan yang mungkin: penulis dokumen mungkin ingin menjaga isi dokumen tetap aman dan tidak ingin mengizinkan orang lain mengubahnya, dll.

Aspose.PDF for Reporting Services telah sangat memperhatikan aspek keamanan tersebut dengan menyediakan fitur-fitur ini kepada pengembang yang dapat berguna bagi mereka untuk melindungi dokumen PDF mereka. Oleh karena itu, ia berisi sejumlah parameter yang memungkinkan pengembang menerapkan berbagai langkah keamanan pada dokumen PDF.

Salah satu langkah ini adalah melindungi dokumen PDF dengan kata sandi selama enkripsi. Anda juga dapat membatasi atau mengizinkan modifikasi konten, menyalin konten, pencetakan dokumen, atau mengizinkan/menonaktifkan pengisian formulir. Fitur-fitur ini saat ini tidak didukung oleh Ekspor PDF default SQL Reporting Services, tetapi Anda dapat mengimplementasikan fitur-fitur ini menggunakan Aspose.PDF for Reporting Services. Cukup tambahkan parameter keamanan yang sesuai ke laporan atau file konfigurasi server laporan, dan Anda akan dapat membuat dokumen PDF yang aman dengan hak istimewa terbatas.

Saat ini, renderer Aspose.PDF for Reporting Services mendukung atribut keamanan berikut:

{{% /alert %}}

{{% alert color="primary" %}}

**Nama Parameter**: Password Pengguna  
**Tipe Data**: String  
**Nilai yang didukung**: Teks biasa apa pun

**Nama Parameter**: Password Master  
**Tipe Data**: String  
**Nilai yang didukung**: Teks biasa apa pun 

**Nama Parameter**: IsCopyingAllowed  
**Tipe Data**: Boolean  
**Nilai yang didukung**: True, False (default)  

**Nama Parameter**: IsPrintingAllowed  
**Tipe Data**: Boolean  
**Nilai yang didukung**: True, False (default)  

**Nama Parameter**: IsContentsModifyingAllowed  
**Tipe Data**: Boolean  
**Nilai yang didukung**: True, False (default)  

**Nama Parameter**: IsFormFillingAllowed  
**Tipe Data**: Boolean  
**Nilai yang didukung**: True, False (default)  

**Contoh**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>Salah</IsCopyingAllowed>
    <IsPrintingAllowed>Salah</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}
