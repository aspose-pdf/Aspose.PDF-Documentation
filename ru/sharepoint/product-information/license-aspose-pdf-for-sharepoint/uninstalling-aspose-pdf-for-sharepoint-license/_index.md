---
title: Удаление лицензии Aspose.PDF для SharePoint
linktitle: Удаление лицензии Aspose.PDF для SharePoint
type: docs
weight: 30
url: /ru/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-08-13"
description: Выполните действия, описанные в этой статье, чтобы удалить лицензию PDF SharePoint API.
---

## Шаги удаления

{{% alert color="primary" %}}

Чтобы удалить лицензию Aspose.PDF for SharePoint, выполните следующие действия из консоли сервера.

1. Отзовите лицензионное решение из фермы:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Выполните задания административного таймера, чтобы немедленно завершить отзыв:

  stsadm.exe -o execadmsvcjobs

3. Подождите, пока отвод завершится. Вы можете использовать Центральный   

  Администрация должна проверить, завершен ли отзыв, в разделе «Центр администрирования» -> «Операции» -> «Управление решениями».

4. Удалите решение из хранилища решений SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}

