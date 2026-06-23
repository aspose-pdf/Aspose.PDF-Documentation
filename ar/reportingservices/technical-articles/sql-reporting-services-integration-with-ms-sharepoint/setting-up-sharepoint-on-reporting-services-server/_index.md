---
title: إعداد SharePoint على خادم خدمات التقارير
linktitle: إعداد SharePoint على خادم خدمات التقارير
type: docs
weight: 30
url: /ar/reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

الآن نحتاج إلى تنفيذ خطوات مماثلة لتلك التي قمنا بها لـ SharePoint WFE. أول شيء هو المرور عبر تثبيت Prereq uisites وبمجرد الانتهاء، تشغيل إعداد SharePoint.

{{% /alert %}}

لإعداد النظام أختار Server Farm وتثبيتًا كاملًا لمطابقة صندوق SharePoint الخاص بي، حيث لا أرغب في تثبيت مستقل لـ SharePoint.

## تكوين SharePoint

{{% alert color="primary" %}}

**في معالج تكوين SharePoint، نريد الاتصال بمزرعة موجودة.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**Image1:- معالج تكوين SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**سنقوم بعد ذلك بتوجيهه إلى قاعدة بيانات SharePoint_Config التي تستخدمها مزرعتنا. إذا لم تكن تعرف مكانها، يمكنك اكتشاف ذلك عبر الإدارة المركزية من خلال إعدادات النظام -> إدارة الخوادم في هذه المزرعة.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**Image2:- تحديد إعدادات تكوين قاعدة البيانات**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**Image3:- معالج تكوين SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**بمجرد الانتهاء من المعالج، هذا كل ما نحتاج إلى القيام به على صندوق خادم التقرير الآن. بالعودة إلى عنوان URL لخادم التقرير، سنرى خطأ آخر، لكن ذلك لأننا لم نقم بتكوينه عبر المسؤول المركزي.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**Image4:- خطأ خادم التقرير**
{{% /alert %}}

