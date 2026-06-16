---
title: قارن مستندات PDF في Python
linktitle: قارن ملفات PDF
type: docs
weight: 130
url: /ar/python-net/compare-pdf-documents/
description: تعرف على كيفية مقارنة مستندات PDF في Python باستخدام مخرجات الفرق جنبًا إلى جنب والرسوم البيانية مع Aspose.PDF لـ Python عبر .NET.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: قارن صفحات PDF والمستندات الكاملة مع إخراج الفرق المرئي في Python
Abstract: توضح هذه المقالة كيفية مقارنة مستندات PDF في Aspose.PDF لـ Python عبر .NET. تعرف على كيفية مقارنة صفحات معينة أو ملفات PDF بأكملها مع الإخراج جنبًا إلى جنب، وكيفية استخدام طرق المقارنة الرسومية لإنشاء تقارير الفرق المستندة إلى الصور أو PDF.
---

## طرق مقارنة مستندات PDF

عند العمل مع مستندات PDF، هناك أوقات تحتاج فيها إلى مقارنة محتوى وثيقتين لتحديد الاختلافات. توفر مكتبة Aspose.PDF لـ Python عبر مكتبة.NET مجموعة أدوات قوية لهذا الغرض. في هذه المقالة، سنستكشف كيفية مقارنة مستندات PDF باستخدام بعض مقتطفات التعليمات البرمجية البسيطة.

استخدم المقارنة جنبًا إلى جنب عندما تريد إخراج PDF يبرز تغييرات النص والتخطيط عبر الصفحات. استخدم المقارنة الرسومية عندما تحتاج إلى اكتشاف الفرق المستند إلى الصور لعمليات سير عمل المراجعة المرئية أو فحوصات الانحدار أو تقارير مقارنة PDF.

تتيح لك وظيفة المقارنة في Aspose.PDF مقارنة وثيقتي PDF صفحة بصفحة. يمكنك اختيار مقارنة صفحات محددة أو مستندات كاملة. تسلط وثيقة المقارنة الناتجة الضوء على الاختلافات، مما يسهل تحديد التغييرات بين الملفين.

فيما يلي قائمة بالطرق الممكنة لمقارنة مستندات PDF باستخدام Aspose.PDF لـ Python عبر مكتبة.NET:

1. **مقارنة صفحات محددة** - قارن الصفحات الأولى من وثيقتي PDF.
1. ** مقارنة المستندات بالكاملة** - قارن المحتوى الكامل لمستندين PDF.
1. **قارن مستندات PDF بيانيًا**:

- قارن PDF مع طريقة «comparer.get_difference» - الصور الفردية حيث يتم وضع علامة على التغييرات.
- قارن PDF مع طريقة «comparer.compare_documents_to_pdf» - مستند PDF مع الصور حيث يتم وضع علامة على التغييرات.

## مقارنة صفحات محددة

يوضح مقتطف الشفرة الأول كيفية مقارنة الصفحات الأولى من مستندين PDF باستخدام فئة SidebysidePDFComparer.

1. تهيئة المستند.
1. قم بإنشاء وظيفة لإجراء المقارنة.
1. عملية المقارنة:

- document1.pages [1] و document2.pages [1]: - تحدد هذه الصفحات الصفحة الأولى من كل مستند للمقارنة. لاحظ أن فهرسة الصفحات تبدأ من 1 في Aspose.PDF.
- خيارات المقارنة جنبًا إلى جنب - تسمح هذه الفئة بتخصيص سلوك المقارنة.
- additional_change_marks = True - يتيح عرض علامات تغيير إضافية، مع إبراز الاختلافات التي قد تكون موجودة في الصفحات الأخرى، حتى لو لم تكن موجودة في الصفحة الحالية التي تتم مقارنتها.
- comparison_mode = comparisonMode.ignorespaces - يضبط وضع المقارنة لتجاهل المسافات في النص، مع التركيز فقط على التغييرات داخل الكلمات.

1. يتم حفظ نتيجة المقارنة كملف PDF جديد باسم ComparingSpecificPages_out.pdf في data_dir المحدد.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_specific_pages(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1.pages[1], document_2.pages[1], outfile, options
    )
```

## مقارنة المستندات بأكملها

يوسع مقتطف الشفرة الثاني النطاق لمقارنة المحتوى الكامل لمستندين PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def comparing_entire_documents(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Compare
    options = ap.comparison.SideBySideComparisonOptions()
    options.additional_change_marks = True
    options.comparison_mode = ap.comparison.ComparisonMode.IGNORE_SPACES

    # Perform comparison and save the result
    ap.comparison.SideBySidePdfComparer.compare(
        document_1, document_2, outfile, options
    )
```

يوضح الكود المقدم مقارنة مستندين PDF باستخدام Aspose.PDF لـ Python عبر .NET. يستخدم فئة SidebysidePDFComparer لإجراء مقارنة صفحة بصفحة، وإنشاء ملف PDF جديد يعرض الاختلافات جنبًا إلى جنب. تم تكوين المقارنة باستخدام sidebysideComparisonOptions، حيث يتم تعيين addition_change_marks إلى True لتسليط الضوء على التغييرات ليس فقط على الصفحة الحالية ولكن أيضًا على الصفحات الأخرى، ويتم تعيين comparison_mode على ignorespaces للتركيز على اختلافات المحتوى ذات المعنى من خلال تجاهل اختلافات المسافات البيضاء.

## قارن باستخدام مقارنة PDF الرسومية

عند التعاون على المستندات، خاصة في البيئات المهنية، غالبًا ما ينتهي بك الأمر بإصدارات متعددة من نفس الملف.
يوضح الكود المقدم كيفية المقارنة المرئية لصفحات معينة من مستندين PDF باستخدام Aspose.PDF لـ Python عبر .NET. باستخدام `GraphicalPdfComparer` الفئة، تسلط الضوء على الاختلافات بين الصفحات الأولى من ملفي PDF وتنشئ الصور المقابلة لتمثيل هذه الاختلافات.

يمكنك تعيين خصائص الفئة التالية:

- الدقة - الدقة بوحدات DPI للصور الناتجة، وكذلك للصور التي تم إنشاؤها أثناء المقارنة.
- اللون - لون علامات التغيير.
- العتبة - تغيير العتبة بالنسبة المئوية. القيمة الافتراضية هي صفر. يتيح لك تعيين قيمة أخرى غير الصفر تجاهل التغييرات الرسومية غير المهمة بالنسبة لك.

باستخدام Aspose.PDF لـ Python عبر .NET، من الممكن مقارنة المستندات والصفحات وإخراج نتيجة المقارنة إلى مستند PDF أو ملف صورة.

ال `GraphicalPdfComparer` يحتوي الفصل الدراسي على طريقة تسمح لك بالحصول على اختلافات في صورة الصفحة في نموذج مناسب لمزيد من المعالجة: `get_difference(document1.pages[1], document2.pages[1])`.

تقوم هذه الطريقة بإرجاع كائن من `images_difference` النوع، الذي يحتوي على صورة للصفحة الأولى التي تتم مقارنتها ومجموعة من الاختلافات.

ال `images_difference` يسمح لك الكائن بإنشاء صورة مختلفة والحصول على صورة للصفحة الثانية التي تتم مقارنتها من خلال تطبيق مجموعة من الاختلافات على الصورة الأصلية. للقيام بذلك، استخدم `difference_to_image` و `get_destination_image` أساليب.

### قارن PDF مع طريقة الحصول على الفرق

تحدد التعليمات البرمجية المقدمة طريقة `get_difference` يقارن وثيقتين من وثائق PDF ويولد تمثيلات مرئية للاختلافات بينهما.

تقارن هذه الطريقة الصفحات الأولى من ملفي PDF وتنشئ صورتين PNG:

- تبرز إحدى الصور الاختلافات بين الصفحات باللون الأحمر.
- الصورة الأخرى عبارة عن تمثيل مرئي لصفحة PDF الوجهة (الثانية).

يمكن أن تكون هذه العملية مفيدة لمقارنة التغييرات أو الاختلافات بشكل مرئي بين نسختين من المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_get_difference_method(infile1, infile2, outfile1, outfile2):
    # Open PDF documents
    document1 = ap.Document(infile1)
    document2 = ap.Document(infile2)

    # Create comparer
    comparer = ap.comparison.GraphicalPdfComparer()

    # Compare specific pages
    images_difference = comparer.get_difference(document1.pages[1], document2.pages[1])

    # Get image showing differences in red over a white background
    diff_img = images_difference.difference_to_image(ap.Color.red, ap.Color.white)
    diff_img.save(outfile1)

    # Get the second image representing the destination page
    dest_img = images_difference.get_destination_image()
    dest_img.save(outfile2)
```

### قارن PDF مع طريقة مقارنة المستندات بـ PDF

يستخدم مقتطف الشفرة المقدم `compare_documents_to_pdf` الطريقة، التي تقارن وثيقتين وتقوم بإنشاء تقرير PDF لنتائج المقارنة.

```python
import aspose.pdf as ap
import sys
from os import path

def compare_pdf_with_compare_documents_to_pdf_method(infile1, infile2, outfile):
    # Open PDF documents
    document_1 = ap.Document(infile1)
    document_2 = ap.Document(infile2)

    # Create comparer and set options
    pdf_comparer = ap.comparison.GraphicalPdfComparer()
    pdf_comparer.threshold = 3.0
    pdf_comparer.color = ap.Color.blue
    pdf_comparer.resolution = ap.devices.Resolution(300)

    # Compare and output to a PDF file
    pdf_comparer.compare_documents_to_pdf(document_1, document_2, outfile)
```

يوضح هذا المثال كيفية إجراء مقارنة رسومية بين مستندين كاملين من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. من خلال الاستفادة من `GraphicalPdfComparer` الفصل، يقوم بإنشاء ملف PDF جديد يبرز بصريًا الاختلافات بين المستندات.

- تم تعيين خاصية threshold على 3.0، مما يعني أنه يتم تجاهل الاختلافات الطفيفة التي تقل عن هذه النسبة أثناء المقارنة، مع التركيز على التغييرات الأكثر أهمية.
- يتم تمييز الاختلافات باللون الأزرق عن طريق تعيين خاصية اللون على AP.color.blue، مما يسمح بتمييز مرئي واضح.
- يتم إجراء المقارنة بدقة 300 نقطة في البوصة عن طريق تعيين خاصية الدقة، وضمان إخراج مفصل وواضح.

ال `compare_documents_to_pdf` تقارن الطريقة جميع صفحات كلا المستندين وتخرج النتيجة إلى ملف PDF جديد، compareDocumentsToPdf_out.pdf، مع تمييز الاختلافات بصريًا.

## موضوعات ذات صلة

- [عمليات PDF المتقدمة في بايثون](/pdf/ar/python-net/advanced-operations/)
- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [العمل مع نص PDF في بايثون](/pdf/ar/python-net/working-with-text/)
