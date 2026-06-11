---
title: بحث واستخراج نص PDF في بايثون
linktitle: ابحث واحصل على نص
type: docs
weight: 60
url: /ar/python-net/search-and-get-text-from-pdf/
description: تعرف على كيفية البحث عن النص وفحصه واستخراجه من مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: ابحث في نص PDF وافحص الأجزاء المستخرجة في Python
Abstract: تشرح هذه المقالة كيفية البحث عن النص واستخراجه من مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. ويغطي «TextAbsorber» و «TextFragmentAbsorber»، بما في ذلك الاستخراج المستند إلى المنطقة، وعمليات البحث الخاصة بالصفحة، ومطابقة العبارات، وفحص موضع النص وخصائص الخط.
---

## ابحث عن نص من PDF

ابحث واستخرج النص من منطقة مستطيلة محددة في مستند PDF باستخدام `TextAbsorber` فئة. يستخدم وضع تنسيق النص النقي للإخراج النظيف وغير المنسق، وهو أمر مفيد لاستخراج المحتوى من المناطق المهيكلة مثل الرؤوس أو التذييلات أو مناطق الجدول. من خلال الجمع `TextExtractionOptions` و `TextSearchOptions` باستخدام القيود المستطيلة، يمكنك التحكم في مكان وكيفية استخراج النص.

استخدم هذه الصفحة عندما تحتاج إلى تدقيق محتوى نص PDF أو استخراج النص للتحليل أو فحص المواضع وتنسيق أجزاء النص المتطابقة.

1. قم بتحميل ملف PDF باستخدام «AP.document».
1. قم بتكوين خيارات استخراج النص.
1. حدد منطقة البحث باستخدام قيود المستطيل.
1. إنشاء وتكوين TextAbsorber.
1. قم بمعالجة جميع الصفحات في المستند.
1. استرداد النص المستخرج وعرضه.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search(input_file_path):
    # Open PDF document
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Process all pages
    document.pages.accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## ابحث عن نص من صفحة PDF محددة

ابحث واستخرج النص من صفحة ومنطقة معينة في PDF باستخدام TextAbsorber الخاص بـ Aspose.PDF. يستهدف الصفحة 2 من المستند ويستخرج فقط النص الموجود داخل منطقة مستطيلة محددة.
من خلال الجمع بين خيارات استخراج النص (للتحكم في التنسيق) وخيارات TextSearchOptions (لحدود المنطقة)، يمكنك إجراء استخراج دقيق لنص خاص بالصفحة بكفاءة.

1. قم بتحميل وثيقة PDF.
1. قم بإعداد خيارات استخراج النص.
1. قم بتقييد استخراج النص إلى منطقة مستطيلة محددة على الصفحة.
1. إنشاء وتكوين TextAbsorber.
1. قم بمعالجة صفحة محددة.
1. استرداد النص المستخرج وعرضه.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    text_extraction_options = ap.text.TextExtractionOptions(
        ap.text.TextExtractionOptions.TextFormattingMode.PURE
    )
    text_search_options = ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))

    absorber = ap.text.TextAbsorber(text_extraction_options, text_search_options)

    # Only page 2
    document.pages[2].accept(absorber)

    print(f"Text fragments found: {absorber.text}")
```

## تحليل واستخراج خصائص أجزاء النص التفصيلية من PDF

على عكس TextAbsorber، الذي يستخرج النص الخام، يوفر TextFragmentAbsorber معلومات تفصيلية منخفضة المستوى حول كل جزء من أجزاء النص - مثل موضعه وسمات الخط واللون وتفاصيل التضمين.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة ممتص أجزاء النص.
1. قم بمعالجة جميع الصفحات في المستند.
1. قم بالتكرار من خلال أجزاء النص المستخرجة.
1. طباعة معلومات النص الأساسية.
1. طباعة الخط وتفاصيل التنسيق.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    document.pages.accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
        print("XIndent:", fragment.position.x_indent)
        print("YIndent:", fragment.position.y_indent)
        print("Font - Name:", fragment.text_state.font.font_name)
        print("Font - IsAccessible:", fragment.text_state.font.is_accessible)
        print("Font - IsEmbedded:", fragment.text_state.font.is_embedded)
        print("Font - IsSubset:", fragment.text_state.font.is_subset)
        print("Font Size:", fragment.text_state.font_size)
        print("Foreground Color:", fragment.text_state.foreground_color)
```

## ابحث عن عبارة نصية محددة على صفحة PDF واحدة

ابحث عن عبارة نصية محددة داخل صفحة مستند PDF باستخدام TextFragmentAbsorber. على عكس البحث في المستند بأكمله، فإن هذا الأسلوب يقصر البحث على صفحة واحدة فقط، مما يجعله أكثر كفاءة لتأكيد وجود النص وموقعه في المناطق المستهدفة مثل الرؤوس أو التذييلات أو أقسام المحتوى المحددة.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة TextFragmentAbsorber باستخدام عبارة البحث.
1. قم بتطبيق Absorber على صفحة محددة.
1. قم بالتكرار فوق الأجزاء الموجودة.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_page(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale")
    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## بحث نصي تسلسلي صفحة بصفحة مع نتائج تراكمية

ابحث عن النص بشكل تدريجي عبر صفحات متعددة من مستند PDF باستخدام TextFragmentAbsorber الخاص بـ Aspose.PDF.
بخلاف البحث في صفحة واحدة أو على مستوى المستند، يتيح لك هذا الأسلوب معالجة الصفحات بالتتابع، وجمع النتائج تدريجيًا، وتحليل أجزاء النص بسياق خاص بالصفحة. هذه الطريقة مثالية للمستندات الكبيرة أو عمليات سير عمل المعالجة التدريجية.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة TextFragmentAbsorber وقم بتعيين عبارة البحث.
1. معالجة الصفحة الأولى. ابحث فقط في الصفحة 1. يطبع النص ورقم الصفحة والموضع. قم بتوفير نتائج معزولة خاصة بالصفحة من أجل الوضوح.
1. قم بمعالجة الصفحة التالية بالتتابع. انتقل إلى الصفحة 2 واستمر اختياريًا في بقية المستند. يضمن «absorber.visit ()» تراكم النتائج من جميع الصفحات التي تمت زيارتها. تطبع نتائج البحث التراكمية، مع عرض النص والموقع.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_sequential_search(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.phrase = "whale"

    # First page
    document.pages[1].accept(absorber)
    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)

    print("--")

    # Continue to next page
    document.pages[2].accept(absorber)
    absorber.visit(document)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Page:", fragment.page.number)
        print("Position:", fragment.position)
```

## البحث عن عبارة مستهدفة داخل منطقة مستطيلة

ابحث عن عبارة محددة داخل PDF مع تقييد البحث بمنطقة مستطيلة محددة في صفحة واحدة.
من خلال الجمع بين البحث بالعبارات والقيود المكانية، يمكنك تحديد موقع المحتوى بدقة في مناطق معينة دون مسح الصفحة أو المستند بأكمله. وهذا مفيد بشكل خاص للنماذج أو الرؤوس أو التذييلات أو التقارير المهيكلة حيث يظهر المحتوى في مواقع يمكن التنبؤ بها.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة TextFragmentAbsorber باستخدام قيود العبارة والمستطيل
1. قم بتطبيق Absorber على الصفحة 2. يقيد المعالجة إلى الصفحة 2، مما يقلل من العمليات الحسابية غير الضرورية. يضمن أن البحث خاص بالصفحة.
1. قم بالتكرار من خلال الأجزاء الموجودة وطباعتها

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_phrase(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        "elephant", ap.text.TextSearchOptions(ap.Rectangle(0, 0, 842, 250, True))
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## البحث عن نمط النص في PDF باستخدام التعبيرات العادية

ابحث عن أنماط النص في PDF باستخدام التعبيرات العادية. من خلال تمكين وضع regex في TextFragmentAbsorber، يمكنك تحديد الأنماط المعقدة مثل الأرقام أو التواريخ أو الأسعار أو الإحداثيات أو تنسيقات النص المخصصة. تقصر الوظيفة البحث على صفحة معينة، مما يجعلها فعالة للاستخراج المستهدف للبيانات المنظمة.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة TextFragmentAbsorber باستخدام نمط Regex.
1. قم بتطبيق Absorber على الصفحة 2. يقصر البحث على الصفحة 2 من أجل الكفاءة والدقة. يتم تحليل النص الموجود في هذه الصفحة فقط.
1. قم بالتكرار من خلال الأجزاء الموجودة. تطبع أجزاء النص المطابقة وإحداثياتها. يوفر معلومات دقيقة عن الموقع للأنماط المستخرجة.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_regex(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber(
        r"\d+\.\d+", ap.text.TextSearchOptions(is_regular_expression_used=True)
    )

    document.pages[2].accept(absorber)

    for fragment in absorber.text_fragments:
        print("Text:", fragment.text)
        print("Position:", fragment.position)
```

## تحويل تطابقات النص إلى ارتباطات تشعبية في PDF باستخدام TextFragmentAbsorber

ابحث عن عبارات نصية محددة في PDF وقم بتحويلها إلى روابط تشعبية قابلة للنقر. باستخدام TextFragmentAbsorber مع أنماط regex، فإنه يحدد الكلمات المستهدفة ويطبق التصميم المرئي (اللون والتسطير) جنبًا إلى جنب مع الروابط التفاعلية.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة TextFragmentAbsorber باستخدام نمط Regex.
1. قم بتطبيق Absorber على الصفحة 1.
1. قم بتصميم وإضافة الارتباطات التشعبية للمباريات.
1. احفظ ملف PDF المعدل.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_add_hyperlink(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber("whale|elephant")
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        fragment.text_state.foreground_color = ap.Color.blue
        fragment.text_state.underline = True
        fragment.hyperlink = ap.WebHyperlink(
            f"https://en.wikipedia.org/wiki/{fragment.text}"
        )

    output = input_file_path.replace("in.pdf", "out.pdf")
    document.save(output)
```

## البحث وتحديد النص المصمم في PDF باستخدام TextFragmentAbsorber

ابحث عن أجزاء النص في PDF بناءً على خصائص التنسيق الخاصة بها بدلاً من محتواها. باستخدام TextFragmentAbsorber، فإنه يحدد النص بأنماط محددة، مثل النص الغامق.

1. قم بتحميل وثيقة PDF.
1. قم بتهيئة ممتص أجزاء النص.
1. قم بتطبيق Absorber على الصفحة 1.
1. افحص أجزاء النص بناءً على التنسيق. يتحقق من نمط الخط للتنسيق الغامق.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_styled_text(input_file_path):
    document = ap.Document(input_file_path)

    absorber = ap.text.TextFragmentAbsorber()
    absorber.text_search_options = ap.text.TextSearchOptions(True)

    absorber.visit(document.pages[1])

    for fragment in absorber.text_fragments:
        if fragment.text_state.font_style == ap.text.FontStyles.BOLD:
            print(f"Bold: {fragment.text}")
        if fragment.text_state.invisible:
            print(f"Invisible: {fragment.text}")
```

## تسليط الضوء على النص المرئي في صفحات PDF

تجمع هذه الوظيفة بين التعرف على النص والعرض في سير عمل واحد. فهو لا يستخرج النص فحسب، بل يتخيله أيضًا من خلال تمييز الأجزاء والمقاطع والأحرف في المستطيلات المرمزة بالألوان على صور PNG لكل صفحة.

يقوم مثالنا بعمل تصور نصي متقدم على PDF من خلال:

- البحث عن جميع أجزاء النص المرئية باستخدام التعبيرات العادية
- تحويل كل صفحة PDF إلى صورة PNG عالية الدقة
- رسم مستطيلات ملونة حول أجزاء النص ومقاطع النص والأحرف الفردية

1. تعيين دقة صورة الإخراج. يتم تحويل كل صفحة PDF إلى صورة PNG 150 DPI.
1. افتح ملف PDF وقم بتهيئة أداة امتصاص النص.
1. قم بمعالجة كل صفحة. قم بتطبيق جهاز الامتصاص على كل صفحة. اجمع كل أجزاء النص المكتشفة ومواقعها الهندسية.
1. تحويل الصفحة إلى بث PNG.
1. قم بإعداد كائن الرسومات للرسم.
1. قم بتطبيق التحويل الإحداثي. قم بتحويل إحداثيات PDF إلى وحدات بكسل للصورة.
1. ارسم مستطيلات لعناصر النص.
1. احفظ النتيجة.

```python
import io
import sys
import shutil
import aspose.pdf as ap
import aspose.pydrawing as drawing
from os import path

def text_fragment_absorber_search_and_highlight(infile):
    resolution = 150
    png_device = ap.devices.PngDevice(ap.devices.Resolution(resolution, resolution))

    # Open PDF document
    document = ap.Document(infile)
    absorber = ap.text.TextFragmentAbsorber(r"[\S]+")
    absorber.text_search_options.is_regular_expression_used = True

    for page in document.pages:
        page.accept(absorber)
        stream = io.BytesIO()
        png_device.process(page, stream)
        with drawing.Bitmap.from_stream(stream) as bmp:
            with drawing.Graphics.from_image(bmp) as gr:
                scale = resolution / 72
                gr.transform = drawing.drawing2d.Matrix(
                    float(scale),
                    float(0),
                    float(0),
                    float(-scale),
                    float(0),
                    float(bmp.height),
                )
                text_fragment_collection = absorber.text_fragments
                # Loop through the fragments
                for text_fragment in text_fragment_collection:
                    gr.draw_rectangle(
                        drawing.Pens.yellow,
                        float(text_fragment.position.x_indent),
                        float(text_fragment.position.y_indent),
                        float(text_fragment.rectangle.width),
                        float(text_fragment.rectangle.height),
                    )
                    for seg_num in range(1, len(text_fragment.segments) + 1):
                        segment = text_fragment.segments[seg_num]
                        for char_num in range(1, len(segment.characters) + 1):
                            character_info = segment.characters[char_num]
                            rect = page.get_page_rect(True)
                            print(
                                f"TextFragment = {text_fragment.text}"
                                + f" Page URY = {rect.ury}"
                                + f" TextFragment URY = {text_fragment.rectangle.ury}"
                            )
                            gr.draw_rectangle(
                                drawing.Pens.black,
                                float(character_info.rectangle.llx),
                                float(character_info.rectangle.lly),
                                float(character_info.rectangle.width),
                                float(character_info.rectangle.height),
                            )
                        gr.draw_rectangle(
                            drawing.Pens.green,
                            float(segment.rectangle.llx),
                            float(segment.rectangle.lly),
                            float(segment.rectangle.width),
                            float(segment.rectangle.height),
                        )

                # Save result
                bmp.save(
                    infile.replace("_in.pdf", str(page.number) + "_out.png"),
                    drawing.imaging.ImageFormat.png,
                )
```

## موضوعات نصية ذات صلة

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [استبدال النص في PDF عبر Python](/pdf/ar/python-net/replace-text-in-pdf/)
- [إضافة تلميحات الأدوات إلى نص PDF في Python](/pdf/ar/python-net/pdf-tooltip/)
- [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)