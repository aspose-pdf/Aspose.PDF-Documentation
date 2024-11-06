---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 90
url: ar/java/licensing/
description: Aspose. PDF for Java يدعو عملاءه للحصول على ترخيص كلاسيكي وترخيص محسوب. وكذلك استخدام ترخيص محدود لاستكشاف المنتج بشكل أفضل.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## تحديدات النسخة التجريبية

نريد من عملائنا اختبار مكوناتنا بدقة قبل الشراء لذلك تتيح النسخة التجريبية لك استخدامها كما تفعل عادة.

- **تم إنشاء PDF بعلامة مائية تجريبية.** توفر النسخة التجريبية من Aspose.PDF for Java جميع وظائف المنتج، ولكن يتم وضع علامة مائية على جميع الصفحات في مستندات PDF التي تم إنشاؤها بكلمات "للتقييم فقط. تم الإنشاء باستخدام Aspose.PDF. حقوق الطبع والنشر 2002-2020 Aspose Pty Ltd" في الأعلى.

- **حد عدد عناصر المجموعة التي يمكن معالجتها.**

في النسخة التجريبية من أي مجموعة، يمكنك معالجة أربعة عناصر فقط (على سبيل المثال، 4 صفحات فقط، 4 حقول نموذج، إلخ.).

You can download an evaluation version of **Aspose.PDF** for Java from [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). النسخة التقييمية توفر نفس الإمكانيات تمامًا مثل النسخة المرخصة من المنتج. علاوة على ذلك، تصبح النسخة التقييمية مرخصة ببساطة عند شراء ترخيص وإضافة بعض الأسطر من التعليمات البرمجية لتطبيق الترخيص.

بمجرد أن تكون راضيًا عن تقييمك لـ **Aspose.PDF**، يمكنك [شراء ترخيص](https://purchase.aspose.com/) من موقع Aspose الإلكتروني. تعرف على أنواع الاشتراكات المختلفة المقدمة. إذا كان لديك أي أسئلة، فلا تتردد في الاتصال بفريق مبيعات Aspose.

كل ترخيص من Aspose يحمل اشتراكًا لمدة عام واحد للترقيات المجانية إلى أي إصدارات جديدة أو إصلاحات تصدر خلال هذه المدة. الدعم الفني مجاني وغير محدود ومقدم لكل من المستخدمين المرخصين والتقييميين.

>إذا كنت ترغب في اختبار Aspose.PDF لـ Java بدون قيود النسخة التقييمية، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا.
 يرجى الرجوع إلى [كيفية الحصول على ترخيص مؤقت؟](https://purchase.aspose.com/temporary-license)

## ترخيص كلاسيكي

يمكن تحميل الترخيص من ملف أو كائن تدفق. أسهل طريقة لتعيين الترخيص هي وضع ملف الترخيص في نفس المجلد الذي يحتوي على ملف Aspose.PDF.dll وتحديد اسم الملف بدون مسار، كما هو موضح في المثال أدناه.

الترخيص هو ملف XML نصي يحتوي على تفاصيل مثل اسم المنتج، عدد المطورين المرخص لهم، تاريخ انتهاء الاشتراك وما إلى ذلك. يتم توقيع الملف رقميًا، لذا لا تقم بتعديل الملف؛ حتى الإضافة غير المقصودة لكسر سطر إضافي في الملف ستؤدي إلى إبطاله.

تحتاج إلى تعيين ترخيص قبل تنفيذ أي عمليات مع المستندات. يُطلب منك فقط تعيين ترخيص مرة واحدة لكل تطبيق أو عملية.

يمكن تحميل الترخيص من تدفق أو ملف في المواقع التالية:

1. المسار الصريح.
1. المجلد الذي يحتوي على aspose-pdf-xx.x.jar.

استخدم طريقة License.setLicense لترخيص المكون. غالبًا ما تكون أسهل طريقة لتعيين الترخيص هي وضع ملف الترخيص في نفس المجلد مع Aspose.PDF.jar وتحديد اسم الملف فقط بدون المسار كما هو موضح في المثال التالي:

{{% alert color="primary" %}}

بدءًا من Aspose.PDF for Java 4.2.0، تحتاج إلى استدعاء أسطر الكود التالية لتفعيل الترخيص.

{{% /alert %}}

### تحميل ترخيص من ملف

في هذا المثال، سيحاول **Aspose.PDF** العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JAR لتطبيقك.

```java
// تهيئة مثيل الترخيص
com.aspose.pdf.License license = new com.aspose.pdf.License();
// استدعاء طريقة setLicense لتعيين الترخيص
license.setLicense("Aspose.Pdf.Java.lic");
```
### تحميل الترخيص من كائن تدفق

يوضح المثال التالي كيفية تحميل ترخيص من تدفق.

```java
// تهيئة مثيل الترخيص
com.aspose.pdf.License license = new com.aspose.pdf.License();
// تعيين الترخيص من Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### تعيين ترخيص تم شراؤه قبل 2005/01/22 **Aspose.PDF** ل‍ Java لم يعد يدعم التراخيص القديمة لذا يرجى الاتصال بفريق [المبيعات](https://company.aspose.com/contact) للحصول على ملف ترخيص جديد.

### تحقق من الترخيص

من الممكن التحقق مما إذا تم تعيين الترخيص بشكل صحيح أم لا. تحتوي فئة Document على طريقة isLicensed التي ستعيد true إذا تم تعيين الترخيص بشكل صحيح.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// تحقق مما إذا تم التحقق من صحة الترخيص
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## ترخيص مدفوع حسب الاستخدام

يسمح Aspose.PDF للمطورين بتطبيق مفتاح مدفوع حسب الاستخدام. إنه آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة مع طريقة الترخيص الحالية. يمكن لأولئك العملاء الذين يرغبون في الفوترة بناءً على استخدام ميزات API استخدام الترخيص المدفوع حسب الاستخدام. لمزيد من التفاصيل، يرجى الرجوع إلى قسم [الأسئلة الشائعة حول الترخيص المدفوع حسب الاستخدام](https://purchase.aspose.com/faqs/licensing/metered).

تم تقديم فئة جديدة [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) لتطبيق المفتاح المدفوع حسب الاستخدام.
 التالي هو مثال على الكود الذي يوضح كيفية تعيين المفتاح العام والخاص المقيّد.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// بشكل اختياري، تعيد السطران التاليان true إذا تم تطبيق ترخيص صالح؛ 
// false إذا كان المكون يعمل في وضع التقييم.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## استخدام منتجات متعددة من Aspose

إذا كنت تستخدم منتجات متعددة من Aspose في تطبيقك، على سبيل المثال Aspose.PDF وAspose.Words، فإليك بعض النصائح المفيدة.

- **قم بتعيين الترخيص لكل منتج من Aspose بشكل منفصل.** حتى إذا كان لديك ملف ترخيص واحد لجميع المكونات، على سبيل المثال 'Aspose.Total.lic'، فلا يزال عليك استدعاء **License.SetLicense** لكل منتج من Aspose تستخدمه في تطبيقك.
- **استخدم اسم الفئة الكامل للترخيص.** كل منتج من Aspose لديه فئة **License** في نطاق أسمائه. على سبيل المثال، تحتوي Aspose.PDF على **com.aspose.pdf.License** وAspose.Words تحتوي على **com.aspose.words.License**. إن استخدام الاسم الكامل للفئة يسمح لك بتجنب أي لبس حول أي ترخيص يطبق على أي منتج.

```java
// إنشاء كائن من فئة الترخيص Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// إعداد الترخيص
license.setLicense("Aspose.Total.Java.lic");

// إعداد الترخيص لـ Aspose.Words لـ Java

// إنشاء كائن من فئة الترخيص Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// إعداد الترخيص
licenseaw.setLicense("Aspose.Total.Java.lic");
```