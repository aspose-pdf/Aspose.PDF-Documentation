---
title: Installing Aspose.Pdf for SharePoint License
type: docs
weight: 10
url: /sharepoint/installing-aspose-pdf-for-sharepoint-license/
lastmod: "2020-12-16"
description: بمجرد أن تكون راضيًا عن تقييمك، يمكنك شراء ترخيص لواجهة برمجة تطبيقات PDF SharePoint واتباع تعليمات التثبيت لتطبيقه.
---

{{% alert color="primary" %}}

بمجرد أن تكون راضيًا عن تقييمك، يمكنك [شراء ترخيص](https://purchase.aspose.com/buy). قبل الشراء، تأكد من أنك تفهم وتوافق على شروط اشتراك الترخيص.

{{% /alert %}}

{{% alert color="primary" %}}

سيتم إرسال الترخيص إليك عبر البريد الإلكتروني بعد دفع الطلب. الترخيص هو أرشيف .zip يحتوي على حزمة حل SharePoint عادية.
{{% /alert %}}

يحتوي هذا الأرشيف على:

- Aspose.PDF.SharePoint.License.wsp

ملف حزمة حل SharePoint. يتم تعبئة Aspose.PDF لترخيص SharePoint كحل SharePoint لتسهيل النشر/الانسحاب عبر مزرعة الخادم.

- readme.txt

تعليمات تثبيت الترخيص.
 تتم عملية تثبيت الترخيص من وحدة التحكم في الخادم عبر stsadm.exe. يتم توضيح الخطوات المطلوبة لتثبيت الترخيص أدناه.

**ملاحظة:** تم حذف المسارات للتوضيح. قد تحتاج إلى إضافة المسار الفعلي إلى stsadm.exe و/أو ملف الحل عند تنفيذها.

1. قم بتشغيل stsadm لإضافة الحل إلى متجر حلول SharePoint:

stsadm.exe -o addsolution -filename Aspose.PDF.SharePoint.License.wsp

2. قم بنشر الحل إلى جميع الخوادم في المزرعة:

stsadm.exe -o deploysolution -name Aspose.PDF.SharePoint.License.wsp -immediate -force

3. نفذ وظائف المؤقت الإدارية لإكمال النشر فوراً.

stsadm.exe -o execadmsvcjobs

**ملاحظة:** ستتلقى تحذيراً عند تشغيل خطوة النشر إذا لم يتم بدء خدمة إدارة خدمات Windows SharePoint. يعتمد stsadm.exe على هذه الخدمة وخدمة Windows SharePoint Timer لتكرار بيانات الحل عبر المزرعة. إذا لم تكن هذه الخدمات قيد التشغيل في مزرعة الخوادم الخاصة بك، فقد تحتاج إلى نشر الترخيص على كل خادم.