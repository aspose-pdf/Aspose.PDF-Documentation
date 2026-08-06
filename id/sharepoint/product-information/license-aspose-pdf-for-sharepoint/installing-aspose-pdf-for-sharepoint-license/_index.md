---
title: Menginstal Aspose.PDF untuk Lisensi SharePoint
linktitle: Menginstal Aspose.PDF untuk Lisensi SharePoint
type: docs
weight: 10
url: /id/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Once you are happy with your evaluation, you can purchase a license for PDF SharePoint API and follow the installation instructions to apply it.
---

{{% alert color="primary" %}}

Once you are happy with your evaluation, you can [purchase a license](https://purchase.aspose.com/buy). Before purchasing make sure you understand and agree to the license subscription terms.

{{% /alert %}}

{{% alert color="primary" %}}

Lisensi akan dikirimkan melalui email kepada Anda setelah pesanan dibayar. Lisensinya adalah arsip .zip yang berisi paket solusi SharePoint reguler.

Arsip ini berisi:

- Aspose.PDF.SharePoint.License.wsp

SharePoint solution package file. Aspose.PDF for SharePoint License is packaged as a SharePoint solution to facilitate deployment/retraction across the server farm.

- readme.txt

License installation instructions. License installation is performed from the server console via stsadm.exe. The steps required to install the license are given below.

**Note:** The paths are omitted for clarity. You may need to add the actual path to stsadm.exe and/or solution file when executing them.

1. Jalankan stsadm untuk menambahkan solusi ke penyimpanan solusi SharePoint:

stsadm.exe -o tambahkan solusi -nama file Aspose.PDF.SharePoint.License.wsp

2. Deploy the solution to all servers in the farm:

stsadm.exe -o deploysolution -nama Aspose.PDF.SharePoint.License.wsp -langsung -kekuatan

3. Jalankan tugas pengatur waktu administratif untuk segera menyelesaikan penerapan.

stsadm.exe -o execadmsvcjobs

**Catatan:** Anda akan menerima peringatan saat menjalankan langkah penerapan jika layanan Administrasi Layanan Windows SharePoint tidak dimulai. Stsadm.exe mengandalkan layanan ini dan Layanan Windows SharePoint Timer untuk mereplikasi data solusi di seluruh farm. Jika layanan ini tidak berjalan di server farm Anda, Anda mungkin perlu menyebarkan lisensi di setiap server.

{{% /alert %}}

