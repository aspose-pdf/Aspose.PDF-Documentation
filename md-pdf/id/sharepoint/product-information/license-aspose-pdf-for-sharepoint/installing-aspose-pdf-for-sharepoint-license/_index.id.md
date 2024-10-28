---
title: Menginstal Lisensi Aspose.Pdf untuk SharePoint
type: docs
weight: 10
url: /sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Setelah Anda puas dengan evaluasi Anda, Anda dapat membeli lisensi untuk PDF SharePoint API dan mengikuti instruksi instalasi untuk menerapkannya.
---

{{% alert color="primary" %}}

Setelah Anda puas dengan evaluasi Anda, Anda dapat [membeli lisensi](https://purchase.aspose.com/buy). Sebelum membeli, pastikan Anda memahami dan menyetujui ketentuan langganan lisensi.

{{% /alert %}}

{{% alert color="primary" %}}

Lisensi akan dikirimkan ke email Anda setelah pesanan telah dibayar. Lisensi adalah arsip .zip yang berisi paket solusi SharePoint biasa.

Arsip ini berisi:

- Aspose.PDF.SharePoint.License.wsp

Berkas paket solusi SharePoint. Lisensi Aspose.PDF untuk SharePoint dikemas sebagai solusi SharePoint untuk memudahkan penyebaran/pencabutan di seluruh server farm.

- readme.txt

Instruksi instalasi lisensi.
 Instalasi lisensi dilakukan dari konsol server melalui stsadm.exe. Langkah-langkah yang diperlukan untuk menginstal lisensi diberikan di bawah ini.

**Catatan:** Jalur dihilangkan untuk kejelasan. Anda mungkin perlu menambahkan jalur sebenarnya ke stsadm.exe dan/atau file solusi saat mengeksekusinya.

1. Jalankan stsadm untuk menambahkan solusi ke penyimpanan solusi SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Terapkan solusi ke semua server dalam farm:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Jalankan pekerjaan timer administratif untuk menyelesaikan penerapan segera.

stsadm.exe -o execadmsvcjobs

**Catatan:** Anda akan menerima peringatan saat menjalankan langkah penerapan jika layanan Administrasi Windows SharePoint Services tidak dimulai. Stsadm.exe bergantung pada layanan ini dan Windows SharePoint Timer Service untuk mereplikasi data solusi di seluruh farm. Jika layanan ini tidak berjalan di farm server Anda, Anda mungkin perlu menerapkan lisensi di setiap server.