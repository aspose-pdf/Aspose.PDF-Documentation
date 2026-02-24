---
title: مقارنة مستندات PDF
linktitle: مقارنة PDF
type: docs
weight: 130
url: /ar/python-net/compare-pdf-documents/
description: يمكن مقارنة محتوى مستندات PDF بعلامات التعليق والمخرجات جنبًا إلى جنب.
lastmod: "2025-05-12"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: 
Abstract: 
---

## طرق مقارنة مستندات PDF

عند العمل مع مستندات PDF، هناك أوقات تحتاج فيها إلى مقارنة محتوى مستندين لتحديد الاختلافات. توفر مكتبة Aspose.PDF للغة بايثون عبر .NET مجموعة أدوات قوية لهذا الغرض. في هذه المقالة، سوف نستكشف كيفية مقارنة مستندات PDF باستخدام بعض مقاطع الشيفرة البسيطة.

تتيح وظيفة المقارنة في Aspose.PDF مقارنة مستندين PDF صفحة بصفحة. يمكنك اختيار مقارنة صفحات محددة أو المستندات بالكامل. يبرز مستند المقارنة الناتج الاختلافات، مما يجعل من السهل تحديد التغييرات بين الملفين.

فيما يلي قائمة بالطرق الممكنة لمقارنة مستندات PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET:

1. **مقارنة الصفحات المحددة** - مقارنة الصفحات الأولى لملفين PDF.
1. **مقارنة المستندات بالكامل** - مقارنة المحتوى الكامل لملفين PDF.
1. **مقارنة مستندات PDF بشكل رسومي**:

- مقارنة PDF باستخدام طريقة 'comparer.get_difference' - صور فردية حيث تم تعليم التغييرات.
- مقارنة PDF باستخدام طريقة 'comparer.compare_documents_to_pdf' - مستند PDF مع صور حيث تم تعليم التغييرات.

## مقارنة الصفحات المحددة

توضح مقطع الشيفرة الأول كيفية مقارنة الصفحات الأولى لملفين PDF باستخدام فئة SideBySidePdfComparer.

1. تهيئة المستند.
1. إنشاء دالة لأداء المقارنة.
1. عملية المقارنة:

- document1.pages[1] and document2.pages[1]: - هذه تحدد الصفحة الأولى من كل مستند للمقارنة. لاحظ أن ترقيم الصفحات يبدأ من 1 في Aspose.PDF.
- SideBySideComparisonOptions - هذه الفئة تسمح بتخصيص سلوك المقارنة.
- additional_change_marks = True - يتيح عرض علامات التغيير الإضافية، مما يبرز الاختلافات التي قد تكون موجودة في صفحات أخرى، حتى وإن لم تكن في الصفحة الحالية التي تتم مقارنتها.
- comparison_mode = ComparisonMode.IgnoreSpaces - يحدد وضع المقارنة لتجاهل الفراغات في النص، مع التركيز فقط على التغييرات داخل الكلمات.

1. يتم حفظ نتيجة المقارنة كملف PDF جديد باسم ComparingSpecificPages_out.pdf في دليل data_dir المحدد.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_specific_pages():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingSpecificPages1.pdf")
        document2 = ap.Document(data_dir + "ComparingSpecificPages2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1.pages[1], document2.pages[1], data_dir + "ComparingSpecificPages_out.pdf", options)
```

## مقارنة المستندات بالكامل

مقطع الشيفرة الثاني يوسع النطاق لمقارنة المحتوى الكامل لملفين PDF.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import SideBySidePdfComparer, SideBySideComparisonOptions, ComparisonMode

    def comparing_entire_documents():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparingEntireDocuments1.pdf")
        document2 = ap.Document(data_dir + "ComparingEntireDocuments2.pdf")

        # Compare
        options = SideBySideComparisonOptions()
        options.additional_change_marks = True
        options.comparison_mode = ComparisonMode.IgnoreSpaces

        # Perform comparison and save the result
        SideBySidePdfComparer.compare(document1, document2, data_dir + "ComparingEntireDocuments_out.pdf", options)
```

توضح الشيفرة المقدمة مقارنة ملفين PDF باستخدام Aspose.PDF للبايثون عبر .NET. تستخدم فئة SideBySidePdfComparer لإجراء مقارنة صفحة بصفحة، وتولد ملف PDF جديد يعرض الاختلافات جنبًا إلى جنب. تم تكوين المقارنة باستخدام SideBySideComparisonOptions، حيث تم ضبط additional_change_marks على True لتسليط الضوء على التغييرات ليس فقط في الصفحة الحالية بل أيضًا في الصفحات الأخرى، وتم ضبط comparison_mode على IgnoreSpaces للتركيز على فروق المحتوى ذات المعنى عبر تجاهل اختلافات المسافات.

## المقارنة باستخدام GraphicalPdfComparer

عند التعاون على المستندات، خاصة في البيئات المهنية، كثيرًا ما تنتهي بأكثر من نسخة من نفس الملف.
توضح الشيفرة المقدمة كيفية مقارنة صفحات محددة من ملفين PDF بصريًا باستخدام Aspose.PDF للبايثون عبر .NET. باستخدام فئة `GraphicalPdfComparer`، يتم إبراز الاختلافات بين الصفحات الأولى للملفين PDF وتوليد صور مقاربة لتمثيل هذه الاختلافات.

يمكنك ضبط الخصائص التالية للفئة:

- Resolution - الدقة بوحدات DPI للصور الناتجة، وكذلك للصور التي تُولّد أثناء المقارنة.
- Color - لون علامات التغيير.
- Threshold - عتبة التغيير بالنسبة المئوية. القيمة الافتراضية هي صفر. تعيين قيمة غير الصفر يسمح لك بتجاهل التغييرات الرسومية التي لا تعتبرها ذات أهمية.

مع Aspose.PDF للبايثون عبر .NET، يمكن مقارنة المستندات والصفحات وإخراج نتيجة المقارنة إلى مستند PDF أو ملف صورة.

تحتوي فئة `GraphicalPdfComparer` على طريقة تتيح لك الحصول على اختلافات صور الصفحات بصيغة مناسبة لمعالجة إضافية: `get_difference(document1.pages[1], document2.pages[1])`.

تُعيد هذه الطريقة كائنًا من نوع `images_difference`، يحتوي على صورة للصفحة الأولى التي تُقارن ومصفوفة من الاختلافات.

يتيح لك كائن `images_difference` توليد صورة مختلفة والحصول على صورة للصفحة الثانية التي تُقارن عن طريق تطبيق مصفوفة الاختلافات على الصورة الأصلية. للقيام بذلك، استخدم طُرُق `difference_to_image` و `get_destination_image`.

### مقارنة PDF باستخدام طريقة Get Difference

تُعرّف الشيفرة المقدمة طريقة `get_difference` التي تقارن ملفين PDF وتولد تمثيلات بصرية للاختلافات بينهما.

تقارن هذه الطريقة الصفحات الأولى لملفين PDF وتولد صورتين PNG:

- صورة واحدة تُبرز الاختلافات بين الصفحات باللون الأحمر.
- الصورة الأخرى هي تمثيل مرئي لصفحة PDF الوجهة (الثانية).

يمكن أن تكون هذه العملية مفيدة لمقارنة التغييرات أو الاختلافات بصريًا بين نسختين من المستند.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer

    def compare_pdf_with_get_difference_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithGetDifferenceMethod2.pdf")

        # Create comparer
        comparer = GraphicalPdfComparer()

        # Compare specific pages
        images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

        # Get image showing differences in red over a white background
        diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
        diff_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDiffPngFilePath_out.png")

        # Get the second image representing the destination page
        dest_img = images_difference.get_destination_image()
        dest_img.save(data_dir + "ComparePDFWithGetDifferenceMethodDestPngFilePath_out.png")
```

### مقارنة PDF باستخدام طريقة CompareDocumentsToPdf

يستخدم مقطع الشفرة المقدم طريقة `compare_documents_to_pdf`، التي تقارن بين مستندين وتولد تقرير PDF لنتائج المقارنة.

```python

    import aspose.pdf as ap
    from aspose.pdf.comparison import GraphicalPdfComparer
    from aspose.pdf.devices import Resolution

    def compare_pdf_with_compare_documents_to_pdf_method():
        # The path to the documents directory
        data_dir = RunExamples.get_data_dir_asposepdf_documentcompare()

        # Open PDF documents
        document1 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod1.pdf")
        document2 = ap.Document(data_dir + "ComparePDFWithCompareDocumentsToPdfMethod2.pdf")

        # Create comparer and set options
        comparer = GraphicalPdfComparer()
        comparer.threshold = 3.0
        comparer.color = ap.Color.blue
        comparer.resolution = Resolution(300)

        # Compare and output to a PDF file
        comparer.compare_documents_to_pdf(document1, document2, data_dir + "compareDocumentsToPdf_out.pdf")
```

يوضح هذا المثال كيفية إجراء مقارنة رسومية بين مستندين كاملين من PDF باستخدام Aspose.PDF للغة Python عبر .NET. من خلال الاستفادة من الفئة `GraphicalPdfComparer`، يتم إنشاء ملف PDF جديد يبرز بصريًا الاختلافات بين المستندين.

- تم تعيين خاصية العتبة إلى 3.0، مما يعني أنه يتم تجاهل الاختلافات الصغيرة التي تقل عن هذه النسبة أثناء المقارنة، والتركيز على التغييرات الأكثر أهمية.
- يتم تمييز الاختلافات باللون الأزرق عن طريق تعيين خاصية اللون إلى ap.Color.blue، مما يسمح بوضوح بصري مميز.
- تُجرى المقارنة بدقة 300 نقطة في البوصة (DPI) عبر ضبط خاصية الدقة، مما يضمن مخرجات مفصلة وواضحة.

تقارن طريقة `compare_documents_to_pdf` جميع صفحات المستندين وتُخرج النتيجة إلى ملف PDF جديد، compareDocumentsToPdf_out.pdf، مع إبراز الاختلافات بصريًا.

