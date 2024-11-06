---
title: مقدمة
type: docs
weight: 10
url: ar/reportingservices/introduction/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

كان Aspose.PDF لخدمات التقارير رائعًا جدًا في إنشاء ملفات PDF من خلال خدمات تقارير SQL منذ سنوات عديدة، ويوفر خيارات متنوعة للتكوين والمعايرة التي لا يدعمها SQL Reporting Services بشكل افتراضي. مؤخرًا، تلقينا بعض الطلبات بخصوص دمج Aspose.PDF لخدمات التقارير مع SharePoint. في هذه المقالة، سوف نركز على MS SharePoint 2010. قبل أن نتابع أكثر، نفترض أنك قد قمت بالفعل بإعداد مزرعة SharePoint. في هذا المثال، سنستخدم كامل سحابة SharePoint. ومع ذلك، فإن الخطوات متشابهة لخادم SharePoint Foundation.

{{% /alert %}}

{{% alert color="primary" %}}

قبل أن نتابع أكثر، دعونا نلقي نظرة على المواضيع المرجعية التي استشرناها أثناء إعداد هذه المقالة.

- [نظرة عامة على تكامل تقنية خدمات التقارير وSharePoint](http://msdn.microsoft.com/en-us/library/bb326358.aspx)
```
- [Deployment Topologies for Reporting Services in SharePoint Integrated Mode](http://msdn.microsoft.com/en-us/library/bb510781.aspx)
- [Configuring Reporting Services for SharePoint 2010 Integration](http://msdn.microsoft.com/en-us/library/bb326356.aspx)

{{% /alert %}}

## إعداد البيئة

يتكون إعدادنا من 4 خوادم. يشمل وحدة تحكم المجال، وخادم SQL، وخادم SharePoint وخادم لخدمات التقارير. يمكنك اختيار أن يكون SharePoint وخدمات التقارير على نفس الجهاز، مما سيبسط هذا قليلاً وسأوضح بعض الفروقات.

## متطلبات التثبيت المسبقة

{{% alert color="primary" %}}

الإضافة البرمجية لخدمات التقارير لـ SharePoint هي واحدة من المكونات الأساسية للحصول على تكامل يعمل بشكل صحيح. The Add-In needs to be installed on any of the Web Front Ends (WFE) that is in your SharePoint farm along with the Central Admin server. One of the new changes with SQL 2008 R2 & SharePoint 2010 is that the 2008 R2 Add-In is now a pre-requisite for the SharePoint Install. This means that the RS Add-In will be laid down when you go to install SharePoint. It has been shown and highlighted in figure below. This actually avoids a lot of issues we saw with SP 2007 and RS 2008 when installing the Add-In.

يجب تثبيت الإضافة على أي من واجهات الويب الأمامية (WFE) التي توجد في مزرعة SharePoint الخاصة بك جنبًا إلى جنب مع خادم الإدارة المركزية. واحدة من التغييرات الجديدة مع SQL 2008 R2 و SharePoint 2010 هي أن الإضافة 2008 R2 أصبحت الآن شرطًا مسبقًا لتثبيت SharePoint. هذا يعني أنه سيتم تثبيت إضافة RS عندما تقوم بتثبيت SharePoint. وقد تم توضيح ذلك وتسليط الضوء عليه في الشكل أدناه. هذا في الواقع يتجنب الكثير من المشاكل التي رأيناها مع SP 2007 و RS 2008 عند تثبيت الإضافة.

![todo:image_alt_text](introduction_1.png)

**Image1 :- Reporting Services Add-in for Share Point** **الصورة 1 :- الإضافة لخدمات التقارير لـ SharePoint**
{{% /alert %}}

## SharePoint Authentication
## مصادقة SharePoint

**Before we jump into the RS Integration pieces, one thing I want to point out about the SharePoint Farm is how you setup the Site.
**قبل أن ننتقل إلى أجزاء التكامل مع RS، شيء واحد أود أن أشير إليه حول مزرعة SharePoint هو كيفية إعداد الموقع. 
بشكل أكثر تحديدًا، كيفية تكوين المصادقة للموقع. سواء ستكون كلاسيكية أو مطالبات. هذا الخيار مهم في البداية. لا أعتقد أنه يمكنك تغيير هذا الخيار بمجرد الانتهاء منه. إذا كان بإمكانك تغييره، فلن تكون عملية بسيطة.

ملاحظة: ***خدمات التقارير 2008 R2 ليست مدركة للمطالبات***

حتى إذا اخترت أن يستخدم موقع SharePoint الخاص بك المطالبات، فإن خدمات التقارير نفسها ليست مدركة للمطالبات. ومع ذلك، فإنه يؤثر على كيفية عمل المصادقة مع خدمات التقارير. إذًا، ما هو الفرق من منظور خدمات التقارير؟ يتلخص الأمر في ما إذا كنت تريد تمرير بيانات اعتماد المستخدم إلى مصدر البيانات. كلاسيكي:- يمكن استخدام Kerberos وتمرير بيانات اعتماد المستخدم إلى مصدر البيانات الخلفي الخاص بك (سيحتاج إلى استخدام Kerberos لذلك). مطالبات:- يتم استخدام رمز المطالبات وليس رمز Windows. ستستخدم RS دائمًا المصادقة الموثوقة في هذا السيناريو وسوف يكون لديها حق الوصول فقط إلى رمز SPUser. ستحتاج إلى تخزين بيانات اعتمادك داخل مصدر البيانات الخاص بك.

كلاسيكي :- يمكن استخدام Kerberos وتمرير بيانات اعتماد المستخدم إلى مصدر البيانات الخلفي الخاص بك (سيحتاج إلى استخدام Kerberos لذلك).
```
```
Claims :- يتم استخدام رمز المطالبات وليس رمز ويندوز. سوف يستخدم RS دائمًا المصادقة الموثوقة في هذا السيناريو وسيكون لديه فقط الوصول إلى رمز SPUser. ستحتاج إلى تخزين بيانات الاعتماد الخاصة بك داخل مصدر البيانات الخاص بك.

في الوقت الحالي، نريد فقط التركيز على إعداد RS. في هذه المرحلة، تم تثبيت SharePoint على صندوق SharePoint الخاص بي وتم إعداده بموقع مصادقة كلاسيكي على المنفذ 80. على خادم RS قمت للتو بتثبيت خدمات التقارير وهذا كل شيء.
```