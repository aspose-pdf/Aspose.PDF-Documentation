---
title: 卸载 Aspose.Pdf for SharePoint License
type: docs
weight: 30
url: zh/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 请按照本文中提到的步骤卸载 PDF SharePoint API 许可证。
---

## 卸载步骤

{{% alert color="primary" %}}

要卸载 Aspose.PDF for SharePoint 许可证，请从服务器控制台使用以下步骤。

1. 从场中撤回许可证解决方案：

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 执行管理计时器作业以立即完成撤回：

  stsadm.exe -o execadmsvcjobs

3. 等待撤回完成。您可以使用中央管理来检查撤回是否已在中央管理 -> 操作 -> 解决方案管理下完成

4. 从 SharePoint 解决方案存储中删除解决方案：

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}