---
title: البحث والحصول على النص من صفحات مستند PDF
linktitle: البحث والحصول على النص
type: docs
weight: 60
url: /ar/java/search-and-get-text-from-pdf/
description: توضح هذه المقالة كيفية استخدام أدوات مختلفة للبحث والحصول على نص من مستندات PDF. يمكننا البحث باستخدام التعبير العادي من صفحات معينة أو كاملة.
lastmod: "2021-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## البحث والحصول على النص من جميع صفحات مستند PDF

يسمح لك TextFragmentAbsorber بالعثور على النص، الذي يطابق عبارة معينة، من جميع صفحات مستند PDF.

للبحث عن نص في المستند بأكمله، قم باستدعاء طريقة accept() لمجموعة [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
 The [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) تأخذ الطريقة كائن TextFragmentAbsorber كمعامل، والذي يعيد مجموعة من كائنات TextFragment. قم بالتكرار عبر جميع الشظايا للحصول على خصائصها، على سبيل المثال النص، الموضع، XIndent، YIndent، اسم الخط، حجم الخط، إمكانية الوصول، التضمين، الجزء الفرعي، اللون الأمامي، إلخ.

يُظهر مقطع الشيفرة التالي كيفية البحث في المستند بأكمله وعرض جميع التطابقات في وحدة التحكم.

```java
// افتح المستند
Document pdfDocument = new Document("input.pdf");

// أنشئ كائن TextAbsorber للعثور على جميع حالات عبارة البحث المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// اقبل الممتص لجميع الصفحات
pdfDocument.getPages().accept(textFragmentAbsorber);

// احصل على الشظايا النصية المستخرجة في مجموعة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// قم بالتكرار عبر الشظايا
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("النص :- " + textFragment.getText());
    System.out.println("الموضع :- " + textFragment.getPosition());
    System.out.println("الإزاحة الأفقية :- " + textFragment.getPosition().getXIndent());
    System.out.println("الإزاحة العمودية :- " + textFragment.getPosition().getYIndent());
    System.out.println("الخط - الاسم :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("الخط - إمكانية الوصول :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("الخط - مدمج - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("الخط - جزء فرعي :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("حجم الخط :- " + textFragment.getTextState().getFontSize());
    System.out.println("اللون الأمامي :- " + textFragment.getTextState().getForegroundColor());
}
```

للبحث عن نص في صفحة معينة والحصول على الخصائص المرتبطة به، حدد فهرس الصفحة:

```java
// قبول المستخلص للصفحة الأولى من المستند
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## البحث واستخراج مقاطع النص من صفحات PDF

للبحث عن مقاطع النص في جميع صفحات المستند، احصل على كائنات TextFragment الخاصة بالمستند.

يسمح لك TextFragmentAbsorber بالعثور على النص، الذي يطابق عبارة معينة، من جميع الصفحات في مستند PDF. للبحث عن النص في المستند بأكمله، استدعِ طريقة [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) الخاصة بمجموعة [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection). تأخذ طريقة [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) كائن TextFragmentAbsorber كمعامل، والذي يعيد مجموعة من كائنات TextFragment.

{{% alert color="primary" %}}

عندما يتم جلب مجموعة TextFragmentCollection من المستند، قم بالتكرار خلالها للحصول على مجموعة TextSegmentCollection لكل كائن TextFragment.
 بعد ذلك، يمكنك الحصول على خصائص كائن TextSegment الفردي.

{{% /alert %}}

يظهر مقتطف الشيفرة التالي كيفية البحث عن أجزاء النص في جميع الصفحات.

```java
// فتح المستند
Document pdfDocument = new Document("input.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع حالات عبارة البحث المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("sample");

// قبول الممتص للصفحة الأولى من المستند
pdfDocument.getPages().accept(textFragmentAbsorber);

// الحصول على أجزاء النص المستخرجة في مجموعة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// حلقة من خلال أجزاء النص
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    // تكرار عبر أجزاء النص
    for (TextSegment textSegment : (Iterable<TextSegment>) textFragment.getSegments()) {
        System.out.println("النص :- " + textSegment.getText());
        System.out.println("الموضع :- " + textSegment.getPosition());
        System.out.println("إزاحة X :- " + textSegment.getPosition().getXIndent());
        System.out.println("إزاحة Y :- " + textSegment.getPosition().getYIndent());
        System.out.println("الخط - الاسم :- " + textSegment.getTextState().getFont().getFontName());
        System.out.println("الخط - متاح :- " + textSegment.getTextState().getFont().isAccessible());
        System.out.println("الخط - مضمن - " + textSegment.getTextState().getFont().isEmbedded());
        System.out.println("الخط - فرعي :- " + textSegment.getTextState().getFont().isSubset());
        System.out.println("حجم الخط :- " + textSegment.getTextState().getFontSize());
        System.out.println("لون المقدمة :- " + textSegment.getTextState().getForegroundColor());
    }
}
```

للبحث عن جزء نصي محدد والحصول على الخصائص المرتبطة به، حدد مؤشر الصفحة للصفحة التي تريد البحث فيها:

```java
// قبول المستخلص للصفحة الأولى من المستند.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber);
```

## البحث والحصول على النص من الصفحات باستخدام التعبير العادي

يساعدك TextFragmentAbsorber في البحث واسترجاع النص من جميع الصفحات في مستند، استنادًا إلى تعبير عادي.

للبحث والحصول على النص من مستند:

1. مرر مصطلح البحث كتعبير عادي إلى منشئ TextFragmentAbsorber.
2. قم بتعيين خاصية TextSearchOptions لكائن TextFragmentAbsorber.
   تتطلب هذه الخاصية كائن TextSearchOptions: مرر true إلى منشئها عند إنشاء كائن جديد.
3. لاسترجاع النص المطابق من جميع الصفحات، استدع طريقة [accept()](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextFragmentAbsorber) لمجموعة [Pages](https://reference.aspose.com/pdf//java/com.aspose.pdf/pagecollection).

   تعيد TextFragmentAbsorber مجموعة TextFragmentCollection تحتوي على جميع الأجزاء المطابقة للمعايير المحددة بواسطة التعبير العادي.

يوضح مقتطف الشيفرة التالي كيفية البحث في جميع الصفحات في مستند والحصول على النص بناءً على تعبير منتظم.

```java
// فتح مستند
Document pdfDocument = new Document("source.pdf");

// إنشاء كائن TextAbsorber للعثور على جميع حالات عبارة البحث المدخلة
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("\\d{4}-\\d{4}"); // مثل 1999-2000

// تعيين خيار البحث النصي لتحديد استخدام التعبير المنتظم
TextSearchOptions textSearchOptions = new TextSearchOptions(true);
textFragmentAbsorber.setTextSearchOptions(textSearchOptions);

// قبول الممتص لأول صفحة من المستند
pdfDocument.getPages().accept(textFragmentAbsorber);

// الحصول على شظايا النص المستخرجة في مجموعة
TextFragmentCollection textFragmentCollection = textFragmentAbsorber.getTextFragments();

// التجول عبر الشظايا
for (TextFragment textFragment : (Iterable<TextFragment>) textFragmentCollection) {
    System.out.println("النص :- " + textFragment.getText());
    System.out.println("الموضع :- " + textFragment.getPosition());
    System.out.println("XIndent :- " + textFragment.getPosition().getXIndent());
    System.out.println("YIndent :- " + textFragment.getPosition().getYIndent());
    System.out.println("الخط - الاسم :- " + textFragment.getTextState().getFont().getFontName());
    System.out.println("الخط - متاح :- " + textFragment.getTextState().getFont().isAccessible());
    System.out.println("الخط - مضمن - " + textFragment.getTextState().getFont().isEmbedded());
    System.out.println("الخط - مجموعة فرعية :- " + textFragment.getTextState().getFont().isSubset());
    System.out.println("حجم الخط :- " + textFragment.getTextState().getFontSize());
    System.out.println("لون المقدمة :- " + textFragment.getTextState().getForegroundColor());
}
```


للبحث عن نص في صفحة معينة والحصول على خصائصه، حدد فهرس الصفحة:

```java
// قَبَل الماصة للصفحة الأولى من المستند.
pdfDocument.getPages().get_Item(1).accept(textFragmentAbsorber)
```

من أجل البحث عن سلسلة نصية إما بحروف كبيرة أو صغيرة، يمكنك التفكير في استخدام التعبير النمطي.

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("(?i)Line", new TextSearchOptions(true));
```

مثال:

```java
TextFragmentAbsorber textFragmentAbsorber = new TextFragmentAbsorber("[\\S]+");
```