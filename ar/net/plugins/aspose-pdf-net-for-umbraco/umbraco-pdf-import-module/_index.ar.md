---
title: وحدة استيراد PDF في Umbraco
type: docs
weight: 10
url: /net/umbraco-pdf-import-module/
description: تعلم كيفية تثبيت واستخدام وحدة استيراد PDF في Umbraco
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.5
---

## مقدمة

**Aspose.PDF لـ .NET** هو مكون إنشاء ومعالجة مستندات PDF يمكّن تطبيقات .NET الخاصة بك من قراءة وكتابة ومعالجة مستندات PDF الموجودة دون استخدام Adobe Acrobat. كما يتيح لك إنشاء النماذج وإدارة حقول النماذج المضمنة في مستند PDF.

**Aspose.PDF لـ .NET** ميسور التكلفة ويقدم مجموعة مذهلة من الميزات بما في ذلك خيارات ضغط PDF؛ إنشاء ومعالجة الجداول؛ دعم للأشياء الرسومية؛ وظائف الرابط التشعبي الموسعة؛ عناصر التحكم الأمنية الموسعة؛ التعامل مع الخطوط المخصصة؛ التكامل مع مصادر البيانات؛ إضافة أو إزالة العلامات المرجعية؛ إنشاء فهرس المحتويات؛ إضافة، تحديث، حذف المرفقات والتعليقات؛ استيراد أو تصدير بيانات نموذج PDF؛ إضافة، استبدال أو إزالة النصوص والصور؛ تقسيم، دمج، استخراج أو إدراج صفحات؛ تحويل الصفحات إلى صورة؛ طباعة مستندات PDF والمزيد.
**Aspose.PDF لـ .NET** هو بأسعار معقولة ويقدم مجموعة هائلة من الميزات بما في ذلك خيارات ضغط ملفات PDF؛ إنشاء ومعالجة الجداول؛ دعم للأشياء البيانية؛ وظائف الرابط التشعبي الموسعة؛ أدوات التحكم الأمنية الموسعة؛ التعامل مع الخطوط المخصصة؛ التكامل مع مصادر البيانات؛ إضافة أو إزالة العلامات المرجعية؛ إنشاء فهرس المحتويات؛ إضافة، تحديث، حذف المرفقات والتعليقات التوضيحية؛ استيراد أو تصدير بيانات نموذج PDF؛ إضافة، استبدال أو إزالة النصوص والصور؛ تقسيم، دمج، استخراج أو إدراج الصفحات؛ تحويل الصفحات إلى صورة؛ طباعة مستندات PDF والمزيد

### **ميزات الوحدة**

Umbraco PDF Import هو إضافة مفتوحة المصدر من [Aspose](http://www.aspose.com/) تتيح للمطورين الحصول على/قراءة محتويات أي مستند PDF دون الحاجة إلى أي برنامج آخر.
إضافة Umbraco PDF Import هي إضافة مفتوحة المصدر من [Aspose](http://www.aspose.com/) تسمح للمطورين بالحصول على محتويات أي مستند PDF دون الحاجة إلى أي برامج أخرى.

## متطلبات النظام والمنصات المدعومة

### **متطلبات النظام**

لتثبيت وحدة Aspose .NET Pdf Import لـ Umbraco، يجب توفر المتطلبات التالية:

- Umbraco 6.0 +

لا تتردد في الاتصال بنا إذا كنت ترغب في تثبيت هذه الوحدة على إصدارات أخرى من Umbraco.

### **المنصات المدعومة**

الوحدة مدعومة على جميع إصدارات

- Umbraco التي تعمل على ASP.NET 4.0

## التحميل

يمكنك تحميل Aspose .NET Pdf Import لـ Umbraco من أحد المواقع التالية

- [CodePlex](https://asposeumbraco.codeplex.com/releases)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/releases)
- [Sourceforge](https://sourceforge.net/projects/asposeumbraco/files/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/downloads)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)
- [Umbraco](https://our.umbraco.org/projects/developer-tools/import-from-pdf-using-aspose-pdf)

## التثبيت

بمجرد التحميل، الرجاء اتباع هذه الخطوات لتثبيت هذه الحزمة على موقع Umbraco الخاص بك:

1. سجل الدخول إلى قسم **المطور** في Umbraco، على سبيل المثال <http://www.myblog.com/umbraco/>
1. من الشجرة، قم بتوسيع مجلد **الحزم**.
   من هنا يوجد طريقتان لتثبيت حزمة: اختر **تثبيت حزمة محلية** أو تصفح **مستودع حزم Umbraco.**
1. إذا قمت بتثبيت **حزمة محلية**، لا تقم بفك ضغط الحزمة ولكن قم بتحميل ملف zip في Umbraco.
1. اتبع التعليمات على الشاشة.

**ملاحظة:** قد تحصل على خطأ 'تم تجاوز الطول الأقصى للطلب' عند التثبيت. يمكنك حل هذه المشكلة بسهولة عن طريق تحديث قيمة 'maxRequestLength' في ملف web.config الخاص بموقع Umbraco.

```xml
  <httpRuntime requestValidationMode="2.0" enableVersionHeader="false" maxRequestLength="25000" />
```

## الاستخدام

بعد تثبيت الماكرو، من السهل جدًا البدء في استخدامه على موقعك الإلكتروني:

1.
1.
1. انقر على **الإعدادات** في قائمة الأقسام الموجودة في أسفل اليسار من الشاشة.
1. قم بتوسيع عقدة **القوالب** واختر القالب الذي تريد إضافة ماكرو إليه، على سبيل المثال تدوينة مدونة.
1. حدد الموقع في القالب المختار حيث تريد الزر.
1. انقر على **إدراج ماكرو** في الشريط العلوي.
1. من **اختر ماكرو**، اختر الماكرو المثبت وانقر على **موافق**.

لقد قمت بإضافة القالب بنجاح. الآن يظهر زر بعنوان **استيراد من Pdf** على جميع الصفحات التي تم إنشاؤها باستخدام هذا القالب. يمكن لأي شخص ببساطة النقر على الزر واستيراد محتويات وثيقة PDF.

## فيديو توضيحي

يرجى التحقق من [الفيديو](https://www.youtube.com/watch?v=zmZTJ86B25E) أدناه لرؤية الوحدة في العمل.

## الدعم، التوسع والمساهمة

### الدعم

منذ الأيام الأولى لشركة Aspose، كنا نعلم أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافيًا.
منذ الأيام الأولى لشركة Aspose، كنا نعلم أن تقديم منتجات جيدة لعملائنا لن يكون كافيًا.

لهذا السبب نقدم الدعم المجاني. أي شخص يستخدم منتجنا، سواء اشتراه أو يستخدم نسخة تقييم، يستحق كل اهتمامنا واحترامنا.

يمكنك تسجيل أي مشكلات أو اقتراحات متعلقة بـ Aspose.PDF .NET لوحدات Umbraco باستخدام أي من المنصات التالية

- [CodePlex](https://asposeumbraco.codeplex.com/workitem/list/basic)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco/issues)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/tickets/?source=navbar)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/issues?status=new&status=open)

#### استيراد من Pdf

- [شبكة مطوري مايكروسوفت - الأسئلة والأجوبة](https://code.msdn.microsoft.com/Umbraco-Import-from-Pdf-d4659bc8/view/Discussions#content)

### توسيع والمساهمة

Aspose .NET PDF Import لـ Umbraco مفتوح المصدر وشيفرته المصدرية متاحة على مواقع التواصل الاجتماعي البرمجي الرئيسية المدرجة أدناه.
Aspose .NET PDF Import لـ Umbraco مفتوح المصدر ويمكن الحصول على شفرته البرمجية من المواقع الاجتماعية البرمجية الكبرى المدرجة أدناه.

#### الشفرة البرمجية

يمكنك الحصول على أحدث شفرة برمجية من أحد المواقع التالية

- [CodePlex](https://asposeumbraco.codeplex.com/SourceControl/latest)
- [Github](https://github.com/asposemarketplace/Aspose_for_Umbraco)
- [Sourceforge](https://sourceforge.net/p/asposeumbraco/code/ci/master/tree/)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-umbraco/src)

#### كيفية تهيئة الشفرة البرمجية

يجب أن يكون لديك التالي مثبتًا لفتح وتوسيع الشفرة البرمجية

- Visual Studio 2010 أو أعلى

الرجاء اتباع هذه الخطوات البسيطة للبدء

1. قم بتنزيل/استنساخ الشفرة البرمجية.
1. افتح Visual Studio 2010 واختر **File** > **Open Project**
1. تصفح إلى أحدث شفرة برمجية قمت بتنزيلها وافتح **Aspose.Import من PDF.sln**
