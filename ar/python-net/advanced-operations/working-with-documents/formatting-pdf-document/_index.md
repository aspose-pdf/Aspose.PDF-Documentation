---
title: تنسيق مستندات PDF في بايثون
linktitle: تنسيق مستند PDF
type: docs
weight: 11
url: /ar/python-net/formatting-pdf-document/
description: تعرف على كيفية تنسيق مستندات PDF وتضمين الخطوط والتحكم في إعدادات العارض وضبط خيارات العرض في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تنسيق مستندات PDF باستخدام Python
Abstract: توفر المقالة دليلًا شاملاً حول معالجة مستندات PDF وتنسيقها باستخدام مكتبة Aspose.PDF في Python. ويغطي جوانب مختلفة من تخصيص PDF، بما في ذلك إعداد نافذة المستند وخصائص عرض الصفحة مثل توسيط النافذة واتجاه القراءة وإخفاء عناصر واجهة المستخدم. توضح المقالة كيفية استرداد هذه الخصائص وتعيينها برمجيًا باستخدام فئة «المستند». بالإضافة إلى ذلك، فإنه يتناول إدارة الخطوط، ويوضح بالتفصيل كيفية تضمين خطوط Standard Type 1 والخطوط الأخرى في ملفات PDF، مما يضمن قابلية نقل المستندات والاتساق المرئي عبر الأنظمة. كما يسلط الضوء على تقنيات تعيين اسم الخط الافتراضي، واسترداد جميع الخطوط من ملف PDF، وتعزيز تضمين الخط باستخدام `FontSubsetStrategy`. علاوة على ذلك، توضح المقالة تعديل عامل التكبير لمستندات PDF باستخدام فئة «GoToAction» وتكوين خصائص الإعداد المسبق لمربع حوار الطباعة، بما في ذلك خيارات الطباعة على الوجهين. ترافق مقتطفات التعليمات البرمجية كل قسم، وتقدم أمثلة عملية لتنفيذ هذه الميزات.
---

هذا الدليل مفيد عندما تحتاج إلى التحكم في سلوك عارض PDF أو تضمين الخط أو إعدادات العرض الافتراضية أو تفضيلات الطباعة في المستندات التي تم إنشاؤها بواسطة Python.

## تنسيق مستند PDF

### احصل على خصائص نافذة المستند وعرض الصفحة

يساعدك هذا الموضوع على فهم كيفية الحصول على خصائص نافذة المستند وتطبيق العارض وكيفية عرض الصفحات. لتعيين هذه الخصائص:

افتح ملف PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة. الآن، يمكنك تعيين خصائص كائن المستند، مثل

- CenterWindow - قم بتوسيط نافذة المستند على الشاشة. الإعداد الافتراضي: خطأ.
- الاتجاه - ترتيب القراءة. يحدد هذا كيفية تخطيط الصفحات عند عرضها جنبًا إلى جنب. الإعداد الافتراضي: من اليسار إلى اليمين.
- DisplayDocTitle - عرض عنوان المستند في شريط عنوان نافذة المستند. الإعداد الافتراضي: خطأ (يتم عرض العنوان).
- HideMenuBar - إخفاء أو عرض شريط قوائم نافذة المستند. الإعداد الافتراضي: خطأ (يتم عرض شريط القوائم).
- HideToolbar - إخفاء شريط أدوات نافذة المستند أو عرضه. الإعداد الافتراضي: خطأ (يتم عرض شريط الأدوات).
- HideWindowUI - إخفاء أو عرض عناصر نافذة المستند مثل أشرطة التمرير. الإعداد الافتراضي: خطأ (يتم عرض عناصر واجهة المستخدم).
- NonFullScreenPageMode - كيفية عرض المستند عندما لا يتم عرضه في وضع الصفحة الكاملة.
- PageLayout - تخطيط الصفحة.
- PageMode - كيفية عرض المستند عند فتحه لأول مرة. الخيارات هي عرض الصور المصغرة، ملء الشاشة، عرض لوحة المرفقات.

يوضح لك مقتطف الشفرة التالي كيفية الحصول على الخصائص باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.

```python
import aspose.pdf as ap


def get_document_window(input_pdf, output_pdf):
    """Print document window metadata for inspection."""
    document = ap.Document(input_pdf)

    print("CenterWindow:", document.center_window)
    print("Direction:", document.direction)
    print("DisplayDocTitle:", document.display_doc_title)
    print("FitWindow:", document.fit_window)
    print("HideMenuBar:", document.hide_menubar)
    print("HideToolBar:", document.hide_tool_bar)
    print("HideWindowUI:", document.hide_window_ui)
    print("NonFullScreenPageMode:", document.non_full_screen_page_mode)
    print("PageLayout:", document.page_layout)
    print("PageMode:", document.page_mode)
```

### تعيين نافذة الوثيقة وخصائص عرض الصفحة

يشرح هذا الموضوع كيفية تعيين خصائص نافذة المستند وتطبيق العارض وعرض الصفحة. لتعيين هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.
1. قم بتعيين خصائص كائن المستند.
1. احفظ ملف PDF المحدث باستخدام طريقة الحفظ.

الخصائص المتاحة هي:

- النافذة المركزية
- اتجاه
- عنوان المستند المعروض
- فيت واندو
- إخفاء شريط القوائم
- إخفاء شريط الأدوات
- إخفاء واجهة المستخدم الخاصة بنافود
- وضع صفحة الشاشة غير الكاملة
- تخطيط الصفحة
- وضع الصفحة

يتم استخدام كل منها ووصفها في الكود أدناه. يوضح لك مقتطف الشفرة التالي كيفية تعيين الخصائص باستخدام [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة.

```python
import aspose.pdf as ap


def set_document_window(input_pdf, output_pdf):
    """Set document window properties and save the result."""
    document = ap.Document(input_pdf)

    document.center_window = True
    document.direction = ap.Direction.R2L
    document.display_doc_title = True
    document.fit_window = True
    document.hide_menubar = True
    document.hide_tool_bar = True
    document.hide_window_ui = True
    document.non_full_screen_page_mode = ap.PageMode.USE_OC
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT
    document.page_mode = ap.PageMode.USE_THUMBS

    document.save(output_pdf)
```

### تضمين الخطوط القياسية من النوع 1

تحتوي بعض مستندات PDF على خطوط من مجموعة خطوط Adobe خاصة. تسمى الخطوط من هذه المجموعة «الخطوط القياسية من النوع الأول». تتضمن هذه المجموعة 14 خطًا ويتطلب تضمين هذا النوع من الخطوط استخدام علامات خاصة على سبيل المثال [تضمين الخطوط القياسية](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). فيما يلي مقتطف الشفرة الذي يمكن استخدامه للحصول على مستند يحتوي على جميع الخطوط المضمنة بما في ذلك الخطوط القياسية من النوع 1:

```python
import aspose.pdf as ap


def embedded_fonts(input_pdf, output_pdf):
    """Ensure fonts in an existing PDF are embedded."""
    document = ap.Document(input_pdf)
    document.embed_standard_fonts = True

    for page in document.pages:
        if page.resources.fonts:
            for page_font in page.resources.fonts:
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### تضمين الخطوط أثناء إنشاء PDF

إذا كنت بحاجة إلى استخدام أي خط بخلاف الخطوط الأساسية الأربعة عشر التي يدعمها Adobe Reader، فيجب عليك تضمين وصف الخط أثناء إنشاء ملف PDF. إذا لم تكن معلومات الخط مضمنة، فسيقوم Adobe Reader بأخذها من نظام التشغيل إذا تم تثبيتها على النظام، أو سيقوم بإنشاء خط بديل وفقًا لوصف الخط في PDF.

>يرجى ملاحظة أنه يجب تثبيت الخط المضمن على الجهاز المضيف، أي في حالة الكود التالي، يتم تثبيت خط «Univers Condensed» على النظام.

نحن نستخدم الخاصية 'is_embedded' لتضمين معلومات الخط في ملف PDF. سيؤدي تعيين قيمة هذه الخاصية إلى «True» إلى تضمين ملف الخط الكامل في PDF، مع العلم أنه سيزيد حجم ملف PDF. فيما يلي مقتطف الشفرة الذي يمكن استخدامه لتضمين معلومات الخط في PDF.

```python
import aspose.pdf as ap


def embedded_fonts_in_new_document(input_pdf, output_pdf):
    """Embed fonts while generating a document from scratch."""
    document = ap.Document()
    page = document.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    text_state = ap.text.TextState()
    text_state.font = ap.text.FontRepository.find_font("Arial")
    text_state.font.is_embedded = True
    segment.text_state = text_state
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    document.save(output_pdf)
```

### قم بتعيين اسم الخط الافتراضي أثناء حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه وعلى الجهاز، تستبدل API هذه الخطوط بالخط الافتراضي. إذا كان الخط متاحًا (مثبتًا على الجهاز أو مضمنًا في المستند)، فيجب أن يكون ملف PDF الناتج بنفس الخط (يجب عدم استبداله بالخط الافتراضي). يجب أن تحتوي قيمة الخط الافتراضي على اسم الخط (وليس المسار إلى ملفات الخطوط). لقد قمنا بتطبيق ميزة لتعيين اسم الخط الافتراضي أثناء حفظ مستند كملف PDF. يمكن استخدام مقتطف الشفرة التالي لتعيين الخط الافتراضي:

```python
import aspose.pdf as ap


def set_default_font(input_pdf, output_pdf):
    """Assign a fallback font when saving a PDF."""
    document = ap.Document(input_pdf)

    save_options = ap.PdfSaveOptions()
    save_options.default_font_name = "Arial"
    document.save(output_pdf, save_options)
```

### احصل على جميع الخطوط من مستند PDF

في حالة رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدامها [أدوات الخط](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) الطريقة المقدمة في [مستند](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) فئة. يرجى التحقق من مقتطف الشفرة التالي للحصول على جميع الخطوط من مستند PDF موجود:

```python
import aspose.pdf as ap


def get_all_fonts(input_pdf, output_pdf):
    """Print all fonts referenced by a document."""
    document = ap.Document(input_pdf)
    for font in document.font_utilities.get_all_fonts():
        print(font.font_name)
```

### تحسين تضمين الخطوط باستخدام FontSubsetStrategy

يوضح مقتطف الشفرة التالي كيفية التعيين [إستراتيجية المجموعة الفرعية للخطوط](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) استعمل [أدوات الخط](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) الملكية:

```python
import aspose.pdf as ap


def improve_fonts_embedding(input_pdf, output_pdf):
    """Apply different font subset strategies to reduce file size."""
    document = ap.Document(input_pdf)

    document.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    document.font_utilities.subset_fonts(
        ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY
    )

    document.save(output_pdf)
```

### احصل على عامل تكبير لملف PDF

في بعض الأحيان، تريد تحديد عامل التكبير الحالي لمستند PDF. باستخدام Aspose.Pdf، يمكنك معرفة القيمة الحالية بالإضافة إلى تعيين واحدة.

ال [انتقل إلى العمل](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) تسمح لك خاصية class Destination بالحصول على قيمة التكبير/التصغير المرتبطة بملف PDF. وبالمثل، يمكن استخدامه لتعيين عامل تكبير الملف.

#### ضبط عامل الزوم

يوضح مقتطف الشفرة التالي كيفية تعيين عامل التكبير لملف PDF.

```python
import aspose.pdf as ap


def set_zoom_factor(input_pdf, output_pdf):
    """Set an initial zoom level via document open action."""
    document = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(
        ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5)
    )
    document.open_action = action
    document.save(output_pdf)
```

#### احصل على زوم فاكتور

يوضح مقتطف الشفرة التالي كيفية الحصول على عامل تكبير ملف PDF.

```python
import aspose.pdf as ap


def get_zoom_factor(input_pdf, output_pdf):
    """Print the zoom level configured in the document open action."""
    document = ap.Document(input_pdf)

    action = document.open_action
    if action and action.destination:
        print("Zoom:", action.destination.zoom)
    else:
        print("Zoom: not set")
```

## موضوعات المستندات ذات الصلة

- [العمل مع مستندات PDF في بايثون](/pdf/ar/python-net/working-with-documents/)
- [إنشاء ملفات PDF في بايثون](/pdf/ar/python-net/create-pdf-document/)
- [معالجة مستندات PDF في Python](/pdf/ar/python-net/manipulate-pdf-document/)
- [تحسين ملفات PDF في بايثون](/pdf/ar/python-net/optimize-pdf/)
