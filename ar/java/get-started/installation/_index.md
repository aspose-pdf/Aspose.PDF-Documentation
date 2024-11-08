---
title: Install Aspose.PDF for Java
linktitle: Installation
type: docs
weight: 20
url: /ar/java/installation/
description: يوضح هذا القسم وصف المنتج وتعليمات تثبيت Aspose.PDF for Java بنفسك، بالإضافة إلى استخدام NuGet.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## مكون Aspose.PDF for Java

{{% alert color="primary" %}}

**Aspose.PDF هو مكون جافا** مصمم للسماح للمطورين بإنشاء مستندات PDF، سواء كانت بسيطة أو معقدة، برمجياً في الوقت الفعلي. يمكن للمطورين باستخدام Aspose.PDF for Java إدراج جداول، رسوم بيانية، صور، روابط تشعبية، خطوط مخصصة - وأكثر - في مستندات PDF. علاوة على ذلك، يمكن أيضاً ضغط مستندات PDF. يوفر Aspose.PDF for Java ميزات أمان ممتازة لتطوير مستندات PDF آمنة. وأبرز ميزة مختلفة في Aspose.PDF for Java هي أنه يدعم إنشاء مستندات PDF من خلال واجهة برمجة التطبيقات ومن قوالب XML.

{{% /alert %}}

## وصف المنتج

**Aspose.PDF for Java** يتم تنفيذه باستخدام Java ويعمل مع JDK 1.8 وما فوق. يمكن دمج Aspose.PDF for Java مع أي تطبيق، على سبيل المثال تطبيق ويب JSP/JSF أو تطبيق Windows.

**Aspose.PDF for Java** سريع وخفيف الوزن. يقوم بإنشاء مستندات PDF بكفاءة ويساعد تطبيقك على الأداء بشكل أفضل. Aspose.PDF for Java هو الخيار الأول لعملائنا عند إنشاء مستندات PDF بسبب سعره، أدائه الرائع ودعمه الممتاز. باستخدام هذه المكتبة، يمكنك تنفيذ قدرات غنية لإنشاء ملفات PDF من البداية، أو معالجة مستندات PDF الحالية بالكامل دون تثبيت Adobe Acrobat.

# التثبيت

## تقييم Aspose.PDF for Java

{{% alert color="primary" %}}

يمكنك تنزيل [Aspose.PDF for Java](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/) للتقييم.
 تنزيل التقييم هو نفس تنزيل النسخة المشتراة. ببساطة تصبح نسخة التقييم مرخّصة عندما تضيف بعض الأسطر من الكود لـ [تطبيق الترخيص](/pdf/ar/java/licensing/).

نسخة التقييم من Aspose.PDF توفر كامل وظائف المنتج، لكنها تحتوي على حدّين:
{{% /alert %}}

- تقوم بإدخال علامة مائية للتقييم.
- لا يمكن عرض/تحرير أكثر من أربعة عناصر من أي مجموعة.
- **مستند يظهر علامة مائية للتقييم**

![تقييم Aspose.PDF](evaluate-aspose-pdf_1.png)

إذا كنت ترغب في اختبار Aspose.PDF for Java بدون حدود نسخة التقييم، يمكنك أيضًا طلب رخصة مؤقتة لمدة 30 يومًا. يرجى الرجوع إلى [كيف تحصل على رخصة مؤقتة؟](https://purchase.aspose.com/temporary-license)

## تثبيت Aspose.PDF لـ Java من مستودع Aspose

تستضيف Aspose جميع واجهات برمجة التطبيقات لـ Java على [مستودع Aspose](https://releases.aspose.com/java/repo/com/aspose/aspose-pdf/). يمكنك بسهولة استخدام Aspose.PDF لواجهة برمجة التطبيقات Java مباشرة في مشاريع Maven الخاصة بك مع تكوينات بسيطة.

### تحديد تكوين مستودع Aspose

أولاً تحتاج إلى تحديد تكوين / موقع مستودع Aspose في ملف pom.xml الخاص بك كما يلي:

```xml
 <repositories>
    <repository>
        <id>AsposeJavaAPI</id>
        <name>Aspose Java API</name>
        <url>https://releases.aspose.com/java/repo/</url>
    </repository>
</repositories>
```

### تعريف اعتماد Aspose.PDF لواجهة برمجة التطبيقات Java

ثم قم بتعريف اعتماد Aspose.PDF لواجهة برمجة التطبيقات Java في ملف pom.xml الخاص بك كما يلي:

```xml
 <dependencies>
    <dependency>
        <groupId>com.aspose</groupId>
        <artifactId>aspose-pdf</artifactId>
        <version>21.7</version>
    </dependency>
</dependencies>
```

بعد تنفيذ الخطوات المذكورة أعلاه، سيتم في النهاية تعريف اعتماد Aspose.PDF لواجهة برمجة التطبيقات Java في مشروع Maven الخاص بك.

### التوافق مع JDK 11 وإرشادات الاستخدام

تم تحسين واجهة برمجة التطبيقات لبيئة Java 11 وجميع الاختبارات والوظائف تعمل بشكل جيد. ومع ذلك، لبعض الفئات يجب عليك إضافة التبعية الخارجية لإضافة مسار الفئة للفئة: javax.xml.bind.annotation.adapters.HexBinaryAdapter، والتي تم حذفها من JRE.

على سبيل المثال:

```xml
<dependency>
    <groupId>javax.xml.bind</groupId>
    <artifactId>jaxb-api</artifactId>
    <version>2.3.0</version>
</dependency>
```