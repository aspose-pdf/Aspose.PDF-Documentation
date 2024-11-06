---
title: إضافة نص إلى PDF باستخدام Python
linktitle: إضافة نص إلى PDF
type: docs
weight: 10
url: ar/python-net/add-text-to-pdf-file/
description: يصف هذا المقال مختلف الجوانب المتعلقة بالعمل مع النصوص في Aspose.PDF. تعلم كيفية إضافة نص إلى PDF، إضافة أجزاء HTML، أو استخدام خطوط OTF مخصصة.
lastmod: "2024-02-17"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "إضافة نص إلى PDF باستخدام Python",
    "alternativeHeadline": "كيفية إضافة نص إلى PDF",
    "author": {
        "@type": "Person",
        "name":"Anastasiia Holub",
        "givenName": "Anastasiia",
        "familyName": "Holub",
        "url":"https://www.linkedin.com/in/anastasiia-holub-750430225/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, python, إضافة نص إلى pdf",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "مبيعات",
                "areaServed": "الولايات المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "مبيعات",
                "areaServed": "المملكة المتحدة",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "مبيعات",
                "areaServed": "أستراليا",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "/python-net/add-text-to-pdf-file/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "/python-net/add-text-to-pdf-file/"
    },
    "dateModified": "2024-02-04",
    "description": "يصف هذا المقال مختلف الجوانب المتعلقة بالعمل مع النصوص في Aspose.PDF for Python. تعلم كيفية إضافة نص إلى PDF، إضافة أجزاء HTML، أو استخدام خطوط OTF مخصصة."
}
</script>


## إضافة نص

1. افتح مستند PDF المدخل باستخدام Aspose.PDF.
2. حدد الصفحة المعينة التي تريد إضافة النص إليها.
3. أنشئ كائن TextFragment. يتم إنشاء جزء النص بالمحتوى 'النص الرئيسي'. يتم وضع هذا الجزء عند الإحداثيات (100, 600) على الصفحة.
4. ضبط خصائص النص. يتم ضبط خصائص مختلفة للنص مثل حجم الخط، نوع الخط (Times New Roman)، لون الخلفية (رمادي فاتح)، ولون الواجهة (أحمر).
5. إنشاء كائن TextBuilder. يتم استحداث كائن TextBuilder مع الصفحة المحددة.
6. إلحاق جزء النص. يتم إلحاق جزء النص الذي تم إنشاؤه سابقاً بصفحة PDF باستخدام كائن TextBuilder.
7. استدعاء طريقة [document.save](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) وحفظ ملف PDF الناتج.

يظهر لك مقطع الشيفرة التالي كيفية إضافة نص في ملف PDF موجود:

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document(input_pdf)

    # الحصول على الصفحة المعينة
    page = document.pages[1]

    # إنشاء جزء النص
    text_fragment = ap.text.TextFragment("main text")
    text_fragment.position = ap.text.Position(100, 600)

    # ضبط خصائص النص
    text_fragment.text_state.font_size = 12
    text_fragment.text_state.font = ap.text.FontRepository.find_font("TimesNewRoman")
    text_fragment.text_state.background_color = ap.Color.light_gray
    text_fragment.text_state.foreground_color = ap.Color.red

    # إنشاء كائن TextBuilder
    builder = ap.text.TextBuilder(page)

    # إلحاق جزء النص بصفحة PDF
    builder.append_text(text_fragment)

    # حفظ مستند PDF الناتج.
    document.save(output_pdf)             
```


## تحميل الخط من التدفق

يُظهر مقطع الشيفرة التالي كيفية تحميل الخط من كائن التدفق عند إضافة نص إلى وثيقة PDF.

```python

    import aspose.pdf as ap

    # تحميل ملف PDF المدخل
    document = ap.Document()
    document.pages.add()
    # إنشاء كائن بناء النص للصفحة الأولى من الوثيقة
    text_builder = ap.text.TextBuilder(document.pages[1])
    # إنشاء جزء نصي مع سلسلة نصية نموذجية
    text_fragment = ap.text.TextFragment("Hello world")

    if input_ttf != "":
        # تحميل خط TrueType إلى كائن التدفق
        font_stream = open(input_ttf, "rb")
        # ضبط اسم الخط للسلسلة النصية
        text_fragment.text_state.font = ap.text.FontRepository.open_font(
            font_stream, ap.text.FontTypes.TTF
        )
        # تحديد الموضع لجزء النص
        text_fragment.position = ap.text.Position(10, 10)
        # إضافة النص إلى TextBuilder حتى يمكن وضعه على ملف PDF
        text_builder.append_text(text_fragment)
        # حفظ وثيقة PDF الناتجة.
        document.save(output_pdf)
```


## إضافة نص باستخدام TextParagraph

يوضح لك مقتطف الشفرة التالي كيفية إضافة نص في مستند PDF باستخدام فئة [TextParagraph](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textparagraph/).

```python

    import aspose.pdf as ap

    # فتح المستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات لكائن المستند
    page = document.pages.add()
    builder = ap.text.TextBuilder(page)
    # إنشاء فقرة نصية
    paragraph = ap.text.TextParagraph()
    # تعيين المسافة البادئة للخطوط اللاحقة
    paragraph.subsequent_lines_indent = 20
    # تحديد الموقع لإضافة TextParagraph
    paragraph.rectangle = ap.Rectangle(100, 300, 200, 700, False)
    # تحديد وضع التفاف الكلمات
    paragraph.formatting_options.wrap_mode = (
        ap.text.TextFormattingOptions.WordWrapMode.BY_WORDS
    )
    # إنشاء جزء نصي
    fragment1 = ap.text.TextFragment("الثعلب البني السريع يقفز فوق الكلب الكسول")
    fragment1.text_state.font = ap.text.FontRepository.find_font("Times New Roman")
    fragment1.text_state.font_size = 12
    # إضافة الجزء إلى الفقرة
    paragraph.append_line(fragment1)
    # إضافة الفقرة
    builder.append_paragraph(paragraph)

    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```


## إضافة رابط تشعبي إلى TextSegment

يوضح هذا الكود كيفية إنشاء محتوى ديناميكي وتفاعلي داخل مستند PDF، بما في ذلك الروابط التشعبية إلى الموارد الخارجية.

قد تحتوي صفحة PDF على واحد أو أكثر من كائنات TextFragment، حيث يمكن لكل كائن TextFragment أن يحتوي على واحد أو أكثر من مثيلات [TextSegment](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textsegment/).

يرجى محاولة استخدام جزء الكود التالي لتحقيق هذا المطلب:

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    page1 = document.pages.add()
    # إنشاء مثيل لـ TextFragment
    tf = ap.text.TextFragment("Sample Text Fragment")
    # تعيين المحاذاة الأفقية لـ TextFragment
    tf.horizontal_alignment = ap.HorizontalAlignment.RIGHT
    # إنشاء نص segment مع نص نموذجي
    segment = ap.text.TextSegment(" ... Text Segment 1...")
    # إضافة segment إلى مجموعة segments لـ TextFragment
    tf.segments.append(segment)
    # إنشاء TextSegment جديد
    segment = ap.text.TextSegment("Link to Google")
    # إضافة segment إلى مجموعة segments لـ TextFragment
    tf.segments.append(segment)
    # تعيين رابط تشعبي لـ TextSegment
    segment.hyperlink = ap.WebHyperlink("www.google.com")
    # تعيين لون المقدمة لجزء النص
    segment.text_state.foreground_color = ap.Color.blue
    # تعيين تنسيق النص كـ مائل
    segment.text_state.font_style = ap.text.FontStyles.ITALIC
    # إنشاء كائن TextSegment آخر
    segment = ap.text.TextSegment("TextSegment without hyperlink")
    # إضافة segment إلى مجموعة segments لـ TextFragment
    tf.segments.append(segment)
    # إضافة TextFragment إلى مجموعة الفقرات لكائن الصفحة
    page1.paragraphs.add(tf)
    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```


## استخدام خط OTF

يوفر Aspose.PDF لـ Python عبر .NET ميزة استخدام الخطوط المخصصة/TrueType أثناء إنشاء/تعديل محتويات ملف PDF بحيث يتم عرض محتويات الملف باستخدام محتويات غير الخطوط الافتراضية للنظام.

```python

    import aspose.pdf as ap

    # إنشاء مثيل مستند جديد
    document = ap.Document()
    # إضافة صفحة إلى مجموعة صفحات ملف PDF
    page = document.pages.add()
    # إنشاء مثيل TextFragment بنص عينة
    fragment = ap.text.TextFragment("نص عينة بخط OTF")
    # أو يمكنك حتى تحديد مسار خط OTF في دليل النظام
    fragment.text_state.font = ap.text.FontRepository.open_font(input_otf)
    # تحديد تضمين الخط داخل ملف PDF، بحيث يتم عرضه بشكل صحيح،
    # حتى إذا لم يكن الخط المحدد مثبتًا/موجودًا على الجهاز المستهدف
    fragment.text_state.font.is_embedded = True
    # إضافة TextFragment إلى مجموعة الفقرات لمثيل الصفحة
    page.paragraphs.add(fragment)
    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```


## إضافة سلسلة HTML باستخدام DOM

يستخدم كود Python التالي مكتبة Aspose.PDF لإنشاء مستند PDF مع جزء HTML.

1. إنشاء مستند. يتم إنشاء مثيل لفئة المستند، ويمثل مستند PDF.
2. إضافة صفحة إلى مستند PDF.
3. إنشاء كائن HtmlFragment مع محتوى HTML.
4. ضبط الهوامش للجزء HTML. في هذه الحالة، يتم تعيين الهامش السفلي إلى 10 نقاط والهامش العلوي إلى 200 نقطة.
5. إضافة جزء HTML إلى الصفحة.
6. حفظ ملف PDF.

```python

    import aspose.pdf as ap

    # إنشاء كائن المستند
    doc = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في ملف PDF
    page = doc.pages.add()
    # إنشاء HtmlFragment مع محتويات HTML
    title = ap.HtmlFragment("<fontsize=10><b><i>جدول</i></b></fontsize>")
    # ضبط معلومات الهامش السفلي
    title.margin.bottom = 10
    # ضبط معلومات الهامش العلوي
    title.margin.top = 200
    # إضافة جزء HTML إلى مجموعة الفقرات في الصفحة
    page.paragraphs.add(title)
    # حفظ ملف PDF
    doc.save(output_pdf)
```


### نمط خط مخصص للحاشية السفلية

يوضح المثال التالي كيفية إضافة حواشي سفلية إلى أسفل صفحة الـ Pdf وتحديد نمط خط مخصص.

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    doc = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في PDF
    page = doc.pages.add()
    # إنشاء كائن GraphInfo
    graph = ap.GraphInfo()
    # تعيين عرض الخط كـ 2
    graph.line_width = 2
    # تعيين اللون لكائن الرسم
    graph.color = ap.Color.red
    # تعيين قيمة مصفوفة الشرطات كـ 3
    graph.dash_array = [3]
    # تعيين قيمة مرحلة الشرطات كـ 1
    graph.dash_phase = 1
    # تعيين نمط خط الحاشية السفلية للصفحة كـ graph
    page.note_line_style = graph
    # إنشاء مثيل TextFragment
    text = ap.text.TextFragment("Hello World")
    # تعيين قيمة الحاشية السفلية لـ TextFragment
    text.foot_note = ap.Note("حاشية سفلية لنص الاختبار 1")
    # إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page.paragraphs.add(text)
    # إنشاء TextFragment ثانية
    text = ap.text.TextFragment("Aspose.Pdf for .NET")
    # تعيين الحاشية السفلية للمقطع النصي الثاني
    text.foot_note = ap.Note("حاشية سفلية لنص الاختبار 2")
    # إضافة المقطع النصي الثاني إلى مجموعة الفقرات في ملف PDF
    page.paragraphs.add(text)
    # حفظ مستند PDF الناتج.
    doc.save(output_pdf)
```


### تخصيص تسمية الحاشية السفلية

توضح الكود التالي كيفية إنشاء مستند PDF يحتوي على جزء نصي يحتوي على حاشية سفلية.

افتراضيًا، يكون رقم الحاشية السفلية متزايدًا بدءًا من 1. ومع ذلك، قد يكون لدينا متطلب لتعيين تسمية حاشية سفلية مخصصة. لتحقيق هذا المتطلب، يرجى محاولة استخدام الكود التالي

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة صفحات PDF
    page = document.pages.add()
    # إنشاء كائن GraphInfo
    graph = ap.GraphInfo()
    # تعيين عرض الخط كـ 2
    graph.line_width = 2
    # تعيين اللون للكائن الجرافيكس
    graph.color = ap.Color.red
    # تعيين قيمة مصفوفة الشرطات كـ 3
    graph.dash_array = [3]
    # تعيين قيمة مرحلة الشرطات كـ 1
    graph.dash_phase = 1
    # تعيين نمط خط الحاشية السفلية للصفحة كجرافيكس
    page.note_line_style = graph
    # إنشاء مثيل TextFragment
    text = ap.text.TextFragment("Hello World")
    # تعيين قيمة الحاشية السفلية لـ TextFragment
    text.foot_note = ap.Note("حاشية سفلية للنص التجريبي 1")
    # تحديد تسمية مخصصة للحاشية السفلية
    text.foot_note.text = " Aspose"
    # إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page.paragraphs.add(text)
    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```


## إضافة صورة وجدول إلى الحاشية

يوضح هذا الكود كيفية إنشاء مستند PDF يحتوي على جزء نصي يضم حاشية معقدة تشمل صورة ونص وجدول باستخدام Aspose.PDF for Python.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()
    text = ap.text.TextFragment("some text")
    page.paragraphs.add(text)

    text.foot_note = ap.Note()
    image = ap.Image()
    image.file = input_jpg
    image.fix_height = 20
    text.foot_note.paragraphs.add(image)
    foot_note = ap.text.TextFragment("footnote text")
    foot_note.text_state.font_size = 20
    foot_note.is_in_line_paragraph = True
    text.foot_note.paragraphs.add(foot_note)
    table = ap.Table()
    table.rows.add().cells.add().paragraphs.add(ap.text.TextFragment("Row 1 Cell 1"))
    text.foot_note.paragraphs.add(table)

    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```

## كيفية إنشاء الحواشي الختامية

الحاشية الختامية هي اقتباس مصدر يشير القراء إلى مكان محدد في نهاية الورقة حيث يمكنهم معرفة مصدر المعلومات أو الكلمات المقتبسة أو المذكورة في الورقة.
 عند استخدام الحواشي السفلية، يتبع الجملة المقتبسة أو المعاد صياغتها أو المادة الملخصة رقم مرتفع.

يوضح هذا الكود كيفية إضافة جزء نصي مع حاشية إلى مستند PDF باستخدام Aspose.PDF لـ Python:

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في PDF
    page = document.pages.add()
    # إنشاء مثيل لـ TextFragment
    text = ap.text.TextFragment("Hello World")
    # تعيين قيمة الحاشية لـ TextFragment
    text.end_note = ap.Note("sample End note")
    # تحديد تسمية مخصصة للحاشية
    text.end_note.text = " Aspose"
    # إضافة TextFragment إلى مجموعة الفقرات في الصفحة الأولى من المستند
    page.paragraphs.add(text)
    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```

## النص والصورة كفقرة مدمجة

التنسيق الافتراضي لملف PDF هو تنسيق انسيابي (من الأعلى لليسار إلى الأسفل لليمين). لذلك يتم إضافة كل عنصر جديد يتم إضافته إلى ملف PDF في التدفق السفلي الأيمن. ومع ذلك، قد يكون لدينا متطلب لعرض عناصر الصفحة المختلفة مثل الصورة والنص على نفس المستوى (واحد بعد الآخر). يمكن أن تكون إحدى الطرق هي إنشاء مثيل جدول وإضافة كلا العنصرين إلى كائنات الخلايا الفردية. ومع ذلك، يمكن أن تكون هناك طريقة أخرى وهي الفقرة الداخلية. من خلال تعيين خاصية IsInLineParagraph للصورة والنص كـ true، ستظهر هذه الفقرات كعناصر مدمجة مع عناصر الصفحة الأخرى.

يُظهر مقتطف الشفرة التالي كيفية إضافة نص وصورة كفقرات مدمجة في ملف PDF.

```python

    import aspose.pdf as ap

    # إنشاء مثيل لوثيقة
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في مثيل الوثيقة
    page = document.pages.add()
    # إنشاء قطعة نص
    text = ap.text.TextFragment("Hello World.. ")
    # إضافة قطعة النص إلى مجموعة الفقرات في كائن الصفحة
    page.paragraphs.add(text)
    # إنشاء مثيل صورة
    image = ap.Image()
    # تعيين الصورة كفقرة مدمجة لتظهر مباشرة بعد
    # كائن الفقرة السابقة (TextFragment)
    image.is_in_line_paragraph = True
    # تحديد مسار ملف الصورة
    image.file = input_jpg
    # تعيين ارتفاع الصورة (اختياري)
    image.fix_height = 30
    # تعيين عرض الصورة (اختياري)
    image.fix_width = 100
    # إضافة الصورة إلى مجموعة الفقرات في كائن الصفحة
    page.paragraphs.add(image)
    # إعادة تهيئة كائن TextFragment بمحتويات مختلفة
    text = ap.text.TextFragment(" Hello Again..")
    # تعيين TextFragment كفقرة مدمجة
    text.is_in_line_paragraph = True
    # إضافة TextFragment الذي تم إنشاؤه حديثًا إلى مجموعة الفقرات في الصفحة
    page.paragraphs.add(text)
    # حفظ وثيقة PDF الناتجة.
    document.save(output_pdf)
```

## تحديد تباعد الحروف عند إضافة نص

يُظهر مقتطف الشيفرة التالي كيفية إنشاء مستند PDF يحتوي على جزء نصي مع زيادة في تباعد الحروف.

يمكن إضافة النص داخل مجموعة فقرات ملفات PDF باستخدام كائن TextFragment أو باستخدام كائن TextParagraph ويمكنك حتى ختم النص داخل PDF باستخدام فئة TextStamp.

### استخدام TextBuilder و TextFragment

```python

    import aspose.pdf as ap

    # إنشاء مثيل Document
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في Document
    document.pages.add()
    # إنشاء مثيل TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # إنشاء مثيل نصي TextFragment مع محتويات عينة
    wide_fragment = ap.text.TextFragment("نص مع زيادة في تباعد الحروف")
    wide_fragment.text_state.apply_changes_from(ap.text.TextState("Arial", 12))
    # تحديد تباعد الحروف لـ TextFragment
    wide_fragment.text_state.character_spacing = 2.0
    # تحديد موقع TextFragment
    wide_fragment.position = ap.text.Position(100, 650)
    # إلحاق TextFragment بمثيل TextBuilder
    builder.append_text(wide_fragment)
    # حفظ مستند PDF الناتج.
    document.save(output_pdf)
```


### استخدام TextParagraph

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في المستند
    document.pages.add()
    # إنشاء مثيل لـ TextBuilder
    builder = ap.text.TextBuilder(document.pages[1])
    # إنشاء مثيل لـ TextParagraph
    paragraph = ap.text.TextParagraph()
    # إنشاء مثيل لـ TextState لتحديد اسم الخط والحجم
    state = ap.text.TextState(12.0)
    state.font = ap.text.FontRepository.find_font("Arial")
    # تحديد تباعد الأحرف
    state.character_spacing = 1.5
    # إلحاق النص بكائن TextParagraph
    tt = "هذا فقرة مع تباعد الأحرف"
    paragraph.append_line(tt, state)
    # تحديد الموقع لـ TextParagraph
    paragraph.position = ap.text.Position(100, 550)
    # إلحاق TextParagraph بمثيل TextBuilder
    builder.append_paragraph(paragraph)
    # حفظ مستند PDF الناتج
    document.save(output_pdf)
```

### استخدام TextStamp

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إضافة صفحة إلى مجموعة الصفحات في المستند
    page = document.pages.add()
    # إنشاء مثيل لـ TextStamp مع نص عينة
    stamp = ap.TextStamp("هذا ختم نصي مع تباعد الأحرف")
    # تحديد اسم الخط لكائن الختم
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    # تحديد حجم الخط لـ TextStamp
    stamp.text_state.font_size = 12
    # تحديد تباعد الأحرف كرقم 1
    stamp.text_state.character_spacing = 1
    # تعيين x_indent للختم
    stamp.x_indent = 100
    # تعيين y_indent للختم
    stamp.y_indent = 500
    # إضافة ختم نصي إلى مثيل الصفحة
    stamp.put(page)
    # حفظ مستند PDF الناتج
    document.save(output_pdf)
```


## إنشاء مستند PDF بعمود متعدد

يوفر [Aspose.PDF for Python عبر .NET](https://docs.aspose.com/pdf/python-net/) أيضًا ميزة لإنشاء أعمدة متعددة داخل صفحات مستندات PDF. لإنشاء ملف PDF بعمود متعدد، يمكننا استخدام فئة FloatingBox لأنها توفر خاصية column_info لتحديد عدد الأعمدة داخل FloatingBox ويمكننا أيضًا تحديد التباعد بين الأعمدة وعرض الأعمدة باستخدام الخصائص column_spacing وwidth وفقًا لذلك.

يعني تباعد الأعمدة المسافة بين الأعمدة والتباعد الافتراضي بين الأعمدة هو 1.25 سم. إذا لم يتم تحديد عرض العمود، فإن [Aspose.PDF for Python عبر .NET](https://docs.aspose.com/pdf/python-net/) يحسب العرض لكل عمود تلقائيًا وفقًا لحجم الصفحة وتباعد الأعمدة.

يوضح المثال أدناه كيفية إنشاء عمودين باستخدام كائنات Graphs (Line) ويتم إضافتها إلى مجموعة الفقرات في FloatingBox، والتي تتم إضافتها بعد ذلك إلى مجموعة الفقرات في مثيل Page.

```python

    import aspose.pdf as ap

    document = ap.Document()
    # حدد معلومات الهامش الأيسر لملف PDF
    document.page_info.margin.left = 40
    # حدد معلومات الهامش الأيمن لملف PDF
    document.page_info.margin.right = 40
    page = document.pages.add()

    graph1 = ap.drawing.Graph(500, 2)
    # أضف الخط إلى مجموعة الفقرات في كائن القسم
    page.paragraphs.add(graph1)

    # حدد الإحداثيات للخط
    pos1 = [1.0, 2.0, 500.0, 2.0]
    l1 = ap.drawing.Line(pos1)
    graph1.shapes.append(l1)
    # إنشاء متغيرات نصية تحتوي على علامات HTML
    s = (
        '<font face="Times New Roman" size=4>'
        + "<strong> كيفية تجنب عمليات الاحتيال المالية</<strong> "
        + "</font>"
    )
    # إنشاء فقرات نصية تحتوي على نص HTML
    heading_text = ap.HtmlFragment(s)
    page.paragraphs.add(heading_text)

    box = ap.FloatingBox()
    # أضف أربعة أعمدة في القسم
    box.column_info.column_count = 2
    # تعيين المسافة بين الأعمدة
    box.column_info.column_spacing = "5"

    box.column_info.column_widths = "105 105"
    text1 = ap.text.TextFragment("بقلم أحد موظفي Google (المدونة الرسمية لـ Google)")
    text1.text_state.font_size = 8
    text1.text_state.line_spacing = 2
    box.paragraphs.add(text1)
    text1.text_state.font_size = 10

    text1.text_state.font_style = ap.text.FontStyles.ITALIC
    # إنشاء كائن الرسوم لرسم خط
    graph2 = ap.drawing.Graph(50, 10)
    # حدد الإحداثيات للخط
    pos2 = [1.0, 10.0, 100.0, 10.0]
    l2 = ap.drawing.Line(pos2)
    graph2.shapes.append(l2)

    # أضف الخط إلى مجموعة الفقرات في كائن القسم
    box.paragraphs.add(graph2)

    text2 = ap.text.TextFragment(
        "سيد اوج تورتور، سوداليس اي دي، لوكتوس ات، بلفينار اوت، ايروس. سوسبينديس فيل دولار. سيد كوام. كيورابيتور اوت ماسا فيتاي ايروس ايوسمود الكوام. بيلينتيسك سيت اميت اليت. فيستيبيولوم انديردوم بيلينتيسك اوج. كراس موليس اركو سيت اميت بوروس. دونيك اوج. نام موليس تورتور اليت. نولا فيفيرا نيسل فيل مورس. فيفاموس سابيين. ناسيتور ريديكلوس موس. نام جوستو لوريم، الكوام لوكتوس، سوداليس اي دي، سيمبر سيد، اينم نام جوستو لوريم، الكوام لوكتوس، سوداليس اي دي، نان ايان بوسير انت نيك. موربي سوليكيتودين كونغي فيليس. بريسنت تيربيس ديام، ايكوليس سيد، فاريترا نون، موليس اك، موريس. فاسيلوس نيسي ايبسم، بريتيوم فيتاي، تيمبور سيد، موليستي يو، دوي. دويس لاكوس بوروس، تريستيك يو، ايكوليس كورسوس، تينسينت فيتاي، ريسوس. سيد كومودو. *** سوسيس ناتوك بيناتيبوس ات ماجنس ديس بارتوريينت مونتيس، ناسيتور ريديكلوس موس. نام جوستو لوريم، الكوام لوكتوس، سوداليس اي دي، سيمبر سيد، اينم نام جوستو لوريم، الكوام لوكتوس، سوداليس اي دي، سيمبر سيد، اينم نام جوستو لوريم، الكوام لوكتوس، سوداليس اي دي، سيمبر سيد، اينم نان ايان بوسير انت نيك. موربي سوليكيتودين كونغي فيليس. بريسنت تيربيس ديام، ايكوليس سيد، فاريترا نون، موليس اك، موريس. فاسيلوس نيسي ايبسم، بريتيوم فيتاي، تيمبور سيد، موليستي يو، دوي. دويس لاكوس بوروس، تريستيك يو، ايكوليس كورسوس، تينسينت فيتاي، ريسوس. سيد كومودو. *** سوسيس ناتوك بيناتيبوس ات ماجنس ديس بارتوريينت مونتيس، ناسيتور ريديكلوس موس. سيد اورنا. . دويس كونفاليس التريس نيسي. ماكيناس نون ليجولا. ننك نيب ايست، تينسينت ان، بلاسيرات سيت اميت، فيستيبيولوم ا، نولا. بريسنت بورتتور تيربيس اليفند انت. موربي سوداليس. نان ايان بوسير انت نيك. موربي سوليكيتودين كونغي فيليس. بريسنت تيربيس ديام، ايكوليس سيد، فاريترا نون، موليس اك، موريس. فاسيلوس نيسي ايبسم، بريتيوم فيتاي، تيمبور سيد، موليستي يو، دوي. دويس لاكوس بوروس، تريستيك يو، ايكوليس كورسوس، تينسينت فيتاي، ريسوس. سيد كومودو. *** سوسيس ناتوك بيناتيبوس ات ماجنس ديس بارتوريينت مونتيس، ناسيتور ريديكلوس موس. سيد اورنا. . دويس كونفاليس التريس نيسي. ماكيناس نون ليجولا. ننك نيب ايست، تينسينت ان، بلاسيرات سيت اميت، فيستيبيولوم ا، نولا. بريسنت بورتتور تيربيس اليفند انت. موربي سوداليس."
    )
    box.paragraphs.add(text2)
    page.paragraphs.add(box)
    # حفظ ملف PDF
    document.save(output_pdf)
```


## العمل مع توقفات الجدولة المخصصة

يوضح مقتطف الكود التالي في بايثون كيفية إنشاء مستند PDF يحتوي على أجزاء نصية مرتبة باستخدام توقفات الجدولة لمحاكاة هيكل الجدول.

إليك مثال عن كيفية تعيين توقفات TAB مخصصة.

```python

    import aspose.pdf as ap

    document = ap.Document()
    page = document.pages.add()

    ts = ap.text.TabStops()
    ts1 = ts.add(100.0)
    ts1.alignment_type = ap.text.TabAlignmentType.RIGHT
    ts1.leader_type = ap.text.TabLeaderType.SOLID
    ts2 = ts.add(200.0)
    ts2.alignment_type = ap.text.TabAlignmentType.CENTER
    ts2.leader_type = ap.text.TabLeaderType.DASH
    ts3 = ts.add(300.0)
    ts3.alignment_type = ap.text.TabAlignmentType.LEFT
    ts3.leader_type = ap.text.TabLeaderType.DOT

    header = ap.text.TextFragment(
        "هذا مثال لتشكيل جدول مع توقفات TAB", ts
    )
    text0 = ap.text.TextFragment("#$TABHead1 #$TABHead2 #$TABHead3", ts)

    text1 = ap.text.TextFragment("#$TABdata11 #$TABdata12 #$TABdata13", ts)
    text2 = ap.text.TextFragment("#$TABdata21 ", ts)
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data22 "))
    text2.segments.append(ap.text.TextSegment("#$TAB"))
    text2.segments.append(ap.text.TextSegment("data23"))

    page.paragraphs.add(header)
    page.paragraphs.add(text0)
    page.paragraphs.add(text1)
    page.paragraphs.add(text2)

    document.save(output_pdf)
```


## كيفية إضافة نص شفاف في ملف PDF

يحتوي ملف PDF على كائنات مثل الصور والنصوص والرسوم والمرفقات والتعليقات التوضيحية، وعند إنشاء TextFragment يمكنك تحديد معلومات الألوان الأمامية والخلفية بالإضافة إلى تنسيق النص. يدعم Aspose.PDF for Python عبر .NET خاصية إضافة النصوص مع قناة لون ألفا.

يظهر مقطع الشيفرة التالي كيفية إضافة نص بلون شفاف.

```python

    import aspose.pdf as ap

    # إنشاء مثيل للمستند
    document = ap.Document()
    # إنشاء صفحة لمجموعة صفحات ملف PDF
    page = document.pages.add()

    # إنشاء مثيل TextFragment مع قيمة نموذجية
    text = ap.text.TextFragment(
        "transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text transparent text "
    )
    # إنشاء كائن لون من قناة ألفا
    color = ap.Color.from_argb(30, 0, 255, 0)
    # تعيين معلومات اللون لمثيل النص
    text.text_state.foreground_color = color
    # إضافة النص إلى مجموعة الفقرات لمثيل الصفحة
    page.paragraphs.add(text)

    document.save(output_pdf)
```


## تحديد تباعد الأسطر للخطوط

كل خط يحتوي على مربع تجريدي، والذي يمثل ارتفاعه المسافة المقصودة بين الأسطر في نفس حجم الخط. يسمى هذا المربع بالمربع em وهو شبكة التصميم التي يتم تعريف حدود الحروف عليها. العديد من حروف خط الإدخال تحتوي على نقاط تم وضعها خارج حدود مربع em للخط، لذا لعرض الخط بشكل صحيح، هناك حاجة لاستخدام إعداد خاص.

الشفرة التالية تقوم بتحميل ملف PDF، تضيف جزء نصي بتباعد أسطر محدد باستخدام خط TrueType، وتحفظ المستند المعدل:

```python

    import aspose.pdf as ap

    # تحميل ملف PDF الإدخال
    document = ap.Document()
    # إنشاء خيارات تنسيق النص مع LineSpacingMode.FULL_SIZE
    options = ap.text.TextFormattingOptions()
    options.line_spacing = ap.text.TextFormattingOptions.LineSpacingMode.FULL_SIZE

    # إنشاء جزء نصي مع جملة مثال
    text_fragment = ap.text.TextFragment("Hello world")

    # تحميل خط TrueType في كائن stream
    font_stream = open(input_ttf, "rb")
    # تعيين اسم الخط لسلسلة النص
    text_fragment.text_state.font = ap.text.FontRepository.open_font(
        font_stream, ap.text.FontTypes.TTF
    )
    # تحديد الموضع لجزء النص
    text_fragment.position = ap.text.Position(100, 600)
    # تعيين خيارات تنسيق النص للجزء الحالي إلى المحدد مسبقًا (الذي يشير إلى LineSpacingMode.FULL_SIZE)
    text_fragment.text_state.formatting_options = options
    page = document.pages.add()
    page.paragraphs.add(text_fragment)

    # حفظ مستند PDF الناتج
    document.save(output_pdf)
```


## الحصول على عرض النص ديناميكيًا

يقوم هذا المقتطف من كود بايثون بإجراء مقارنة بين قياسات السلاسل النصية التي يتم الحصول عليها من كائن الخط وكائن حالة النص في Aspose.PDF:

```python

    import math as ap

    font = ap.text.FontRepository.find_font("Arial")
    ts = ap.text.TextState()
    ts.font = font
    ts.font_size = 14

    if mt.fabs(font.measure_string("A", 14) - 9.337) > 0.001:
        print("قياس غير متوقع لسلسلة الخط!")

    if mt.fabs(ts.measure_string("z") - 7.0) > 0.001:
        print("قياس غير متوقع لسلسلة الخط!")

    c_code = ord("A")
    while c_code <= ord("z"):
        c = chr(c_code)

        fn_measure = font.measure_string(str(c), 14)
        ts_measure = ts.measure_string(str(c))

        print(str(c_code) + "-" + c + "-" + str(ts_measure))

        if mt.fabs(fn_measure - ts_measure) > 0.001:
            print("قياس سلسلة الخط وحالة النص لا يتطابقان!")

        c_code += 1
```

<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "SoftwareApplication",
    "name": "Aspose.PDF for Python via .NET Library",
    "image": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
    "url": "https://www.aspose.com/",
    "publisher": {
        "@type": "Organization",
        "name": "Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-net.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://www.youtube.com/channel/UCmV9sEg_QWYPi6BJJs7ELOg/featured",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "offers": {
        "@type": "Offer",
        "price": "1199",
        "priceCurrency": "USD"
    },
    "applicationCategory": "PDF Manipulation Library for .NET",
    "downloadUrl": "https://www.nuget.org/packages/Aspose.PDF/",
    "operatingSystem": "Windows, MacOS, Linux",
    "screenshot": "https://docs.aspose.com/pdf/python-net/create-pdf-document/screenshot.png",
    "softwareVersion": "2024.1",
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "5",
        "ratingCount": "16"
    }
}
</script>