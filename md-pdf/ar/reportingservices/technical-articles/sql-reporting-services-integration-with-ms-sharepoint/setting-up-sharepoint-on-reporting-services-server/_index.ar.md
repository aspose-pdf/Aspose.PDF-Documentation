---
title: إعداد SharePoint على خادم خدمات التقارير
type: docs
weight: 30
url: /reportingservices/setting-up-sharepoint-on-reporting-services-server/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

الآن نحتاج إلى تنفيذ خطوات مشابهة كما فعلنا مع WFE SharePoint. أول شيء هو المرور بتثبيت المتطلبات المسبقة وبمجرد الانتهاء، بدء إعداد SharePoint.

{{% /alert %}}

لإعداد SharePoint اخترت Server Farm وتثبيت كامل ليتناسب مع صندوق SharePoint الخاص بي، حيث لا أريد تثبيتًا مستقلًا لـ SharePoint.

## تكوين SharePoint

{{% alert color="primary" %}}

**في معالج تكوين SharePoint، نريد الاتصال بمزرعة موجودة.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_1.png)

**الصورة 1:- معالج تكوين SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**ثم سنوجهه إلى قاعدة بيانات SharePoint_Config التي تستخدمها مزرعتنا.**
``` ```
إذا لم تكن تعرف مكان هذا، يمكنك معرفة ذلك من خلال الإدارة المركزية عبر إعدادات النظام -> إدارة الخوادم في هذه المزرعة.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_2.png)

**الصورة 2:- تحديد إعدادات تكوين قاعدة البيانات**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_3.png)

**الصورة 3:- معالج تكوين SharePoint**
{{% /alert %}}

{{% alert color="primary" %}}

**بمجرد الانتهاء من المعالج، هذا كل ما نحتاج إلى القيام به على صندوق خادم التقارير في الوقت الحالي. عند العودة إلى عنوان URL الخاص بـ ReportServer، سنرى خطأ آخر، ولكن ذلك لأننا لم نقم بتكوينه عبر الإدارة المركزية.**

![todo:image_alt_text](setting-up-sharepoint-on-reporting-services-server_4.png)

**الصورة 4:- خطأ في خادم التقارير**
{{% /alert %}}
```