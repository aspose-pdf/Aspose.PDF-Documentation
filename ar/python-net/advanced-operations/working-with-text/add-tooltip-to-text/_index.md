---
title: إضافة تلميحات الأدوات إلى نص PDF في Python
linktitle: تلميح أداة PDF
type: docs
weight: 20
url: /ar/python-net/pdf-tooltip/
description: تعرف على كيفية إضافة تلميحات الأدوات إلى أجزاء النص في مستندات PDF في Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: أضف تلميحات الأدوات التفاعلية إلى أجزاء نص PDF باستخدام Python
Abstract: تقدم هذه المقالة مثالين من Python لإضافة مساعدة تفاعلية إلى نص PDF باستخدام Aspose.PDF لـ Python عبر .NET. يضيف المثال الأول تلميحات الأدوات إلى أجزاء النص المتطابقة عن طريق وضع عناصر «ButtonField» غير المرئية وإعداد `alternate_name`. يقوم المثال الثاني بإنشاء «TextBoxField» المخفي الذي يظهر عند التمرير عن طريق توصيل أحداث «HideAction» إلى «ButtonField» غير المرئي.
---

## إضافة تلميح الأدوات إلى النص الذي تم البحث عنه في PDF

يوضح مقتطف الشفرة هذا كيفية التراكب غير المرئي [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) عناصر محددة [`TextFragment`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragment/) كائنات في PDF لعرض تلميحات الأدوات عندما يحوم المستخدم فوقها. وهو يدعم كلاً من رسائل تلميحات الأدوات القصيرة والطويلة باستخدام `alternate_name` ملكية لـ `ButtonField`.

استخدم هذه الصفحة عندما تحتاج إلى جعل نص PDF أكثر تفاعلية عن طريق إضافة تعليمات التمرير أو التفسيرات المضمنة أو الملاحظات السياقية.

1. قم بإنشاء ملف جديد [`Document`](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/).
1. احفظ المستند الأولي.
1. أعد فتح مستند PDF.
1. ابحث عن النص المستهدف باستخدام [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. أضف صورة غير مرئية [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) مع تلميح قصير.
1. ابحث عن النص الهدف الثاني.
1. أضف صورة غير مرئية [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) مع تلميح طويل فوق الجزء المطابق.
1. احفظ المستند النهائي.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

# region PDF Tooltip
def add_tool_tip_to_searched_text(outfile):
    # Create PDF document
    with ap.Document() as document:
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display a tooltip")
        )
        document.pages[1].paragraphs.add(
            ap.text.TextFragment(
                "Move the mouse cursor here to display a very long tooltip"
            )
        )
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a tooltip"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the extracted text fragments
        text_fragments = absorber.text_fragments

        # Loop through the fragments
        for fragment in text_fragments:
            # Create invisible button on text fragment position
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # alternate_name value will be displayed as tooltip by a viewer application
            field.alternate_name = "Tooltip for text."
            # Add button field to the document
            document.form.add(field)

        # Next will be sample of very long tooltip
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display a very long tooltip"
        )
        document.pages.accept(absorber)
        text_fragments = absorber.text_fragments

        for fragment in text_fragments:
            field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
            # Set very long text
            field.alternate_name = (
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
                " sed do eiusmod tempor incididunt ut labore et dolore magna"
                " aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
                " ullamco laboris nisi ut aliquip ex ea commodo consequat."
                " Duis aute irure dolor in reprehenderit in voluptate velit"
                " esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
                " occaecat cupidatat non proident, sunt in culpa qui officia"
                " deserunt mollit anim id est laborum."
            )
            document.form.add(field)

        # Save document
        document.save(outfile)
```

## قم بإنشاء كتلة نصية مخفية تظهر عند التمرير في ملف PDF

أضف نصًا عائمًا تفاعليًا إلى مستند PDF. إنها تتراكب مع صورة غير مرئية [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/) على عبارة مستهدفة وتكشف عن مخفي [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/) عندما يحوم المستخدم فوقها. هذه التقنية مثالية للمساعدة السياقية أو التعليقات التوضيحية أو عرض المحتوى الديناميكي.

1. قم بإنشاء مستند PDF جديد.
1. احفظ ملف PDF حتى يمكن إعادة فتحه لإعداد التفاعل.
1. أعد فتح مستند PDF.
1. حدد موقع النص الهدف باستخدام [`TextFragmentAbsorber`](https://reference.aspose.com/pdf/python-net/aspose.pdf.text/textfragmentabsorber/).
1. قم بإنشاء ملف مخفي [`TextBoxField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).
1. أضف الحقل المخفي إلى المستند [`Form`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) مجموعة.
1. قم بإنشاء صورة غير مرئية [`ButtonField`](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/buttonfield/).
1. تعيين إجراءات الماوس (`on_enter`, `on_exit`) باستخدام [`HideAction`](https://reference.aspose.com/pdf/python-net/aspose.pdf.annotations/hideaction/) لإظهار/إخفاء الحقل المخفي.
1. احفظ المستند النهائي.

```python
import aspose.pdf as ap
import aspose.pydrawing as drawing
import sys
from os import path

def create_hidden_text_block(outfile):
    # Create PDF document
    with ap.Document() as document:
        #  Add paragraph with text
        document.pages.add().paragraphs.add(
            ap.text.TextFragment("Move the mouse cursor here to display floating text")
        )
        # Save PDF document
        document.save(outfile)

    # Open document with text
    with ap.Document(outfile) as document:
        # Create TextAbsorber object to find all the phrases matching the regular expression
        absorber = ap.text.TextFragmentAbsorber(
            "Move the mouse cursor here to display floating text"
        )
        # Accept the absorber for the document pages
        document.pages.accept(absorber)
        # Get the first extracted text fragment
        text_fragments = absorber.text_fragments
        fragment = text_fragments[1]

        # Create hidden text field for floating text in the specified rectangle of the page
        floating_field = ap.forms.TextBoxField(
            fragment.page, ap.Rectangle(100.0, 700.0, 220.0, 740.0, False)
        )
        # Set text to be displayed as field value
        floating_field.value = 'This is the "floating text field".'
        # We recommend to make field 'readonly' for this scenario
        floating_field.read_only = True
        # Set 'hidden' flag to make field invisible on document opening
        floating_field.flags |= ap.annotations.AnnotationFlags.HIDDEN

        # Setting a unique field name isn't necessary but allowed
        floating_field.partial_name = "FloatingField_1"

        # Setting characteristics of field appearance isn't necessary but makes it better
        floating_field.default_appearance = ap.annotations.DefaultAppearance(
            "Helv", 10, drawing.Color.blue
        )
        floating_field.characteristics.background = drawing.Color.light_blue
        floating_field.characteristics.border = drawing.Color.dark_blue
        floating_field.border = ap.annotations.Border(floating_field)
        floating_field.border.width = 1
        floating_field.multiline = True

        # Add text field to the document
        document.form.add(floating_field)
        # Create invisible button on text fragment position
        button_field = ap.forms.ButtonField(fragment.page, fragment.rectangle)
        # Create new hide action for specified field (annotation) and invisibility flag.
        # (You also may refer floating field by the name if you specified it above.)
        # Add actions on mouse enter/exit at the invisible button field

        button_field.actions.on_enter = ap.annotations.HideAction(floating_field, False)
        button_field.actions.on_exit = ap.annotations.HideAction(floating_field)

        # Add button field to the document
        document.form.add(button_field)

        # Save document
        document.save(outfile)
```

## موضوعات نصية ذات صلة

- [العمل مع النص في PDF باستخدام Python](/pdf/ar/python-net/working-with-text/)
- [استخدم FloatingBox لتخطيط نص PDF في بايثون](/pdf/ar/python-net/floating-box/)
- [ابحث واستخرج نص PDF في بايثون](/pdf/ar/python-net/search-and-get-text-from-pdf/)
- [إضافة نص إلى PDF](/pdf/ar/python-net/add-text-to-pdf-file/)