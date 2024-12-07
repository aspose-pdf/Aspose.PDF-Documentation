---
title: Install with MSI Installer
type: docs
weight: 10
url: /reportingservices/install-with-msi-installer/
description: Learn how to install Aspose.PDF for Reporting Services using the MSI installer. A straightforward guide for quick setup.
lastmod: "2021-06-05"
---

You can install Aspose.Pdf for Reporting Services by using a MSI installer. Run Aspose.Pdf.ReportingServices.msi and follow the steps offered by the installer. Installer will copy the assembly and other files to the specified directory and install the product on the default instance of the Reporting Services. You do not need to copy or modify any files manually unless you want to add special configuration parameters as described in the 'Configure Aspose.Pdf for Reporting Services' section.

Automatic installation is the best option that works in most cases. However, you may need to install the product manually in some situations like:
 
- Automatic installation fails due to I/O security issues.
- You need to install the product on a named (not default) instance of Reporting Services 2016 or on multiple instances.
- You upgrade to the latest version and just want to replace the assembly instead of uninstalling the old version and installing the new one using MSI installer.
 
{{% alert color="primary" %}}

Note: Take notice that in the latter case you may end up with other components (such as the offline documentation) not upgraded to the corresponding version.

{{% /alert %}}
