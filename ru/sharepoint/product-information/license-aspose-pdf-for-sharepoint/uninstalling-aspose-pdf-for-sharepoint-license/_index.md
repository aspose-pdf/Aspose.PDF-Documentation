---
title: Удаление лицензии Aspose.Pdf для SharePoint
linktitle: Удаление лицензии Aspose.Pdf для SharePoint
type: docs
weight: 30
url: /ru/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: Пожалуйста, следуйте указаниям в этой статье, чтобы удалить лицензию PDF SharePoint API.
---

## Шаги по удалению

{{% alert color="primary" %}}

Чтобы удалить лицензию Aspose.PDF для SharePoint, используйте указанные ниже шаги в консоли сервера.

1. Отозвать решение лицензии с фермы:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Выполните задачи административного таймера, чтобы сразу завершить откат:

  stsadm.exe -o execadmsvcjobs

3. Подождите, пока откат завершится. Вы можете использовать Central   

  Administration, чтобы проверить, завершён ли откат, в Central Administration -> Operations -> Solution Management

4. Удалите решение из хранилища решений SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
