---
title: استبدل النص في PDF باستخدام Python
linktitle: استبدال النص في PDF
type: docs
weight: 40
url: /ar/python-net/replace-text-in-pdf/
description: تعرف على كيفية استبدال النص في ملفات PDF باستخدام Python، بما في ذلك استبدال النص عبر الصفحات، وتقييد التغييرات في منطقة الصفحة، واستخدام regex، وإزالة النص.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
aliases:
    - /python-net/replace-text-in-a-pdf-document/
TechArticle: true
AlternativeHeadline: استبدال النص وإزالته في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية استبدال النص في مستندات PDF بـ Aspose.PDF لـ Python عبر .NET. ويغطي استبدال النص في جميع الصفحات، واستبدال منطقة الصفحة، ومطابقة التعبير العادي، واستبدال الخط، وتعديل تخطيط النص، وإزالة النص المرئي أو المخفي.
---

تعرض هذه الصفحة كيفية**استبدال النص في ملف PDF باستخدام Python** باستخدام Aspose.PDF لبيثون عبر .NET.

استخدم هذه الأمثلة عندما تحتاج إلى تحديث قيم النص أو إزالة المحتوى غير المرغوب فيه أو استبدال النص في منطقة صفحة معينة أو تطبيق قواعد استبدال النص عبر صفحات PDF متعددة.

## استبدل النص في PDF باستخدام Python

### استبدال النص في جميع صفحات وثيقة PDF

{{% alert color="primary" %}}

يمكنك تجربة البحث عن النص واستبداله عبر الإنترنت باستخدام Aspose.PDF [تطبيق التنقيح](https://products.aspose.app/pdf/redaction).

{{% /alert %}}

يعد استبدال النص مطلبًا شائعًا عند تحديث أو تصحيح المحتوى في مستندات PDF الحالية - على سبيل المثال، تغيير أسماء المنتجات أو إصلاح الأخطاء المطبعية أو تحديث المصطلحات عبر صفحات متعددة.

يقدم Aspose.PDF لـ Python عبر .NET طريقة قوية وفعالة للبحث عن النص واستبداله برمجيًا من خلال [ممتص أجزاء النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) فئة.

يوضح هذا المثال كيفية العثور على جميع تكرارات عبارة معينة (في هذه الحالة، «القطة السوداء») واستبدالها بعبارة جديدة («White dog») في مستند PDF بأكمله.

1. حدد عبارات البحث والاستبدال. قم بتعيين النص الذي تريد البحث عنه والنص الذي تريد استبداله به.
1. قم بتحميل وثيقة PDF.
1. قم بإنشاء أداة امتصاص النص. تتم تهيئة TextFragmentAbsorber باستخدام عبارة البحث. يقوم بمسح المستند بحثًا عن جميع مثيلات العبارة المحددة.
1. قم بتطبيق جهاز الامتصاص على جميع الصفحات. يتكرر هذا من خلال جميع الصفحات ويجمع أجزاء النص المطابقة للعبارة.
1. استبدل كل جزء موجود. يجب تغيير كل نسخة من «القطة السوداء» إلى «الكلب الأبيض».
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

في بعض الأحيان، قد تحتاج إلى استبدال النص فقط داخل منطقة معينة من صفحة PDF بدلاً من البحث في المستند بأكمله - على سبيل المثال، تحديث رأس الصفحة أو تذييلها أو خلية جدول ضمن موضع معروف.

تتيح مكتبة Aspose.PDF لـ Python عبر مكتبة.NET هذه الوظيفة من خلال استخدام [ممتص أجزاء النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/) بالتزامن مع البحث عن النص المستند إلى المنطقة.

يوضح هذا المثال كيفية البحث عن جميع تكرارات العبارة المستهدفة واستبدالها داخل منطقة مستطيلة محددة على صفحة معينة.

1. حدد عبارات البحث والاستبدال.
1. قم بتحميل وثيقة PDF.
1. قم بإنشاء ممتص نص للبحث. قم بتهيئة TextFragmentAbsorber للعثور على النص المطلوب.
1. قم بتقييد منطقة البحث. يحدد المستطيل حدود الإحداثيات x و y على الصفحة.
1. قم بتطبيق جهاز الامتصاص على صفحة محددة. يؤدي هذا إلى إجراء البحث وجمع أجزاء النص المطابقة داخل المنطقة المحددة.
1. استبدل النص الذي تم العثور عليه. كل تكرار لـ «doc» في المنطقة المحددة يصبح «DOC».
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

### تغيير حجم النص وتحويله دون تغيير حجم الخط

عند استبدال النص في PDF، قد ترغب أحيانًا في ملاءمة النص الجديد أو إعادة وضعه داخل منطقة معينة دون تعديل حجم الخط.
يوفر Aspose.PDF لـ Python عبر .NET خيارات لضبط تخطيط النص والمسافات مع الحفاظ على حجم الخط الأصلي كما هو.

1. قم بتحميل وثيقة PDF.
1. اجمع كل أجزاء النص على الصفحة باستخدام «TextFragmentAbsorber».
1. حدد الجزء لتعديله.
1. قم بتحويل مستطيل النص وتغيير حجمه.
1. اضبط تباعد النص. قم بتمكين ضبط المسافات لملاءمة النص داخل المستطيل المعدل.
1. استبدل نص الجزء.
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

### تغيير حجم وتحويل فقرة في PDF

عند العمل مع ملفات PDF، تحتاج أحيانًا إلى استبدال فقرة أو توسيعها مع الحفاظ على مواءمتها بصريًا مع تخطيط الصفحة. يسمح لك Aspose.PDF بتغيير حجم المستطيل المحيط بالفقرة وضبط المسافات لتناسب النص الجديد، كل ذلك دون تغيير حجم الخط.

1. قم بتحميل وثيقة PDF.
1. استخدم «TextFragmentAbsorber» لجمع كل أجزاء النص على الصفحة.
1. حدد الجزء لتعديله.
1. قم بتغيير حجم الفقرة وتحويلها. استخدم مربع وسائط الصفحة لتحديد الحدود وضبط المستطيل.
1. اضبط المسافات. يؤدي هذا إلى تعديل المسافات بين الكلمات/الحروف بدلاً من تغيير حجم الخط.
1. استبدل نص الجزء.
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

### استبدل النص وقم بتوسيع الخط تلقائيًا لملء المنطقة المستهدفة

استبدل النص في PDF مع تغيير حجم الخط وتوسيعه تلقائيًا لملء منطقة مستطيلة معينة. باستخدام Aspose.PDF لـ Python عبر مكتبة.NET، تقوم الشفرة بضبط حجم الخط والمسافات ديناميكيًا بحيث يتناسب محتوى النص الجديد تمامًا مع مربع محيط محدد - بدون حسابات الخط اليدوية.

1. قم بتحميل ملف PDF.
1. التقاط أجزاء النص.
1. حدد جزءًا محددًا.
1. حدد المستطيل المستهدف.
1. قم بتمكين خيارات تعديل النص.
1. استبدل النص.
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

### استبدل النص وقم بتركيبه في مستطيل

استبدل النص في مستند PDF مع التأكد من أن المحتوى الجديد يتناسب مع المنطقة المستطيلة للنص الأصلي عن طريق تقليل حجم الخط تلقائيًا عند الحاجة.

باستخدام Aspose.PDF لـ Python عبر مكتبة.NET، تقوم هذه الوظيفة بضبط كل من تخطيط النص وحجم الخط ديناميكيًا، مع الحفاظ على بنية المستند مع منع تجاوز السعة.

1. قم بإنشاء كائن TextFragmentAbsorber لاستخراج جميع أجزاء النص من الصفحة الأولى.
1. قم بالوصول إلى جزء نصي محدد.
1. قم بتعيين منطقة الاستبدال.
1. قم بتكوين خيارات تعديل النص. قم بتعيين خيارين رئيسيين للاستبدال:
    - تعديل حجم الخط - يعمل 'SHRINK_TO_FIT' تلقائيًا على تقليل حجم الخط إذا كان النص الجديد طويلًا جدًا.
    - تعديل المسافات - «ADJUST_SPACE_WIDTH» يحافظ على التباعد متناسبًا.
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

### استبدال نص العنصر النائب تلقائيًا وإعادة ترتيب تخطيط PDF

استبدل نص العنصر النائب داخل PDF (مثل القوالب أو النماذج) بالبيانات الفعلية مثل الأسماء أو معلومات الشركة.
يقوم تلقائيًا بضبط تخطيط الصفحة ليناسب النص الجديد أثناء تطبيق التنسيق المخصص (الخط واللون والحجم).

1. قم باستيراد وتحميل ملف PDF.
1. قم بإنشاء أداة امتصاص النص للعنصر النائب.
1. قم بتطبيق جهاز الامتصاص على جميع الصفحات.
1. حلقة من خلال أجزاء النص الموجودة.
1. قم بتطبيق تنسيق النص المخصص.
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

### استبدال النص بناءً على تعبير عادي

عند التعامل مع مستندات PDF، قد تحتاج إلى استبدال النص الذي يتبع نمطًا بدلاً من عبارة محددة - على سبيل المثال، أرقام الهواتف أو الرموز أو التنسيقات الشبيهة بالتاريخ.

يسمح لك Aspose.PDF لـ Python عبر .NET بإجراء مثل هذه الاستبدالات باستخدام التعبيرات العادية (regex) مع فئة TextFragmentAbsorber.

يوضح هذا المثال كيفية العثور على أنماط النص (في هذه الحالة، أي نص يطابق التنسيق ####-####، مثل 1234-5678) واستبدالها بسلسلة منسقة «ABC1-2XZY». كما يوضح كيفية تخصيص الخط واللون وحجم النص الذي تم استبداله.

يوضح لك مقتطف الشفرة التالي كيفية استبدال النص استنادًا إلى تعبير عادي.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء ممتص نص يستند إلى Regex. قم بتهيئة TextFragmentAbsorber بنمط تعبير عادي.
1. قم بتمكين وضع التعبير العادي. تقوم المعلمة «True» بتنشيط وضع البحث عن التعبير العادي.
1. قم بتطبيق جهاز الامتصاص على الصفحة. يقوم هذا بمسح الصفحة بحثًا عن جميع أجزاء النص التي تطابق نمط regex المحدد.
1. استبدل كل مباراة بنص جديد وقم بتطبيق التصميم المخصص.
1. احفظ المستند المعدل.

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

### استبدل الخطوط في ملف PDF الحالي

في بعض الأحيان، تحتاج إلى توحيد الخطوط أو تحديثها عبر PDF - على سبيل المثال، استبدال خط قديم أو خاص بخط يسهل الوصول إليه. تتيح لك مكتبة Aspose.PDF for Python عبر مكتبة.NET اكتشاف الخطوط واستبدالها برمجيًا، مما يضمن الطباعة المتسقة وتوافق المستندات.

يوضح هذا المثال كيفية استبدال جميع مثيلات خط معين (على سبيل المثال، «Arial-BoldMT») بخط آخر (على سبيل المثال، «Verdana») في جميع أنحاء مستند PDF.

يوضح مقتطف الشفرة التالي كيفية استبدال الخط داخل مستند PDF:

1. افتح وثيقة PDF.
1. قم بتهيئة ممتص أجزاء النص.
1. استخدم Absorber لاستخراج أجزاء النص من كل صفحة في المستند.
1. تحديد الخطوط واستبدالها. يتحقق البرنامج النصي مما إذا كان الخط الحالي للجزء هو «Arial-BoldMT». إذا كان هذا صحيحًا، فسيتم استبداله بخط «فيردانا» باستخدام طريقة fontrepository.find_Font ().
1. احفظ المستند المعدل.

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

بمرور الوقت، يمكن لمستندات PDF تجميع الخطوط غير المستخدمة أو المضمنة التي تزيد من حجم الملف وتبطئ المعالجة. غالبًا ما تظل هذه الخطوط غير المستخدمة حتى بعد تحرير النص أو استبداله، خاصة عند العمل مع ملفات PDF الكبيرة أو المعقدة.

توفر مكتبة Aspose.PDF لـ Python عبر مكتبة.NET طريقة فعالة لإزالة هذه الخطوط الزائدة باستخدام فئة TextEditOptions. لا يؤدي ذلك إلى تحسين المستند فحسب، بل يضمن أيضًا أنه يستخدم فقط الخطوط المطبقة فعليًا على النص المرئي.

طريقة «remove_unused_fonts ()» هي طريقة بسيطة ولكنها قوية لتحسين ملفات PDF عن طريق إزالة بيانات الخط الزائدة عن الحاجة.

يوضح هذا المثال كيفية:

- قم بمسح ملف PDF بحثًا عن الخطوط غير المستخدمة.
- قم بإزالتها بأمان.
- أعد تعيين أجزاء النص النشط إلى خط ثابت (على سبيل المثال، Times New Roman).

1. افتح وثيقة PDF.
1. قم بتكوين خيارات تحرير النص. هذا يوجه المحرك لإزالة أي خطوط مضمنة غير مستخدمة حاليًا في النص المرئي.
1. قم بإنشاء أداة امتصاص النص باستخدام الخيارات. يقوم TextFragmentAbsorber باستخراج أجزاء النص من المستند لتحريرها.
1. أعد تعيين خط قياسي. بمجرد أن يجمع جهاز الامتصاص جميع الأجزاء، قم بتكرارها وتطبيق خط ثابت.
1. احفظ ملف PDF الذي تم تنظيفه.

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

## إزالة كل النص

### إزالة النص من PDF

قم بإزالة كل محتوى النص من ملف PDF مع الحفاظ على الصور والأشكال وهياكل التخطيط سليمة.
باستخدام TextFragmentAbsorber، تقوم الشفرة بمسح المستند بأكمله بكفاءة وحذف كل جزء نصي موجود في كل صفحة.

1. قم بتحميل وثيقة PDF.
1. يتم إنشاء كائن TextFragmentAbsorber لاكتشاف ومعالجة أجزاء النص في PDF.
1. قم بإزالة كل محتوى النص. تقوم الطريقة 'absorber.remove_all_text () 'بإزالة كل عنصر نصي من المستند المحمل، مع ترك المكونات غير النصية دون تغيير.
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

### قم بإزالة كل النص من صفحة محددة

قم بإزالة كل النص من صفحة واحدة من مستند PDF باستخدام فئة TextFragmentAbsorber في Aspose.PDF.
على عكس إزالة المستند الكامل، تقوم هذه الطريقة بتنظيف النص على مستوى الصفحة، وحذف النص فقط من الصفحة المختارة مع ترك جميع الصفحات الأخرى دون تغيير.

1. قم بتحميل ملف PDF.
1. قم بإنشاء مثيل TextFragmentAbsorber.
1. أزل كل النص من الصفحة الأولى.
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

### قم بإزالة كل النص من منطقة معينة على صفحة PDF

قم بإزالة كل النص من منطقة مستطيلة معينة على الصفحة باستخدام TextFragmentAbsorber الخاص بـ Aspose.PDF.
بدلاً من مسح صفحة بأكملها، تقوم هذه الطريقة بإزالة النص المستهدف، مما يسمح بالتحكم الدقيق في أي جزء من الصفحة يتأثر.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء ممتص أجزاء النص.
1. حدد المنطقة المستهدفة (المستطيل).
1. قم بإزالة النص من المنطقة المحددة.
1. احتفظ ببقية المستند.
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

### قم بإزالة كل النص المخفي من وثيقة PDF

قم بإزالة كل النص من منطقة مستطيلة معينة على الصفحة باستخدام TextFragmentAbsorber الخاص بـ Aspose.PDF.
بدلاً من مسح صفحة بأكملها، تقوم هذه الطريقة بإزالة النص المستهدف، مما يسمح بالتحكم الدقيق في أي جزء من الصفحة يتأثر.

1. قم بتحميل وثيقة PDF.
1. قم بإنشاء ممتص أجزاء النص.
1. حدد المنطقة المستهدفة (المستطيل).
1. قم بإزالة النص من المنطقة المحددة.
1. احتفظ ببقية المستند.
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

## موضوعات نصية ذات صلة

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)
- [ابحث واستخرج نص PDF في بايثون](/pdf/ar/python-net/search-and-get-text-from-pdf/)
- [تنسيق نص PDF في بايثون](/pdf/ar/python-net/text-formatting-inside-pdf/)
