---
title: إعداد خدمات التقارير
linktitle: إعداد خدمات التقارير
type: docs
weight: 20
url: /ar/reportingservices/setting-up-reporting-services/
lastmod: "2026-06-19"
---

{{% alert color="primary" %}}

محطتنا الأولى على خادم خدمات التقارير هي مدير تكوين خدمات التقارير.

{{% /alert %}}

## حساب الخدمة:

**تأكد من فهم حساب الخدمة الذي تستخدمه لخدمات الإبلاغ. إذا واجهنا مشكلات، قد تكون مرتبطة بحساب الخدمة الذي تستخدمه. الافتراضي هو Network Service. عند نشر بنى جديدة، نستخدم دائمًا حسابات المجال، لأن هذا هو المكان الذي قد نواجه فيه مشاكل. لهذا الخادم، استخدمنا حساب مجال يدعى RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**Image1:- إعداد حساب الخدمة**

## عنوان URL لخدمة الويب:

{{% alert color="primary" %}}

**سيتعين علينا تكوين Web Service URL. هذا هو الدليل الافتراضي ReportServer (vdir) الذي يستضيف Web Services التي يستخدمها Reporting Services، وهو ما سيتواصل معه SharePoint. ما لم ترغب في تخصيص خصائص vdir (مثل SSL، المنافذ، رؤوس المضيف، إلخ…) ، يجب أن تكون قادرًا على النقر على Apply هنا والبدء مباشرة.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**Image2:- إعداد Web Service URL بمجرد إعداد Web Service URL، ينبغي أن تكون قادرًا على رؤية النتائج التالية**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**Image3:- تم إعداد Web Service URL بنجاح**
{{% /alert %}}

## قاعدة البيانات:

**نحتاج إلى إنشاء قاعدة بيانات كاتالوج خدمات التقارير. يمكن وضعها على أي محرك قاعدة بيانات SQL 2008 أو SQL 2008 R2. سيعمل SQL11 أيضاً بشكل جيد، لكنه لا يزال في مرحلة التجربة (BETA). سيقوم هذا الإجراء بإنشاء قاعدة بياناتين، ReportServer و ReportServerTempDB، بشكل افتراضي.**

{{% alert color="primary" %}}
**الخطوة المهمة الأخرى هي التأكد من اختيار SharePoint Integrated كنمط قاعدة البيانات. بمجرد اتخاذ هذا الاختيار، لا يمكن تغييره.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**Image4:- إنشاء قاعدة بيانات خادم التقارير**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**Image5:- إعداد خادم قاعدة البيانات ونوع المصادقة**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**Image6:- إعداد اسم قاعدة البيانات والوضع**
{{% /alert %}}

**بالنسبة لبيانات الاعتماد، هذه هي الطريقة التي سيقوم بها خادم التقارير بالتواصل مع خادم SQL. أي حساب تختاره سيُمنح بعض الحقوق داخل قاعدة البيانات Catalog وكذلك بعض قواعد البيانات النظامية عبر دور RSExecRole. قاعدة البيانات MSDB هي إحدى هذه القواعد لاستخدام الاشتراكات حيث نستخدم وكيل SQL.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**Image7:- إعداد بيانات اعتماد قاعدة بيانات خادم التقارير**

{{% alert color="primary" %}}

**بمجرد تحديد بيانات اعتماد قاعدة البيانات، يجب أن نكون قادرين على الحصول على النتائج كما هو موضح أدناه.**

![todo:image_alt_text](setting-up-reporting-services_8.png)

**Image8:- تقدم إنشاء قاعدة بيانات خادم التقارير**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**Image9:- ملخص اكتمال قاعدة بيانات خادم التقارير**
{{% /alert %}}

## عنوان URL لمدير التقارير:

**يمكننا تخطي عنوان URL لمدير التقارير لأنه غير مستخدم عندما نكون في وضع SharePoint المتكامل. SharePoint هو الواجهة الأمامية لنا. مدير التقارير لا يعمل.**

## مفاتيح التشفير:

{{% alert color="primary" %}}
**قم بعمل نسخة احتياطية من مفاتيح التشفير وتأكد من معرفتك لمكان حفظها. إذا وجدت نفسك في موقف تحتاج فيه إلى ترحيل قاعدة البيانات أو استعادتها، ستحتاج إلى هذه المفاتيح.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**Image10:- نسخة احتياطية لمفتاح تشفير خادم التقارير**
{{% /alert %}}

{{% alert color="primary" %}}
**تهانينا! لقد قمنا بتكوين خدمات التقارير بنجاح باستخدام مدير التكوين. إذا انتقلت إلى العنوان URL في تبويب عنوان خدمة الويب، يجب أن يظهر شيء مشابه لما يلي.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- وصول خادم التقرير بعد التثبيت**

**سبب الخطأ: تم تثبيت SharePoint على وحدة WFE لدينا وقد انتهينا من إعداد خدمات التقارير. في هذا المثال، خدمات التقارير وSharePoint على أجهزة مختلفة. إذا كانا على نفس الجهاز، لما رأيت هذا الخطأ. نحن بحاجة تقنياً إلى تثبيت SharePoint على صندوق RS. وهذا يعني أن IIS سيفعل أيضًا.**
{{% /alert %}}


