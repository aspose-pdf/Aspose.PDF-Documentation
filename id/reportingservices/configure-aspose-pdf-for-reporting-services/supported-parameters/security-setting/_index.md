---
title: Pengaturan Keamanan
linktitle: Security Setting
type: docs
weight: 30
url: /reportingservices/security-setting/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Keamanan selalu menjadi isu terpenting di segala bidang, baik itu perlindungan jaringan atau dokumen PDF. Dokumen dibuat aman karena berbagai kemungkinan alasan: penulis dokumen mungkin ingin menjaga konten dokumen tetap aman dan tidak ingin membiarkan orang lain mengubahnya, dll.

Aspose.PDF untuk Layanan Pelaporan telah sangat memperhatikan aspek keamanan tersebut dengan menyediakan fitur-fitur ini kepada pengembang yang dapat berguna bagi mereka untuk melindungi dokumen PDF mereka. Oleh karena itu, ini berisi sejumlah parameter yang memungkinkan pengembang menerapkan tindakan keamanan berbeda pada dokumen PDF.

Salah satu langkah ini adalah melindungi dokumen PDF dengan kata sandi selama enkripsi. Anda juga dapat membatasi atau mengizinkan modifikasi konten, penyalinan konten, pencetakan dokumen, atau mengizinkan/menonaktifkan pengisian formulir. Fitur-fitur ini saat ini tidak didukung oleh Eksportir PDF Layanan Pelaporan SQL default tetapi Anda dapat mengimplementasikan fitur-fitur ini menggunakan Aspose.PDF untuk Layanan Pelaporan. Cukup tambahkan parameter keamanan yang sesuai ke laporan atau file konfigurasi server laporan, dan Anda akan dapat membuat dokumen PDF aman dengan hak istimewa terbatas.

Saat ini, perender Aspose.PDF untuk Layanan Pelaporan mendukung atribut keamanan berikut:

{{% /alert %}}

```text
Parameter Name: User Password  
Date Type: String  
Values supported: Any plain text
```

```text
Parameter Name: Master Password  
Date Type: String  
Values supported: Any plain text 
```

```text
Parameter Name: IsCopyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsPrintingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

```text
Parameter Name: IsContentsModifyingAllowed  
Date Type: Boolean  
Values supported: True, False (default) 
```

```text
Parameter Name: IsFormFillingAllowed  
Date Type: Boolean  
Values supported: True, False (default)  
```

## Contoh

```xml
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
```

