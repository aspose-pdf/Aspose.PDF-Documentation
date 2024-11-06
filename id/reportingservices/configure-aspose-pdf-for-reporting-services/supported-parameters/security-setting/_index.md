---
title: Security Setting
type: docs
weight: 30
url: id/reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Keamanan selalu menjadi masalah paling penting di setiap bidang, baik itu perlindungan jaringan atau dokumen PDF. Dokumen dibuat aman karena berbagai alasan: penulis dokumen mungkin ingin menjaga isi dokumen tetap aman dan tidak ingin mengizinkan orang lain mengubahnya, dll.

Aspose.Pdf for Reporting Services telah memperhatikan aspek keamanan semacam itu dengan menyediakan fitur-fitur ini kepada pengembang yang dapat berguna bagi mereka untuk melindungi dokumen PDF mereka. Oleh karena itu, ia berisi sejumlah parameter yang memungkinkan pengembang menerapkan langkah-langkah keamanan yang berbeda pada dokumen PDF.

Salah satu langkah ini adalah melindungi dokumen PDF dengan kata sandi selama enkripsi. Anda juga dapat membatasi atau mengizinkan modifikasi konten, menyalin konten, mencetak dokumen, atau mengizinkan/menonaktifkan pengisian formulir. Fitur-fitur ini saat ini tidak didukung oleh SQL Reporting Services PDF Exporter default, tetapi Anda dapat mengimplementasikan fitur-fitur ini menggunakan Aspose.Pdf for Reporting Services. Cukup tambahkan parameter keamanan yang sesuai ke laporan atau file konfigurasi server laporan, dan Anda akan dapat membuat dokumen PDF yang aman dengan hak istimewa terbatas.

Saat ini, renderer Aspose.Pdf for Reporting Services mendukung atribut keamanan berikut:

{{% /alert %}}

{{% alert color="primary" %}}

**Parameter Name**: User Password  
**Date Type**: String  
**Values supported**: Any plain text

**Parameter Name**: Master Password  
**Date Type**: String  
**Values supported**: Any plain text 

**Parameter Name**: IsCopyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsPrintingAllowed  
**Date Type**: Boolean  

**Values supported**: True, False (default)  
**Parameter Name**: IsContentsModifyingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Parameter Name**: IsFormFillingAllowed  
**Date Type**: Boolean  
**Values supported**: True, False (default)  

**Contoh**

{{< highlight csharp >}}

<Render>
…
    <Extension Name="APPDF" Type="Aspose.Pdf.ReportingServices.Renderer,Aspose.Pdf.ReportingServices">
    <Configuration>
    <UserPassword>aspose</UserPassword>
    <IsCopyingAllowed>False</IsCopyingAllowed>
    <IsPrintingAllowed>False</IsPrintingAllowed>
    </Configuration>
    </Extension>
</Render>

{{< /highlight >}}

{{% /alert %}}