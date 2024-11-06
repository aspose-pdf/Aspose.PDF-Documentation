---
title: Detail pemasangan lebih lanjut
type: docs
weight: 30
url: id/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: Informasi lebih lanjut tentang pemasangan PDF SharePoint API menjelaskan cara menerapkan, mengaktifkan, dan menonaktifkannya pada koleksi situs.
---

## **Penerapan**

{{% alert color="primary" %}}

**Aspose.PDF untuk SharePoint melakukan tindakan berikut selama penerapan:**
- Menginstal Aspose.PDF.SharePoint.dll ke dalam Global Assembly Cache dan menambahkan entri SafeControl ke file web.config.
- Menginstal manifest fitur dan file lain yang diperlukan ke direktori yang sesuai.
- Mendaftarkan fitur dalam database SharePoint dan membuatnya tersedia untuk aktivasi pada lingkup fitur.

{{% /alert %}}


## **Aktivasi**

{{% alert color="primary" %}}

**Aspose.PDF untuk SharePoint dikemas sebagai fitur tingkat situs (koleksi situs) dan dapat diaktifkan serta dinonaktifkan pada koleksi situs.**

{{% /alert %}}

{{% alert color="primary" %}}

Selama aktivasi, fitur ini membuat beberapa perubahan pada direktori virtual dari aplikasi web induk dari koleksi situs: Menambahkan halaman pengaturan konversi ke file sitemap.
 Salin file sumber daya yang diperlukan ke folder App_GlobalResources di direktori virtual.
 {{% /alert %}}
