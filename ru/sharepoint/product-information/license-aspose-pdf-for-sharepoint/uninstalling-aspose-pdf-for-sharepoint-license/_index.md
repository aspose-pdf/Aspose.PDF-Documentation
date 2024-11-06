---
title: Удаление лицензии Aspose.Pdf для SharePoint
type: docs
weight: 30
url: ru/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: Пожалуйста, выполните шаги, указанные в этой статье, чтобы удалить лицензию PDF SharePoint API.
---

## Шаги удаления

{{% alert color="primary" %}}

Чтобы удалить лицензию Aspose.PDF для SharePoint, выполните следующие шаги с консоли сервера.

1. Извлеките решение с лицензией из фермы:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. Выполните административные задания таймера, чтобы завершить извлечение немедленно:

  stsadm.exe -o execadmsvcjobs

3. Подождите, пока извлечение не завершится. Вы можете использовать Центр   

  администрирования, чтобы проверить, завершилось ли извлечение, в разделе Центр администрирования -> Операции -> Управление решениями

4. Удалите решение из хранилища решений SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}