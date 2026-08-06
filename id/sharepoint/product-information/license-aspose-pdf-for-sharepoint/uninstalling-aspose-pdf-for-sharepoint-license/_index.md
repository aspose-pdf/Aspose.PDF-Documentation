---
title: Menghapus instalasi Aspose.PDF untuk Lisensi SharePoint
linktitle: Menghapus instalasi Aspose.PDF untuk Lisensi SharePoint
type: docs
weight: 30
url: /id/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Silakan ikuti langkah-langkah yang disebutkan dalam artikel ini untuk menghapus instalasi Lisensi PDF SharePoint API.
---

## Langkah-Langkah Penghapusan Instalasi

{{% alert color="primary" %}}

Untuk menghapus instalasi Aspose.PDF untuk lisensi SharePoint, silakan gunakan langkah-langkah di bawah ini dari konsol server.

1. Cabut solusi lisensi dari peternakan:

  stsadm.exe -o retractsolution -nama Aspose.PDF.SharePoint.License.wsp -langsung

2. Jalankan tugas pengatur waktu administratif untuk segera menyelesaikan pencabutan:

  stsadm.exe -o execadmsvcjobs

3. Tunggu hingga pencabutan selesai. Anda dapat menggunakan Pusat   

  Administrasi untuk memeriksa apakah pencabutan selesai di bawah Administrasi Pusat -> Operasi -> Manajemen Solusi

4. Hapus solusi dari penyimpanan solusi SharePoint:

  stsadm.exe -o deletesolution -nama Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

