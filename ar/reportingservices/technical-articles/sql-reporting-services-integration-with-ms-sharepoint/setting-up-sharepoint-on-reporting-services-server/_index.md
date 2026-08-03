---
title: إعداد SharePoint على خادم خدمات التقارير
linktitle: إعداد SharePoint على خادم خدمات التقارير
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

نحن الآن بحاجة إلى تنفيذ خطوات مماثلة كما فعلنا مع SharePoint WFE. أول شيء هو إجراء تثبيت Prereq uisites وبمجرد الانتهاء من ذلك، قم ببدء تشغيل إعداد SharePoint.

{{% /alert %}}

بالنسبة للإعداد، اخترت Server Farm وتثبيتًا كاملاً ليتوافق مع SharePoint Box الخاص بي، حيث لا أريد تثبيتًا مستقلاً لـ SharePoint.

## تكوين شيربوينت

{{% alert color="primary" %}}

**في معالج تكوين SharePoint، نريد الاتصال بمزرعة موجودة.**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_1.png)

**الصورة1:- معالج تكوين SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**سنقوم بعد ذلك بتوجيهه إلى قاعدة بيانات SharePoint_Config التي تستخدمها مزرعتنا. إذا كنت لا تعرف مكان ذلك، فيمكنك معرفة ذلك من خلال الإدارة المركزية من خلال إعدادات النظام -> خوادم المدير في هذه المزرعة.**

![SharePoint Configuration Database](setting-up-sharepoint-on-reporting-services-server_2.png)

**الصورة2:- تحديد إعدادات تكوين قاعدة البيانات**

![SharePoint Configuration Wizard](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- معالج تكوين SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**بمجرد الانتهاء من المعالج، فهذا هو كل ما يتعين علينا القيام به في مربع خادم التقارير في الوقت الحالي. بالعودة إلى عنوان URL الخاص بـ ReportServer، سنرى خطأً آخر، ولكن ذلك لأننا لم نقم بتكوينه من خلال المسؤول المركزي.**

![SharePoint Configuration Error](setting-up-sharepoint-on-reporting-services-server_4.png)

**الصورة4:- الإبلاغ عن خطأ في الخادم**
{{% /alert %}}
