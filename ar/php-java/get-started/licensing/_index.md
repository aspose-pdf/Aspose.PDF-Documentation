---
title: Licensing and limitations
linktitle: Licensing and limitations
type: docs
weight: 90
url: /ar/php-java/licensing/
description: يدعو Aspose.PDF for PHP عبر Java عملاءه للحصول على ترخيص كلاسيكي وترخيص مدفوع الأجر. وكذلك استخدام ترخيص محدود لاستكشاف المنتج بشكل أفضل.
lastmod: "2024-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## قيود النسخة التجريبية

نريد من عملائنا اختبار مكوناتنا بدقة قبل الشراء، لذا تتيح لك النسخة التجريبية استخدامها كما تفعل عادةً.

- **PDF تم إنشاؤه بعلامة مائية للتقييم.** توفر النسخة التجريبية من Aspose.PDF for PHP عبر Java جميع وظائف المنتج بالكامل، ولكن يتم وضع علامة مائية على جميع الصفحات في مستندات PDF المُنشأة بعلامة "للتقييم فقط. تم الإنشاء باستخدام Aspose.PDF. حقوق الطبع والنشر 2002-2020 Aspose Pty Ltd" في الأعلى.

- **الحد من عدد عناصر المجموعة التي يمكن معالجتها.**

في النسخة التجريبية من أي مجموعة، يمكنك معالجة أربعة عناصر فقط (على سبيل المثال، 4 صفحات فقط، 4 حقول نموذج، إلخ).

يمكنك تنزيل نسخة تجريبية من **Aspose.PDF** لـ Java من [مستودع Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). توفر النسخة التجريبية نفس الإمكانيات تمامًا مثل النسخة المرخصة من المنتج. علاوة على ذلك، تصبح النسخة التجريبية مرخصة ببساطة عندما تشتري ترخيصًا وتضيف بضعة أسطر من التعليمات البرمجية لتطبيق الترخيص.

بمجرد أن تكون راضيًا عن تقييمك لـ **Aspose.PDF**، يمكنك [شراء ترخيص](https://purchase.aspose.com/) من موقع Aspose. تعرف على أنواع الاشتراكات المختلفة المقدمة. إذا كان لديك أي أسئلة، لا تتردد في الاتصال بفريق مبيعات Aspose.

كل ترخيص من Aspose يحمل اشتراكًا لمدة عام واحد للحصول على ترقيات مجانية لأي إصدارات جديدة أو إصلاحات تصدر خلال هذه الفترة. الدعم الفني مجاني وغير محدود ومقدم لكل من المستخدمين المرخصين والمستخدمين التجريبيين.

>إذا كنت ترغب في اختبار Aspose.PDF لـ PHP عبر Java بدون قيود النسخة التجريبية، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا.
 يرجى الرجوع إلى [كيفية الحصول على رخصة مؤقتة؟](https://purchase.aspose.com/temporary-license)

## الرخصة الكلاسيكية

يمكن تحميل الرخصة من ملف أو كائن تدفق. أسهل طريقة لتعيين الرخصة هي وضع ملف الرخصة في نفس المجلد مثل ملف Aspose.PDF.dll وتحديد اسم الملف بدون مسار، كما هو موضح في المثال أدناه.

الرخصة هي ملف XML نصي بسيط يحتوي على تفاصيل مثل اسم المنتج، وعدد المطورين المرخص له، وتاريخ انتهاء الاشتراك وما إلى ذلك. الملف موقع رقميًا، لذا لا تقم بتعديل الملف؛ حتى الإضافة غير المقصودة لفاصل سطر إضافي في الملف ستجعله غير صالح.

تحتاج إلى تعيين رخصة قبل القيام بأي عمليات مع المستندات. يُطلب منك تعيين رخصة مرة واحدة فقط لكل تطبيق أو عملية.

يمكن تحميل الرخصة من تدفق أو ملف في المواقع التالية:

1. مسار محدد.
1. المجلد الذي يحتوي على aspose-pdf-xx.x.jar.

استخدم طريقة License.setLicense لترخيص المكون. غالبًا ما يكون أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مع Aspose.PDF.jar وتحديد اسم الملف فقط بدون المسار كما هو موضح في المثال التالي:

{{% alert color="primary" %}}

بدءًا من Aspose.PDF لـ PHP عبر Java 4.2.0، تحتاج إلى استدعاء أسطر الكود التالية لتهيئة الترخيص.

{{% /alert %}}

### تحميل الترخيص من ملف

في هذا المثال، سيحاول **Aspose.PDF** العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JAR لتطبيقك.

```java
// تهيئة مثيل الترخيص
com.aspose.pdf.License license = new com.aspose.pdf.License();
// استدعاء طريقة setLicense لتعيين الترخيص
license.setLicense("Aspose.Pdf.Java.lic");
```
### تحميل الترخيص من كائن دفق

يظهر المثال التالي كيفية تحميل ترخيص من دفق.

```java
// تهيئة مثيل الترخيص
com.aspose.pdf.License license = new com.aspose.pdf.License();
// تعيين الترخيص من الدفق
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### تعيين ترخيص تم شراؤه قبل 22/01/2005**Aspose.PDF** لـ Java لا يدعم التراخيص القديمة بعد الآن، لذا يرجى الاتصال بفريق [المبيعات لدينا](https://company.aspose.com/contact) للحصول على ملف ترخيص جديد.

### التحقق من صحة الترخيص

من الممكن التحقق مما إذا كان الترخيص قد تم تعيينه بشكل صحيح أم لا. تحتوي فئة Document على الطريقة isLicensed التي ستعيد القيمة true إذا تم تعيين الترخيص بشكل صحيح.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// التحقق مما إذا تم التحقق من صحة الترخيص
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## الترخيص المقياسي

يسمح Aspose.PDF للمطورين بتطبيق مفتاح مقياسي. إنها آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة مع الطريقة الحالية للترخيص. يمكن لأولئك العملاء الذين يرغبون في أن يتم احتساب الفواتير بناءً على استخدام ميزات API استخدام الترخيص المقياسي. لمزيد من التفاصيل، يرجى الرجوع إلى قسم [الأسئلة الشائعة حول الترخيص المقياسي](https://purchase.aspose.com/faqs/licensing/metered).

تم تقديم فئة جديدة [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered) لتطبيق مفتاح مقياسي.
 فيما يلي نموذج كود يوضح كيفية تعيين المفتاح العام والخاص المُمَيَّز.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// بشكل اختياري، السطران التاليان يعيدان true إذا تم تطبيق ترخيص صالح;
// false إذا كان المكون يعمل في وضع التقييم.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## استخدام منتجات متعددة من Aspose

إذا كنت تستخدم منتجات Aspose متعددة في تطبيقك، على سبيل المثال Aspose.PDF و Aspose.Words، فإليك بعض النصائح المفيدة.

- **قم بتعيين الترخيص لكل منتج Aspose بشكل منفصل.** حتى إذا كان لديك ملف ترخيص واحد لجميع المكونات، على سبيل المثال 'Aspose.Total.lic'، لا يزال عليك استدعاء **License.SetLicense** بشكل منفصل لكل منتج Aspose تستخدمه في تطبيقك.
- **استخدم الاسم الكامل لفئة الترخيص.** كل منتج Aspose لديه فئة **License** في فضاء الأسماء الخاص به. على سبيل المثال، يحتوي Aspose.PDF على **com.aspose.pdf.License** وAspose.Words يحتوي على **com.aspose.words.License**. يسمح لك استخدام اسم الفئة الكامل بتجنب أي لبس حول أي ترخيص يتم تطبيقه على أي منتج.

```java
// إنشاء كائن من فئة الترخيص لـ Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// تعيين الترخيص
license.setLicense("Aspose.Total.Java.lic");

// تعيين الترخيص لـ Aspose.Words for Java

// إنشاء كائن من فئة الترخيص لـ Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// تعيين الترخيص
licenseaw.setLicense("Aspose.Total.Java.lic");
```