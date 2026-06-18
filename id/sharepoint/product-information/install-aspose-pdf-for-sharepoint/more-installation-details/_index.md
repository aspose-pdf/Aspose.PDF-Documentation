---
title: Detail instalasi lebih lanjut
linktitle: Detail instalasi lebih lanjut
type: docs
weight: 30
url: /id/sharepoint/more-installation-details/
lastmod: "2026-06-18"
description: Informasi lebih lanjut tentang instalasi PDF SharePoint API menjelaskan cara menyebarkan, mengaktifkan, dan menonaktifkannya pada koleksi situs.
---

## **Penyebaran**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint melakukan tindakan berikut selama penyebaran:**
- Instal Aspose.PDF.SharePoint.dll ke Global Assembly Cache dan tambahkan entri SafeControl ke file web.config.
- Instal manifest fitur dan file lain yang diperlukan ke direktori yang sesuai.
- Daftarkan fitur di database SharePoint dan buat tersedia untuk aktivasi pada ruang lingkup fitur.

{{% /alert %}}


## **Aktivasi**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint dikemas sebagai fitur tingkat situs (koleksi situs) dan dapat diaktifkan serta dinonaktifkan pada koleksi situs.**

{{% /alert %}}

{{% alert color="primary" %}}

Selama aktivasi, fitur membuat beberapa perubahan pada direktori virtual dari aplikasi web induk koleksi situs: Tambahkan halaman pengaturan konversi ke file sitemap. Salin file sumber daya yang diperlukan ke folder App_GlobalResources di direktori virtual.

{{% /alert %}}
