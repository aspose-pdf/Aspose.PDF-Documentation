---
title: استبدال النص في PDF باستخدام Python
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /ar/python-net/replace-text-in-pdf/
description: تعرّف على كيفية استبدال النص في ملفات PDF باستخدام Python، بما في ذلك استبدال النص عبر الصفحات، وتحديد التغييرات إلى منطقة معينة في الصفحة، واستخدام التعبيرات النمطية (regex)، وإزالة النص.
lastmod: "2026-06-05"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: استبدل النص وأزِل النص في ملفات PDF باستخدام Python
Abstract: توفر هذه المقالة طريقة استبدال النص في مستندات PDF باستخدام Aspose.PDF for Python via .NET. وتغطي استبدال النص عبر جميع الصفحات، واستبدال النص في منطقة الصفحة، ومطابقة التعبيرات النمطية، واستبدال الخط، وضبط تخطيط النص، وإزالة النص الظاهر أو المخفي.
---

تُظهر هذه الصفحة كيفية **استبدال النص في PDF باستخدام Python** باستخدام Aspose.PDF for Python via .NET.

استخدم هذه الأمثلة عندما تحتاج إلى تحديث قيم النص، وإزالة المحتوى غير المرغوب فيه، واستبدال النص في منطقة صفحة معينة، أو تطبيق قواعد استبدال النص عبر صفحات PDF متعددة.

## استبدال النص في PDF باستخدام Python

### استبدال النص في جميع صفحات مستند PDF

{{% alert color="primary" %}}

يمكنك تجربة البحث عن النص والاستبدال عبر الإنترنت باستخدام Aspose.PDF. [تطبيق التعتيم](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

استبدال النص هو طلب شائع عند تحديث أو تصحيح المحتوى في مستندات PDF الموجودة — على سبيل المثال، تغيير أسماء المنتجات، تصحيح الأخطاء المطبعية، أو تحديث المصطلحات عبر صفحات متعددة.

توفر Aspose.PDF for Python via .NET طريقة قوية وفعّالة للبحث واستبدال النص برمجياً عبر [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) فئة.

يوضح هذا المثال كيفية العثور على جميع تكرارات عبارة محددة (في هذه الحالة، "Black cat") واستبدالها بعبارة جديدة ("White dog") عبر كامل مستند PDF.

1. حدد عبارات البحث والاستبدال. عيّن النص الذي تريد العثور عليه والنص الذي تريد استبداله به.
1. حمّل مستند PDF.
1. إنشاء Text Absorber. يتم تهيئة TextFragmentAbsorber بعبارة البحث. يقوم بمسح المستند للعثور على جميع حالات العبارة المعطاة.
1. طبق الـ Absorber على جميع الصفحات. يُجري هذا التكرار عبر جميع الصفحات ويجمع مقاطع النص التي تطابق العبارة.
1. استبدل كل جزء تم العثور عليه. يجب تغيير كل ظهور لـ "Black cat" إلى "White dog".
1. احفظ ملف PDF المحدث.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_on_all_pages(infile, outfile):
    search_phrase = "PDF"
    replace_phrase = "pdf"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### استبدال النص في منطقة صفحة محددة

أحيانًا، قد تحتاج إلى استبدال النص فقط داخل منطقة محددة من صفحة PDF بدلاً من البحث في المستند بأكمله — على سبيل المثال، تحديث عنوان، تذييل، أو خلية جدول ضمن موضع معروف.

تمكّن مكتبة Aspose.PDF for Python via .NET من هذه الوظيفة باستخدام [TextFragmentAbsorber](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) بالاشتراك مع البحث النصي القائم على المناطق.

يوضح هذا المثال كيفية البحث عن جميع تكرارات العبارة المستهدفة واستبدالها داخل منطقة مستطيلة محددة على صفحة معينة.

1. حدد عبارات البحث والاستبدال.
1. حمّل مستند PDF.
1. إنشاء Text Absorber للبحث. تهيئة TextFragmentAbsorber للعثور على النص المطلوب.
1. قصر منطقة البحث. يحدد المستطيل حدود إحداثيات x و y على الصفحة.
1. تطبيق Absorber على صفحة محددة. يؤدي هذا إلى إجراء البحث وجمع شظايا النص المتطابقة داخل المنطقة المحددة.
1. استبدل النص الموجود. كل ظهور لـ 'doc' في المنطقة المحددة يصبح 'DOC'.
1. احفظ ملف PDF المحدث.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_in_particular_page_region(infile, outfile):
    search_phrase = "doc"
    replace_phrase = "DOC"

    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(search_phrase)
        absorber.text_search_options.limit_to_page_bounds = True
        absorber.text_search_options.rectangle = ap.Rectangle(300, 442, 500, 742, True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = replace_phrase

        document.save(outfile)
```

### تغيير حجم النص وتحريكه دون تغيير حجم الخط

عند استبدال النص في ملف PDF، قد ترغب أحيانًا في ملاءمة النص الجديد أو إعادة وضعه داخل مساحة محددة دون تعديل حجم الخط.
يوفر Aspose.PDF for Python via .NET خيارات لضبط تخطيط النص والمسافات مع الحفاظ على حجم الخط الأصلي دون تغيير.

1. حمّل مستند PDF.
1. اجمع جميع قطع النص على الصفحة باستخدام 'TextFragmentAbsorber'.
1. حدد المقتطف لتعديله.
1. تحريك وتغيير حجم مستطيل النص.
1. ضبط تباعد النص. تمكين ضبط التباعد لتلائم النص داخل المستطيل المعدل.
1. استبدل نص القطعة.
1. احفظ ملف PDF المحدث.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_without_changing_font_size(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = fragment.rectangle
        rect.llx += 50
        rect.urx -= 50
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### تغيير حجم وتحريك فقرة في PDF

عند العمل مع ملفات PDF، قد تحتاج أحيانًا إلى استبدال فقرة أو توسيعها مع الحفاظ على محاذاتها البصرية مع تخطيط الصفحة. يتيح لك Aspose.PDF إعادة تحجيم المستطيل الحدودي للفقرة وضبط التباعد لتناسب النص الجديد، كل ذلك دون تغيير حجم الخط.

1. حمّل مستند PDF.
1. استخدم 'TextFragmentAbsorber' لجمع جميع مقاطع النص في الصفحة.
1. حدد المقتطف لتعديله.
1. تغيير حجم الفقرة وتحريكها. استخدم مربع وسائط الصفحة لتحديد الحدود وضبط المستطيل.
1. ضبط التباعد. هذا يعدل التباعد بين الكلمات/الحروف بدلاً من تغيير حجم الخط.
1. استبدل نص القطعة.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_shift_paragraph(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        rect = document.pages[1].media_box
        rect.llx += 20
        rect.urx -= 20
        rect.ury -= 20
        fragment.replace_options.rectangle = rect
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### استبدال النص وتوسيع الخط تلقائيًا لملء المنطقة المستهدفة

استبدال النص في ملف PDF مع تغيير حجم الخط وتوسيعه تلقائيًا لملء منطقة مستطيلة محددة. باستخدام مكتبة Aspose.PDF for Python via .NET، يقوم الكود بضبط حجم الخط والمسافات ديناميكيًا بحيث يتناسب المحتوى النصي الجديد تمامًا داخل صندوق حدودي محدد — دون الحاجة إلى حسابات يدوية للخط.

1. حمّل ملف PDF.
1. التقاط مقاطع النص.
1. حدد جزءًا محددًا.
1. حدد المستطيل المستهدف.
1. تمكين خيارات تعديل النص.
1. استبدال النص.
1. احفظ المستند.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_resize_and_expand_font(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = ap.Rectangle(100, 300, 512, 692, True)
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SCALE_TO_FILL
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### استبدال النص وتكييفه داخل مستطيل

استبدل النص في مستند PDF مع ضمان أن المحتوى الجديد يتناسب مع المنطقة المستطيلة للنص الأصلي عن طريق تقليل حجم الخط تلقائيًا عند الحاجة.

باستخدام مكتبة Aspose.PDF for Python via .NET، تقوم هذه الدالة بضبط كل من تخطيط النص وحجم Font ديناميكيًا، مع الحفاظ على بنية المستند ومنع الفائض.

1. إنشاء كائن TextFragmentAbsorber لاستخراج جميع مقاطع النص من الصفحة الأولى.
1. الوصول إلى مقطع نصي محدد.
1. حدد منطقة الاستبدال.
1. قم بتكوين خيارات تعديل النص. اضبط خيارين رئيسيين للاستبدال:
    - ضبط حجم الخط - 'SHRINK_TO_FIT' يقلل حجم الخط تلقائيًا إذا كان النص الجديد طويلاً جدًا.
    - تعديل المسافة - \u0027ADJUST_SPACE_WIDTH\u0027 يحافظ على تناسب المسافات.
1. استبدل النص.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_and_fit_text_into_rectangle(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.visit(document.pages[1])
        fragment = absorber.text_fragments[1]
        text = fragment.text
        fragment.replace_options.rectangle = fragment.rectangle
        fragment.replace_options.font_size_adjustment_action = (
            ap.text.TextReplaceOptions.FontSizeAdjustment.SHRINK_TO_FIT
        )
        fragment.replace_options.replace_adjustment_action = (
            ap.text.TextReplaceOptions.ReplaceAdjustment.ADJUST_SPACE_WIDTH
        )
        fragment.text = f"{text} {text}"
        document.save(outfile)
```

### استبدال النص النائب تلقائيًا وإعادة ترتيب تخطيط PDF

استبدل نص العنصر النائب داخل ملف PDF (مثلاً القوالب أو النماذج) ببيانات فعلية مثل الأسماء أو معلومات الشركة.
يقوم تلقائيًا بتعديل تخطيط الصفحة ليتناسب مع النص الجديد مع تطبيق تنسيق مخصص (الخط، اللون، الحجم).

1. استيراد وتحميل ملف PDF.
1. إنشاء TextAbsorber للعنصر النائب.
1. طبق الـ Absorber على جميع الصفحات.
1. التكرار عبر مقاطع النص المكتشفة.
1. تطبيق تنسيق النص المخصص.
1. احفظ المستند المحدث.

```python
import sys
import aspose.pdf as ap
from os import path

def automatically_rearrange_page_contents(input_file, output_file):
    document = ap.Document(input_file)

    absorber = ap.text.TextFragmentAbsorber("[Long_placeholder_Long_placeholder]")
    document.pages.accept(absorber)

    for text_fragment in absorber.text_fragments:
        # text_fragment.text = "John Smith"
        text_fragment.text = "John Smith, South Development Studio"
        text_fragment.text_state.font = ap.text.FontRepository.find_font("Calibri")
        text_fragment.text_state.font_size = 12
        text_fragment.text_state.foreground_color = ap.Color.navy

    # Save PDF document
    document.save(output_file)
```

### استبدال النص بناءً على تعبير نمطي

عند العمل مع مستندات PDF، قد تحتاج إلى استبدال النص الذي يتبع نمطًا بدلاً من عبارة محددة — على سبيل المثال، أرقام الهواتف، الأكواد، أو الصيغ الشبيهة بالتواريخ.

يسمح لك Aspose.PDF for Python via .NET بإجراء مثل هذه الاستبدالات باستخدام تعبيرات عادية (regex) مع الفئة TextFragmentAbsorber.

يوضح هذا المثال كيفية العثور على أنماط النص (في هذه الحالة، أي نص يطابق الشكل ####-####، مثل 1234-5678) واستبداله بسلسلة منسقة 'ABC1-2XZY'. كما يظهر كيفية تخصيص الخط واللون والحجم للنص المستبدل.

المقتطف البرمجي التالي يوضح لك كيفية استبدال النص بناءً على تعبير نمطي.

1. حمّل مستند PDF.
1. إنشاء Text Absorber يعتمد على تعبير نمطي. قم بتهيئة TextFragmentAbsorber باستخدام نمط تعبير نمطي.
1. تمكين وضع التعبير النمطي. المعامل \u0027True\u0027 يُفعِّل وضع البحث بالتعبير النمطي.
1. طبق الـ Absorber على صفحة. يقوم هذا بمسح الصفحة للعثور على جميع TextFragment التي تطابق نمط regex المحدد.
1. استبدل كل تطابق بنص جديد وطبق تنسيقًا مخصصًا.
1. احفظ المستند المعدَّل.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_text_based_on_regex(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber(r"\d{4}-\d{4}")
        absorber.text_search_options = ap.text.TextSearchOptions(True)
        document.pages[1].accept(absorber)

        for fragment in absorber.text_fragments:
            fragment.text = "ABC1-2XZY"
            fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")
            fragment.text_state.font_size = 12
            fragment.text_state.foreground_color = ap.Color.blue
            fragment.text_state.background_color = ap.Color.light_green

        document.save(outfile)
```

## استبدال الخطوط أو إزالة الخطوط غير المستخدمة

### استبدال الخطوط في ملف PDF موجود

في بعض الأحيان، تحتاج إلى توحيد أو تحديث الخطوط عبر PDF — على سبيل المثال، استبدال خط قديم أو مملوك بخط أكثر سهولة. مكتبة Aspose.PDF for Python via .NET تسمح لك باكتشاف الخطوط واستبدالها برمجيًا، مما يضمن تناسق الطباعة وتوافق المستند.

يوضح هذا المثال كيفية استبدال جميع حالات الخط المحدد (مثل 'Arial-BoldMT') بخط آخر (مثل 'Verdana') عبر مستند PDF.

يظهر مقتطف الكود التالي كيفية استبدال الخط داخل مستند PDF:

1. افتح مستند PDF.
1. تهيئة TextFragmentAbsorber.
1. استخدم الـ Absorber لاستخراج شظايا النص من كل صفحة في المستند.
1. تحديد واستبدال الخطوط. يتحقق البرنامج النصي مما إذا كان الخط الحالي للجزء هو ‘Arial-BoldMT’. إذا كان كذلك، فإنه يستبدله بخط ‘Verdana’ باستخدام طريقة FontRepository.find_font().
1. احفظ المستند المعدَّل.

```python
import sys
import aspose.pdf as ap
from os import path

def replace_fonts(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        document.pages.accept(absorber)

        for fragment in absorber.text_fragments:
            if fragment.text_state.font.font_name == "Arial-BoldMT":
                fragment.text_state.font = ap.text.FontRepository.find_font("Verdana")

        document.save(outfile)
```

### إزالة الخطوط غير المستخدمة

مع مرور الوقت، يمكن أن تتراكم في مستندات PDF خطوط غير مستخدمة أو مدمجة تزيد من حجم الملف وتبطئ المعالجة. غالبًا ما تبقى هذه الخطوط غير المستخدمة حتى بعد تعديل النص أو استبداله، خاصةً عند العمل مع ملفات PDF الكبيرة أو المعقدة.

توفر مكتبة Aspose.PDF for Python via .NET طريقة فعّالة لإزالة الخطوط الزائدة باستخدام فئة TextEditOptions. فهذا لا يحسّن مستندك فحسب، بل يضمن أيضًا أنه يستخدم الخطوط التي تم تطبيقها فعليًا على النص الظاهر فقط.

طريقة 'remove_unused_fonts()' هي طريقة بسيطة ولكن قوية لتحسين ملفات PDF عن طريق إزالة بيانات الخط الزائدة.

هذا المثال يوضح كيفية:

- مسح ملف PDF للخطوط غير المستخدمة.
- أزلهم بأمان.
- إعادة تعيين مقاطع النص النشطة إلى خط موحد (مثل Times New Roman).

1. افتح مستند PDF.
1. قم بتكوين خيارات تحرير النص. هذا يوجه المحرك لحذف أي خطوط مضمنة غير مستخدمة حاليًا في النص الظاهر.
1. إنشاء Text Absorber مع خيارات. يقوم TextFragmentAbsorber باستخراج مقاطع النص من المستند للتحرير.
1. إعادة تعيين خط قياسي. بمجرد أن يجمع الـ absorber جميع الـ fragments، قم بالتكرار عبرها وتطبيق خط موحد.
1. احفظ ملف PDF المنقّح.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_unused_fonts(input_file, output_file):
    # Open PDF document
    document = ap.Document(input_file)

    # Initialize text edit options to remove unused fonts
    options = ap.text.TextEditOptions(
        ap.text.TextEditOptions.FontReplace.REMOVE_UNUSED_FONTS
    )

    # Create a TextFragmentAbsorber with the specified options
    absorber = ap.text.TextFragmentAbsorber(options)
    document.pages.accept(absorber)

    # Iterate through all TextFragments
    for text_fragment in absorber.text_fragments:
        text_fragment.text_state.font = ap.text.FontRepository.find_font(
            "TimesNewRoman"
        )

    # Save the updated PDF document
    document.save(output_file)
```

## إزالة جميع النص

### إزالة النص من PDF

إزالة جميع محتوى النص من ملف PDF مع الحفاظ على الصور والأشكال وهياكل التخطيط دون تغيير.
باستخدام TextFragmentAbsorber، يقوم الكود بمسح المستند بالكامل بكفاءة ويحذف كل مجزأ نصي موجود في كل صفحة.

1. حمّل مستند PDF.
1. يتم إنشاء كائن TextFragmentAbsorber لاكتشاف ومعالجة مقاطع النص في ملف PDF.
1. إزالة جميع محتوى النص. الطريقة 'absorber.remove_all_text()' تزيل كل عنصر نصي من المستند المحمَّل، وتترك المكونات غير النصية دون تعديل.
1. احفظ المستند المحدث.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber1(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document)
        document.save(outfile)
```

### إزالة كل النص من صفحة محددة

إزالة جميع النصوص من صفحة واحدة في مستند PDF باستخدام الفئة TextFragmentAbsorber في Aspose.PDF.
على عكس إزالة المستند بالكامل، تقوم هذه الطريقة بتنظيف النص على مستوى الصفحة، حيث تُحذف النصوص فقط من الصفحة المختارة بينما تُترك جميع الصفحات الأخرى دون تعديل.

1. حمّل ملف PDF.
1. إنشاء مثيل TextFragmentAbsorber.
1. إزالة كل النص من الصفحة الأولى.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber2(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(document.pages[1])
        document.save(outfile)
```

### إزالة جميع النص من منطقة معينة في صفحة PDF

إزالة جميع النصوص من منطقة مستطيلة محددة على صفحة باستخدام TextFragmentAbsorber من Aspose.PDF.
بدلاً من مسح صفحة كاملة، تقوم هذه الطريقة بإزالة النص المستهدف، مما يسمح بتحكم دقيق في الجزء المتأثر من الصفحة.

1. حمّل مستند PDF.
1. إنشاء TextFragmentAbsorber.
1. حدد المنطقة المستهدفة (مستطيل).
1. إزالة النص من المنطقة المحددة.
1. احفظ بقية المستند.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_all_text_using_absorber3(infile, outfile):
    with ap.Document(infile) as document:
        absorber = ap.text.TextFragmentAbsorber()
        absorber.remove_all_text(
            document.pages[1], ap.Rectangle(10, 200, 120, 600, True)
        )
        document.save(outfile)
```

### إزالة كل النص المخفي من مستند PDF

إزالة جميع النصوص من منطقة مستطيلة محددة على صفحة باستخدام TextFragmentAbsorber من Aspose.PDF.
بدلاً من مسح صفحة كاملة، تقوم هذه الطريقة بإزالة النص المستهدف، مما يسمح بتحكم دقيق في الجزء المتأثر من الصفحة.

1. حمّل مستند PDF.
1. إنشاء TextFragmentAbsorber.
1. حدد المنطقة المستهدفة (مستطيل).
1. إزالة النص من المنطقة المحددة.
1. احفظ بقية المستند.
1. احفظ ملف PDF المعدل.

```python
import sys
import aspose.pdf as ap
from os import path

def remove_hidden_text(infile, outfile):
    # Open PDF document
    with ap.Document(infile) as document:
        text_absorber = ap.text.TextFragmentAbsorber()
        # This option can be used to prevent other text fragments from moving after hidden text replacement
        text_absorber.text_replace_options = ap.text.TextReplaceOptions(
            ap.text.TextReplaceOptions.ReplaceAdjustment.NONE
        )
        document.pages.accept(text_absorber)
        # Remove hidden text
        for fragment in text_absorber.text_fragments:
            if fragment.text_state.invisible:
                fragment.text = ""
        # Save PDF document
        document.save(outfile)
```

## المواضيع ذات الصلة بالنص

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)
- [البحث واستخراج نص PDF في Python](/pdf/ar/python-net/search-and-get-text-from-pdf/)
- [تنسيق نص PDF في Python](/pdf/ar/python-net/text-formatting-inside-pdf/)
