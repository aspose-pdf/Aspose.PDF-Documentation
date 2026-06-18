---
title: Mencopot Lisensi Aspose.Pdf untuk SharePoint
linktitle: Mencopot Lisensi Aspose.Pdf untuk SharePoint
type: docs
weight: 30
url: /id/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Silakan ikuti langkah-langkah yang disebutkan dalam artikel ini untuk mencopot Lisensi PDF SharePoint API.
---

## Langkah Pencopotan

{{% alert color="primary" %}}

Untuk mencopot lisensi Aspose.PDF untuk SharePoint, silakan gunakan langkah-langkah di bawah ini dari konsol server.

1. Tarik kembali solusi lisensi dari farm:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Jalankan pekerjaan timer administratif untuk menyelesaikan penarikan segera:

  stsadm.exe -o execadmsvcjobs

3. Tunggu penarikan selesai. Anda dapat menggunakan Central   

  Administration untuk memeriksa apakah penarikan selesai di Central Administration -> Operations -> Solution Management

4. Hapus solusi dari penyimpanan solusi SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
