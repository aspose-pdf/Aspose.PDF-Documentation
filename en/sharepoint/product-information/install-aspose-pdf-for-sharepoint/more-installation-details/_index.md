---
title: More installation details
type: docs
weight: 30
url: /sharepoint/more-installation-details/
lastmod: "2020-12-16"
description: More information on the installation of PDF SharePoint API explains how to deploy, activate, and deactivate it on site collections.
---

## **Deployment**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint performs the following actions during deployment:**
- Install Aspose.PDF.SharePoint.dll into Global Assembly Cache and add SafeControl entry to the web.config file.
- Install feature manifest and other necessary files to the appropriate directories.
- Register the feature in the SharePoint database and make it available for the activation at the feature scope.

{{% /alert %}}


## **Activation**

{{% alert color="primary" %}}

**Aspose.PDF for SharePoint is packaged as a site (site collection) level feature and can be activated and deactivated on site collections.**

{{% /alert %}}

{{% alert color="primary" %}}

During activation, the feature makes some changes to the virtual directory of the parent web application of the site collection: Add conversion settings page to the sitemap file. Copy necessary resource files to the App_GlobalResources folder in the virtual directory.

{{% /alert %}}
