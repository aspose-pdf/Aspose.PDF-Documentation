---
title: Aspose.PDF Java للـ Jython
linktitle: Aspose.PDF Java للـ Jython
type: docs
weight: 60
url: /ar/java/aspose-pdf-java-for-jython/
description: اجمع بين قوة Aspose.PDF for Java و Jython. قم بالتعامل بسهولة مع ملفات PDF في بيئة Java مستندة إلى Python.
lastmod: "2026-10-01"
---
## مقدمة

### ما هو Jython؟

Jython هو تنفيذ Java للغة Python يجمع بين القوة التعبيرية والوضوح. Jython متاح مجانًا لكل من الاستخدام التجاري وغير التجاري ويُوزَّع مع شفرة المصدر. Jython يكمل Java ومناسب خصيصًا للمهام التالية:

- **البرمجة المدمجة** - يمكن لمبرمجي Java إضافة مكتبات Jython إلى نظامهم للسماح للمستخدمين النهائيين بكتابة سكريبتات بسيطة أو معقدة تضيف وظائف إلى التطبيق.
- **التجربة التفاعلية** - Jython يوفر مفسراً تفاعلياً يمكن استخدامه للتفاعل مع حزم Java أو مع تطبيقات Java القيد التشغيل. يتيح ذلك للمبرمجين تجربة وتصحيح أي نظام Java باستخدام Jython.
- **التطوير السريع للتطبيقات** - برامج Python عادةً ما تكون أقصر بمقدار 2-10 مرات مقارنةً بالبرنامج المكافئ في Java. هذا يترجم مباشرةً إلى زيادة إنتاجية المبرمج. التفاعل السلس بين Python و Java يتيح للمطورين خلط اللغتين بحرية أثناء التطوير وكذلك عند إصدار المنتجات.

### Aspose.PDF for Java

Aspose.PDF for Java هو مكوّن إنشاء مستندات PDF يتيح لتطبيقات Java الخاصة بك قراءة وكتابة ومعالجة مستندات PDF دون الحاجة إلى استخدام Adobe Acrobat.

Aspose.PDF for Java هو مكوّن بسعر معقول يقدم مجموعة هائلة من الميزات، والتي تشمل: خيارات ضغط PDF، إنشاء الجداول ومعالجتها، دعم الرسوم البيانية، وظائف الصور، وظائف الروابط التشعبية الواسعة، ضوابط أمان موسّعة، ومعالجة الخطوط المخصصة.

Aspose.PDF for Java يتيح لك إنشاء ملفات PDF مباشرةً من خلال واجهة برمجة التطبيقات (API) والقوالب XML المقدمة. استخدام Aspose.PDF for Java سيمكنك أيضًا من إضافة إمكانات PDF إلى تطبيقاتك في وقت قصير.

### Aspose.PDF Java للـ Jython

Aspose.PDF Java for Jython هو مشروع يوضح / يوفر أمثلة استخدام واجهة برمجة التطبيقات Aspose.PDF for Java في Jython.

## متطلبات النظام والمنصات المدعومة

### متطلبات النظام

المتطلبات التالية للنظام لاستخدام Aspose.PDF Java for Jython:

- Java 1.5 أو أعلى مثبتة
- تم تنزيل مكوّن Aspose.PDF
- Jython 2.7.0

### المنصات المدعومة

المنصات المدعومة هي التالية:

- Aspose.PDF 15.4 وما فوق.
- بيئة تطوير Java (Eclipse, NetBeans ...)

## تنزيل التثبيت والاستخدام

### التنزيل

الإصدارات التالية من الأمثلة القابلة للتنفيذ متاحة للتنزيل من GitHub:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose-Pdf-Java-for-Jython)

تنزيل مكوّن Aspose.PDF for Java:

- [Aspose.PDF for Java](https://downloads.aspose.com/pdf/java)

### التثبيت

- ضع ملف jar الخاص بـ Aspose.PDF for Java الذي تم تنزيله في دليل "lib".
- استبدل "your-lib" باسم ملف jar الذي تم تنزيله في ملف _*init*_.py.

### باستخدام

يمكنك تحويل ملف Pdf إلى مستند doc باستخدام مثال الشيفرة التالي:

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

## الدعم، التوسّع والمساهمة

### الدعم

منذ الأيام الأولى لشركة Aspose، كنا نعلم أن مجرد تقديم منتجات جيدة لعملائنا لن يكون كافيًا. كنا بحاجة أيضًا إلى تقديم خدمة جيدة. نحن مطورون بأنفسنا ونفهم مدى الإحباط عندما توقف مشكلة تقنية أو خلل في البرنامج عن قيامك بما تحتاج إلى القيام به. نحن هنا لحل المشكلات، لا لخلقها.

لهذا السبب نقدم دعمًا مجانيًا. أي شخص يستخدم منتجنا، سواءً كان قد اشتراه أو يستخدم نسخة تجريبية، يستحق كامل اهتمامنا واحترامنا.

يمكنك تسجيل أي مشاكل أو اقتراحات متعلقة بـ Aspose.PDF Java for Jython باستخدام أيٍ من المنصات التالية:

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

### التوسيع والمساهمة

Aspose.PDF Java for Jython هو برنامج مفتوح المصدر ورمز المصدر الخاص به متاح على مواقع الترميز الاجتماعية الكبرى المذكورة أدناه. يُشجّع المطورون على تنزيل رمز المصدر والمساهمة من خلال اقتراح أو إضافة ميزة جديدة أو تحسين الميزات الحالية، حتى يتمكن الآخرون أيضًا من الاستفادة منه.

### الكود المصدري

يمكنك الحصول على أحدث الكود المصدري من أحد المواقع التالية

- [GitHub](https://github.com/aspose-pdf/Aspose.PDF-for-Java)
