---
title: Aspose.PDF جافا لجيثون
linktitle: Aspose.PDF جافا لجيثون
type: docs
weight: 60
url: /java/aspose-pdf-java-for-jython/
description: اجمع بين قوة Aspose.PDF لـ Java مع Jython. يمكنك معالجة ملفات PDF بسهولة في بيئة Java المستندة إلى Python.
lastmod: "2026-06-09"
---
## مقدمة

### ما هو جيثون؟

Jython هو تطبيق Java لـ Python يجمع بين القوة التعبيرية والوضوح. Jython متاح مجانًا للاستخدام التجاري وغير التجاري ويتم توزيعه مع كود المصدر. يعد Jython مكملاً لـ Java وهو مناسب بشكل خاص للمهام التالية:

- **البرمجة النصية المضمنة** - يمكن لمبرمجي Java إضافة مكتبات Jython إلى نظامهم للسماح للمستخدمين النهائيين بكتابة نصوص برمجية بسيطة أو معقدة تضيف وظائف إلى التطبيق.
- **التجريب التفاعلي** - توفر Jython مترجمًا تفاعليًا يمكن استخدامه للتفاعل مع حزم Java أو تشغيل تطبيقات Java. يتيح ذلك للمبرمجين تجربة وتصحيح أي نظام Java باستخدام Jython.
- **التطوير السريع للتطبيقات** - عادةً ما تكون برامج Python أقصر بمقدار 2 إلى 10 مرات من برنامج Java المكافئ. وهذا يترجم مباشرة إلى زيادة إنتاجية المبرمج. يتيح التفاعل السلس بين Python وJava للمطورين إمكانية مزج اللغتين بحرية أثناء التطوير وفي شحن المنتجات.

### Aspose.PDF لجافا

Aspose.PDF for Java هو أحد مكونات إنشاء مستندات PDF التي تمكن تطبيقات Java الخاصة بك من قراءة مستندات PDF وكتابتها ومعالجتها دون استخدام Adobe Acrobat.

يعد Aspose.PDF for Java مكونًا بسعر معقول يوفر ثروة لا تصدق من الميزات، بما في ذلك: خيارات ضغط PDF، وإنشاء الجدول ومعالجته، ودعم الرسم البياني، ووظائف الصور، ووظيفة الارتباط التشعبي الشاملة، وضوابط الأمان الموسعة، ومعالجة الخطوط المخصصة.

يتيح لك Aspose.PDF for Java إنشاء ملفات PDF مباشرة من خلال قوالب API وXML المتوفرة. سيمكنك استخدام Aspose.PDF لـ Java أيضًا من إضافة إمكانيات PDF إلى تطبيقاتك في وقت قصير جدًا.

### Aspose.PDF جافا لجيثون

Aspose.PDF Java for Jython هو مشروع يوضح/يوفر أمثلة استخدام Aspose.PDF لـ Java API في Jython.

## متطلبات النظام والمنصات المدعومة

### متطلبات النظام

فيما يلي متطلبات النظام لاستخدام Aspose.PDF Java لـ Jython:

- تم تثبيت Java 1.5 أو أعلى
- تم تنزيل مكون Aspose.PDF
- جيثون 2.7.0

### المنصات المدعومة

فيما يلي المنصات المدعومة:

- Aspose.PDF 15.4 وما فوق.
- Java IDE (Eclipse، NetBeans ...)

## تنزيل التثبيت والاستخدام

### جاري التحميل

الإصدارات التالية من الأمثلة قيد التشغيل متاحة للتنزيل من GitHub:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

تنزيل Aspose.PDF لمكون Java:

- [Aspose.PDF لجافا](https://downloads.aspose.com/pdf/java)

### التثبيت

- ضع ملف Aspose.PDF لـ Java jar الذي تم تنزيله في الدليل "lib".
- استبدل "your-lib" باسم ملف jar الذي تم تنزيله في ملف _*init*_.py.

### استخدام

يمكنك تحويل ملف Pdf إلى مستند doc باستخدام كود المثال التالي:

```java
from aspose-pdf import Settings
from com.aspose.pdf import Document

class PdfToDoc:

    def __init__(self):
        dataDir = Settings.dataDir + 'WorkingWithDocumentConversion/PdfToDoc/'

        # Open the target document
        pdf = Document(dataDir + 'input1.pdf')

        # Save the concatenated output file (the target document)
        pdf.save(dataDir + "output.doc")

        print "Document has been converted successfully"

if __name__ == '__main__':

    PdfToDoc()
```

## الدعم والتوسيع والمساهمة

### يدعم

منذ الأيام الأولى لـ Aspose، كنا نعلم أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافيًا. نحن بحاجة أيضًا إلى تقديم خدمة جيدة. نحن مطورون بأنفسنا ونتفهم مدى الإحباط الذي تشعر به عندما تمنعك مشكلة فنية أو خلل في البرنامج من القيام بما تحتاج إلى القيام به. نحن هنا لحل المشاكل وليس خلقها.

ولهذا السبب نقدم الدعم المجاني. أي شخص يستخدم منتجنا، سواء كان قد اشتراه أو يستخدم التقييم، يستحق اهتمامنا واحترامنا الكاملين.

يمكنك تسجيل أي مشكلات أو اقتراحات تتعلق بـ Aspose.PDF Java for Jython باستخدام أي من الأنظمة الأساسية التالية:

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### توسيع والمساهمة

Aspose.PDF Java for Jython مفتوح المصدر وكود المصدر الخاص به متاح على مواقع البرمجة الاجتماعية الرئيسية المدرجة أدناه. يتم تشجيع المطورين على تنزيل الكود المصدري والمساهمة من خلال اقتراح أو إضافة ميزات جديدة أو تحسين الميزات الموجودة، حتى يتمكن الآخرون أيضًا من الاستفادة منها.

### كود المصدر

يمكنك الحصول على أحدث كود المصدر من أحد المواقع التالية

- [جيثب](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
