---
title: استخراج نص من PDF C#
linktitle: استخراج نص من PDF
type: docs
weight: 10
url: ar/net/extract-text-from-all-pdf/
description: يصف هذا المقال الطرق المختلفة لاستخراج النصوص من مستندات PDF باستخدام Aspose.PDF في C#. 
lastmod: "2021-06-05"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## استخراج النص من جميع صفحات مستند PDF

استخراج النص من مستند PDF هو متطلب شائع. في هذا المثال، سترى كيف يتيح Aspose.PDF لـ .NET استخراج النص من جميع صفحات مستند PDF. تحتاج إلى إنشاء كائن من الفئة **TextAbsorber**. بعد ذلك، افتح PDF باستخدام فئة **Document** واستدعي طريقة **Accept** لمجموعة **Pages**. فئة **TextAbsorber** تمتص النص من المستند وتعيده في خاصية **Text**. يُظهر الجزء التالي من الشفرة كيفية استخراج النص من جميع صفحات مستند PDF.

يعمل الجزء التالي من الشفرة أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// لأمثلة كاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// إنشاء كائن TextAbsorber لاستخراج النص
TextAbsorber textAbsorber = new TextAbsorber();
// قبول الامتصاص لجميع الصفحات
pdfDocument.Pages.Accept(textAbsorber);
// الحصول على النص المستخرج
string extractedText = textAbsorber.Text;
// إنشاء كاتب وفتح الملف
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// كتابة سطر من النص إلى الملف
tw.WriteLine(extractedText);
// إغلاق الدفق
tw.Close();
```
استدعِ الطريقة **Accept** على صفحة معينة من كائن المستند. الفهرس هو رقم الصفحة المعين حيث يلزم استخراج النص.

هذا المقتطف من الكود يعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

// إنشاء كائن TextAbsorber لاستخراج النص
TextAbsorber textAbsorber = new TextAbsorber();

// قبول الامتصاص لصفحة معينة
pdfDocument.Pages[1].Accept(textAbsorber);

// الحصول على النص المستخرج
string extractedText = textAbsorber.Text;

dataDir = dataDir + "extracted-text_out.txt";
// إنشاء كاتب وفتح الملف
TextWriter tw = new StreamWriter(dataDir);

// كتابة سطر من النص إلى الملف
tw.WriteLine(extractedText);

// إغلاق الدفق
tw.Close();
```
## استخراج النص من الصفحات باستخدام جهاز النص

يمكنك استخدام فئة **TextDevice** لاستخراج النص من ملف PDF. يستخدم TextDevice TextAbsorber في تنفيذه، وبالتالي، في الواقع، يقومان بنفس الشيء لكن تم تنفيذ TextDevice لتوحيد نهج "الجهاز" لاستخراج أي شيء من صورة الصفحة، جهاز الصفحة، إلخ. قد يستخرج TextAbsorber النص من صفحة، PDF بأكملها أو XForm، هذا TextAbsorber أكثر عمومية

### استخراج النص من جميع الصفحات

توضح الخطوات والشفرة التالية كيفية استخراج النص من PDF باستخدام جهاز النص.

1. إنشاء كائن من فئة Document مع تحديد ملف PDF المدخل
1. إنشاء كائن من فئة TextDevice
1. استخدم كائن من فئة TextExtractOptions لتحديد خيارات الاستخراج
1. استخدم الطريقة Process لفئة TextDevice لتحويل المحتويات إلى نص
1. حفظ النص في ملف الإخراج

تعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "input.pdf");
System.Text.StringBuilder builder = new System.Text.StringBuilder();
// سلسلة لحفظ النص المستخرج
string extractedText = "";

foreach (Page pdfPage in pdfDocument.Pages)
{
    using (MemoryStream textStream = new MemoryStream())
    {
        // إنشاء جهاز نصي
        TextDevice textDevice = new TextDevice();

        // تعيين خيارات استخراج النص - تعيين وضع استخراج النص (Raw أو Pure)
        TextExtractionOptions textExtOptions = new
        TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
        textDevice.ExtractionOptions = textExtOptions;

        // تحويل صفحة معينة وحفظ النص في الدفق
        textDevice.Process(pdfPage, textStream);
        // تحويل صفحة معينة وحفظ النص في الدفق
        textDevice.Process(pdfDocument.Pages[1], textStream);

        // إغلاق الدفق الذاكري
        textStream.Close();

        // الحصول على النص من الدفق الذاكري
        extractedText = Encoding.Unicode.GetString(textStream.ToArray());
    }
    builder.Append(extractedText);
}

dataDir = dataDir + "input_Text_Extracted_out.txt";
// حفظ النص المستخرج في ملف نصي
File.WriteAllText(dataDir, builder.ToString());
```
## استخراج النص من منطقة محددة بالصفحة

توفر الفئة **TextAbsorber** القدرة على استخراج النص من صفحة معينة أو جميع صفحات مستند PDF. تعيد هذه الفئة النص المستخرج في خاصية **النص**. ومع ذلك، إذا كان لدينا متطلب لاستخراج النص من منطقة محددة بالصفحة، يمكننا استخدام خاصية **المستطيل** في **خيارات بحث النص**. تأخذ خاصية المستطيل كائن المستطيل كقيمة وباستخدام هذه الخاصية، يمكننا تحديد المنطقة من الصفحة التي نحتاج إلى استخراج النص منها.

يتم استدعاء طريقة **قبول** لصفحة لاستخراج النص. قم بإنشاء كائنات لفئات **المستند** و **ممتص النص**. استدعي طريقة **قبول** على الصفحة الفردية، كما هو مؤشر **الصفحة**، لكائن **المستند**. **المؤشر** هو رقم الصفحة المحدد حيث يحتاج إلى استخراج النص. يمكنك الحصول على النص من خاصية **النص** لفئة **ممتص النص**. يوضح الكود التالي كيفية استخراج النص من صفحة فردية.

يعمل الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
يعمل الشفرة التالية أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ExtractTextAll.pdf");

// إنشاء كائن TextAbsorber لاستخراج النص
TextAbsorber absorber = new TextAbsorber();
absorber.TextSearchOptions.LimitToPageBounds = true;
absorber.TextSearchOptions.Rectangle = new Aspose.Pdf.Rectangle(100, 200, 250, 350);

// تقبل الممتص للصفحة الأولى
pdfDocument.Pages[1].Accept(absorber);

// الحصول على النص المستخرج
string extractedText = absorber.Text;
// إنشاء كاتب وفتح الملف
TextWriter tw = new StreamWriter(dataDir + "extracted-text.txt");
// كتابة سطر من النص إلى الملف
tw.WriteLine(extractedText);
// إغلاق التيار
tw.Close();
```

## استخراج النص بناءً على الأعمدة

قد يتكون ملف PDF من عناصر نص، صورة، تعليقات، مرفقات، رسوم بيانية، وغيرها وتقدم Aspose.PDF لـ .NET الميزة لإضافة وكذلك التعامل مع كل هذه العناصر.
قد يتكون ملف PDF من نصوص، صور، تعليقات، مرفقات، رسوم بيانية، وغيرها من العناصر، ويقدم Aspose.PDF لـ.NET القدرة على إضافة والتعامل مع كل هذه العناصر.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح المستند
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextFragmentAbsorber tfa = new TextFragmentAbsorber();
pdfDocument.Pages.Accept(tfa);
TextFragmentCollection tfc = tfa.TextFragments;
foreach (TextFragment tf in tfc)
{
    // يلزم تقليل حجم الخط بنسبة 70% على الأقل
    tf.TextState.FontSize = tf.TextState.FontSize * 0.7f;
}
Stream st = new MemoryStream();
pdfDocument.Save(st);
pdfDocument = new Document(st);
TextAbsorber textAbsorber = new TextAbsorber();
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
textAbsorber.Visit(pdfDocument);

dataDir = dataDir + "ExtractColumnsText_out.txt";

System.IO.File.WriteAllText(dataDir, extractedText);
```
### النهج الثاني - استخدام معامل التحجيم

في هذا الإصدار الجديد، قمنا أيضًا بتقديم عدة تحسينات في TextAbsorber وفي آلية تنسيق النصوص الداخلية. لذا الآن أثناء استخراج النصوص باستخدام وضع 'Pure'، يمكنك تحديد خيار معامل التحجيم وقد يكون هذا نهجًا آخر لاستخراج النص من وثيقة PDF متعددة الأعمدة بجانب النهج المذكور أعلاه. يمكن ضبط هذا المعامل لتعديل الشبكة المستخدمة لآلية تنسيق النصوص الداخلية أثناء استخراج النص. تحديد قيم معامل التحجيم بين 1 و0.1 (بما في ذلك 0.1) له نفس تأثير تقليل الخط.

تحديد قيم معامل التحجيم بين 0.1 و-0.1 يُعامل كقيمة صفر، ولكنه يجعل الخوارزمية تحسب معامل التحجيم المطلوب أثناء استخراج النص تلقائيًا.
تُعامل قيم ScaleFactor المحددة بين 0.1 و -0.1 على أنها قيمة صفرية، لكنها تجعل الخوارزمية تحسب معامل القياس اللازم أثناء استخراج النص تلقائيًا.

نقترح استخدام التحجيم التلقائي (ScaleFactor = 0) عند معالجة عدد كبير من ملفات PDF لاستخراج محتوى النص. أو يمكنك تعيين تقليل زائد يدويًا لعرض الشبكة (حوالي ScaleFactor = 0.5). ومع ذلك، يجب ألا تحدد ما إذا كان التحجيم ضروريًا للوثائق الملموسة أم لا. إذا قمت بتعيين تقليل زائد لعرض الشبكة للوثيقة (التي لا تحتاج إليه)، فسيظل المحتوى النصي المستخرج كاملاً بشكل كافٍ. يرجى إلقاء نظرة على مقتطف الكود التالي.

يعمل مقتطف الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل الوثائق.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

// فتح الوثيقة
Document pdfDocument = new Document(dataDir + "ExtractTextPage.pdf");

TextAbsorber textAbsorber = new TextAbsorber();
textAbsorber.ExtractionOptions = new TextExtractionOptions(TextExtractionOptions.TextFormattingMode.Pure);
// تعيين معامل القياس إلى 0.5 كافٍ لتقسيم الأعمدة في غالبية الوثائق
// تعيين الصفر يسمح للخوارزمية باختيار معامل القياس تلقائيًا
textAbsorber.ExtractionOptions.ScaleFactor = 0.5; /* 0; */
pdfDocument.Pages.Accept(textAbsorber);
String extractedText = textAbsorber.Text;
System.IO.File.WriteAllText( dataDir + "ExtractTextUsingScaleFactor_out.text", extractedText);
```
{{% alert color="primary" %}}
يرجى ملاحظة أنه لا يوجد تطابق مباشر بين ScaleFactor الجديد ومعامل تقليل الخط اليدوي القديم. ومع ذلك، يأخذ الخوارزمية الافتراضية بعين الاعتبار قيمة حجم الخط التي تم تقليلها بالفعل لأسباب داخلية. على سبيل المثال، تقليل حجم الخط من 10 إلى 7 له نفس تأثير تعيين عامل مقياس إلى 5/8 (= 0.625).
{{% /alert %}}

## استخراج النص المميز من مستند PDF

في سيناريوهات مختلفة لاستخراج النص من مستند PDF، قد تحتاج إلى استخراج النص المميز فقط من مستند PDF. لتنفيذ هذه الوظيفة، أضفنا الطرق TextMarkupAnnotation.GetMarkedText() و TextMarkupAnnotation.GetMarkedTextFragments() في API. يمكنك استخراج النص المميز من مستند PDF عن طريق تصفية TextMarkupAnnotation واستخدام الطرق المذكورة. يوضح الجزء التالي من الكود كيف يمكنك استخراج النص المميز من مستند PDF.

يعمل جزء الكود التالي أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).
يعمل الجزء التالي من الكود أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للأمثلة الكاملة وملفات البيانات، يرجى الذهاب إلى https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// المسار إلى دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Annotations();
Document doc = new Document(dataDir + "ExtractHighlightedText.pdf");
// التكرار عبر جميع الحواشي
foreach (Annotation annotation in doc.Pages[1].Annotations)
{
    // تصفية TextMarkupAnnotation
    if (annotation is TextMarkupAnnotation)
    {
        TextMarkupAnnotation highlightedAnnotation = annotation as TextMarkupAnnotation;
        // استرجاع قطع النص المميزة
        TextFragmentCollection collection = highlightedAnnotation.GetMarkedTextFragments();
        foreach (TextFragment tf in collection)
        {
            // عرض النص المميز
            Console.WriteLine(tf.Text);
        }
    }
}
```

## الوصول إلى عناصر Fragment النصية وعناصر Segment من XML

أحيانًا نحتاج إلى الوصول إلى عناصر TextFragement أو TextSegment عند معالجة المستندات PDF المولدة من XML.
أحيانًا نحتاج إلى الوصول إلى عناصر TextFragement أو TextSegment عند معالجة المستندات PDF المولدة من XML.

الشفرة التالية تعمل أيضًا مع مكتبة [Aspose.PDF.Drawing](/pdf/net/drawing/).

```csharp
// للحصول على أمثلة كاملة وملفات بيانات، يرجى زيارة https://github.com/aspose-pdf/Aspose.PDF-for-.NET
// مسار دليل المستندات.
string dataDir = RunExamples.GetDataDir_AsposePdf_Text();

string inXml = "40014.xml";
string outFile = "40014_out.pdf";

Document doc = new Document();
doc.BindXml(dataDir + inXml);

Page page = (Page)doc.GetObjectById("mainSection");

TextSegment segment = (TextSegment)doc.GetObjectById("boldHtml");
segment = (TextSegment)doc.GetObjectById("strongHtml");
doc.Save(dataDir + outFile);
```
