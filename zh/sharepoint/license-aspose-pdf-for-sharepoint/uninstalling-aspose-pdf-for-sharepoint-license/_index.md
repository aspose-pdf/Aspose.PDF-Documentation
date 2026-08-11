---
title: 卸载 Aspose.PDF for SharePoint 许可证
linktitle: 卸载 Aspose.PDF for SharePoint 许可证
type: docs
weight: 30
url: /zh/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: 请按照本文中提到的步骤卸载 PDF SharePoint API 许可证。
---

## 卸载步骤

{{% alert color="primary" %}}

要卸载 Aspose.PDF for SharePoint 许可证，请从服务器控制台执行以下步骤。

1. 从场中撤回许可证解决方案：

  stsadm.exe -o 收缩解决方案 -name Aspose.PDF.SharePoint.License.wsp -immediate

2. 执行管理计时器作业以立即完成撤回：

  stsadm.exe -o execadmsvcjobs

3. 等待撤回完成。您可以使用中央

  管理可在管理中心 -> 操作 -> 解决方案管理下检查撤回是否完成

4. 从 SharePoint 解决方案存储中删除解决方案：

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
