---
title: إلغاء تثبيت ترخيص Aspose.Pdf لـ SharePoint
type: docs
weight: 30
url: /sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: يرجى اتباع الخطوات المذكورة في هذه المقالة لإلغاء تثبيت ترخيص PDF SharePoint API.
---

## خطوات إلغاء التثبيت

{{% alert color="primary" %}}

لإلغاء تثبيت ترخيص Aspose.PDF لـ SharePoint، يرجى استخدام الخطوات التالية من وحدة تحكم الخادم.

1. سحب حل الترخيص من المزرعة:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. تنفيذ وظائف المؤقت الإدارية لإكمال السحب فورًا:

  stsadm.exe -o execadmsvcjobs

3. انتظر حتى يكتمل السحب. يمكنك استخدام الإدارة المركزية للتحقق مما إذا كانت عملية السحب قد اكتملت تحت الإدارة المركزية -> العمليات -> إدارة الحلول

4. إزالة الحل من مخزن حلول SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}