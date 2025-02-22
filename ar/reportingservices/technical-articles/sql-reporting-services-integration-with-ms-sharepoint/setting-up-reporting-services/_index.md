---
title: إعداد خدمات التقارير
type: docs
weight: 20
url: /ar/reportingservices/setting-up-reporting-services/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

محطتنا الأولى في خادم خدمات التقارير هي مدير تكوين خدمات التقارير.

{{% /alert %}}

## حساب الخدمة:

**تأكد من فهم حساب الخدمة الذي تستخدمه لخدمات التقارير. إذا واجهنا مشكلات، قد تكون متعلقة بحساب الخدمة الذي تستخدمه. الافتراضي هو خدمة الشبكة. عندما نذهب لنشر إصدارات جديدة، نستخدم دائماً حسابات المجال، لأن ذلك هو المكان الذي من المرجح أن نواجه فيه مشكلات. في هذه الحالة من الخادم، استخدمنا حساب مجال يسمى RSService.**

![todo:image_alt_text](setting-up-reporting-services_1.png)

**صورة1:- إعداد حساب الخدمة**

## عنوان ويب للخدمة:

{{% alert color="primary" %}}

**سنحتاج إلى تكوين عنوان ويب للخدمة. هذا هو الدليل الافتراضي ReportServer (vdir) الذي يستضيف خدمات الويب التي تستخدمها خدمات التقارير، والذي ستتواصل معه SharePoint. ما لم تكن ترغب في تخصيص خصائص vdir (مثل SSL، المنافذ، رؤوس المضيف، إلخ...)، يجب أن تكون قادرًا على النقر فوق تطبيق هنا وأن تكون جاهزًا للانطلاق.**
![todo:image_alt_text](setting-up-reporting-services_2.png)

**الصورة 2:- إعداد عنوان URL لخدمة الويب بمجرد إعداد عنوان URL لخدمة الويب، يجب أن تكون قادرًا على رؤية النتائج التالية**

![todo:image_alt_text](setting-up-reporting-services_3.png)

**الصورة 3:- الإعداد الناجح لعنوان URL لخدمة الويب**
{{% /alert %}}

## قاعدة البيانات:

**نحتاج إلى إنشاء قاعدة بيانات كتالوج خدمات التقارير. يمكن وضع هذا على أي محرك قاعدة بيانات SQL 2008 أو SQL 2008 R2. سيعمل SQL11 بشكل جيد أيضًا، ولكنه لا يزال في المرحلة التجريبية. ستقوم هذه العملية بإنشاء قاعدتي بيانات، ReportServer وReportServerTempDB، بشكل افتراضي.**

{{% alert color="primary" %}}
**الخطوة المهمة الأخرى في هذا هي التأكد من اختيار SharePoint Integrated لنوع قاعدة البيانات. 
بمجرد اتخاذ هذا الاختيار، لا يمكن تغييره.**

![todo:image_alt_text](setting-up-reporting-services_4.png)

**صورة 4:- إنشاء قاعدة بيانات خادم التقرير**

![todo:image_alt_text](setting-up-reporting-services_5.png)

**صورة 5:- إعداد خادم قاعدة البيانات ونوع المصادقة**

![todo:image_alt_text](setting-up-reporting-services_6.png)

**صورة 6:- إعداد اسم قاعدة البيانات والوضع**
{{% /alert %}}

**بالنسبة لأوراق الاعتماد، هكذا سيتواصل خادم التقرير مع خادم SQL. أي حساب تختاره، سيمنح حقوق معينة داخل قاعدة بيانات الكتالوج وكذلك بعض قواعد بيانات النظام عبر RSExecRole. MSDB هي واحدة من هذه القواعد للاستخدام في الاشتراك حيث نستخدم SQL Agent.**

![todo:image_alt_text](setting-up-reporting-services_7.png)

**صورة 7:- إعداد بيانات اعتماد قاعدة بيانات خادم التقرير**

{{% alert color="primary" %}}

**بمجرد تحديد بيانات اعتماد قاعدة البيانات، يجب أن نكون قادرين على الحصول على النتائج كما هو محدد أدناه.**


![todo:image_alt_text](setting-up-reporting-services_8.png)

**الصورة 8:- تقدم إنشاء قاعدة بيانات خادم التقارير**

![todo:image_alt_text](setting-up-reporting-services_9.png)

**الصورة 9:- ملخص إتمام قاعدة بيانات خادم التقارير**
{{% /alert %}}

## عنوان URL الخاص بمدير التقارير:

**يمكننا تخطي عنوان URL الخاص بمدير التقارير لأنه لا يُستخدم عندما نكون في وضع التكامل مع SharePoint. SharePoint هو واجهتنا الأمامية. مدير التقارير لا يعمل.**

## مفاتيح التشفير:

{{% alert color="primary" %}}
**قم بعمل نسخة احتياطية من مفاتيح التشفير الخاصة بك وتأكد من أنك تعرف مكان الاحتفاظ بها. إذا واجهت موقفًا حيث تحتاج إلى نقل قاعدة البيانات أو استعادتها، ستحتاج إلى هذه المفاتيح.**

![todo:image_alt_text](setting-up-reporting-services_10.png)

**الصورة 10:- النسخ الاحتياطي لمفتاح تشفير خادم التقارير**
{{% /alert %}}

{{% alert color="primary" %}}
**تهانينا! لقد قمنا بتكوين خدمات التقارير بنجاح باستخدام مدير التكوين. إذا قمت بتصفح عنوان URL في علامة التبويب الخاصة بعنوان URL لخدمة الويب، يجب أن يظهر شيء مشابه لما يلي.**

![todo:image_alt_text](setting-up-reporting-services_11.png)

**Image11:- Report Server access after installation**

**سبب الخطأ: تم تثبيت SharePoint على WFE لدينا وانتهينا من إعداد خدمات التقارير. في هذا المثال، توجد خدمات التقارير وSharePoint على أجهزة مختلفة. إذا كانت على نفس الجهاز، فلن ترى هذا الخطأ. نحن بحاجة تقنيًا لتثبيت SharePoint على صندوق RS. وهذا يعني أنه سيتم تمكين IIS كذلك.**
{{% /alert %}}
