---
title: Detail instalasi lebih lanjut
linktitle: Detail instalasi lebih lanjut
type: docs
weight: 30
url: /id/sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: More information on the installation of PDF SharePoint API explains how to deploy, activate, and deactivate it on site collections.
---

## Deployment

{{% alert color="primary" %}}

**Aspose.PDF untuk SharePoint melakukan tindakan berikut selama penerapan:**
- Install Aspose.PDF.SharePoint.dll into Global Assembly Cache and add SafeControl entry to the web.config file.
- Instal manifes fitur dan file lain yang diperlukan ke direktori yang sesuai.
- Daftarkan fitur di database SharePoint dan sediakan untuk aktivasi di cakupan fitur.

{{% /alert %}}

## Pengaktifan

{{% alert color="primary" %}}

**Aspose.PDF untuk SharePoint dikemas sebagai fitur tingkat situs (kumpulan situs) dan dapat diaktifkan dan dinonaktifkan pada kumpulan situs.**

{{% /alert %}}

{{% alert color="primary" %}}

During activation, the feature makes some changes to the virtual directory of the parent web application of the site collection: Add conversion settings page to the sitemap file. Copy necessary resource files to the App_GlobalResources folder in the virtual directory.

{{% /alert %}}

