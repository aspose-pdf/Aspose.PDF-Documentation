---
title: إضافة رؤوس وتذييلات PDF في Python
linktitle: إضافة رأس وتذييل الصفحة إلى PDF
type: docs
weight: 50
url: /ar/python-net/add-headers-and-footers-of-pdf-file/
description: تعرف على كيفية إضافة الرؤوس والتذييلات إلى ملفات PDF في Python باستخدام النصوص والصور والمحتوى المنظم.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف الرؤوس والتذييلات إلى ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية إضافة الرؤوس والتذييلات إلى مستندات PDF باستخدام Aspose.PDF لـ Python عبر .NET. وهو يغطي النص وترقيم الصفحات وHTML والصورة والجدول ومحتوى رأس الصفحة وتذييلها المستند إلى اللاتكس.
---

استخدم هذه الصفحة لإضافة محتوى متسق للرأس والتذييل عبر صفحات PDF باستخدام **Aspose.pdf لـ Python عبر .NET**.

يمكنك إنشاء رؤوس وتذييلات باستخدام [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/), [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/), [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/), [`Image`](https://reference.aspose.com/pdf/python-net/aspose.pdf/image/)، و [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) الكائنات، ثم قم بتطبيقها من خلال [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) في كل صفحة.

## إضافة الرؤوس والتذييلات كأجزاء نصية

أضف رؤوس وتذييلات نصية بسيطة إلى جميع الصفحات في PDF. إنه يخلق [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) الكائنات والإدخالات [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textfragment/) عناصر فيها، مجموعات [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) لتحديد الموضع المناسب، وإرفاقها بكل صفحة في المستند. والنتيجة هي ملف PDF حيث تعرض كل صفحة نصًا ثابتًا لرأس وتذييل الصفحة.

يوضح مقتطف الشفرة التالي كيفية إضافة الرؤوس والتذييلات كأجزاء نصية في PDF باستخدام Python:

1. قم بإنشاء أجزاء نصية لرأس الصفحة وتذييلها.
1. قم بإنشاء كائنات HeaderFooter وإضافة أجزاء النص إليها.
1. حدد إعدادات الهامش للتحكم في موضع رأس الصفحة وتذييلها.
1. قم بتحميل وثيقة PDF من ملف الإدخال.
1. قم بالتكرار من خلال جميع الصفحات في المستند.
1. قم بتعيين رأس الصفحة وتذييلها لكل صفحة.
1. احفظ ملف PDF المعدل في ملف الإخراج.

```python
import aspose.pdf as ap

def add_header_and_footer_as_text(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Demo header")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Demo footer")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

هذه الطريقة مفيدة لإضافة عناوين متسقة أو مؤشرات الصفحات أو إخلاء المسؤولية القانونية في أعلى وأسفل كل صفحة. يمكنك أيضًا توسيعه ليشمل الصور أو المحتوى الديناميكي، مثل أرقام الصفحات.

## إضافة رؤوس وتذييلات لترقيم الصفحات

أضف ترقيمًا تلقائيًا للصفحات إلى رؤوس وتذييلات مستند PDF باستخدام Aspose.PDF لـ Python. باستخدام المتغيرات المضمنة $p (رقم الصفحة الحالية) و $P (إجمالي عدد الصفحات)، يقوم البرنامج النصي بإدراج ترقيم الصفحات ديناميكيًا في كل صفحة. تعرض العناوين التنسيق «صفحة X من Y»، بينما تعرض التذييلات «الصفحة X/Y». ال [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) يضمن الموضع المناسب في كل صفحة.

1. قم بإنشاء TextFragment للرأس باستخدام «صفحة $p من $P» لعرض الصفحات الحالية والإجمالية.
1. قم بإنشاء كائن HeaderFooter وأضف نص الرأس إليه.
1. قم بإنشاء TextFragment للتذييل باستخدام «الصفحة $p/$P» لنمط ترقيم بديل.
1. قم بإنشاء كائن تذييل وأضف نص التذييل.
1. حدد إعدادات الهامش (اليسار = 50، الجزء العلوي = 20) وقم بتطبيقها على كل من رأس الصفحة وتذييلها.
1. افتح مستند PDF من ملف الإدخال.
1. قم بالتمرير عبر جميع الصفحات وقم بتعيين رأس وتذييل الصفحة لكل صفحة.
1. احفظ ملف PDF المحدث في مسار الإخراج.

```python
import aspose.pdf as ap

def using_header_and_footer_for_page_numbering(input_file, output_file):
    # Create header text
    header_text = ap.text.TextFragment("Page $p from $P")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_text)

    # Create footer text
    footer_text = ap.text.TextFragment("Page $p / $P")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_text)

    # Create margins
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20

    # Set header margin
    header.margin = margin
    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## إضافة رؤوس وتذييلات كأجزاء HTML

قم بتطبيق الرؤوس والتذييلات بتنسيق HTML على كل صفحة من مستند PDF باستخدام Aspose.PDF لـ Python. باستخدام [`HtmlFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/htmlfragment/)، يتيح البرنامج النصي ظهور نمط النص الغني - مثل الخط العريض والمائل - في رأس الصفحة وتذييلها. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) يتم تطبيقه على الموضع المناسب، ويتم إرفاق نفس العناصر المنسقة بكل صفحة في المستند.

يوضح مقتطف الشفرة التالي كيفية إضافة الرؤوس والتذييلات كأجزاء HTML إلى PDF باستخدام Python:

1. قم بإنشاء مقتطف رأس HTML باستخدام HtmlFragment - بما في ذلك النص المصمم مثل '<strong>'للبنط العريض.
1. قم بإنشاء كائن HeaderFooter وأضف رأس HTML إليه.
1. قم بإنشاء مقتطف تذييل HTML باستخدام '<i>'للتصميم المائل.
1. قم بإنشاء كائن تذييل وأضف تذييل HTML إليه.
1. قم بتكوين الهوامش (اليسار = 50، الجزء العلوي = 20) وقم بتعيينها لكل من الرأس والتذييل.
1. قم بتحميل مستند PDF باستخدام «AP.document ()».
1. قم بالتمرير عبر جميع الصفحات وقم بتعيين رأس الصفحة وتذييلها لكل منها.
1. احفظ ملف PDF المعدل إلى مسار الإخراج المحدد.

```python
import aspose.pdf as ap

def add_header_and_footer_as_html(input_file, output_file):
    # Create header HTML
    header_html = ap.HtmlFragment("This is an HTML <strong>Header</strong>")
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_html)

    # Create footer HTML
    footer_html = ap.HtmlFragment("Powered by <i>Aspose.PDF</i>")

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_html)

    # Set header margin
    margin = ap.MarginInfo()
    margin.left = 50
    margin.top = 20
    header.margin = margin

    # Set footer margin
    footer.margin = margin

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

يتيح استخدام HTMLFragment التنسيق الغني باستخدام الأنماط المضمنة أو ترميز HTML، مما يمنحك المزيد من مرونة التصميم مقارنة بالنص العادي.

## إضافة رؤوس وتذييلات كصور

أضف الرؤوس والتذييلات المستندة إلى الصور إلى كل صفحة من وثيقة PDF باستخدام Aspose.PDF لـ Python. يتم استخدام نفس ملف الصورة لكل من رأس الصفحة وتذييلها في كل صفحة. [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) يضع الصور، ويتم ضبط الصورة تلقائيًا لتناسب منطقة الرأس/التذييل.

يوضح مقتطف الشفرة التالي كيفية إضافة الرؤوس والتذييلات كصور إلى PDF باستخدام Python:

1. قم بتحميل الصورة إلى كائن «AP.image» وقم بإعدادها للاستخدام كرأس.
1. قم بإنشاء كائن HeaderFooter وإرفاق صورة الرأس به.
1. قم بتحميل نفس الصورة مرة أخرى لاستخدامها كتذييل.
1. قم بإنشاء كائن تذييل وأضف صورة التذييل إليه.
1. قم بتحميل مستند PDF الذي تم إدخاله باستخدام «AP.document ()».
1. قم بالتكرار من خلال جميع صفحات المستند.
1. قم بتطبيق الهوامش (اليسار = 50) لوضع كل من الرأس والتذييل.
1. قم بتعيين رأس وتذييل الصفحة لكل صفحة في PDF.
1. احفظ ملف PDF المحدث إلى ملف الإخراج المحدد.

هذه التقنية مثالية لوضع العلامات التجارية للمستندات التي تحتوي على شعارات أو علامات مائية في منطقة الرأس/التذييل.

```python
import aspose.pdf as ap

def add_header_and_footer_as_image(input_file, image_file, output_file):
    # Create header image
    header_image = ap.Image()
    header_image.file = image_file
    # Create header
    header = ap.HeaderFooter()
    header.paragraphs.add(header_image)

    # Create footer image
    footer_image = ap.Image()
    footer_image.file = image_file

    # Create footer
    footer = ap.HeaderFooter()
    footer.paragraphs.add(footer_image)

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Set header margin
            margin = ap.MarginInfo()
            margin.left = 50
            header.margin = margin

            # Set footer margin
            footer.margin = margin

            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## إضافة رؤوس وتذييلات كجدول

أضف رؤوس وتذييلات منظمة قائمة على الجدول إلى جميع صفحات مستند PDF باستخدام Aspose.PDF لـ Python. [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) توفر الكائنات تحكمًا أفضل في التخطيط والمحاذاة والتنسيق المتسق للرؤوس والتذييلات المعقدة. يتم توسيط نص الرأس بينما يتم محاذاة نص التذييل إلى اليسار، وكلاهما يستخدم خط Arial 12pt. يتم حساب عرض الأعمدة ديناميكيًا استنادًا إلى أبعاد الصفحة لضمان الموضع المناسب.

يضيف مقتطف الشفرة هذا الرؤوس والتذييلات (باستخدام الجداول) إلى كل صفحة من مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET.

1. تعريف أنماط النص باستخدام [`TextState`](https://reference.aspose.com/pdf/python-net/aspose.pdf/textstate/) لرأس الصفحة وتذييلها (الخط والحجم والمحاذاة).
1. ابتكر [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) كائنات لرأس الصفحة وتذييلها.
1. قم ببناء العنوان [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) مع صف واحد وخلية تحتوي على نص العنوان.
1. قم ببناء التذييل [`Table`](https://reference.aspose.com/pdf/python-net/aspose.pdf/table/) مع صف واحد وخلية تحتوي على نص التذييل.
1. أضف الجداول إلى المقابلة [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) الكائنات.
1. تعيين تذييل الصفحة [`MarginInfo`](https://reference.aspose.com/pdf/python-net/aspose.pdf/margininfo/) لتحديد المواقع الأفقية المناسبة.
1. افتح [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الطرق المناسبة.
1. قم بالتكرار في جميع الصفحات وقم بتعيين رأس وتذييل المستند إلى الجدول لكل صفحة.
1. احفظ التعديل [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى ملف الإخراج.

```python
import aspose.pdf as ap

def add_header_and_footer_as_table(input_file, output_file):
    text_state_header = ap.text.TextState()
    text_state_header.font = ap.text.FontRepository.find_font("Arial")
    text_state_header.font_size = 12
    text_state_header.horizontal_alignment = ap.HorizontalAlignment.CENTER
    text_state_footer = ap.text.TextState()
    text_state_footer.font = ap.text.FontRepository.find_font("Arial")
    text_state_footer.font_size = 12
    text_state_footer.horizontal_alignment = ap.HorizontalAlignment.LEFT
    # Create header
    header = ap.HeaderFooter()
    # Create footer
    footer = ap.HeaderFooter()
    # Create header Table
    table_header = ap.Table()
    table_header.column_widths = str(594 - header.margin.left - header.margin.right)
    header_row = table_header.rows.add()
    header_row.cells.add("This is a Table Header", text_state_header)
    # Create footer Table
    table = ap.Table()
    table.column_widths = str(594 - footer.margin.left - footer.margin.right)
    table.rows.add().cells.add("Powered by Aspose.PDF", text_state_footer)
    header.paragraphs.add(table_header)
    footer.paragraphs.add(table)
    # Set footer margin
    footer.margin.left = 150

    # Open PDF document
    with ap.Document(input_file) as document:
        for i in range(1, len(document.pages) + 1):
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## إضافة رؤوس وتذييلات كـ LaTeX

أضف الرؤوس والتذييلات التي تحتوي على محتوى بتنسيق Latex إلى جميع صفحات مستند PDF باستخدام Aspose.PDF لـ Python. يسمح LaTeX بعرض الرموز الرياضية والتواريخ وعلامات حقوق النشر والتنسيقات المتقدمة الأخرى. يتضمن العنوان تاريخًا ديناميكيًا، بينما يعرض التذييل رمز حقوق الطبع والنشر إلى جانب رقم الصفحة الحالية وإجمالي عدد الصفحات.

يوضح مقتطف الشفرة التالي كيفية الاستخدام [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) في الرؤوس والتذييلات لملف PDF باستخدام Aspose.PDF لبيثون عبر .NET.

1. افتح [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) باستخدام الطرق المناسبة.
1. حدد إجمالي عدد الصفحات لاستخدامها في التذييلات الديناميكية.
1. قم بالتكرار من خلال جميع صفحات المستند.
1. قم بإنشاء [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) كائن للرأس.
1. قم بإنشاء [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) لنص العنوان الذي يحتوي على أوامر LaTeX (على سبيل المثال، `\\today\\`).
1. قم بإنشاء [`HeaderFooter`](https://reference.aspose.com/pdf/python-net/aspose.pdf/headerfooter/) كائن للتذييل.
1. قم بإنشاء [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) لنص التذييل بما في ذلك رموز LaTeX وترقيم الصفحات.
1. أضف [`TeXFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf/texfragment/) إلى كائن الرأس/التذييل المقابل.
1. اربط رأس الصفحة وتذييلها بالصفحة الحالية.
1. احفظ التعديل [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) إلى ملف الإخراج.

```python
import aspose.pdf as ap

def add_header_and_footer_as_latex(input_file, output_file):
    # Open PDF document
    with ap.Document(input_file) as document:
        page_count = len(document.pages)
        for i in range(1, page_count + 1):
            # Create header
            header = ap.HeaderFooter()
            h_latex_text = "This is a LaTeX Header. \\today\\"
            h_l_text = ap.TeXFragment(h_latex_text, True)
            # Create footer
            footer = ap.HeaderFooter()
            f_latex_text = (
                f"\\copyright\\ 2025 My Company -- Page \\thepage\\ is {page_count}"
            )
            f_l_text = ap.TeXFragment(f_latex_text, True)

            header.paragraphs.add(h_l_text)
            footer.paragraphs.add(f_l_text)
            # Bind the header and footer to the page
            document.pages[i].header = header
            document.pages[i].footer = footer

        # Save PDF document
        document.save(output_file)
```

## موضوعات الصفحة ذات الصلة

- [العمل مع صفحات PDF في بايثون](/pdf/ar/python-net/working-with-pages/)
- [إضافة أرقام الصفحات إلى PDF في Python](/pdf/ar/python-net/add-page-number/)
- [ختم صفحات PDF في بايثون](/pdf/ar/python-net/stamping/)
- [تنسيق مستندات PDF في بايثون](/pdf/ar/python-net/formatting-pdf-document/)