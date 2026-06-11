---
title: إضافة نص إلى PDF في بايثون
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: /ar/python-net/add-text-to-pdf-file/
description: تعرف على كيفية إضافة نص وأجزاء HTML والقوائم والروابط والخطوط المخصصة إلى مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف النص والروابط وHTML والخطوط إلى ملفات PDF باستخدام Python
Abstract: تشرح هذه المقالة كيفية إضافة نص وتنسيقه في مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي التقنيات الأساسية مثل تحديد موضع النص، وتطبيق إعدادات الخط والنمط، وإدراج الروابط والقوائم، واستخدام HTML و LaTeX والخطوط المخصصة في عمليات سير عمل Python.
---

يشرح هذا الدليل كيفية إضافة محتوى نصي إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ستتعلم تقنيات إدراج النص الأساسية - من وضع جزء نصي بسيط في موضع معين، إلى تصميمه (الخط والحجم واللون والنمط)، والتعامل مع اللغات من اليمين إلى اليسار (RTL)، وتضمين الارتباطات التشعبية، والعمل مع تخطيطات الفقرات والقوائم وتأثيرات الشفافية. تتناول المقالة أيضًا سيناريوهات متقدمة مثل استخدام أجزاء HTML أو LaTeX والخطوط المخصصة وخيارات تنسيق النص مثل تباعد الأسطر وتباعد الأحرف.

سواء كنت تنشئ تعليقات توضيحية بسيطة أو تخطيطات مطبعية غنية، فإن هذا المورد يزودك باللبنات الأساسية للعمل مع النص في ملفات PDF باستخدام Aspose.PDF.

## إدراج نص أساسي

يوفر Aspose.PDF لـ Python عبر .NET واجهة برمجة تطبيقات قوية ومرنة للتعامل مع النص داخل ملفات PDF.
سواء كنت بحاجة إلى تسميات ثابتة بسيطة أو محتوى منسق بشكل غني أو نص متعدد اللغات أو ارتباطات تشعبية تفاعلية، فإن مجموعة الأدوات تتيح لك القيام بكل ذلك باستخدام كود Python المختصر.

### إضافة حالة نصية بسيطة

يوضح Aspose.PDF لـ Python عبر .NET كيفية إضافة جزء نصي بسيط إلى موضع معين على الصفحة. سوف تتعلم كيفية إنشاء مستند PDF جديد وإضافة صفحة وإدراج نص في إحداثيات معينة وحفظ الملف الناتج.

1. قم بإنشاء ملف جديد [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) كائن.
1. استخدم `document.pages.add()` لإنشاء فراغ جديد [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/).
1. قم بإنشاء [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) مع محتوى النص.
1. قم بتعيين موضع النص باستخدام [`Position`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/position/) فئة. إذا قمت بتحديد `Position`، سيتم وضع النص في المستند الخاص بك من اليسار إلى اليمين وسيتم نقله إلى الأسفل.
1. تخصيص مظهر النص. يمكنك تعيين حجم الخط واللون ونمط الخط والمزيد عبر [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/).
1. قم بإلحاق `TextFragment` إلى مجموعة فقرات الصفحة مع `page.paragraphs.add(text_fragment)`.
1. احفظ المستند.

يوضح مقتطف الشفرة التالي كيفية إضافة نص في ملف PDF موجود:

```python
import math
import sys
import os
import aspose.pdf as ap

# region Basic text insertion
def add_text_simple_case(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

يستخدم مثال التعليمات البرمجية هذا TextFragment. يمكنك أيضًا إضافة نص إلى صفحة PDF باستخدام TextParagraph.
ذا **[جزء من النص](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)** عبارة عن جزء واحد من النص. وهي تمثل سلسلة نصية واحدة يمكن وضعها وتصميمها ووضعها بشكل مستقل. إنه مثالي عندما تحتاج إلى إضافة محتوى نصي صغير وبسيط.

ذا **[فقرة نصية](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/)** عبارة عن مجموعة من أجزاء النص. يمكنه إضافة أسطر نصية متعددة. TextParagrapa عبارة عن حاوية أو مجموعة من كائن واحد أو أكثر من كائنات TextFragment. إنه مثالي عندما تحتاج إلى تجميع أجزاء متعددة - على سبيل المثال، لإنشاء كتلة نصية تحتوي على عدة أسطر أو كلمات أو عناصر منسقة.
تدير TextParagrapage أيضًا محاذاة النص وتباعد الأسطر والتخطيط التلقائي على الصفحة. استخدام الخط الأحمر ممكن فقط مع TextParagrapage.

لمزيد من المعلومات حول التعامل مع النص، راجع [تنسيق النص داخل PDF](/pdf/ar/python-net/text-formatting-inside-pdf/) و [ابحث واحصل على نص من PDF](/pdf/ar/python-net/search-and-get-text-from-pdf/).

### إضافة نص باستخدام فقرة نصية

يمكن لـ Aspose.PDF لبيثون عبر .NET إضافة فقرة من النص باستخدام [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) و [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) مع خيارات التغليف.

1. قم بإنشاء ملف جديد [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) وفارغة [صفحة](https://reference.aspose.com/pdf/python-net/aspose.pdf/page/) باستخدام `document.pages.add()`.
1. اقرأ نصًا من ملف أو استخدم النص الافتراضي.
1. قم بإنشاء [`TextBuilder`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textbuilder/) لإضافة محتوى على مستوى الفقرة مع التحكم في التخطيط والتفاف.
1. قم بإنشاء [`TextParagraph`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/) وقم بتعيين وضع الالتفاف (يستخدم المثال `DISCRETIONARY_HYPHENATION`).
1. قم بإنشاء [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/)وتطبيق الأنماط وإلحاق الجزء بالفقرة.
1. قم بإلحاق الفقرة بالصفحة باستخدام `TextBuilder`.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraph(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    builder = ap.text.TextBuilder(page)
    paragraph = ap.text.TextParagraph()
    paragraph.first_line_indent = 20
    paragraph.rectangle = ap.Rectangle(80, 800, 400, 200, True)
    # paragraph.formatting_options.wrap_mode = TextFormattingOptions.WordWrapMode.BY_WORDS
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.DISCRETIONARY_HYPHENATION
    )

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    paragraph.append_line(fragment)
    builder.append_paragraph(paragraph)

    document.save(output_file_name)
```

![إضافة نص باستخدام فقرة نصية](text_paragraph.png)

### إضافة فقرات مع المسافات البادئة في PDF

يوضح مقتطف الشفرة التالي كيفية إنشاء مستند PDF جديد وإضافة فقرتين من النص بأنماط المسافة البادئة المختلفة:

- توضح الفقرة الأولى المسافة البادئة للسطر الأول (يتم تحديد المسافة البادئة للسطر الأول فقط).

- توضح الفقرة الثانية المسافة البادئة للأسطر اللاحقة (يتم وضع مسافة بادئة لجميع الأسطر بعد الأولى).

يستخدم فئات «TextParagraph» و «TextBuilder» و «TextFragment» من Aspose.PDF للتحكم بدقة في التخطيط والتنسيق.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_paragraphs_indents(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    lorem_path = LOREM_PATH
    if os.path.exists(lorem_path):
        with open(lorem_path, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = "Lorem ipsum sample text not found."

    fragment = ap.text.TextFragment(text)
    fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment.text_state.font_size = 12

    builder = ap.text.TextBuilder(page)
    paragraph1 = ap.text.TextParagraph()
    paragraph1.first_line_indent = 20
    paragraph1.rectangle = ap.Rectangle(80, 800, 300, 50, True)
    paragraph1.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph1.append_line(fragment)
    builder.append_paragraph(paragraph1)

    paragraph2 = ap.text.TextParagraph()
    paragraph2.subsequent_lines_indent = 20
    paragraph2.rectangle = ap.Rectangle(320, 800, 500, 50, True)
    paragraph2.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )

    paragraph2.append_line(fragment)
    builder.append_paragraph(paragraph2)
    document.save(output_file_name)
```

### أضف سطرًا جديدًا من النص في PDF

Aspose.PDF لبيثون عبر .NET يسمح لك بإدراج نص متعدد الأسطر في مستند PDF باستخدام فئات TextFragment و TextParagrapage و TextBuilder.

1. قم بإنشاء مستند جديد.
1. قم بتعريف جزء نصي يحتوي على حرف سطر جديد.
1. تعيين نمط النص.
1. أضف الجزء إلى فقرة.
1. ضع الفقرة.
1. اعرض الفقرة على الصفحة.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_new_line(output_file):
    """Add a new line of text to a PDF document."""
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Initialize new TextFragment with text containing required newline markers
    text_fragment = ap.text.TextFragment("Applicant Name: " + os.linesep + " Joe Smoe")

    # Set text fragment properties if necessary
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # Create TextParagraph object
    par = ap.text.TextParagraph()

    # Add new TextFragment to paragraph
    par.append_line(text_fragment)

    # Set paragraph position
    par.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)

    # Add the TextParagraph using TextBuilder
    text_builder.append_paragraph(par)

    # Save PDF document
    document.save(output_file)
```

### تحديد فواصل الأسطر وتسجيل الإشعارات في PDF

يوضح كيفية إنشاء مستند PDF يحتوي على أجزاء نصية متعددة وتمكين تسجيل إشعارات Aspose.PDF لمراقبة أحداث التخطيط - مثل فواصل الأسطر ولف النص - أثناء العرض.

1. قم بإنشاء مستند PDF جديد.
1. قم بتمكين تسجيل الإشعارات.
1. استخدم document.pages.add () لإنشاء الصفحة الأولى.
1. أضف أجزاء نصية متعددة.
1. استخدم page.paragrahs.add (نص) لعرض كل جزء من النص.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def determine_line_break(output_file):
    """Create a PDF document with multiple text fragments and log notifications."""
    # Create PDF document
    document = ap.Document()

    # Enable notification logging
    document.enable_notification_logging = True

    page = document.pages.add()

    for i in range(4):
        text = ap.text.TextFragment(
            "Lorem ipsum \r\ndolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in "
            "reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla "
            "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in "
            "culpa qui officia deserunt mollit anim id est laborum."
        )
        text.text_state.font_size = 20
        page.paragraphs.add(text)

    # Save PDF document
    document.save(output_file)

    notifications = document.pages[1].get_notifications()
    print(notifications)
```

### قم بقياس عرض النص ديناميكيًا في PDF

قم بقياس عرض الأحرف والسلاسل بشكل ديناميكي في خط معين باستخدام Aspose.PDF لـ Python عبر .NET. يستخدم أسلوبي 'font.measure_string () 'و 'textState.Measure_String ()' للتحقق من أن عروض السلسلة المقاسة متسقة ودقيقة.

1. استخدم 'fontrepository.find_Font () 'لاسترداد كائن الخط Arial من المستودع.
1. قم بإنشاء كائن TextState لإدارة خصائص الخط.
1. قم بقياس الأحرف الفردية.
1. قارن نتائج كلتا الطريقتين لجميع الأحرف بين «A» و «z».
1. تأكد من أن كلا نهجي القياس يؤديان إلى نفس النتائج.

```python
import math
import sys
import os
import aspose.pdf as ap

def get_text_width_dynamically(output_file):
    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if math.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("Unexpected font string measure!")

    if math.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("Unexpected font string measure!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        if math.fabs(fn_measure - ts_measure) > 0.001:
            print("Font and state string measuring doesn't match!")

        c_code += 1
```

### إضافة نص مع الارتباطات التشعبية

أضف ارتباطات تشعبية قابلة للنقر إلى نص في ملف PDF باستخدام Aspose.PDF لـ Python عبر .NET. توضح مكتبتنا كيفية إضافة مقاطع نصية متعددة داخل TextFragment واحد وتطبيق ارتباط تشعبي على مقطع معين، وتصميم مقاطع النص بشكل فردي (على سبيل المثال، اللون والخط المائل).

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. قم بإنشاء جزء نصي.
1. أضف كائنات TextSegment متعددة. يمكن أن يكون لكل مقطع محتواه وتصميمه الخاص. على سبيل المثال نص عادي أو نص ارتباط تشعبي.
1. قم بتطبيق ارتباط تشعبي على مقطع. قم بإنشاء كائن WebHyperlink باستخدام عنوان URL المطلوب.
1. صمم المقطع. قم بتخصيص اللون ونمط الخط والحجم وما إلى ذلك باستخدام text_state.
1. أضف الجزء إلى الصفحة باستخدام «page.paragrahs.add ()».
1. احفظ ملف PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_hyperlink(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Sample Text Fragment")

    segment = ap.text.TextSegment(" ... Text Segment 1...")
    fragment.segments.append(segment)

    segment = ap.text.TextSegment("Link to Aspose")
    fragment.segments.append(segment)
    segment.hyperlink = ap.WebHyperlink("https://products.aspose.com/pdf")
    segment.text_state.foreground_color = ap.Color.blue
    segment.text_state.font_style = ap.text.FontStyles.ITALIC

    segment = ap.text.TextSegment("TextSegment without hyperlink")
    fragment.segments.append(segment)

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![جزء نصي معروض في ملف PDF يعرض محتوى مختلطًا مع نموذج لجزء النص متبوعًا بمقطع النص 1، ثم نص أزرق مرتبط تشعبيًا يقرأ «رابط إلى Aspose» (رابط إلى Aspose) (يرتبط بـ https://products.aspose.com/pdf)، وتنتهي بـ TextSegment بدون ارتباط تشعبي بتنسيق نص أسود عادي](hyperlink_text.png)

### إضافة نص من اليمين إلى اليسار (RTL) إلى مستند PDF

RTL (من اليمين إلى اليسار) هي خاصية تشير إلى اتجاه كتابة النص، حيث يتم كتابة النص من اليمين إلى اليسار.
Aspose.PDF لـ Python عبر .NET. يوضح كيفية إضافة نص من اليمين إلى اليسار (RTL)، مثل العربية أو العبرية، إلى مستند PDF.

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. قم بإنشاء جزء نصي بمحتوى RTL. أدخل النص العربي أو العبري أو أي نص بلغة RTL كمحتوى مجزأ.
تعيين الخط والتصميم. اختر الخط الذي يدعم البرنامج النصي RTL (على سبيل المثال، تاهوما، Arial Unicode MS). قم بتعيين حجم الخط ولون المقدمة حسب الحاجة.
1. قم بتعيين المحاذاة الأفقية إلى اليمين باستخدام «text_fragment.horizontal_alignment».
1. أضف جزء النص إلى الصفحة.
1. احفظ مستند PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_rtl_text(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    # Styled text fragment
    text_fragment = ap.text.TextFragment(
        "يعتبر خوجا نصر الدين شخصية فولكلورية من الشرق الإسلامي وبعض شعوب البحر الأبيض المتوسط ​​والبلقان، وهو بطل القصص والحكايات القصيرة الفكاهية والساخرة، وأحيانًا الحكايات اليومية."
    )
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Tahoma")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.RIGHT

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![نص من اليمين إلى اليسار](rtl_text.png)

## تصميم النص

### إضافة نص باستخدام نمط الخط

هذا مثال أكثر تقدمًا يوضح نمط النص وتخصيص الخط والنص ذي التنسيق المختلط (باستخدام مقاطع نصية فرعية). يشرح Aspose.PDF كيفية تطبيق خصائص الخط مثل عائلة الخط والحجم واللون والخط الغامق والمائل والتسطير على جزء من النص.
بالإضافة إلى ذلك، يوضح مقتطف الشفرة هذا كيفية استخدام مقاطع نصية متعددة داخل جزء واحد لإنشاء تعبيرات نصية معقدة - على سبيل المثال، بما في ذلك الأحرف المنخفضة أو المرتفعة، والتي غالبًا ما تكون مطلوبة في الصيغ أو الرموز العلمية.

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. قم بإنشاء TextFragment للنص البسيط.
1. تعريف محتوى النص.
1. حدد الموضع باستخدام إحداثيات الموضع (x، y).
1. قم بتطبيق التصميم عبر «خاصية text_state» - الخط، حجم الخط، لون المقدمة، نمط الخط، التسطير.
1. قم بإنشاء تعبير معقد باستخدام كائنات TextSegment متعددة. يمثل كل TextSegment جزءًا من النص يمكن أن يكون له أسلوبه الخاص. يتيح لك ذلك إنشاء تعبيرات، مثل الصيغ الرياضية أو الكيميائية.
1. حدد كائنات TextState متعددة. واحد للنص الرئيسي (text_state_letters). آخر للنص الفرعي أو المرتفع (text_state_index).
1. ادمج مقاطع النص. قم بإلحاق كل مقطع بـ «TextFragment» باستخدام 'segments.append () '.
1. أضف كلا الكائنين النصين إلى الصفحة. استخدم «page.paragrahs.add ()» لوضعها في المستند.
1. احفظ المستند النهائي.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_with_font_styling(output_file_name):
    document = ap.Document()
    page = document.pages.add()

    # Initialize an empty TextFragment to build a formula using segments
    formula = ap.text.TextFragment()
    text_fragment = ap.text.TextFragment("Hello, Aspose!")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    text_fragment.text_state.font_size = 14
    text_fragment.text_state.foreground_color = ap.Color.blue
    text_fragment.text_state.font_style = (
        ap.text.FontStyles.BOLD | ap.text.FontStyles.ITALIC
    )
    text_fragment.text_state.underline = True
    text_fragment.horizontal_alignment = ap.HorizontalAlignment.LEFT

    text_state_letters = ap.text.TextState()
    text_state_letters.font = ap.text.FontRepository.find_font("Arial")
    text_state_letters.font_size = 14
    text_state_letters.foreground_color = ap.Color.blue
    text_state_letters.font_style = ap.text.FontStyles.BOLD

    text_state_index = ap.text.TextState()
    text_state_index.font = ap.text.FontRepository.find_font("Arial")
    text_state_index.font_size = 14
    text_state_index.foreground_color = ap.Color.dark_red
    # text_state_index.superscript = True
    text_state_index.subscript = True

    position = ap.text.Position(100, 500)

    # Helper function to add segments
    def add_segment(text, state):
        seg = ap.text.TextSegment(text)
        seg.text_state = state
        seg.position = position
        formula.segments.append(seg)

    add_segment("S = a", text_state_letters)
    add_segment("2n", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+1", text_state_index)
    add_segment(" + a", text_state_letters)
    add_segment("2n+2", text_state_index)
    formula.horizontal_alignment = ap.HorizontalAlignment.LEFT

    page.paragraphs.add(text_fragment)
    page.paragraphs.add(formula)
    document.save(output_file_name)
```

![جزء نصي معروض بخط Arial مائل باللون الأزرق يحتوي على النص Hello, Aspose! متبوعة بصيغة رياضية تُظهر S = الرمز الفرعي 2n + الرمز الفرعي 2n+1 + الرمز الفرعي 2n+2 مع النص الرئيسي الأزرق وتنسيق النص الأحمر](styled_text.png)

## إضافة نص شفاف

أضف أشكالًا ونصًا شبه شفافة إلى مستند PDF باستخدام Aspose.PDF لـ Python.
يقوم بإنشاء مستطيل ملون مع عتامة جزئية ويتراكب مع TextFragment بلون أمامي شفاف.

1. قم بتهيئة كائن المستند وأضف صفحة فارغة لرسم المحتوى.
1. استخدم «Ap.drawing.graph» لإنشاء لوحة تسمح لك برسم الأشكال.
1. أضف مستطيلًا بحشو شبه شفاف.
1. منع تغيير موضع اللوحة القماشية.
1. أضف اللوحة القماشية إلى الصفحة. أدخل الأشكال الرسومية في مجموعة فقرات الصفحة.
1. قم بإنشاء جزء نصي شفاف.
1. أدخل جزء النص في مجموعة فقرات الصفحة.
1. احفظ مستند PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_transparent(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create Graph object
    canvas = ap.drawing.Graph(100.0, 400.0)

    # Create rectangle with semi-transparent fill
    rect = ap.drawing.Rectangle(100, 100, 400, 400)
    rect.graph_info.fill_color = ap.Color.from_argb(128, 0xC5, 0xB5, 0xFF)
    canvas.shapes.add(rect)

    # Prevent position shift
    canvas.is_change_position = False
    page.paragraphs.add(canvas)

    # Create transparent text
    text = ap.text.TextFragment(
        "This is the transparent text. "
        "This is the transparent text. "
        "This is the transparent text."
    )
    text.text_state.foreground_color = ap.Color.from_argb(30, 0, 255, 0)
    page.paragraphs.add(text)

    document.save(output_file_name)
```

### إضافة نص غير مرئي إلى PDF

يوضح هذا المثال كيفية إنشاء مستند PDF يحتوي على نص مرئي وغير مرئي. يظل النص غير المرئي جزءًا من بنية المستند ولكنه مخفي عن العرض، مما يجعله مفيدًا لتضمين البيانات الوصفية أو علامات إمكانية الوصول أو المحتوى القابل للبحث دون التأثير على التخطيط.

1. قم بإنشاء مستند PDF وصفحة.
1. قم بإنشاء جزء نصي بمحتوى مرئي متكرر.
1. أضف جزءًا نصيًا ثانيًا وقم بتمييزه على أنه غير مرئي.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_invisible(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Add visible text
    text1 = ap.text.TextFragment(
        "This is the visible text. This is the visible text. This is the visible text."
    )
    page.paragraphs.add(text1)

    # Create transparent text
    text2 = ap.text.TextFragment(
        "This is the invisible text. "
        "This is the invisible text. "
        "This is the invisible text."
    )
    text2.text_state.invisible = True
    page.paragraphs.add(text2)

    document.save(output_file_name)
```

### إضافة نص مع تصميم الحدود في PDF

تعرض مكتبة Aspose.PDF كيفية إنشاء مستند PDF يحتوي على جزء نصي ذو حدود مرئية. تقوم الطريقة بتطبيق ألوان الخلفية والأمامية وإعدادات الخط والحد (الحدود) حول مستطيل النص لتحسين التركيز المرئي.

1. قم بإنشاء مستند PDF وصفحة.
1. إنشاء جزء نصي ووضعه. أضف جزءًا نصيًا مع الرسالة وقم بتعيين موضعه.
1. قم بتطبيق نمط النص. اضبط الخط على تايمز نيو رومان، مقاس 12. قم بتطبيق خلفية رمادية فاتحة ولون أمامي أحمر (نص).
1. قم بتكوين نمط الحدود.
1. إضافة نص إلى الصفحة. استخدم TextBuilder لإلحاق النص المصمم بالصفحة.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_border(output_file_name):
    # Create PDF document
    document = ap.Document()
    # Get particular page
    page = document.pages.add()
    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample text with border.")
    text_fragment.position = ap.text.Position(10, 700)

    # Set text properties
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    # Set StrokingColor property for drawing border (stroking) around text rectangle.
    # Note: This only affects the border if draw_text_rectangle_border is set to True.
    text_fragment.text_state.stroking_color = ap.Color.dark_red
    # Enable drawing of the text rectangle border
    text_fragment.text_state.draw_text_rectangle_border = True

    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

### إضافة نص Strikeout إلى ملف PDF

أضف تنسيق الخط (يتوسطه خط) إلى جزء نصي في مستند PDF. يُعد نص Strikeout مفيدًا للإشارة إلى عمليات الحذف أو المراجعات أو التركيز في المستندات المشروحة.

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. إنشاء جزء نصي وتصفيفه.
1. قم بتطبيق تنسيق اللون والشطب. قم بتعيين الخلفية إلى اللون الرمادي الفاتح، ولون النص إلى اللون الأحمر، وقم بتمكين strikeout.
1. ضع النص.
1. استخدم «TextBuilder» لإلحاق النص المصمم بالصفحة.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_strikeout_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    # Create text fragment
    text_fragment = ap.text.TextFragment("This is sample strikeout text.")
    # Set text properties
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red
    text_fragment.text_state.strike_out = True
    text_fragment.text_state.font_style = ap.text.FontStyles.BOLD
    text_fragment.position = ap.text.Position(100, 600)

    # Create TextBuilder object
    text_builder = ap.text.TextBuilder(page)
    text_builder.append_text(text_fragment)

    # Save PDF document
    document.save(output_file_name)
```

## تأثيرات لونية متقدمة

### تطبيق التدرج المحوري على النص في PDF

يوضح Aspose.PDF لـ Python عبر .NET كيفية تطبيق تأثير التدرج الخطي على النص في مستند PDF. ينتقل التدرج المحوري بسلاسة من الأحمر إلى الأزرق في جميع أنحاء النص، مما يخلق عنوانًا رائعًا بصريًا. هذه التقنية مثالية للعناوين الأنيقة أو العلامات التجارية أو العناصر الزخرفية في تخطيطات مستندات PDF.

1. قم بتهيئة مستند جديد وإضافة صفحة فارغة.
1. إنشاء جزء نصي وتصفيفه. أضف العنوان وحدد الموضع والخط والحجم.
1. قم بتطبيق تظليل التدرج المحوري باستخدام «التظليل المحوري المتدرج». قم بتعيين لون المقدمة باستخدام GradientAxialShading من الأحمر إلى الأزرق.
1. أضف تصميم تسطير.
1. أدخل جزء النص المصمم في الصفحة.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_axial_shading_to_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientAxialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

### تطبيق التدرج الشعاعي على النص في PDF

ينشئ التدرج الشعاعي انتقالًا دائريًا للألوان يشع إلى الخارج من مركز النص، مما يوفر خيار تصميم ديناميكي بصريًا للعناوين أو الرؤوس أو العناصر الزخرفية.

1. قم بتهيئة مستند جديد وإضافة صفحة فارغة.
1. إنشاء جزء نصي وتصفيفه. أضف العنوان وحدد الموضع والخط والحجم.
1. قم بتطبيق التدرج الشعاعي باستخدام «التظليل الشعاعي المتدرج». قم بتعيين لون المقدمة باستخدام GradientRadialShading من الأحمر إلى الأزرق.
1. أضف تصميم تسطير.
1. أدخل جزء النص المصمم في الصفحة.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def apply_gradient_radial_shading_to_text(output_file_name):
    # Create PDF document
    document = ap.Document()
    page = document.pages.add()

    text_fragment = ap.text.TextFragment("PDF TITLE")
    text_fragment.position = ap.text.Position(100, 600)
    text_fragment.text_state.font_size = 36
    text_fragment.text_state.font = ap.text.FontRepository.find_font("Arial Bold")

    # Apply radial gradient shading (red to blue)
    text_fragment.text_state.foreground_color = ap.Color()
    text_fragment.text_state.foreground_color.pattern_color_space = (
        ap.drawing.GradientRadialShading(ap.Color.red, ap.Color.blue)
    )
    text_fragment.text_state.underline = True

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![قم بتطبيق تظليل متدرج شعاعي](gradient_radial_shading.png)

## أجزاء HTML و LaTeX

### إضافة نص HTML إلى وثيقة PDF

يسمح لك Aspose.PDF لـ Python عبر مكتبة.NET بإدراج محتوى بتنسيق HTML في مستند PDF باستخدام فئة HTMLFragment. باستخدام علامات HTML، يمكنك عرض نص منمق أو منظم أو يشبه الصيغة مباشرة في PDF.

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. قم بإنشاء مثيل لفئة HTMLFragment وقم بتمرير سلسلة HTML الخاصة بك كمعامل.
1. أضف الجزء إلى الصفحة باستخدام «page.paragrahs.add ()» لإدراج محتوى HTML.
1. احفظ ملف PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_html_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.HtmlFragment("<pre>S=a<sub>2n</sub>+a<sup>2</sup><pre>")

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![إضافة نص HTML إلى وثيقة PDF](html_fragment.png)

### أضف جزء HTML المصمم بتنسيقات متنوعة إلى مستند PDF

يمكننا تحديد جزء HTML وتعيين نمط النص مباشرة باستخدام علامات HTML. قم بتضمين محتوى HTML المصمم في مستند PDF. يقوم مقتطف الشفرة هذا بإنشاء ملف PDF جديد، وإضافة صفحة، وإدراج جزء HTML مع عناصر تنسيق مختلفة (العناوين والفقرات والروابط والأنماط المضمنة)، وحفظ النتيجة في المسار المحدد.

1. يقوم بتهيئة كائن مستند جديد لتمثيل PDF.
1. يقوم بإلحاق صفحة فارغة بالمستند حيث سيتم وضع محتوى HTML.
1. إعداد محتوى HTML. تحتوي سلسلة HTML على عنوان h1 وفقرة ذات لون أخضر بنص غامق ومائل ومسطّر وارتباط تشعبي إلى موقع ويب بحجم خط متزايد.
1. إنشاء جزء HTML. لف سلسلة HTML في كائن HTMLFragment.
1. إدراج HTML في الصفحة. يضيف جزء HTML إلى مجموعة فقرات الصفحة، ويعرض HTML كمحتوى PDF أصلي.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    page.paragraphs.add(html_fragment)
    document.save(output_file_name)
```

![إضافة محتوى HTML إلى وثيقة PDF](html_content.png)

### إضافة جزء HTML مع حالة النص التي تم تجاوزها

كما رأينا في المثال السابق، من الممكن تعيين الأنماط مباشرة في كود HTML. هذا له مزاياه، ولكن أيضًا بعض العيوب. لنفترض أننا نعمل مع HTML الخاص بالعميل ونريد توحيد مظهر مخرجاتنا.
في هذه الحالة، يمكننا تجاوز تصميم العميل باستخدام TextState الخاص بنا، كما هو موضح في المثال التالي.

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. إعداد محتوى HTML. تحتوي سلسلة HTML على عنوان h1 بخط Verdana، وفقرة ذات لون أخضر بنص غامق ومائل ومسطّر، وارتباط تشعبي إلى موقع ويب بحجم خط أكبر.
1. إنشاء جزء HTML. لف سلسلة HTML في كائن HTMLFragment.
1. قم بتجاوز تنسيق النص. قم بإنشاء كائن TextState وقم بتعيين الخط وحجم الخط ولون النص.
1. أضف جزء HTML إلى مجموعة فقرات الصفحة.
1. احفظ المستند.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_html_fragment_override_text_state(output_file_name):
    document = ap.Document()
    page = document.pages.add()
    html_content = """
        <h1 style='color:blue;font-family:Verdana'>Hello, Aspose!</h1>
        <p>This is a sample paragraph with <b>bold</b>, <i>italic</i>, and <u>underlined</u> text.</p>
        <p style='color:green;'>This paragraph is green.</p>
        <a href='https://www.aspose.com' style='font-size:16px;'>Visit Aspose</a>
    """
    html_fragment = ap.HtmlFragment(html_content)
    html_fragment.text_state = ap.text.TextState()
    html_fragment.text_state.font = ap.text.FontRepository.find_font("Arial")
    html_fragment.text_state.font_size = 14
    html_fragment.text_state.foreground_color = ap.Color.red

    page.paragraphs.add(html_fragment)
    document.save(output_file_name)
```

![إضافة جزء HTML لتجاوز حالة النص](html_override.png)

### إضافة نص LaTeX إلى مستند PDF

أضف تعبيرات رياضية بتنسيق Latex إلى مستند PDF باستخدام فئة TexFragment في Aspose.PDF لـ Python عبر .NET.
LaTeX هو نظام تنضيد قوي يستخدم على نطاق واسع لإنشاء مستندات علمية ورياضية. باستخدام TexFragment، يمكنك عرض الرموز والرموز الرياضية لـ LaTeX مباشرة داخل صفحة PDF.

1. قم بإنشاء مستند وصفحة جديدة باستخدام «Document ()» و «document.pages.add ()» لإضافة صفحة فارغة.
1. استخدم فئة TexFragment لعرض صيغة LaTeX مباشرة.
1. أضف محتوى LaTeX إلى تخطيط PDF باستخدام «page.paragraphs.add ()».
1. احفظ ملف PDF.

```python
import math
import sys
import os
import aspose.pdf as ap

def add_text_latex_fragment(output_file_name):
    # Create a new document
    document = ap.Document()
    page = document.pages.add()

    # Add a text fragment at a specific position
    text_fragment = ap.TeXFragment(
        "\\underbrace{\\overbrace{a+b}^6 \\cdot \\overbrace{c+d}^7}_\\text{example of text} = 42"
    )

    page.paragraphs.add(text_fragment)
    document.save(output_file_name)
```

![تعبير رياضي معقد معروض في ملف PDF يُظهر صيغة LaTeX مع تدوين الأقواس فوق (a+b)، وترميز الدعامة السفلية تحت التعبير الكامل (a+b) · (c+d)، المسمى كمثال للنص، ويساوي 42. توضح الصيغة تنضيد الحروف الرياضي المتقدم مع المسافات المناسبة وتصميم الأقواس النموذجي لعرض LaTeX](latex_fragment.png)

## خطوط مخصصة

### استخدم خطًا مخصصًا من ملف

يتيح لك هذا المثال إضافة نص إلى ملف PDF باستخدام خط OpenType مخصص في Aspose.PDF لـ Python عبر .NET. يوضح كيفية إنشاء مستند PDF جديد، ووضع النص بدقة على الصفحة، وتطبيق التنسيق المخصص مثل نوع الخط والحجم واللون والنمط المائل.

1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. حدد محتوى النص الذي تريد إضافته إلى PDF.
1. قم بتعيين موضع النص.
1. أضف جزء النص إلى الصفحة.
1. احفظ مستند PDF.

لا تعمل هذه الوظيفة فقط مع OTF ولكن أيضًا مع خطوط TTF.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_file(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("Hello, Aspose!")
    fragment.position = ap.text.Position(100, 600)
    fragment.text_state.font = ap.text.FontRepository.open_font(font_path)
    fragment.text_state.font_size = 24
    fragment.text_state.foreground_color = ap.Color.blue
    fragment.text_state.font_style = ap.text.FontStyles.ITALIC

    page.paragraphs.add(fragment)
    document.save(output_file_name)
```

![جزء نصي معروض في مستند PDF يعرض مرحبًا، Aspose! تم تقديمه بخط BrioSoPro المائل باللون الأزرق، مما يوضح تكامل خط OpenType المخصص وإمكانيات التصميم داخل تنسيق نص PDF](custom_font.png)

### استخدم خطًا مخصصًا من البث

يوضح مقتطف الشفرة هذا كيفية إضافة نص إلى مستند PDF باستخدام خط OpenType (OTF) مضمن مخصص مع Aspose.PDF لـ Python عبر .NET. يوضح كيفية فتح ملف الخط كتدفق، وتضمينه في PDF لضمان توفر الخط عبر الأنظمة المختلفة، وتطبيق تنسيق النص مثل حجم الخط واللون والنمط المائل. يعد هذا الأسلوب مثاليًا لإنشاء ملفات PDF متسقة بصريًا تحافظ على الطباعة حتى عند مشاركتها أو عرضها على الأجهزة بدون الخط المثبت.

1. قم بتحميل ملف الخط كتدفق ثنائي.
1. افتح الخط وقم بتضمينه باستخدام 'fontrepository.open_font'.
1. قم بإنشاء مستند PDF جديد وإضافة صفحة.
1. أضف جزءًا نصيًا أنيقًا باستخدام:
    - خط مخصص مضمن.
    - أسلوب مائل ولون أزرق.
    - حجم الخط المحدد وموضعه.
1. احفظ المستند النهائي إلى مسار إخراج محدد.

```python
import math
import sys
import os
import aspose.pdf as ap

def use_custom_font_from_stream(output_file_name):
    font_path = os.path.join(FONT_DIR, "BriosoPro Italic.otf")
    with open(font_path, "rb") as font_stream:
        font = ap.text.FontRepository.open_font(font_stream, ap.text.FontTypes.OTF)
        font.is_embedded = True

        document = ap.Document()
        page = document.pages.add()

        fragment = ap.text.TextFragment("Hello, Aspose!")
        fragment.position = ap.text.Position(100, 600)
        fragment.text_state.font = font
        fragment.text_state.font_size = 14
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.font_style = ap.text.FontStyles.ITALIC

        page.paragraphs.add(fragment)
        document.save(output_file_name)
```

يضمن تضمين الخطوط عرضًا متسقًا عبر الأنظمة الأساسية، مما يجعل هذا النهج مثاليًا للعلامة التجارية ودقة التصميم والدعم متعدد اللغات.

## موضوعات نصية ذات صلة

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [تنسيق نص PDF في بايثون](/pdf/ar/python-net/text-formatting-inside-pdf/)
- [استبدال النص في PDF عبر Python](/pdf/ar/python-net/replace-text-in-pdf/)
- [ابحث واستخرج نص PDF في بايثون](/pdf/ar/python-net/search-and-get-text-from-pdf/)