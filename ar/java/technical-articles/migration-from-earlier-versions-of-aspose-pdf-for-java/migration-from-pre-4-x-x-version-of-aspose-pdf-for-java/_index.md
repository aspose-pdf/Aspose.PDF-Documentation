---
title: الهجرة من الإصدار ما قبل 4.x.x من Aspose.PDF لـ Java
type: docs
weight: 20
url: /ar/java/migration-from-pre-4-x-x-version-of-aspose-pdf-for-java/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

تم إصدار نسخة جديدة من Aspose.PDF لـ Java وتم الآن دعم القدرة على إنشاء مستندات PDF من الصفر وكذلك توفير القدرة على معالجة مستندات PDF الموجودة.

{{% /alert %}}

## ملفات المنتج الثنائية

{{% alert color="primary" %}}

في إصدار النسخة الأولى (v4.0.0)، نقوم بشحن ملفين jar وهما **aspose.pdf-3.3.0.jdk15.jar** و **aspose.pdf-new-4.0.0.jar**.
{{% /alert %}}

- **aspose.pdf-3.3.0.jdk14.jar**

هذا الملف jar هو نفس إصدار المنتج المتاح حاليًا تحت وحدة التنزيل بعنوان [Aspose.PDF for java 3.3.0](http://www.aspose.com/community/files/72/java-components/aspose.pdf-for-java/entry417659.aspx). في المستقبل، سنطلق على هذا الإصدار إصدار Aspose.PDF for Java القديم. في هذا الإصدار الأول، قد لا يتأثر المستخدمون الحاليون لـ Aspose.PDF for Java لأنهم يحصلون على نفس إصدار الإصدار. ومع ذلك، في وقت قريب، سنقوم بإزالة هذا الملف jar المنفصل وستصبح جميع الفئات والتعدادات الخاصة بـ Aspose.PDF for Java القديم (قبل 4.x.x) متاحة تحت حزمة com.aspose.pdf.generator في ملف aspose.pdf-new-4.x.x.jar الوحيد.
- **aspose.pdf-new-4.0.0.jar**
  هذا الملف jar هو إصدار جديد حقيقي تم نقله تلقائيًا من Aspose.PDF for .NET إلى منصة Java.
 هذا الملف jar يحتوي على النموذج الجديد لمستند Document Object Model (DOM) لإنشاء وكذلك معالجة ملفات PDF الحالية وأيضًا Aspose.PDF.Kit الحالي لجافا. جميع الفئات والتعدادات لـ Aspose.PDF.Kit لجافا مجمعة تحت حزمة com.aspose.pdf.facades وفي الربع الثالث من عام 2013، سيتم إيقاف Aspose.PDF.Kit لجافا. لذلك نشجع عملائنا الحاليين لـ Aspose.PDF.Kit لجافا على محاولة ترحيل كودهم إلى الإصدار المحوّل تلقائيًا الجديد.

يرجى الاطلاع على منشور المدونة التالي للحصول على مزيد من الفهم حول هيكل Aspose.PDF المحوّل تلقائيًا لجافا.