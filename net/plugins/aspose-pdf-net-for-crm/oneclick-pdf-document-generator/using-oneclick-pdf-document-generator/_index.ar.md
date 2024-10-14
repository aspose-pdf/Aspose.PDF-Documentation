---
title: استخدام مولد مستندات PDF بنقرة واحدة
type: docs
weight: 10
url: /net/using-oneclick-pdf-document-generator/
description: تعلم كيفية استخدام مولد مستندات PDF بنقرة واحدة في Microsoft Dynamics
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## إنشاء قالب وإضافته في CRM

- افتح وورد وأنشئ قالبًا.
- أدخل حقول MailMerge للبيانات القادمة من CRM.

![أدخل حقول MailMerge](using-oneclick-pdf-document-generator_1.png)

- تأكد من أن اسم الحقل يطابق تمامًا مع حقل CRM.
- القوالب مخصصة للاستخدام مع كيان فردي.

![قالب توضيحي](using-oneclick-pdf-document-generator_2.png)

- بمجرد إنشاء القالب، افتح كيان تكوين PDF بنقرة واحدة في CRM وأنشئ سجلًا جديدًا.
- أعط اسم القالب، حدد الكيان الذي تم تعريف القالب من أجله وأرفق المستند المُنشأ في المرفق.

![اختر القالب](using-oneclick-pdf-document-generator_3.png)

## إنشاء مستند من زر الشريط

- افتح السجل حيث تريد إنشاء المستند.
- افتح السجل حيث تريد توليد المستند.
- انقر على زر OneClick PDF من الشريط.

![انقر على OneClick PDF](using-oneclick-pdf-document-generator_4.png)

- من النافذة المنبثقة: اختر القالب، اسم الملف والإجراء ثم انقر على توليد.
- تحقق من الملف المحمل أو الملاحظات، بناءً على الاختيار.

## تهيئة أزرار OneClick واستخدامها

- لاستخدام زر OneClick مباشرة من النموذج، افتح تخصيص النموذج.
- أدخل WebResource حيث تريد إضافة أزرار OneClick.
- اختر OpenButtonPage في WebResource وقم بتسميته.
- قم بتكوين الأزرار في حقل البيانات في العينة التالية.

![خصائص WebResource](using-oneclick-pdf-document-generator_5.png)

- استخدم سطر منفصل لكل زر واستخدم الصياغة التالية:
  - الصياغة:اسم القالب |<الإجراء: تحميل/ملاحظة>|اسم الملف الناتج
  - مثال:Demo|Download|My Downloaded File
- احفظ وانشر التخصيص.
- الزر متاح على النموذج.

![الزر متاح على النموذج](using-oneclick-pdf-document-generator_6.png)
![الزر متوفر في النموذج](using-oneclick-pdf-document-generator_6.png)
