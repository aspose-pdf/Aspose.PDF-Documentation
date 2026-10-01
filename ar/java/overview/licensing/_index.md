---
title: رخصة Aspose PDF
linktitle: الترخيص والقيود
type: docs
weight: 50
url: /ar/java/licensing/
description: تدعو Aspose.PDF for Python عملائها للحصول على رخصة Classic. كذلك يمكنهم استخدام رخصة محدودة لاستكشاف المنتج بشكل أفضل.
lastmod: "2026-10-01"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ترخيص Aspose.PDF for Java
Abstract: تناقش المقالة القيود وخيارات الترخيص لـ Aspose.PDF for Python. وتبرز أن نسخة التقييم تسمح باختبار كامل الوظائف ولكنها تضيف علامة مائية إلى ملفات PDF المولدة، تُظهر النص “Evaluation Only” إلى جانب معلومات حقوق النشر. للمستخدمين الذين يرغبون في الاختبار دون هذه القيود، تتوفر ترخيص مؤقت لمدة 30 يومًا. توضح المقالة أيضًا كيفية تنفيذ ترخيص كلاسيكي عن طريق تحميله من ملف أو تدفق، وتوصي بوضع ملف الترخيص في نفس الدليل الذي يتواجد فيه ملف Aspose.PDF.dll وتعيين الترخيص باستخدام الفئة `Aspose.Pdf.License`. يتم توفير مقتطفات شفرة لتوضيح عملية الترخيص.
---
## قيود نسخة التقييم

نريد أن يقوم عملاؤنا باختبار مكوناتنا بدقة قبل الشراء، لذا تسمح لك نسخة التقييم باستخدامها كما تفعل عادةً.

- **PDF تم إنشاؤه بعلامة مائية للتقييم.** توفر نسخة التقييم من Aspose.PDF for Java كافة وظائف المنتج، لكن جميع الصفحات في مستندات PDF المُولدة تحمل علامة مائية بالنص "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" في الأعلى.

- **حد عدد عناصر المجموعة التي يمكن معالجتها.**
في نسخة التقييم من أي مجموعة، يمكنك معالجة أربعة عناصر فقط (على سبيل المثال، 4 صفحات فقط، 4 حقول نموذج، إلخ).

يمكنك تنزيل نسخة تجريبية من **Aspose.PDF** لـ Java من [مستودع Aspose.](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). توفر النسخة التجريبية نفس القدرات تمامًا كما النسخة المرخصة من المنتج. علاوة على ذلك، تصبح النسخة التجريبية مرخصة بمجرد شرائك ترخيص وإضافة بضع أسطر من الشيفرة لتطبيق الترخيص.

بمجرد أن تكون راضيًا عن تقييمك لـ **Aspose.PDF**, يمكنك [شراء ترخيص](https://purchase.aspose.com/) على موقع Aspose. تعرف على أنواع الاشتراكات المختلفة المتاحة. إذا كان لديك أي أسئلة، لا تتردد في الاتصال بفريق مبيعات Aspose.

كل ترخيص Aspose يتضمن اشتراكًا لمدة سنة واحدة للحصول على ترقيات مجانية لأي إصدارات جديدة أو تصحيحات تصدر خلال هذه الفترة. الدعم الفني مجاني غير محدود ويُقدَّم لكل من المستخدمين المرخصين ومستخدمي النسخة التجريبية.

>إذا كنت تريد اختبار Aspose.PDF for Java دون قيود نسخة التقييم، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا. يرجى الرجوع إلى [كيف تحصل على ترخيص مؤقت؟](https://purchase.aspose.com/temporary-license)

## ترخيص كلاسيكي

يمكن تحميل الترخيص من ملف أو كائن تدفق. أسهل طريقة لتعيين الترخيص هي وضع ملف الترخيص في نفس المجلد الذي يحتوي على ملف Aspose.PDF.dll وتحديد اسم الملف دون مسار، كما هو موضح في المثال أدناه.

الترخيص هو ملف XML نص عادي يحتوي على تفاصيل مثل اسم المنتج، عدد المطورين المرخص لهم، تاريخ انتهاء الاشتراك، وما إلى ذلك. الملف موقع رقمياً، لذا لا تقم بتعديل الملف؛ حتى الإضافة غير المقصودة لسطر جديد إضافي في الملف ستؤدي إلى إبطاله.

تحتاج إلى تعيين ترخيص قبل تنفيذ أي عمليات على المستندات. يُطلب منك تعيين الترخيص مرة واحدة فقط لكل تطبيق أو عملية.

يمكن تحميل الترخيص من تدفق أو ملف في المواقع التالية:

1. مسار صريح.
1. المجلد الذي يحتوي على aspose-pdf-xx.x.jar.

استخدم طريقة License.setLicense لترخيص المكوّن. غالبًا ما تكون أسهل طريقة لتعيين الترخيص هي وضع ملف الترخيص في نفس المجلد مع Aspose.PDF.jar وتحديد اسم الملف فقط دون المسار كما هو موضح في المثال التالي:

{{% alert color="primary" %}}

بدءًا من Aspose.PDF for Java 4.2.0، تحتاج إلى استدعاء أسطر الكود التالية لتهيئة الترخيص.

{{% /alert %}}

### تحميل ترخيص من ملف

في هذا المثال **Aspose.PDF** سيحاول العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JAR لتطبيقك.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### تحميل الترخيص من كائن تدفق

المثال التالي يوضح كيفية تحميل الترخيص من تدفق.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### تحقق من الترخيص

من الممكن التحقق مما إذا كان الترخيص قد تم ضبطه بشكل صحيح أم لا. تحتوي الفئة Document على الطريقة isLicensed التي ستعيد true إذا تم ضبط الترخيص بشكل صحيح.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## ترخيص مقنن

Aspose.PDF تسمح للمطورين بتطبيق مفتاح مقنن. إنها آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة إلى جانب طريقة الترخيص الحالية. يمكن للعملاء الذين يرغبون في الفوترة بناءً على استخدام ميزات API استخدام الترخيص المقنن.В For more details, please refer toВ [الأسئلة الشائعة حول الترخيص المقنن](https://purchase.aspose.com/faqs/licensing/metered)В القسم.

فئة جديدةВ [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В تم تقديمه لتطبيق المفتاح المقاس. التالي هو رمز العينة الذي يوضح كيفية ضبط المفتاح العمومي والخاص المقاس.

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
- **استخدم اسم الفئة الكامل للترخيص.** كل منتج Aspose يحتوي على فئة **License** في مساحة الاسم الخاصة به. على سبيل المثال، Aspose.PDF لديه فئة **com.aspose.pdf.License** و Aspose.Words لديه فئة **com.aspose.words.License**. يتيح لك استخدام اسم الفئة الكامل تجنب أي لبس بشأن الترخيص المطبق على أي منتج.

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
