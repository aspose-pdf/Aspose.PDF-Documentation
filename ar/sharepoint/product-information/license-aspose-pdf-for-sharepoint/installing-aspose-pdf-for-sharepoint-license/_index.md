---
title: تثبيت ترخيص Aspose.Pdf لـ SharePoint
linktitle: تثبيت ترخيص Aspose.Pdf لـ SharePoint
type: docs
weight: 10
url: /ar/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2026-06-18"
description: بمجرد أن تكون راضيًا عن تقييمك، يمكنك شراء ترخيص لواجهة برمجة تطبيقات PDF SharePoint واتباع تعليمات التثبيت لتطبيقه.
---

{{% alert color="primary" %}}

بمجرد أن تكون راضيًا عن تقييمك، يمكنك [شراء ترخيص](https://purchase.aspose.com/buy). قبل الشراء تأكد من أنك تفهم وتوافق على شروط اشتراك الترخيص.

{{% /alert %}}

{{% alert color="primary" %}}

سيتم إرسال الترخيص إليك عبر البريد الإلكتروني بعد دفع الطلب. الترخيص هو أرشيف .zip يحتوي على حزمة حل SharePoint عادية.

هذا الأرشيف يحتوي على:

- Aspose.PDF.SharePoint.License.wsp

ملف حزمة حل SharePoint. تم حزم ترخيص Aspose.PDF for SharePoint كحل SharePoint لتسهيل النشر/الإزالة عبر مجموعة الخوادم.

- readme.txt

تعليمات تثبيت الترخيص. يتم تثبيت الترخيص من وحدة تحكم الخادم عبر stsadm.exe. الخطوات المطلوبة لتثبيت الترخيص موضحة أدناه.

**ملاحظة:** تم حذف المسارات للتوضيح. قد تحتاج إلى إضافة المسار الفعلي إلى stsadm.exe و/أو ملف الحل عند تنفيذها.

1. قم بتشغيل stsadm لإضافة الحل إلى مخزن حلول SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. نشر الحل على جميع الخوادم في المزرعة:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. نفّذ وظائف المؤقت الإدارية لإكمال النشر فورًا.

stsadm.exe -o execadmsvcjobs

**ملاحظة:** ستتلقى تحذيرًا عند تشغيل خطوة النشر إذا لم يتم تشغيل خدمة إدارة خدمات Windows SharePoint. يعتمد Stsadm.exe على هذه الخدمة وخدمة مؤقت Windows SharePoint لتكرار بيانات الحل عبر المزرعة. إذا لم تكن هذه الخدمات قيد التشغيل في مزرعة الخوادم لديك، قد تحتاج إلى نشر الترخيص على كل خادم.


{{% /alert %}}
