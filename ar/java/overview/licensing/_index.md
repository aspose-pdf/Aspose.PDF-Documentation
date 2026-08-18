---
title: Aspose PDF الترخيص
linktitle: الترخيص والقيود
type: docs
weight: 50
url: /java/licensing/
description: يدعو Aspose.PDF for Python عملائه للحصول على ترخيص كلاسيكي. بالإضافة إلى استخدام ترخيص محدود لاستكشاف المنتج بشكل أفضل.
lastmod: "2026-06-09"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ترخيص Aspose.PDF لجافا
Abstract: تتناول المقالة القيود وخيارات الترخيص لـ Aspose.PDF لـ Python. ويسلط الضوء على أن الإصدار التقييمي يسمح باختبار الوظائف الكاملة ولكنه يضيف علامة مائية إلى ملفات PDF التي تم إنشاؤها، مع الإشارة إلى "التقييم فقط" إلى جانب معلومات حقوق الطبع والنشر. بالنسبة للمستخدمين الراغبين في الاختبار بدون هذه القيود، يتوفر ترخيص مؤقت لمدة 30 يومًا. تشرح المقالة أيضًا كيفية تنفيذ الترخيص الكلاسيكي عن طريق تحميله من ملف أو دفق، وتوصي بوضع ملف الترخيص في نفس الدليل مثل ملف Aspose.PDF.dll وتعيين الترخيص باستخدام الفئة `Aspose.Pdf.License`. يتم توفير مقتطفات من التعليمات البرمجية لتوضيح عملية الترخيص.
---
## القيود المفروضة على نسخة التقييم

نريد أن يقوم عملاؤنا باختبار مكوناتنا بدقة قبل الشراء حتى يسمح لك الإصدار التقييمي باستخدامها كما تفعل عادةً.

- **تم إنشاء ملف PDF بعلامة مائية للتقييم.** يوفر الإصدار التقييمي من Aspose.PDF لـ Java وظائف كاملة للمنتج، ولكن يتم وضع علامة مائية على جميع الصفحات الموجودة في مستندات PDF التي تم إنشاؤها مع عبارة "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2020 Aspose Pty Ltd" في الجزء العلوي.

- **الحد الأقصى لعدد عناصر المجموعة التي يمكن معالجتها.**
في النسخة التقييمية من أي مجموعة، يمكنك معالجة أربعة عناصر فقط (على سبيل المثال، 4 صفحات فقط، 4 حقول نموذج، وما إلى ذلك).

يمكنك تنزيل نسخة تقييمية من **Aspose.PDF** لـ Java من [Aspose Repository](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-pdf). يوفر الإصدار التقييمي نفس الإمكانيات تمامًا مثل الإصدار المرخص للمنتج. علاوة على ذلك، يصبح الإصدار التقييمي مرخصًا ببساطة عند شراء ترخيص وإضافة سطرين من التعليمات البرمجية لتطبيق الترخيص.

بمجرد أن تكون راضيًا عن تقييمك لـ **Aspose.PDF**، يمكنك [شراء ترخيص](https://purchase.aspose.com/) على موقع Aspose الإلكتروني. تعرف على أنواع الاشتراكات المختلفة المقدمة. إذا كانت لديك أي أسئلة، فلا تتردد في الاتصال بفريق مبيعات Aspose.

يحمل كل ترخيص Aspose اشتراكًا لمدة عام واحد للحصول على ترقيات مجانية لأي إصدارات أو إصلاحات جديدة يتم طرحها خلال هذا الوقت. الدعم الفني مجاني وغير محدود ويتم توفيره للمستخدمين المرخصين والمقيمين.

>إذا كنت تريد اختبار Aspose.PDF لـ Java دون قيود الإصدار التقييمي، فيمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا. يرجى الرجوع إلى [كيفية الحصول على ترخيص مؤقت؟](https://purchase.aspose.com/temporary-license)

## الترخيص الكلاسيكي

يمكن تحميل الترخيص من ملف أو كائن دفق. أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل ملف Aspose.PDF.dll وتحديد اسم الملف بدون مسار، كما هو موضح في المثال أدناه.

الترخيص عبارة عن ملف XML نصي عادي يحتوي على تفاصيل مثل اسم المنتج وعدد المطورين المرخص لهم وتاريخ انتهاء صلاحية الاشتراك وما إلى ذلك. تم توقيع الملف رقميًا، لذا لا تقم بتعديل الملف؛ حتى الإضافة غير المقصودة لفاصل أسطر إضافي في الملف ستؤدي إلى إبطاله.

تحتاج إلى تعيين ترخيص قبل إجراء أي عمليات مع المستندات. لا يُطلب منك سوى تعيين ترخيص مرة واحدة لكل تطبيق أو عملية.

يمكن تحميل الترخيص من دفق أو ملف في المواقع التالية:

1. المسار الصريح.
1. المجلد الذي يحتوي على ملف aspose-pdf-xx.x.jar.

استخدم الأسلوب License.setLicense لترخيص المكون. غالبًا ما تكون أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل Aspose.PDF.jar وتحديد اسم الملف فقط بدون مسار كما هو موضح في المثال التالي:

{{% alert color="primary" %}}

بدءًا من Aspose.PDF لـ Java 4.2.0، يتعين عليك استدعاء أسطر التعليمات البرمجية التالية لتهيئة الترخيص.

{{% /alert %}}

### تحميل الترخيص من الملف

في هذا المثال، سيحاول **Aspose.PDF** العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JAR الخاصة بتطبيقك.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Call setLicense method to set license
license.setLicense("Aspose.Pdf.Java.lic");
```

### تحميل الترخيص من كائن دفق

يوضح المثال التالي كيفية تحميل ترخيص من الدفق.

```java
// Initialize License Instance
com.aspose.pdf.License license = new com.aspose.pdf.License();
// Set license from Stream
license.setLicense(new java.io.FileInputStream("Aspose.Pdf.Java.lic"));
```

### التحقق من صحة الترخيص

من الممكن التحقق مما إذا كان الترخيص قد تم ضبطه بشكل صحيح أم لا. تحتوي فئة المستند على الأسلوب isLicensed الذي سيعود صحيحًا إذا تم تعيين الترخيص بشكل صحيح.

```java
License license = new License();
license.setLicense("Aspose.Pdf.Java.lic");
// Check if license has been validated
if (com.aspose.pdf.Document.isLicensed()) {
    System.out.println("License is Set!");
}
```

## الترخيص المقنن

يسمح Aspose.PDF للمطورين بتطبيق المفتاح المقنن. إنها آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة مع طريقة الترخيص الحالية. يمكن للعملاء الذين يريدون أن تتم محاسبتهم على أساس استخدام ميزات واجهة برمجة التطبيقات استخدام الترخيص المقنن. لمزيد من التفاصيل، يرجى الرجوع إلى قسم الأسئلة الشائعة حول الترخيص المقنن](https://purchase.aspose.com/faqs/licensing/metered)В.

تم تقديم فئة جديدة В [Metered](https://reference.aspose.com/pdf/java/com.aspose.pdf/Metered)В لتطبيق المفتاح المقنن. فيما يلي نموذج التعليمات البرمجية الذي يوضح كيفية تعيين المفتاح العام والخاص.

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

إذا كنت تستخدم العديد من منتجات Aspose في تطبيقك، على سبيل المثال Aspose.PDF وAspose.Words، فإليك بعض النصائح المفيدة.

- **قم بتعيين الترخيص لكل منتج Aspose بشكل منفصل.** حتى إذا كان لديك ملف ترخيص واحد لجميع المكونات، على سبيل المثال 'Aspose.Total.lic'، فلا تزال بحاجة إلى الاتصال بـ **License.SetLicense** بشكل منفصل لكل منتج Aspose الذي تستخدمه في تطبيقك.
- **استخدم اسم فئة الترخيص المؤهل بالكامل.** يحتوي كل منتج من منتجات Aspose على فئة **الترخيص** في مساحة الاسم الخاصة به. على سبيل المثال، يحتوي Aspose.PDF على فئة **com.aspose.pdf.License** وAspose.Words يحتوي على فئة **com.aspose.words.License**. يتيح لك استخدام اسم الفئة المؤهل بالكامل تجنب أي ارتباك حول الترخيص المطبق على أي منتج.

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
