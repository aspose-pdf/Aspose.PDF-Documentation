---
title: Menginstal Lisensi Aspose.Pdf for SharePoint
linktitle: Menginstal Lisensi Aspose.Pdf for SharePoint
type: docs
weight: 10
url: /id/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-08-07"
description: Setelah Anda puas dengan evaluasi Anda, Anda dapat membeli lisensi untuk PDF SharePoint API dan mengikuti petunjuk instalasi untuk menerapkannya.
---

{{% alert color="primary" %}}

Setelah Anda puas dengan evaluasi Anda, Anda dapat [membeli lisensi](https://purchase.aspose.com/buy). Sebelum membeli, pastikan Anda memahami dan menyetujui ketentuan langganan lisensi.

{{% /alert %}}

{{% alert color="primary" %}}

Lisensi akan dikirim melalui email kepada Anda setelah pesanan dibayar. Lisensi tersebut berupa arsip .zip yang berisi paket solusi SharePoint standar.

Arsip ini berisi:

- Aspose.PDF.SharePoint.License.wsp

Berkas paket solusi SharePoint. Lisensi Aspose.PDF for SharePoint dikemas sebagai solusi SharePoint untuk memudahkan penyebaran/pengembalian di seluruh farm server.

- readme.txt

Instruksi pemasangan lisensi. Pemasangan lisensi dilakukan dari konsol server melalui stsadm.exe. Langkah-langkah yang diperlukan untuk memasang lisensi diberikan di bawah.

**Catatan:** Jalur-jalur dihilangkan demi kejelasan. Anda mungkin perlu menambahkan jalur sebenarnya ke stsadm.exe dan/atau file solusi saat mengeksekusinya.

1. Jalankan stsadm untuk menambahkan solusi ke penyimpanan solusi SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. Sebarkan solusi ke semua server di farm:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. Jalankan pekerjaan timer administratif untuk menyelesaikan penyebaran secara segera.

stsadm.exe -o execadmsvcjobs

**Catatan:** Anda akan menerima peringatan saat menjalankan langkah penyebaran jika Windows SharePoint Services Administration service tidak dimulai. Stsadm.exe bergantung pada layanan ini dan Windows SharePoint Timer Service untuk menyalin data solusi di seluruh farm. Jika layanan ini tidak berjalan di farm server Anda, Anda mungkin perlu menyebarkan lisensi pada setiap server.

{{% /alert %}}
