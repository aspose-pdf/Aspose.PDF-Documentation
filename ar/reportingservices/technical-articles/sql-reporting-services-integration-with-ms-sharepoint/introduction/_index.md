---
title: مقدمة
linktitle: مقدمة
type: docs
weight: 10
url: /reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF for Reporting Services has been very remarkable for PDF generation through SQL Reporting Services since many years and it provides diverse configuration and parameterization options which are not supported by default in SQL Reporting Services. Recently we have received some requested regarding Aspose.PDF for Reporting Services Integration with SharePoint. For this article, we are going to focus on MS SharePoint 2010. Before we proceed further, we assume that you already have a SharePoint Farm setup. In this example we are going to use full SharePoint Cloud. However the steps are similar for SharePoint Foundation Server.

{{% /alert %}}

{{% alert color="primary" %}}

Before we proceed further, let's take a look over reference topics that we have consulted during the preparation of this article.

- [نظرة عامة على خدمات التقارير وتكامل تكنولوجيا SharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
- [طبولوجيا النشر لخدمات التقارير في وضع SharePoint المتكامل](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## Environment Setup

يتكون الإعداد الخارجي من 4 خوادم. وهو يشتمل على وحدة تحكم المجال وSQL Server وSharePoint Server وخادم لخدمات التقارير. يمكنك اختيار وجود SharePoint وReporting Services في نفس المربع، مما سيبسط الأمر قليلاً وسأشير إلى بعض الاختلافات.

## متطلبات التثبيت المسبقة

{{% alert color="primary" %}}

تعد الوظيفة الإضافية لخدمات التقارير لـ SharePoint أحد المكونات الأساسية لتشغيل التكامل بشكل صحيح. يجب تثبيت الوظيفة الإضافية على أي من واجهات الويب الأمامية (WFE) الموجودة في مزرعة SharePoint الخاصة بك بالإضافة إلى خادم الإدارة المركزية. أحد التغييرات الجديدة في SQL 2008 R2 وSharePoint 2010 هو أن الوظيفة الإضافية 2008 R2 أصبحت الآن شرطًا أساسيًا لتثبيت SharePoint. وهذا يعني أنه سيتم وضع وظيفة RS الإضافية عندما تنتقل إلى تثبيت SharePoint. وقد تم عرضه وإبرازه في الشكل أدناه. يؤدي هذا في الواقع إلى تجنب الكثير من المشكلات التي رأيناها مع SP 2007 وRS 2008 عند تثبيت الوظيفة الإضافية.

![Introduction](introduction_1.png)

**Image1 :- Reporting Services Add-in for Share Point**
{{% /alert %}}

## مصادقة شيربوينت

**قبل أن ننتقل إلى أجزاء تكامل RS، هناك شيء واحد أريد الإشارة إليه حول SharePoint Farm وهو كيفية إعداد الموقع. وبشكل أكثر تحديدًا كيفية تكوين المصادقة للموقع. سواء كانت كلاسيكية أو مطالبات. هذا الاختيار مهم في البداية. لا أعتقد أنه يمكنك تغيير هذا الخيار بمجرد الانتهاء منه. إذا كان بإمكانك تغييره، فلن تكون عملية بسيطة.

NOTE: ***Reporting Services 2008 R2 is NOT Claims aware***

Even if you choose your SharePoint site to use Claims, Reporting Services itself isn't Claims aware. That said, it does affect how authentication works with Reporting Services. So, what is the difference from a Reporting Services perspective? It comes down to whether you want to forward User Credentials to the data source. Classic:- Can use Kerberos and forward the user's credentials to your back end datasource (will need to use Kerberos for that). Claims:- A Claims token is used and not a windows token. RS will always use Trusted Authentication in this scenario and will only have access to the SPUser token. You will need to store your credentials within your data source.

كلاسيكي: - يمكن استخدام Kerberos وإعادة توجيه بيانات اعتماد المستخدم إلى مصدر البيانات الخلفي الخاص بك (سوف تحتاج إلى استخدام Kerberos لذلك.

Claims :- A Claims token is used and not a windows token. RS will always use Trusted Authentication in this scenario and will only have access to the SPUser token. You will need to store your credentials within your data source.

في الوقت الحالي، نريد فقط التركيز على إعداد RS. في هذه المرحلة، تم تثبيت SharePoint على SharePoint Box الخاص بي وتم إعداده باستخدام موقع Classic Auth على المنفذ 80. على خادم RS، قمت للتو بتثبيت خدمات التقارير وهذا كل شيء.
