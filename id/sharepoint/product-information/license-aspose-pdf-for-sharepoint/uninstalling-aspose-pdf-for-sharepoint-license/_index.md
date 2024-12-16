---
title: Menghapus Lisensi Aspose.Pdf untuk SharePoint
type: docs
weight: 30
url: /id/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Silakan ikuti langkah-langkah yang disebutkan dalam artikel ini untuk menghapus Lisensi API SharePoint PDF.
---

## Langkah-langkah Penghapusan

{{% alert color="primary" %}}

Untuk menghapus lisensi Aspose.PDF untuk SharePoint, silakan gunakan langkah-langkah berikut dari konsol server.

1. Tarik kembali solusi lisensi dari farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Jalankan pekerjaan timer administratif untuk menyelesaikan penarikan segera:

  stsadm.exe -o execadmsvcjobs

3. Tunggu hingga penarikan selesai. Anda dapat menggunakan Central   

  Administration untuk memeriksa apakah penarikan telah selesai di bawah Central Administration -> Operations -> Solution Management

4. Hapus solusi dari penyimpanan solusi SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}