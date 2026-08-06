---
title: تثبيت Aspose.PDF لترخيص SharePoint
linktitle: تثبيت Aspose.PDF لترخيص SharePoint
type: docs
weight: 10
url: /ar/sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: بمجرد أن تصبح راضيًا عن تقييمك، يمكنك شراء ترخيص لـ PDF SharePoint API واتباع تعليمات التثبيت لتطبيقه.
---

{{% alert color="primary" %}}

بمجرد أن تصبح راضيًا عن تقييمك، يمكنك [شراء ترخيص](https://purchase.aspose.com/buy). قبل الشراء، تأكد من أنك تفهم شروط الاشتراك في الترخيص وتوافق عليها.

{{% /alert %}}

{{% alert color="primary" %}}

سيتم إرسال الترخيص إليك عبر البريد الإلكتروني بعد دفع الطلب. الترخيص عبارة عن أرشيف بتنسيق .zip يحتوي على حزمة حلول SharePoint عادية.

يحتوي هذا الأرشيف على:

- Aspose.PDF.SharePoint.License.wsp

ملف حزمة حلول SharePoint. يتم حزم Aspose.PDF لترخيص SharePoint كحل SharePoint لتسهيل النشر/السحب عبر مجموعة الخوادم.

- readme.txt

تعليمات تثبيت الترخيص. يتم إجراء تثبيت الترخيص من وحدة تحكم الخادم عبر stsadm.exe. الخطوات المطلوبة لتثبيت الترخيص موضحة أدناه.

**ملاحظة:** تم حذف المسارات من أجل الوضوح. قد تحتاج إلى إضافة المسار الفعلي إلى ملف stsadm.exe و/أو ملف الحل عند تنفيذها.

1. قم بتشغيل stsadm لإضافة الحل إلى مخزن حلول SharePoint:

stsadm.exe -o addsolution -اسم الملف Aspose.PDF.SharePoint.License.wsp

2. نشر الحل على كافة الخوادم في المزرعة:

stsadm.exe -o Publishsolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. قم بتنفيذ مهام المؤقت الإداري لإكمال النشر على الفور.

stsadm.exe -o execadmsvcjobs

**ملاحظة:** ستتلقى تحذيرًا عند تشغيل خطوة النشر إذا لم يتم بدء تشغيل خدمة إدارة Windows SharePoint Services. يعتمد Stsadm.exe على هذه الخدمة وWindows SharePoint Timer Service لنسخ بيانات الحل عبر المزرعة. إذا لم تكن هذه الخدمات قيد التشغيل في مجموعة الخوادم الخاصة بك، فقد تحتاج إلى نشر الترخيص على كل خادم.

{{% /alert %}}

