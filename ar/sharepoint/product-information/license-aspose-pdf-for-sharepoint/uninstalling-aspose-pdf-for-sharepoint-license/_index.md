---
title: إلغاء تثبيت Aspose.PDF لترخيص SharePoint
linktitle: إلغاء تثبيت Aspose.PDF لترخيص SharePoint
type: docs
weight: 30
url: /ar/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: يرجى اتباع الخطوات المذكورة في هذه المقالة لإلغاء تثبيت ترخيص PDF SharePoint API.
---

## خطوات إلغاء التثبيت

{{% alert color="primary" %}}

لإلغاء تثبيت Aspose.PDF لترخيص SharePoint، يرجى استخدام الخطوات أدناه من وحدة تحكم الخادم.

1. سحب حل الترخيص من المزرعة:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. قم بتنفيذ مهام المؤقت الإداري لإكمال عملية السحب على الفور:

  stsadm.exe -o execadmsvcjobs

3. انتظر حتى يكتمل التراجع. يمكنك استخدام المركزية

  Administration to check if the retraction completed under Central Administration -> Operations -> Solution Management

4. قم بإزالة الحل من مخزن حلول SharePoint:

  stsadm.exe -o حذف الحل -اسم Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
