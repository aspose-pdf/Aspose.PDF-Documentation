---
title: Uninstalling Aspose.PDF for SharePoint License
linktitle: 卸载 Aspose.PDF for SharePoint 许可证
type: docs
weight: 30
url: /zh/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Please follow the steps mentioned in this article to uninstall PDF SharePoint API License.
---

## Uninstallation Steps

{{% alert color="primary" %}}

要卸载 Aspose.PDF for SharePoint 许可证，请从服务器控制台执行以下步骤。

1. 从场中撤回许可证解决方案：

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Execute administrative timer jobs to complete the retraction immediately:

  stsadm.exe -o execadmsvcjobs

3. Wait for the retraction to complete. You can use Central   

  Administration to check if the retraction completed under Central Administration -> Operations -> Solution Management

4. 从 SharePoint 解决方案存储中删除解决方案：

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

