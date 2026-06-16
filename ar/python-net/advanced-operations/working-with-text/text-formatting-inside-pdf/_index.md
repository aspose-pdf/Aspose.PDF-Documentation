---
title: تنسيق نص PDF في بايثون
linktitle: تنسيق النص داخل PDF
type: docs
weight: 70
url: /ar/python-net/text-formatting-inside-pdf/
description: تعرف على كيفية تنسيق النص داخل مستندات PDF في Python باستخدام خيارات المسافات والحدود والمسافات البادئة والتصميم.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تنسيق النص ونمطه داخل ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية تنسيق النص في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعرف على كيفية التحكم في المسافات والمسافات البادئة والحدود والتسطير وتأثيرات الخط وخيارات تصميم النص الأخرى في Python.
---

## تباعد الأسطر والحروف

### استخدام تباعد الأسطر

#### كيفية تنسيق النص باستخدام تباعد الأسطر المخصص في Python - حالة بسيطة

يوفر Aspose.PDF for Python نهجًا مباشرًا للتحكم في تخطيط النص وقابلية القراءة من خلال تعديلات تباعد الأسطر.

يوضح مقتطف الشفرة الخاص بنا كيفية التحكم في تباعد الأسطر في مستند PDF. يقرأ النص من ملف (أو يستخدم رسالة احتياطية)، ويطبق حجم الخط المخصص وتباعد الأسطر، ويضيف النص المنسق إلى صفحة جديدة في PDF.

1. قم بإنشاء مستند PDF جديد.
1. قم بتحميل النص المصدر.
1. قم بتهيئة كائن TextFragment وقم بتعيين النص المحمل له.
1. قم بتعيين خصائص الخط والمسافات للنص. تحدد هذه القيم مدى إحكام أو عدم وضوح خطوط النص:
    - حجم الخط: 12 نقطة
    - تباعد الأسطر: 16 نقطة
1. أدخل جزء النص المنسق في مجموعة فقرات الصفحة.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_simple_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    text_fragment = ap.text.TextFragment(text)
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.line_spacing = 16
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

#### كيفية تنسيق النص باستخدام تباعد الأسطر المخصص في Python - حالة محددة

دعونا نتحقق من كيفية تطبيق أوضاع تباعد الأسطر المختلفة في مستند PDF باستخدام خط TrueType مخصص (TTF).
يقوم بتحميل نص من ملف، ويدمج خطًا معينًا، ويعرض نفس النص مرتين على صفحة PDF - في كل مرة باستخدام وضع تباعد الأسطر المختلف:

- وضع FONT_SIZE: تباعد الأسطر يساوي حجم الخط.
- وضع FULL_SIZE: يمثل تباعد الأسطر الارتفاع الكامل للخط، بما في ذلك الصعود والنزول.

يوضح المثال كيف يمكن أن يختلف سلوك تباعد الأسطر وفقًا للوضع المحدد.

1. قم بإنشاء مستند PDF جديد.
1. حدد المسارات لكل من ملف الخط المخصص وملف مصدر النص.
1. تحميل محتوى نصي.
1. افتح الخط المخصص.
1. قم بإنشاء وتكوين أول جزء من النص (وضع FONT_SIZE). قم بتعيين تباعد الأسطر إلى 'TextFormattingOptions.linespacingMode.font_Size'، مما يعني أن تباعد الأسطر يساوي حجم الخط.
1. قم بإنشاء وتكوين جزء النص الثاني (وضع FULL_SIZE). قم بتعيين line_spacing إلى 'تنسيق النص Options.linespacingMode.full_Size'، والذي يستخدم الارتفاع الكامل للخط.
1. قم بإلحاق كلا الجزأين النصين بنفس صفحة PDF.
1. احفظ المستند النهائي إلى موقع الإخراج المحدد.

```python
import aspose.pdf as ap
import sys
from os import path

def specify_line_spacing_specific_case(outfile):
    document = ap.Document()
    page = document.pages.add()

    font_file = path.join(DATA_DIR, "HPSimplified.ttf")
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        text = "Lorem ipsum text not found."

    with open(font_file, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.TTF)

        fragment1 = ap.text.TextFragment(text)
        fragment1.text_state.font = font
        fragment1.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment1.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FONT_SIZE
        )
        page.paragraphs.add(fragment1)

        fragment2 = ap.text.TextFragment(text)
        fragment2.text_state.font = font
        fragment2.text_state.formatting_options = ap.text.TextFormattingOptions()
        fragment2.text_state.formatting_options.line_spacing = (
            ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE
        )
        page.paragraphs.add(fragment2)

    document.save(outfile)
```

![مستند PDF يعرض نصًا مع تباعد أسطر مخصص يوضح تباعدًا بمقدار 16 نقطة بين الأسطر لتحسين إمكانية القراءة وتنسيق تخطيط النص](line_spacing.png)

### استخدام تباعد الأحرف

#### كيفية التحكم في تباعد الأحرف في نص PDF باستخدام فئة TextFragment

يحدد تباعد الأحرف المسافة بين الأحرف الفردية في سطر النص - وهو مفيد لضبط مظهر النص أو تحقيق تأثيرات مطبعية محددة.

1. يقوم بتهيئة كائن مستند جديد وإضافة صفحة فارغة لوضع النص.
1. تعريف مولد الأجزاء. تنفذ وظيفة مساعدة make_fragment (تباعد):
    - إنشاء TextFragment مع نموذج النص.
    - ضبط الخط.
1. أضف أجزاء نصية بقيم تباعد مختلفة.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_fragment(outfile):
    document = ap.Document()
    page = document.pages.add()

    def make_fragment(spacing):
        fragment = ap.text.TextFragment("Sample Text with character spacing")
        fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
        fragment.text_state.font_size = 14
        fragment.text_state.character_spacing = spacing
        return fragment

    page.paragraphs.add(make_fragment(2.0))
    page.paragraphs.add(make_fragment(1.0))
    page.paragraphs.add(make_fragment(0.75))

    document.save(outfile)
```

![مستند PDF يعرض ثلاثة أسطر من النص المتطابق نموذج نص مع تباعد الأحرف يوضح تباعدًا أكثر إحكامًا بين الأحرف من أعلى إلى أسفل، حيث يحتوي السطر الأول على مسافات أوسع بين الأحرف، والخط الأوسط به تباعد معتدل، والخط السفلي يحتوي على أقرب تباعد بين الأحرف، مما يوضح التأثير المرئي لقيم تباعد الأحرف المختلفة في تنسيق نص PDF](character_spacing_simple.png)

#### كيفية التحكم في تباعد الأحرف في نص PDF باستخدام TextParagrapage و TextBuilder

يسمح Aspose.PDF بتطبيق تباعد الأحرف المخصص عند إضافة نص إلى مستند PDF باستخدام TextParagrapage و TextBuilder.
فهو يحدد منطقة معينة على الصفحة، ويقوم بتكوين التفاف النص، ويعرض جزءًا نصيًا بمسافات معدلة بين الأحرف.

يعد استخدام TextParagrapation مثاليًا عندما تحتاج إلى تحكم دقيق في موضع النص وتخطيطه، مثل عند إنشاء كتل نصية منظمة أو متعددة الأعمدة.

1. قم بإنشاء مستند PDF جديد.
1. قم بتهيئة مثيل TextBuilder للصفحة.
1. قم بإنشاء وتكوين فقرة نصية.
    - اضبط وضع التفاف الكلمات على «خيارات تنسيق النص. WordWrapMode.by_words».
1. قم بإنشاء TextFragment مع تباعد الأحرف المخصص.
    - إنشاء TextFragment جديد وتعيين نصه (على سبيل المثال، «نموذج النص مع تباعد الأحرف»).
    - حدد سمات الخط مثل Arial وحجم الخط 14 نقطة.
    - تطبيق تباعد الأحرف = 2.0، مما يزيد المسافة بين الأحرف.
1. أضف جزء النص إلى فقرة النص.
1. أضف فقرة النص إلى الصفحة.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def character_spacing_using_text_paragraph(outfile):
    document = ap.Document()
    page = document.pages.add()

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(100, 700, 500, 750, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    fragment = ap.text.TextFragment("Sample Text with character spacing")
    fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment.text_state.font_size = 14
    fragment.text_state.character_spacing = 2.0

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)
    document.save(outfile)
```

## إنشاء قوائم

عند التعامل مع ملفات PDF، قد تحتاج إلى عرض معلومات منظمة مثل القوائم - سواء كانت نقطية أو مرقمة أو منسقة باستخدام HTML أو LaTeX.
يوفر Aspose.PDF for Python عبر .NET عدة طرق مرنة لإنشاء وتنسيق القوائم مباشرة داخل مستندات PDF الخاصة بك، مما يمنحك التحكم الكامل في التخطيط والخط والأسلوب.

توضح هذه المقالة طرقًا متعددة لإنشاء قوائم في ملفات PDF، من تنسيق النص العادي إلى عرض HTML و LaTeX المتقدم. تخدم كل طريقة حالة استخدام محددة - سواء كنت تفضل التحكم البرمجي الدقيق أو التصميم المريح القائم على الترميز.

في نهاية هذه المقالة، ستعرف كيفية القيام بما يلي:

- قم بإنشاء قوائم نقطية ومرقمة مخصصة باستخدام TextParagrapage و TextBuilder.

- استخدم أجزاء HTML (HTMLFragment) لعرض قوائم HTML غير المرتبة والمرتبة في ملفات PDF.

- استفد من أجزاء LaTeX (TexFragment) لتنسيق القائمة الرياضية أو العلمية.

- تحكم في التفاف النص وأنماط الخطوط وموضع التخطيط داخل الصفحة.

- افهم الفرق بين إنشاء القائمة اليدوية والنهج القائمة على الترميز.

### إنشاء قائمة مرقمة

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for item in items:
        fragment = ap.text.TextFragment("• " + item)
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### إنشاء قائمة نقطية

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.rectangle = ap.Rectangle(80, 200, 400, 800, True)
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    for i, item in enumerate(items):
        fragment = ap.text.TextFragment(f"{i + 1}. {item}")
        fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
        fragment.text_state.font_size = 12
        paragraph.append_line(fragment)

    builder.append_paragraph(paragraph)
    document.save(outfile)
```

### إنشاء إصدار HTML لقائمة مرقمة

قم بإنشاء قائمة مرقمة (مرتبة) في مستند PDF باستخدام أجزاء HTML. يقوم بتحويل قائمة سلاسل Python إلى عنصر قائمة مرتبة بتنسيق HTML وإدراجه في صفحة PDF كملف HTMLFragment.

يتيح لك استخدام أجزاء HTML دمج ميزات التنسيق المستندة إلى HTML، مثل القوائم المرقمة والخط الغامق والمائل والمزيد، مباشرةً في ملف PDF الخاص بك.

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. قم بإعداد عناصر القائمة.
1. قم بتحويل القائمة إلى قائمة HTML مرتبة.
    - استخدم علامة القائمة المرتبة لقائمة مرقمة.
    - لف كل عنصر كعنصر قائمة باستخدام فهم القائمة.
1. قم بتحويل سلسلة HTML إلى كائن HTMLFragment يمكن إضافته إلى صفحة PDF.
1. أدخل HtmlFragment في مجموعة فقرات الصفحة.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_html_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ol>" + "".join([f"<li>{item}</li>" for item in items]) + "</ol>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![قائمة مرقمة معروضة في وثيقة PDF تعرض أربعة عناصر مرقمة تلقائيًا: 1. العنصر الأول في القائمة، 2. العنصر الثاني مع المزيد من النص لإظهار سلوك التغليف، 3. البند الثالث، و 4. البند الرابع. توضح القائمة عرض القائمة المرتبة بتنسيق HTML داخل بنية PDF مع التسلسل الرقمي المناسب والمسافة البادئة والمسافات بين العناصر](numbered_list_html.png)

### إنشاء إصدار HTML لقائمة نقطية

تعرض مكتبتنا كيفية إنشاء قائمة نقطية (غير مرتبة) في مستند PDF باستخدام أجزاء HTML. يقوم بتحويل قائمة سلاسل Python إلى عنصر قائمة HTML غير مرتبة وإدراجها في صفحة PDF كملف HTMLFragment. يتيح لك استخدام أجزاء HTML الاستفادة من ميزات تنسيق HTML (مثل القوائم والخط الغامق والمائل) مباشرة في PDF.

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. قم بإعداد عناصر القائمة.
1. قم بتحويل القائمة إلى قائمة HTML غير مرتبة.
    - استخدم علامة القائمة غير المرتبة لقائمة غير مرتبة (نقطية).
    - لف كل عنصر كعنصر قائمة باستخدام فهم القائمة.
1. قم بإنشاء جزء HTML. قم بتحويل سلسلة HTML إلى كائن HTMLFragment يمكن إضافته إلى صفحة PDF.
1. أدخل HtmlFragment في مجموعة فقرات الصفحة.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_html_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item in the list",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    html_list = "<ul>" + "".join([f"<li>{item}</li>" for item in items]) + "</ul>"
    html_fragment = ap.HtmlFragment(html_list)
    page.paragraphs.add(html_fragment)
    document.save(outfile)
```

![قائمة نقطية معروضة في وثيقة PDF تعرض أربعة عناصر: العنصر الأول في القائمة، العنصر الثاني مع المزيد من النص لإظهار سلوك التغليف، العنصر الثالث، العنصر الرابع. يسبق كل عنصر نقطة نقطية قياسية ويوضح عرض القائمة بتنسيق HTML داخل بنية PDF مع المسافة البادئة والمسافات المناسبة](bullet_list_html.png)

### قم بإنشاء قائمة نقطية (إصدار LaTeX)

قم بإنشاء قائمة نقطية (غير مرتبة) في PDF باستخدام أجزاء LaTeX (TexFragment). يقوم بتحويل قائمة سلاسل Python إلى بيئة تصنيف LaTeX وإدراجها في صفحة PDF. يعد استخدام أجزاء LaTeX مثاليًا عندما تريد عرض الصيغ الرياضية أو الرموز أو القوائم المنظمة بتنسيق دقيق.

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. حدد قائمة Python للسلاسل التي ستصبح نقاطًا نقطية في بيئة تصنيف LaTeX.
1. قم بتحويل القائمة إلى بيئة تصنيف LaTeX:
    - لف العناصر باستخدام بيئة تصنيف LaTeX.
    - بادئة كل عنصر باستخدام أمر عنصر LaTeX باستخدام فهم القائمة.
1. قم بتحويل سلسلة LaTeX إلى كائن TexFragment يمكن تقديمه في PDF.
1. أضف جزء LaTeX إلى الصفحة.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_bullet_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{itemize}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{itemize}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![من السهل إنشاء قائمة نقطية معروضة في PDF تعرض التنسيق الذي تم عرضه بواسطة Latex مع القوائم النصية: متبوعة بأربعة عناصر نقطية: العنصر الأول، العنصر الثاني مع المزيد من النص لإظهار سلوك الالتفاف، العنصر الثالث، العنصر الرابع. توضح القائمة تنضيد LaTeX الاحترافي مع التنسيق النقطي المناسب والمسافات المتسقة وإمكانيات تغليف النص ضمن تخطيط مستند PDF نظيف](bullet_list_latex.png)

### إنشاء قائمة مرقمة (إصدار LaTeX)

قم بإنشاء قائمة مرقمة (مرتبة) في PDF باستخدام أجزاء LaTeX (TexFragment). يقوم بتحويل قائمة سلاسل Python إلى بيئة تعداد LaTeX وإدراجها في صفحة PDF. يعد استخدام أجزاء LaTeX مثاليًا عندما تريد تنسيقًا دقيقًا أو قوائم منظمة أو تدوينًا رياضيًا في ملفات PDF.

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. حدد قائمة Python للسلاسل التي ستصبح عناصر مرقمة في بيئة تعداد LaTeX.
1. قم بتحويل القائمة إلى بيئة تعداد LaTeX.
1. قم بتحويل سلسلة LaTeX إلى كائن TexFragment يمكن تقديمه في PDF.
1. أضف جزء LaTeX إلى الصفحة.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def create_numbered_list_latex_version(outfile):
    document = ap.Document()
    page = document.pages.add()
    items = [
        "First item",
        "Second item with more text to demonstrate wrapping behavior.",
        "Third item",
        "Fourth item",
    ]
    tex_list = (
        "Lists are easy to create: \\begin{enumerate}"
        + "".join([f"\\item {i}" for i in items])
        + "\\end{enumerate}"
    )
    tex_fragment = ap.TeXFragment(tex_list)
    page.paragraphs.add(tex_fragment)
    document.save(outfile)
```

![قائمة مرقمة معروضة في PDF تعرض التنسيق المعروض من اللاتكس مع العناصر 1. البند الأول، 2. العنصر الثاني مع المزيد من النص لإظهار سلوك التغليف، 3. البند الثالث، و 4. العنصر الرابع، الذي يسبقه النص، من السهل إنشاء القوائم](numbered_list_latex.png)

## الحواشي السفلية والتعليقات الختامية

### إضافة حواشي سفلية

تُستخدم الحواشي السفلية للإشارة إلى الملاحظات داخل نص المستند عن طريق وضع أرقام مرتفعة متتالية بجوار النص ذي الصلة. تتوافق هذه الأرقام مع الملاحظات التفصيلية التي عادةً ما يتم وضع مسافة بادئة لها ووضعها في أسفل نفس الصفحة، مما يوفر سياقًا إضافيًا أو اقتباسات أو تعليقًا.

أضف حاشية سفلية إلى جزء نصي في مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET. تعتبر الحواشي السفلية مفيدة لتوفير معلومات تكميلية أو اقتباسات أو توضيحات دون تشويش المحتوى الرئيسي. تضمن هذه الطريقة دمج الحواشي السفلية بصريًا وهيكليًا في تخطيط PDF.

1. قم بإنشاء مستند جديد.
1. قم بإنشاء TextFragment بالمحتوى الرئيسي.
1. إضافة نص مضمن. قم بإنشاء TextFragment آخر يستمر في نفس الفقرة.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    inline_text = ap.text.TextFragment(
        " This is another text after footnote in the same paragraph."
    )
    inline_text.is_in_line_paragraph = True
    inline_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    inline_text.text_state.font_size = 14
    page.paragraphs.add(inline_text)

    document.save(outfile)
```

### إضافة حاشية سفلية مع تصميم مخصص في PDF

1. قم بتهيئة مستند PDF جديد وإضافة صفحة فارغة.
1. إنشاء جزء النص الرئيسي.
1. قم بإنشاء وتصميم الحاشية السفلية (الخط والحجم واللون والنمط).
1. أدخل جزء النص المصمم مع حاشية سفلية في الصفحة.
1. أضف جزءًا نصيًا آخر بدون حاشية سفلية.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text_style(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text_state = ap.text.TextState()
    note.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    note.text_state.font_size = 10
    note.text_state.foreground_color = ap.Color.red
    note.text_state.font_style = ap.text.FontStyles.ITALIC
    text_fragment.foot_note = note

    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    document.save(outfile)
```

### إضافة حواشي سفلية برموز مخصصة في PDF

أضف الحواشي السفلية إلى أجزاء النص في مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET، مع إمكانية تخصيص رمز علامة الحاشية السفلية.

1. قم بإنشاء مستند PDF وصفحة.
1. أضف أول جزء نصي برمز حاشية سفلية مخصص.
1. أضف جزءًا نصيًا آخر يتابع الفقرة بدون حاشية سفلية.
1. أضف جزءًا نصيًا ثانيًا مع حاشية سفلية افتراضية.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14

    note = ap.Note("This is the footnote content with custom text style.")
    note.text = "*"
    text_fragment.foot_note = note
    page.paragraphs.add(text_fragment)

    another_text = ap.text.TextFragment(" This is another text without footnote.")
    another_text.text_state.font = ap.text.FontRepository.find_font("Arial")
    another_text.text_state.font_size = 14
    page.paragraphs.add(another_text)

    text_fragment = ap.text.TextFragment("This is a sample text with a footnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.foot_note = ap.Note("This is the footnote content.")
    page.paragraphs.add(text_fragment)

    document.save(outfile)
```

### إضافة حواشي سفلية بنمط خط مخصص في PDF

قم بتخصيص المظهر المرئي لخطوط الحاشية السفلية في مستند PDF باستخدام مكتبة Python. يؤدي تخصيص خطوط الحاشية السفلية إلى تحسين الوضوح البصري ويسمح بالاتساق الأسلوبي في المستندات مثل التقارير والأوراق الأكاديمية والمنشورات المشروحة.

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. حدد نمط خط مخصص لموصلات الحواشي السفلية (اللون والعرض ونمط لوحة القيادة).
1. أضف أجزاء نصية متعددة مع الحواشي السفلية.
1. احفظ المستند النهائي.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_custom_line_style(outfile):
    document = ap.Document()
    page = document.pages.add()

    # Define custom line style
    graph_info = ap.GraphInfo()
    graph_info.line_width = 2
    graph_info.color = ap.Color.red
    graph_info.dash_array = [3]
    graph_info.dash_phase = 1
    page.note_line_style = graph_info

    # First text fragment with footnote
    text1 = ap.text.TextFragment("This is a sample text with a footnote.")
    text1.foot_note = ap.Note("foot note for text 1")
    page.paragraphs.add(text1)

    # Second text fragment with footnote
    text2 = ap.text.TextFragment("This is yet another sample text with a footnote.")
    text2.foot_note = ap.Note("foot note for text 2")
    page.paragraphs.add(text2)

    document.save(outfile)
```

### إضافة حواشي سفلية مع صورة وجدول في PDF

كيفية إثراء الحواشي السفلية في مستند PDF عن طريق تضمين الصور والنصوص المصممة والجداول باستخدام Aspose.PDF لـ Python عبر .NET؟

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. أضف جزءًا نصيًا مع حاشية سفلية مرفقة.
1. قم بتضمين صورة ونص نمطي وجدول داخل الحاشية السفلية.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def add_footnote_with_image_and_table(outfile):
    document = ap.Document()
    page = document.pages.add()

    text = ap.text.TextFragment("This is a sample text with a footnote.")
    page.paragraphs.add(text)

    note = ap.Note()

    # Add image
    image_note = ap.Image()
    image_note.file = path.join(DATA_DIR, "logo.jpg")
    image_note.fix_height = 20
    image_note.fix_width = 20
    note.paragraphs.add(image_note)

    # Add text
    text_note = ap.text.TextFragment("This is the footnote content.")
    text_note.text_state.font_size = 20
    text_note.is_in_line_paragraph = True
    note.paragraphs.add(text_note)

    # Add table
    table = ap.Table()
    table.rows.add().cells.add("Cell 1,1")
    table.rows.add().cells.add("Cell 1,2")
    note.paragraphs.add(table)

    text.foot_note = note

    document.save(outfile)
```

### إضافة تعليقات ختامية إلى مستندات PDF

التعليق الختامي هو نوع من الاقتباسات التي توجه القراء إلى قسم معين في نهاية المستند، حيث يمكنهم العثور على المرجع الكامل للاقتباس أو الفكرة المعاد صياغتها أو المحتوى الملخص. عند استخدام التعليقات الختامية، يتم وضع رقم مرتفع مباشرة بعد المادة المشار إليها، لتوجيه القارئ إلى الملاحظة المقابلة في نهاية الورقة.

يوضح مقتطف الشفرة هذا كيفية إضافة تعليق ختامي إلى جزء نصي في مستند PDF. على عكس الحواشي السفلية، التي تظهر بالقرب من النص المشار إليه، يتم وضع التعليقات الختامية عادةً في نهاية المستند أو المقطع. تحاكي هذه الطريقة أيضًا مستندًا أطول لتوضيح كيفية تصرف التعليقات الختامية في المحتوى الموسع.

1. قم بإنشاء مستند PDF وصفحة.
1. إضافة جزء نصي مع تعليق ختامي.
1. تحميل محتوى نص خارجي.
1. محاكاة المستند الطويل. أضف النص الذي تم تحميله عدة مرات لمحاكاة مستند أطول.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

### إضافة تعليقات ختامية مع نص علامة مخصص في PDF

قم بإضافة تعليق ختامي إلى جزء نصي في وثيقة PDF، مع رمز علامة مخصص. عادةً ما يتم وضع التعليقات الختامية في نهاية المستند أو القسم وتكون مفيدة لتوفير سياق إضافي أو اقتباسات أو تعليق.

1. قم بإنشاء مستند PDF وصفحة.
1. أضف جزءًا نصيًا أنيقًا مع تعليق ختامي.
1. قم بتخصيص نص علامة التعليق الختامي.
1. قم بتحميل محتوى خارجي من ملف .txt.
1. قم بمحاكاة المحتوى الطويل لتوضيح موضع التعليق الختامي.
1. احفظ مستند PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def add_endnote_custom_text(outfile):
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("This is a sample text with an endnote.")
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.end_note = ap.Note("This is the EndNote content.")
    text_fragment.end_note.text = "***"
    page.paragraphs.add(text_fragment)

    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, encoding="utf-8") as f:
            text_content = f.read()
    else:
        text_content = "Lorem ipsum sample text not found."

    # Simulate long text
    for _ in range(5):
        tf = ap.text.TextFragment(text_content)
        tf.text_state.font = ap.text.FontRepository.find_font("Arial")
        tf.text_state.font_size = 14
        page.paragraphs.add(tf)

    document.save(outfile)
```

## التخطيط والتحكم في الصفحة

### إجبار الجدول على البدء في صفحة جديدة في PDF

أضف محتوى محددًا للبدء في صفحة جديدة في مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET.
من خلال تعيين الخاصية 'is_in_new_page'، يمكنك التحكم بدقة في تخطيط الصفحة وهيكلها، مما يضمن أن أقسام معينة (مثل الجداول أو التقارير أو الملخصات) تبدأ دائمًا في صفحة جديدة - وهي مثالية لتنسيق المستندات أو التقارير الجاهزة للطباعة أو إنشاء مخرجات منظمة.

1. قم بإنشاء جدول وتكوينه.
1. أضف بيانات إلى الجدول.
1. قم بفرض صفحة جديدة للجدول. وهذا يضمن بدء الجدول في أعلى الصفحة الجديدة، حتى إذا كان هناك محتوى موجود في الصفحة الحالية.
1. أضف الجدول إلى الصفحة. استخدم «page.paragrahs.add ()» لتضمين الجدول في تخطيط PDF.
1. احفظ المستند.

```python
import aspose.pdf as ap
import sys
from os import path

def force_new_page(output_file_name):
    # Create new PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create a table
    table = ap.Table()
    table.column_widths = "150 150 150"
    table.default_cell_border = ap.BorderInfo(ap.BorderSide.ALL)

    # Add rows with sample data
    for i in range(5):
        row = table.rows.add()
        row.cells.add(f"Row {i + 1} - Col 1")
        row.cells.add(f"Row {i + 1} - Col 2")
        row.cells.add(f"Row {i + 1} - Col 3")

    # --- Key part: force table to start on a new PDF page ---
    table.is_in_new_page = True

    # Add table to page
    page.paragraphs.add(table)

    # Save the PDF
    document.save(output_file_name)
```

### استخدام خاصية الفقرة المضمنة في PDF

تتيح لك مكتبتنا استخدام خاصية «is_in_line_paragrah» للتحكم في التدفق المضمن بين النص والصور داخل PDF.
عادةً، عند إضافة عناصر جديدة (مثل أجزاء النص أو الصور)، يبدأ كل عنصر بسطر جديد أو فقرة جديدة.
من خلال إعداد «is_in_line_paragraph = True»، يمكنك جعل العناصر تظهر على نفس السطر أو داخل نفس الفقرة، وإنشاء تخطيطات مضمنة سلسة - مثالية لدمج النص والصور المضمنة، مثل إضافة الشعارات أو الرموز أو الرموز داخل الجمل.

يظهر جزء النص الأول والصورة وجزء النص الثاني على نفس السطر، مما يشكل فقرة مضمنة مستمرة.
يبدأ جزء النص الثالث فقرة جديدة، مما يوضح السلوك الافتراضي لكسر الأسطر.

1. قم بإنشاء مستند PDF جديد.
1. أضف الجزء النصي الأول.
1. قم بإدراج صورة مضمنة.
1. أضف المزيد من النص المضمن.
1. أضف فقرة جديدة.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def using_inline_paragraph_property(output_file_name):
    # Create a PDF document
    document = ap.Document()
    page = document.pages.add()

    # --- First text fragment (normal paragraph) ---
    fragment1 = ap.text.TextFragment("This is the first part of the paragraph. ")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment1.text_state.font_size = 14
    page.paragraphs.add(fragment1)

    # --- Inline image (continues same paragraph flow) ---
    image = ap.Image()
    image.is_in_line_paragraph = True  # Makes image inline with previous paragraph
    image.file = path.join(DATA_DIR, "logo.jpg")
    image.fix_height = 30
    image.fix_width = 30
    page.paragraphs.add(image)

    # --- Second inline text fragment (keeps same paragraph flow) ---
    fragment2 = ap.text.TextFragment("This is the second part of the same paragraph.")
    fragment2.is_in_line_paragraph = True
    fragment2.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment2.text_state.font_size = 14
    page.paragraphs.add(fragment2)

    # --- Third fragment (starts new paragraph automatically) ---
    fragment3 = ap.text.TextFragment("This is a new paragraph.")
    fragment3.text_state.font = ap.text.FontRepository.find_font("Arial")
    fragment3.text_state.font_size = 14
    page.paragraphs.add(fragment3)

    # Save PDF
    document.save(output_file_name)
```

### قم بإنشاء ملف PDF متعدد الأعمدة

قم بإنشاء تخطيط بنمط صحيفة متعدد الأعمدة في ملف PDF باستخدام Aspose.PDF لـ Python عبر .NET.
ويعرض كيفية الجمع بين النص وتنسيق HTML والرسومات داخل FloatingBox، مما يتيح التحكم المتقدم في التخطيط على غرار المجلات متعددة الأعمدة أو تصميمات الرسائل الإخبارية.

1. قم بتهيئة مستند PDF.
1. أضف خط فاصل أفقي في الأعلى.
1. أضف عنوان HTML ذو نمط.
1. قم بإنشاء FloatingBox للتحكم في التخطيط.
1. قم بتكوين تخطيط متعدد الأعمدة.
1. إضافة معلومات المؤلف.
1. ارسم خطًا أفقيًا داخليًا آخر.
1. أضف نص المقالة.
1. احفظ ملف PDF النهائي.

```python
import aspose.pdf as ap
import sys
from os import path

def create_multi_column_pdf(output_file_name):
    # Create PDF document
    document = ap.Document()

    # Set margins
    document.page_info.margin.left = 40
    document.page_info.margin.right = 40

    page = document.pages.add()

    #
    # Draw horizontal line at the top
    #
    graph1 = ap.drawing.Graph(500.0, 2.0)
    page.paragraphs.add(graph1)

    pos_arr = [1.0, 2.0, 500.0, 2.0]
    line1 = ap.drawing.Line(pos_arr)
    graph1.shapes.add(line1)

    #
    # Add HTML heading text
    #
    html = "<span style=\"font-family: 'Times New Roman'; font-size: 18px;\"><strong>How to Steer Clear of money scams</strong></span>"
    heading_text = ap.HtmlFragment(html)
    page.paragraphs.add(heading_text)

    #
    # Floating box: enables multi-column layout
    #
    box = ap.FloatingBox()

    box.column_info.column_count = 2  # Two columns
    box.column_info.column_spacing = "5"  # Space between columns
    box.column_info.column_widths = "105 105"  # Width of each column

    #
    # Add title text to the FloatingBox
    #
    text1 = ap.text.TextFragment("By A Googler (The Official Google Blog)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)

    text1.text_state.font_size = 10
    text1.text_state.font_style = ap.text.FontStyles.ITALIC

    #
    # Add another horizontal line inside the box
    #
    graph2 = ap.drawing.Graph(50.0, 10.0)

    pos_arr2 = [1.0, 10.0, 100.0, 10.0]
    line2 = ap.drawing.Line(pos_arr2)
    graph2.shapes.add(line2)

    box.paragraphs.add(graph2)

    #
    # Add long text content
    #
    lorem_path = path.join(DATA_DIR, "lorem.txt")
    if path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as f:
            lorem_text = f.read()
    else:
        lorem_text = "Lorem ipsum text not found."
    text2 = ap.text.TextFragment(lorem_text * 5)
    box.paragraphs.add(text2)

    page.paragraphs.add(box)

    # Save PDF
    document.save(output_file_name)
```

### توقفات علامة التبويب المخصصة لمحاذاة النص في PDF

قم بإنشاء تخطيط نصي يشبه الجدول في PDF باستخدام نقاط توقف مخصصة - دون الاعتماد على هياكل الجدول.
من خلال تحديد مواضع توقف علامات التبويب والمحاذاة وأنماط القائد، يمكنك محاذاة النص بدقة عبر الأعمدة. وهذا مفيد للفواتير أو التقارير أو البيانات النصية المهيكلة.

1. قم بإنشاء مستند PDF جديد.
1. حدد توقفات علامات التبويب المخصصة.
1. استخدم العناصر النائبة لعلامات التبويب في النص.
1. أضف نصًا إلى PDF.
1. احفظ ملف PDF.

```python
import aspose.pdf as ap
import sys
from os import path

def custom_tab_stops(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Define tab stops
    tab_stops = ap.text.TabStops()

    tab_stop1 = tab_stops.add(100)
    tab_stop1.alignment_type = ap.text.TabAlignmentType.RIGHT
    tab_stop1.leader_type = ap.text.TabLeaderType.SOLID

    tab_stop2 = tab_stops.add(200)
    tab_stop2.alignment_type = ap.text.TabAlignmentType.CENTER
    tab_stop2.leader_type = ap.text.TabLeaderType.DASH

    tab_stop3 = tab_stops.add(300)
    tab_stop3.alignment_type = ap.text.TabAlignmentType.LEFT
    tab_stop3.leader_type = ap.text.TabLeaderType.DOT

    # Create TextFragments with tab placeholders
    header = ap.text.TextFragment(
        "This is an example of forming table with TAB stops", tab_stops
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", tab_stops)
    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", tab_stops)

    text2 = ap.text.TextFragment("#$TABdata21 ", tab_stops)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    # Add text fragments to page
    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    # Save PDF document
    document.save(output_file_name)
```

### موضوعات نصية ذات صلة

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)
- [قم بتدوير النص داخل PDF باستخدام Python](/pdf/ar/python-net/rotate-text-inside-pdf/)
- [استبدال النص في PDF عبر Python](/pdf/ar/python-net/replace-text-in-pdf/)