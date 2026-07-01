---
title: الترخيص والقيود
linktitle: الترخيص والقيود
type: docs
weight: 50
url: /ar/androidjava/licensing/
description: يدعو Aspose.PDF for Android via Java عملائه للحصول على ترخيص Classic وترخيص Metered. كما يمكنهم استخدام ترخيص محدود لاستكشاف المنتج بشكل أفضل.
lastmod: "2026-06-30"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## قيود نسخة التقييم

نريد من عملائنا اختبار مكوّناتنا بدقة قبل الشراء، لذلك تتيح نسخة التقييم لك استخدامها كما تفعل عادةً.

- **تم إنشاء PDF بعلامة مائية للتقييم.** نسخة التقييم من Aspose.PDF لنظام Android عبر Java توفر جميع وظائف المنتج، لكن جميع الصفحات في مستندات PDF التي تم إنشاؤها تحمل علامة مائية تقول "تقييم فقط. تم الإنشاء باستخدام Aspose.PDF. حقوق النشر 2002-2020 Aspose Pty Ltd" في الأعلى.

- **حد عدد عناصر المجموعة التي يمكن معالجتها.**
في نسخة التقييم من أي مجموعة، يمكنك معالجة أربعة عناصر فقط (على سبيل المثال، 4 صفحات فقط، 4 حقول نموذج، إلخ).

يمكنك تنزيل نسخة التقييم من Aspose.PDF لنظام Android عبر Java من [مستودع Aspose](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). يوفر الإصدار التجريبي نفس القدرات تمامًا كما الإصدار المرخص من المنتج. وعلاوة على ذلك، يصبح الإصدار التجريبي مرخصًا ببساطة عندما تشتري ترخيصًا وتضيف بضع أسطر من الشيفرة لتطبيق الترخيص.

بمجرد أن تكون راضيًا عن تقييمك لـ **Aspose.PDF**، يمكنك [شراء ترخيص](https://purchase.aspose.com/) على موقع Aspose. تعرّف على أنواع الاشتراكات المختلفة المتاحة. إذا كان لديك أي أسئلة، لا تتردد في الاتصال بفريق مبيعات Aspose.

كل ترخيص من Aspose يتضمن اشتراكًا لمدة عام واحد لتحديثات مجانية لأي إصدارات جديدة أو تصحيحات تُصدر خلال هذه الفترة. الدعم الفني مجاني وغير محدود ويُقدم لكل من المستخدمين المرخصين ومستخدمي التقييم.

>إذا كنت ترغب في اختبار Aspose.PDF for Android عبر Java دون قيود نسخة التقييم، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا. يرجى الرجوع إلى [كيف تحصل على ترخيص مؤقت؟](https://purchase.aspose.com/temporary-license)

## رخصة كلاسيكية

يمكن تحميل الرخصة من ملف أو كائن تدفق. أسهل طريقة لتعيين رخصة هي وضع ملف الرخصة في نفس المجلد الذي يوجد فيه ملف Aspose.PDF.dll وتحديد اسم الملف بدون مسار، كما هو موضح في المثال أدناه.

الرخصة هي ملف XML نص عادي يحتوي على تفاصيل مثل اسم المنتج، عدد المطورين المرخص لهم، تاريخ انتهاء الاشتراك وما إلى ذلك. الملف موقع رقمياً، لذا لا تقم بتعديل الملف؛ حتى الإضافة غير المقصودة لسطر جديد إضافي في الملف ستبطل صلاحيته.

يتعين عليك تعيين رخصة قبل تنفيذ أي عمليات على المستندات. لا يلزمك تعيين رخصة سوى مرة واحدة لكل تطبيق أو عملية.

يمكن تحميل الترخيص من تدفق أو ملف في المواقع التالية:

1. مسار صريح.
1. المجلد الذي يحتوي على ملف aspose-pdf-xx.x.jar.

استخدم طريقة License.setLicense لترخيص المكوّن. غالبًا ما يكون أسهل طريقة لتعيين الترخيص هي وضع ملف الترخيص في نفس المجلد الذي يحتوي على Aspose.PDF.jar وتحديد اسم الملف فقط دون مسار كما هو موضح في المثال التالي:

{{% alert color="primary" %}}

بدءًا من Aspose.PDF for Java 4.2.0، تحتاج إلى استدعاء أسطر الشيفرة التالية لتهيئة الترخيص.

{{% /alert %}}

### تحميل الترخيص من ملف

في هذا المثال **Aspose.PDF** سيحاول العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JAR لتطبيقك.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### تحميل الترخيص من كائن تدفق

يوضح المثال التالي كيفية تحميل الترخيص من تدفق.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

#### تعيين ترخيص تم شراؤه قبل 2005/01/22

**Aspose.PDF** للـ Java لا يدعم الآن التراخيص القديمة لذا يرجى الاتصال بـ [فريق المبيعات](https://company.aspose.com/contact) للحصول على ملف ترخيص جديد.

### تحقق من الترخيص

يمكن التحقق مما إذا تم تعيين الترخيص بشكل صحيح أم لا. تحتوي فئة Document على طريقة isLicensed التي ستُعيد true إذا تم تعيين الترخيص بشكل صحيح.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```
## رخصة مترية

يتيح Aspose.PDF للمطورين تطبيق مفتاح مترى. إنه آلية ترخيص جديدة. ستُستخدم آلية الترخيص الجديدة إلى جانب طريقة الترخيص الحالية. يمكن للعملاء الذين يرغبون في الفوترة بناءً على استخدام ميزات واجهة برمجة التطبيقات استخدام الترخيص بالمترى. لمزيد من التفاصيل، يرجى الرجوع إلى [الأسئلة الشائعة حول الترخيص المترى](https://purchase.aspose.com/faqs/licensing/metered) القسم.

```java
String publicKey = "";
String privateKey = "";

Metered m = new Metered();
m.setMeteredKey(publicKey, privateKey);

// Optionally, the following two lines returns true if a valid license has been applied;
// false if the component is running in evaluation mode.
License lic = new License();
System.out.println("License is set = " + lic.isLicensed());
```
## استخدام منتجات متعددة من Aspose

إذا كنت تستخدم منتجات Aspose متعددة في تطبيقك، على سبيل المثال Aspose.PDF و Aspose.Words، فإليك بعض النصائح المفيدة.

- **قم بتعيين الترخيص لكل منتج Aspose على حدة.** حتى إذا كان لديك ملف ترخيص واحد لجميع المكونات، على سبيل المثال 'Aspose.Total.lic'، لا يزال عليك استدعاء **License.SetLicense** بشكل منفصل لكل منتج Aspose تستخدمه في تطبيقك.
- **استخدم الاسم المؤهل بالكامل لفئة الترخيص.** كل منتج من Aspose يحتوي على فئة **License** في مساحة الاسم الخاصة به. على سبيل المثال، Aspose.PDF لديها الفئة **com.aspose.pdf.License** و Aspose.Words لديها الفئة **com.aspose.words.License**. يسمح لك استخدام الاسم المؤهل بالكامل للفئة بتجنب أي ارتباك بشأن أي ترخيص يتم تطبيقه على أي منتج.

```java
// Instantiate the License class of Aspose.Pdf
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set the license
license.setLicense("Aspose.Total.Java.lic");

// Setting license for Aspose.Words for Java

// Instantiate the License class of Aspose.Words
com.aspose.words.License licenseaw = new com.aspose.words.License();
// Set the license
licenseaw.setLicense("Aspose.Total.Java.lic");
```
