---
title: الدعم، التوسيع والمساهمة في Aspose.Pdf في Struts
type: docs
weight: 20
url: /ar/java/support-extend-and-contribute-to-aspose-pdf-in-struts/
lastmod: "2021-06-05"
---

## الدعم

{{% alert color="primary" %}}

- إذا كنت ترغب في رؤية المشاكل المعروفة / المبلغ عنها (من قبل المستخدمين أو فريق Q.A) في التطبيق.
- أو إذا كنت ترغب في الإبلاغ عن أي مشكلة وجدتها في التطبيق
- لديك أي اقتراح تحسين أو ترغب في تقديم طلب ميزة

يرجى استخدام أي من متتبعات المشاكل للمشروع التالية:

- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/issues)

{{% /alert %}}


## التوسيع والمساهمة

Aspose.PDF Java لـ Struts 1.3 مفتوح المصدر وكود المصدر متاح على مواقع الترميز الاجتماعي الرئيسية المدرجة أدناه. يُشجع المطورون على تنزيل كود المصدر والمساهمة من خلال اقتراح أو إضافة ميزات جديدة أو تحسين الميزات الحالية، حتى يستفيد الآخرون منها أيضًا.

## كود المصدر

يمكنك الحصول على أحدث كود مصدر من أحد المواقع التالية

- [CodePlex](https://asposepdfforstruts.codeplex.com)
- [Github](https://github.com/aspose-pdf/Aspose.PDF-for-Java/tree/master/Plugins/Aspose_Pdf_for_Struts)

changefreq: "monthly"

type: docs

```java
// تحميل المستند
Document pdfDocument = new Document("input.pdf");

// الحصول على عدد الصفحات
int pageCount = pdfDocument.getPages().size();

// عرض عدد الصفحات
System.out.println("عدد الصفحات: " + pageCount);
```

```yaml
key: هذا مثال على كيفية تحميل مستند وحساب عدد الصفحات
```

```json
{
  "key": "هذه بيانات تجريبية ولا تمثل مستندًا حقيقيًا"
}