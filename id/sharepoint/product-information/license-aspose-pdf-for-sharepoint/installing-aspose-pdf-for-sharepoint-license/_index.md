---
title: Menginstal Lisensi Aspose.Pdf untuk SharePoint
linktitle: Menginstal Lisensi Aspose.Pdf untuk SharePoint
type: docs
weight: 10
url: /id/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Setelah Anda puas dengan evaluasi Anda, Anda dapat membeli lisensi untuk API PDF SharePoint dan mengikuti petunjuk instalasi untuk menerapkannya.
---

{{% alert color="primary" %}}

Setelah Anda puas dengan evaluasi Anda, Anda dapat [membeli lisensi](https://purchase.aspose.com/buy). Sebelum membeli pastikan Anda memahami dan menyetujui ketentuan langganan lisensi.

{{% /alert %}}

{{% alert color="primary" %}}

Lisensi akan dikirimkan ke email Anda setelah pesanan dibayar. Lisensi berupa arsip .zip yang berisi paket solusi SharePoint reguler.

Arsip ini berisi:

- Aspose.PDF.SharePoint.License.wsp

File paket solusi SharePoint. Lisensi Aspose.PDF untuk SharePoint dikemas sebagai solusi SharePoint untuk memudahkan penyebaran/pengambilan kembali di seluruh farm server.

- readme.txt

Instruksi pemasangan lisensi. Pemasangan lisensi dilakukan dari konsol server melalui stsadm.exe. Langkah-langkah yang diperlukan untuk memasang lisensi diberikan di bawah ini.

**Catatan:** Jalur-jalur dihilangkan demi kejelasan. Anda mungkin perlu menambahkan jalur sebenarnya ke stsadm.exe dan/atau file solusi saat mengeksekusinya.

1. Jalankan stsadm untuk menambahkan solusi ke penyimpanan solusi SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Sebarkan solusi ke semua server di farm:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Jalankan pekerjaan timer administratif untuk menyelesaikan penyebaran secara langsung.

stsadm.exe -o execadmsvcjobs

**Note:** Anda akan menerima peringatan saat menjalankan langkah penyebaran jika layanan Windows SharePoint Services Administration tidak dimulai. Stsadm.exe bergantung pada layanan ini dan Windows SharePoint Timer Service untuk mereplikasi data solusi di seluruh farm. Jika layanan ini tidak berjalan di farm server Anda, Anda mungkin perlu menyebarkan lisensi di setiap server.


{{% /alert %}}
