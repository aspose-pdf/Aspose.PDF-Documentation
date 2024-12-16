---
title: استخراج النص الخام من ملف PDF
linktitle: استخراج النص من PDF
type: docs
weight: 10
url: /ar/java/extract-text-from-all-pdf/
description: توضح هذه المقالة طرقًا مختلفة لاستخراج النص من مستندات PDF باستخدام Aspose.PDF لـ Java. من صفحات كاملة، أو من جزء محدد، بناءً على الأعمدة، إلخ.
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

يعتبر استخراج النص من مستند PDF مطلبًا شائعًا. في هذا المثال، سترى كيف يتيح لك Aspose.PDF لـ Java استخراج النص من جميع صفحات مستند PDF.
لاستخراج النص من جميع صفحات PDF:

1. قم بإنشاء كائن من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber).

1. افتح ملف PDF باستخدام فئة [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) واستدعِ طريقة [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) لمجموعة [Pages](https://reference.aspose.com/pdf/java/com.aspose.pdf/Page).
1. تقوم فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) بامتصاص النص من المستند وتعيده في خاصية **Text**.

يظهر لك المقتطف البرمجي التالي كيفية استخراج النص من جميع صفحات مستند PDF.

```java
public static void ExtractFromAllPages(){
    // المسار إلى دليل المستندات.
    String _dataDir = "/home/admin1/pdf-examples/Samples/";
    String filePath = _dataDir + "ExtractTextAll.pdf";

    // افتح المستند
    com.aspose.pdf.Document pdfDocument = new com.aspose.pdf.Document(filePath);

    // أنشئ كائن TextAbsorber لاستخراج النص
    com.aspose.pdf.TextAbsorber textAbsorber = new com.aspose.pdf.TextAbsorber();
    
    // قبول المستوعب لجميع الصفحات
    pdfDocument.getPages().accept(textAbsorber);
    
    // الحصول على النص المستخرج
    String extractedText = textAbsorber.getText();                
    try {
        java.io.FileWriter writer = new java.io.FileWriter(_dataDir + "extracted-text.txt", true);
        // كتابة سطر من النص إلى الملف
        writer.write(extractedText);            
        // إغلاق التدفق
        writer.close();
    } catch (java.io.IOException e) {
        e.printStackTrace();
    }

}
```


## استخراج النص من الصفحات باستخدام جهاز النص

يمكنك استخدام فئة **TextDevice** لاستخراج النص من ملف PDF. يستخدم TextDevice [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) في تنفيذه، وبالتالي، في الواقع، يقومون بنفس الشيء ولكن تم تنفيذ TextDevice فقط لتوحيد نهج "الجهاز" لاستخراج أي شيء من الصفحة مثل ImageDevice، PageDevice، إلخ. قد يقوم TextAbsorber باستخراج النص من الصفحة، أو PDF بالكامل أو XForm، هذا TextAbsorber أكثر شمولية.

### استخراج النص من جميع الصفحات

توضح الخطوات التالية والشفرة البرمجية كيفية استخراج النص من PDF باستخدام جهاز النص.

1. قم بإنشاء كائن من فئة Document مع تحديد ملف PDF المدخل
1. قم بإنشاء كائن من فئة TextDevice
1. استخدم كائن من فئة TextExtractOptions لتحديد خيارات الاستخراج
1. استخدم طريقة Process من فئة TextDevice لتحويل المحتويات إلى نص
1. احفظ النص في ملف الإخراج

```java
public static void extractTextFromAllPagesOfPDF() throws IOException {
    // فتح المستند
    Document pdfDocument = new Document("input.pdf");
    // ملف النص الذي سيتم حفظ النص المستخرج فيه
    java.io.OutputStream text_stream = new java.io.FileOutputStream("ExtractedText.txt", false);
    // التكرار عبر جميع صفحات ملف PDF
    for (Page page : (Iterable<Page>) pdfDocument.getPages()) {
        // إنشاء جهاز النص
        TextDevice textDevice = new TextDevice();
        // تعيين خيارات استخراج النص - تعيين وضع استخراج النص (خام أو
        // نقي)
        TextExtractionOptions textExtOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Raw);
        textDevice.setExtractionOptions(textExtOptions);
        // الحصول على النص من صفحات PDF وحفظه في كائن OutputStream
        textDevice.process(page, text_stream);
    }
    // إغلاق كائن التدفق
    text_stream.close();
}
```


## استخراج النص من منطقة معينة في الصفحة

يوفر فصل [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber) القدرة على استخراج النص من صفحة معينة أو جميع صفحات مستند PDF. تعيد هذه الفئة النص المستخرج في خاصية **Text**. ومع ذلك، إذا كان لدينا متطلب لاستخراج النص من منطقة معينة في الصفحة، يمكننا استخدام خاصية **Rectangle** الخاصة بـ [TextSearchOptions](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextSearchOptions). تأخذ خاصية Rectangle كائنًا من نوع Rectangle كقيمة، وباستخدام هذه الخاصية، يمكننا تحديد منطقة الصفحة التي نحتاج إلى استخراج النص منها.

يتم استدعاء طريقة [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) للصفحة لاستخراج النص.
 إنشاء كائنات من الفئات [Document](https://reference.aspose.com/pdf/java/com.aspose.pdf/Document) و [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). قم باستدعاء طريقة [Accept](https://reference.aspose.com/pdf/java/com.aspose.pdf/PageCollection#accept-com.aspose.pdf.TextAbsorber-) على الصفحة الفردية، كفهرس **Page**، من كائن **Document**. الفهرس هو رقم الصفحة المحددة التي يجب استخراج النص منها. يمكنك الحصول على النص من خاصية **Text** من فئة [TextAbsorber](https://reference.aspose.com/pdf/java/com.aspose.pdf/TextAbsorber). يوضح لك مقتطف الشيفرة التالية كيفية استخراج النص من صفحة فردية.

```java
public static void ExtractTextFromParticularPageRegion(String[] args) throws IOException {
    // فتح المستند
    Document doc = new Document("page_0001.pdf");
    // إنشاء كائن TextAbsorber لاستخراج النص
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // قبول الماص للصفحة الأولى
    doc.getPages().get_Item(1).accept(absorber);
    // الحصول على النص المستخرج
    String extractedText = absorber.getText();
    // إنشاء كاتب وفتح الملف
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // كتابة المحتويات المستخرجة
    writer.write(extractedText);
    // إغلاق الكاتب
    writer.close();
}
```

## استخراج النص بناءً على الأعمدة

قد يحتوي ملف PDF على عناصر نصية، صور، تعليقات توضيحية، مرفقات، رسوم بيانية، إلخ، ويوفر Aspose.PDF for .NET ميزة إضافة وكذلك التلاعب بجميع هذه العناصر. هذه الواجهة البرمجية رائعة عندما يتعلق الأمر بإضافة النص واستخراجه من مستند PDF وقد نواجه سيناريو حيث يتكون مستند PDF من أكثر من عمود واحد (مستند PDF متعدد الأعمدة) ونحتاج إلى استخراج محتويات الصفحة مع الحفاظ على نفس التخطيط، فإن Aspose.PDF for .NET هو الخيار المناسب لتحقيق هذا المتطلب. إحدى الطرق هي تقليل حجم الخط للمحتويات داخل مستند PDF ثم تنفيذ استخراج النص. يوضح مقتطف الشيفرة التالي الخطوات لتقليل حجم النص ثم محاولة استخراج النص من مستند PDF.

```java
public static void ExtractTextBasedOnColumns() throws IOException {
    // فتح المستند
    Document doc = new Document("page_0001.pdf");
    // إنشاء كائن TextAbsorber لاستخراج النص
    TextAbsorber absorber = new TextAbsorber();
    absorber.getTextSearchOptions().setLimitToPageBounds(true);
    absorber.getTextSearchOptions().setRectangle(new Rectangle(100, 200, 250, 350));
    // قبول المستخرج للصفحة الأولى
    doc.getPages().get_Item(1).accept(absorber);
    // الحصول على النص المستخرج
    String extractedText = absorber.getText();
    // إنشاء كاتب وفتح الملف
    BufferedWriter writer = new BufferedWriter(new FileWriter(new java.io.File("ExtractedText.txt")));
    // كتابة المحتويات المستخرجة
    writer.write(extractedText);
    // إغلاق الكاتب
    writer.close();
}
```


### النهج الثاني - استخدام ScaleFactor

في هذا الإصدار الجديد، قدمنا أيضًا عدة تحسينات في TextAbsorber وفي آلية تنسيق النص الداخلية. لذا الآن أثناء استخراج النص باستخدام الوضع 'Pure'، يمكنك تحديد خيار ScaleFactor ويمكن أن يكون نهجًا آخر لاستخراج النص من مستند PDF متعدد الأعمدة بالإضافة إلى النهج المذكور أعلاه. يمكن ضبط هذا العامل لتعديل الشبكة التي تُستخدم لآلية تنسيق النص الداخلية أثناء استخراج النص. تحديد قيم ScaleFactor بين 1 و 0.1 (بما في ذلك 0.1) له نفس تأثير تقليل الخط.


تحديد قيم ScaleFactor بين 0.1 و -0.1 يتم التعامل معها كقيمة صفرية، ولكنه يجعل الخوارزمية تحسب معامل المقياس المطلوب أثناء استخراج النص تلقائيًا. يتم الحساب بناءً على متوسط عرض الرمز لأكثر الخطوط شعبية على الصفحة، لكن لا يمكننا ضمان أنه في النص المستخرج لا تصل أي سلسلة من الأعمدة إلى بداية العمود التالي. يرجى ملاحظة أنه إذا لم يتم تحديد قيمة ScaleFactor، فسيتم استخدام القيمة الافتراضية 1.0. وهذا يعني أنه لن يتم تنفيذ أي عملية قياس. إذا كانت قيمة ScaleFactor المحددة أكثر من 10 أو أقل من -0.1، فسيتم استخدام القيمة الافتراضية 1.0.

نقترح استخدام التحجيم التلقائي (ScaleFactor = 0) عند معالجة عدد كبير من ملفات PDF لاستخراج محتوى النص. أو ضبط تقليل عرض الشبكة يدويًا (حوالي ScaleFactor = 0.5). ومع ذلك، يجب عليك عدم تحديد ما إذا كان التحجيم ضروريًا للمستندات المحددة أم لا. إذا قمت بتحديد تقليل عرض الشبكة بشكل زائد لمستند (لا يحتاج إلى ذلك)، سيظل محتوى النص المستخرج كافيًا تمامًا. يرجى إلقاء نظرة على مقتطف الشيفرة التالي.

```java
public static void usingSetScaleFactorMethod() {
    Document pdfDocument = new Document("inputFile.pdf");
    TextAbsorber textAbsorber = new TextAbsorber();
    textAbsorber.setExtractionOptions(new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure));
    // ضبط عامل التحجيم إلى 0.5 يكفي لتقسيم الأعمدة في معظم المستندات
    // ضبط الصفر يسمح للخوارزمية باختيار عامل التحجيم تلقائيًا
    textAbsorber.getExtractionOptions().setScaleFactor((double) 0.5);
    pdfDocument.getPages().accept(textAbsorber);
    String extractedText = textAbsorber.getText();
}
```


{{% alert color="primary" %}}

يرجى ملاحظة أنه لا يوجد تطابق مباشر بين معامل ScaleFactor الجديد والمعامل القديم لتقليل حجم الخط يدوياً. ومع ذلك، فإن الخوارزمية تأخذ في الاعتبار بشكل افتراضي قيمة حجم الخط الذي تم تقليله بالفعل لأسباب داخلية. على سبيل المثال، تقليل حجم الخط من 10 إلى 7 له نفس تأثير ضبط عامل المقياس إلى 5/8 (= 0.625).

{{% /alert %}}

## استخراج النص المميز من مستند PDF

في مختلف سيناريوهات استخراج النص من مستند PDF، قد تحتاج إلى استخراج النص المميز فقط من مستند PDF. من أجل تنفيذ هذه الوظيفة، قمنا بإضافة طرق TextMarkupAnnotation.GetMarkedText() و TextMarkupAnnotation.GetMarkedTextFragments() في API. يمكنك استخراج النص المميز من مستند PDF عن طريق تصفية TextMarkupAnnotation واستخدام الطرق المذكورة. يوضح مقتطف الشيفرة التالي كيفية استخراج النص المميز من مستند PDF.

```java
public static void ExtractHighlightedText() {
    Document doc = new Document(_dataDir + "ExtractHighlightedText.pdf");
    // حلقة عبر جميع التعليقات التوضيحية
    for (Annotation annotation : doc.getPages().get_Item(1).getAnnotations())
    {
        // تصفية TextMarkupAnnotation
        if (annotation.getAnnotationType()==AnnotationType.Highlight)
        {
            HighlightAnnotation highlightedAnnotation = (HighlightAnnotation) annotation;
            // استرجاع أجزاء النص المميز
            TextFragmentCollection collection = highlightedAnnotation.getMarkedTextFragments();
            for (TextFragment tf : collection)
            {
                // عرض النص المميز
                System.out.println(tf.getText());
            }
        }
    }        
}
```


## الوصول إلى عناصر النص المجزأ والمقطع من XML

أحيانًا نحتاج إلى الوصول إلى عناصر TextFragement أو TextSegment عند معالجة مستندات PDF التي تم إنشاؤها من XML. يوفر Aspose.PDF for .NET الوصول إلى مثل هذه العناصر بالاسم. يوضح مقتطف الشيفرة أدناه كيفية استخدام هذه الوظيفة.

```java
public static void AccessTextFragmentAndSegmentElements() {
    String inXml = "40014.xml";        
    Document doc = new Document();
    doc.bindXml(_dataDir + inXml);

    TextSegment segment = (TextSegment) doc.getObjectById("boldHtml");
    segment = (TextSegment) doc.getObjectById("strongHtml");

    System.out.println(segment.getText());
    
}
```