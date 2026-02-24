---
title: تنسيق مستند PDF باستخدام بايثون
linktitle: تنسيق مستند PDF
type: docs
weight: 11
url: /ar/python-net/formatting-pdf-document/
description: إنشاء وتنسيق مستند PDF باستخدام Aspose.PDF لبايثون عبر .NET. استخدم مقتطف الشيفرة التالي لحل مهامك.
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: تنسيق مستندات PDF باستخدام بايثون
Abstract: توفر المقالة دليلًا شاملاً حول معالجة وتنسيق مستندات PDF باستخدام مكتبة Aspose.PDF في بايثون. تغطي جوانب مختلفة من تخصيص PDF، بما في ذلك ضبط نافذة المستند وخصائص عرض الصفحات مثل توسيط النافذة، واتجاه القراءة، وإخفاء عناصر واجهة المستخدم. تشرح المقالة كيفية استرجاع وتعيين هذه الخصائص برمجيًا باستخدام فئة `Document`. بالإضافة إلى ذلك، تتناول إدارة الخطوط، موضحةً كيفية تضمين خطوط Standard Type 1 وغيرها من الخطوط في ملفات PDF، مما يضمن قابلية نقل المستند وتناسق المظهر عبر الأنظمة. كما تسلط الضوء على تقنيات تحديد اسم الخط الافتراضي، واسترجاع جميع الخطوط من PDF، وتعزيز تضمين الخطوط باستخدام `FontSubsetStrategy`. علاوة على ذلك، تتعمق المقالة في ضبط عامل التكبير لوثائق PDF باستخدام فئة `GoToAction` وتكوين خصائص حوار الطباعة المسبق، بما في ذلك خيارات الطباعة المزدوجة. ترافق مقتطفات الشيفرة كل قسم، مقدمة أمثلة عملية لتطبيق هذه الميزات.
---

## تنسيق مستند PDF

### الحصول على خصائص نافذة المستند وعرض الصفحة

يساعدك هذا الموضوع على فهم كيفية الحصول على خصائص نافذة المستند، وتطبيق العارض، وكيفية عرض الصفحات. لتعيين هذه الخصائص:

افتح ملف PDF باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) . الآن، يمكنك تعيين خصائص كائن Document، مثل

- CenterWindow – توسيط نافذة المستند على الشاشة. الافتراضي: false.
- Direction – ترتيب القراءة. يحدد هذا كيفية تنظيم الصفحات عندما تُعرض جنبًا إلى جنب. الافتراضي: من اليسار إلى اليمين.
- DisplayDocTitle – عرض عنوان المستند في شريط عنوان نافذة المستند. الافتراضي: false (يتم عرض العنوان).
- HideMenuBar – إخفاء أو عرض شريط قوائم نافذة المستند. الافتراضي: false (يتم عرض شريط القوائم).
- HideToolBar – إخفاء أو عرض شريط الأدوات في نافذة المستند. الافتراضي: false (يتم عرض شريط الأدوات).
- HideWindowUI – إخفاء أو عرض عناصر واجهة نافذة المستند مثل أشرطة التمرير. الافتراضي: false (يتم عرض عناصر الواجهة).
- NonFullScreenPageMode – طريقة عرض المستند عندما لا يكون في وضع ملء الشاشة.
- PageLayout – تخطيط الصفحة.
- PageMode – طريقة عرض المستند عند فتحه لأول مرة. الخيارات هي عرض المصغرات، ملء الشاشة، عرض لوحة المرفقات.

يعرض مقتطف الشيفرة التالي كيفية الحصول على الخصائص باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Get different document properties
    # Position of document's window - Default: false
    print("CenterWindow :", document.center_window)

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    print("Direction :", document.direction)

    # Whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    print("DisplayDocTitle :", document.display_doc_title)

    # Whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    print("FitWindow :", document.fit_window)

    # Whether to hide menu bar of the viewer application - Default: false
    print("HideMenuBar :", document.hide_menubar)

    # Whether to hide tool bar of the viewer application - Default: false
    print("HideToolBar :", document.hide_tool_bar)

    # Whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    print("HideWindowUI :", document.hide_window_ui)

    # Document's page mode. How to display document on exiting full-screen mode.
    print("NonFullScreenPageMode :", document.non_full_screen_page_mode)

    # The page layout i.e. single page, one column
    print("PageLayout :", document.page_layout)

    # How the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    print("pageMode :", document.page_mode)

```

### تعيين خصائص نافذة المستند وعرض الصفحة

يشرح هذا الموضوع كيفية تعيين خصائص نافذة المستند، وتطبيق العارض، وعرض الصفحة. لتعيين هذه الخصائص المختلفة:

1. افتح ملف PDF باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .
1. عيّن خصائص كائن Document.
1. احفظ ملف PDF المحدث باستخدام طريقة الحفظ.

الخصائص المتاحة هي:

- CenterWindow
- Direction
- DisplayDocTitle
- FitWindow
- HideMenuBar
- HideToolBar
- HideWindowUI
- NonFullScreenPageMode
- PageLayout
- PageMode

يتم استخدام كل منها ووصفه في الشيفرة أدناه. يوضح مقتطف الشيفرة التالي كيفية تعيين الخصائص باستخدام الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) .

```python

    import aspose.pdf as ap

    # Open document
    document = ap.Document(input_pdf)

    # Set different document properties
    # Sepcify to position document's window - Default: false
    document.center_window = True

    # Predominant reading order; determins the position of page
    # When displayed side by side - Default: L2R
    document.direction = ap.Direction.R2L

    # Specify whether window's title bar should display document title
    # If false, title bar displays PDF file name - Default: false
    document.display_doc_title = True

    # Specify whether to resize the document's window to fit the size of
    # First displayed page - Default: false
    document.fit_window = True

    # Specify whether to hide menu bar of the viewer application - Default: false
    document.hide_menubar = True

    # Specify whether to hide tool bar of the viewer application - Default: false
    document.hide_tool_bar = True

    # Specify whether to hide UI elements like scroll bars
    # And leaving only the page contents displayed - Default: false
    document.hide_window_ui = True

    # Document's page mode. specify how to display document on exiting full-screen mode.
    document.non_full_screen_page_mode = ap.PageMode.USE_OC

    # Specify the page layout i.e. single page, one column
    document.page_layout = ap.PageLayout.TWO_COLUMN_LEFT

    # Specify how the document should display when opened
    # I.e. show thumbnails, full-screen, show attachment panel
    document.page_mode = ap.PageMode.USE_THUMBS

    # Save updated PDF file
    document.save(output_pdf)
```

### تضمين خطوط Standard Type 1

بعض مستندات PDF تحتوي على خطوط من مجموعة خطوط Adobe الخاصة. تُسمى الخطوط في هذه المجموعة “Standard Type 1 Fonts”. تشمل هذه المجموعة 14 خطًا وتضمين هذا النوع من الخطوط يتطلب استخدام أعلام خاصة مثل [embed_standard_fonts](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties). المقتطف التالي يمكن استخدامه للحصول على مستند مع جميع الخطوط مضمنة بما في ذلك خطوط Standard Type 1:

```python

    import aspose.pdf as ap

    # Load an existing PDF Document
    document = ap.Document(input_pdf)
    # Set EmbedStandardFonts property of document
    document.embed_standard_fonts = True
    for page in document.pages:
        if page.resources.fonts != None:
            for page_font in page.resources.fonts:
                # Check if font is already embedded
                if not page_font.is_embedded:
                    page_font.is_embedded = True

    document.save(output_pdf)
```

### تضمين الخطوط أثناء إنشاء PDF

إذا كنت بحاجة لاستخدام أي خط غير الخطوط الأساسية الـ 14 التي يدعمها Adobe Reader، يجب تضمين وصف الخط أثناء إنشاء ملف PDF. إذا لم يتم تضمين معلومات الخط، سيأخذ Adobe Reader الخط من نظام التشغيل إذا كان مثبتًا على النظام، أو سيُنشئ خطًا بديلًا وفقًا لوصف الخط في PDF.

> يرجى ملاحظة أنه يجب تثبيت الخط المضمن على الجهاز المضيف، أي في حالة الكود التالي تم تثبيت خط ‘Univers Condensed’ على النظام.

نستخدم الخاصية 'is_embedded' لتضمين معلومات الخط في ملف PDF. ضبط قيمة هذه الخاصية إلى 'True' سيضمّن ملف الخط بالكامل في PDF، مع العلم أن ذلك سيزيد من حجم ملف PDF. المقتطف التالي يمكن استخدامه لتضمين معلومات الخط في PDF.

```python

    import aspose.pdf as ap

    # Instantiate Pdf object by calling its empty constructor
    doc = ap.Document()

    # Create a section in the Pdf object
    page = doc.pages.add()

    fragment = ap.text.TextFragment("")
    segment = ap.text.TextSegment(" This is a sample text using Custom font.")
    ts = ap.text.TextState()
    ts.font = ap.text.FontRepository.find_font("Arial")
    ts.font.is_embedded = True
    segment.text_state = ts
    fragment.segments.append(segment)
    page.paragraphs.add(fragment)

    # Save PDF Document
    doc.save(output_pdf)
```

### تعيين اسم الخط الافتراضي أثناء حفظ PDF

عندما يحتوي مستند PDF على خطوط غير متوفرة في المستند نفسه ولا على الجهاز، تقوم API باستبدال هذه الخطوط بالخط الافتراضي. إذا كان الخط متاحًا (مثبتًا على الجهاز أو مدمجًا في المستند)، يجب أن يكون ملف PDF الناتج بنفس الخط (يجب ألا يُستبدل بالخط الافتراضي). يجب أن يحتوي قيمة الخط الافتراضي على اسم الخط (ليس مسار ملفات الخط). لقد قمنا بتنفيذ ميزة لتعيين اسم الخط الافتراضي أثناء حفظ المستند كملف PDF. يمكن استخدام مقتطف الشفرة التالي لتعيين الخط الافتراضي:

```python

    import aspose.pdf as ap

    # Load an existing PDF document with missing font
    document = ap.Document(input_pdf)

    pdfSaveOptions = ap.PdfSaveOptions()
    # Specify Default Font Name
    newName = "Arial"
    pdfSaveOptions.default_font_name = newName
    document.save(output_pdf, pdfSaveOptions)
```

### الحصول على جميع الخطوط من مستند PDF

في حال رغبتك في الحصول على جميع الخطوط من مستند PDF، يمكنك استخدام طريقة [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties) المقدمة في فئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/). الرجاء مراجعة مقتطف الشفرة التالي للحصول على جميع الخطوط من مستند PDF موجود:

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    fonts = doc.font_utilities.get_all_fonts()
    for font in fonts:
        print(font.font_name)
```

### تحسين تضمين الخطوط باستخدام FontSubsetStrategy

يعرض مقتطف الشفرة التالي كيفية تعيين [FontSubsetStrategy](https://reference.aspose.com/pdf/python-net/aspose.pdf/fontsubsetstrategy/) المستخدم في خاصية [font_utilities](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#properties):

```python

    import aspose.pdf as ap

    doc = ap.Document(input_pdf)
    # All fonts will be embedded as subset into document in case of SubsetAllFonts.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_ALL_FONTS)
    # Font subset will be embedded for fully embedded fonts but fonts which are not embedded into document will not be affected.
    doc.font_utilities.subset_fonts(ap.FontSubsetStrategy.SUBSET_EMBEDDED_FONTS_ONLY)
    doc.save(output_pdf)
```

### الحصول على/تعيين مستوى التكبير لملف PDF

أحيانًا تريد معرفة ما هو مستوى التكبير الحالي لمستند PDF. باستخدام Aspose.Pdf، يمكنك اكتشاف القيمة الحالية وكذلك تعيينها.

تسمح لك خاصية Destination في صنف [GoToAction](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/gotoaction/) بالحصول على قيمة التكبير المرتبطة بملف PDF. وبالمثل، يمكن استخدامها لتعيين مستوى التكبير للملف.

#### تعيين مستوى التكبير

يعرض مقتطف الشفرة التالي كيفية تعيين مستوى التكبير لملف PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    action = ap.annotations.GoToAction(ap.annotations.XYZExplicitDestination(1, 0.0, 0.0, 0.5))
    doc.open_action = action
    # Save the document
    doc.save(output_pdf)
```

#### الحصول على مستوى التكبير

يعرض مقتطف الشفرة التالي كيفية الحصول على مستوى التكبير لملف PDF.

```python

    import aspose.pdf as ap

    # Instantiate new Document object
    doc = ap.Document(input_pdf)

    # Create GoToAction object
    action = doc.open_action

    # Get the Zoom factor of PDF file
    print(action.destination.zoom)
```

### إعداد خصائص حوار الطباعة المسبقة

يسمح Aspoose.PDF بتعيين العنصر [DUPLEX_FLIP_LONG_EDGE](https://reference.aspose.com/pdf/python-net/aspose.pdf/printduplex/#members) في مستند PDF. يتيح لك تغيير خاصية DuplexMode لمستند PDF التي تكون مضبوطة على الوضع الأحادي بشكل افتراضي. يمكن تحقيق ذلك باستخدام طريقتين مختلفتين كما هو موضح أدناه.

```python

    import aspose.pdf as ap

    doc = ap.Document()
    doc.pages.add()
    doc.duplex = ap.PrintDuplex.DUPLEX_FLIP_LONG_EDGE
    doc.save(output_pdf)
```

### إعداد خصائص حوار الطباعة المسبقة باستخدام محرر محتوى PDF

```python

    import aspose.pdf as ap

    ed = ap.facades.PdfContentEditor()
    ed.bind_pdf(input_pdf)
    if (ed.get_viewer_preference() & ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE) > 0:
        print("The file has duplex flip short edge")

    ed.change_viewer_preference(ap.facades.ViewerPreference.DUPLEX_FLIP_SHORT_EDGE)
    ed.save(output_pdf)
```


