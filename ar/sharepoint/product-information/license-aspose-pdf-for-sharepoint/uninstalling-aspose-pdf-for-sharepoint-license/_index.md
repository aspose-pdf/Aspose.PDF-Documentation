---
title: إلغاء تثبيت ترخيص Aspose.Pdf لـ SharePoint
linktitle: إلغاء تثبيت ترخيص Aspose.Pdf لـ SharePoint
type: docs
weight: 30
url: /ar/sharepoint/uninstalling-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: يرجى اتباع الخطوات المذكورة في هذه المقالة لإلغاء تثبيت ترخيص PDF SharePoint API.
---

## خطوات إلغاء التثبيت

{{% alert color="primary" %}}

لإلغاء تثبيت ترخيص Aspose.PDF لـ SharePoint، يرجى استخدام الخطوات أدناه من وحدة التحكم الخاصة بالخادم.

1. سحب حل الترخيص من المزرعة:

  stsadm.exe -o retractsolution -name Aspose.PDF.SharePoint.License.wsp -immediate

2. نفّذ وظائف المؤقت الإدارية لإكمال السحب فورًا:

  stsadm.exe -o execadmsvcjobs

3. انتظر حتى يكتمل السحب. يمكنك استخدام الإدارة المركزية   

  الإدارة للتحقق مما إذا كان السحب قد اكتمل تحت الإدارة المركزية -> العمليات -> إدارة الحلول

4. أزل الحل من مخزن حلول SharePoint:

  stsadm.exe -o deletesolution -name Aspose.PDF.SharePoint.License.wsp

{{% /alert %}}
