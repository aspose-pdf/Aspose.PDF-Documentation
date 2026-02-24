---
title: العمل مع الإجراءات في مستند PDF
linktitle: الإجراءات
type: docs
weight: 20
url: /ar/python-net/actions/
description: استكشف كيفية استخراج وإدارة بيانات تعريف PDF، مثل المؤلف والعنوان، باستخدام بايثون وAspose.PDF.
lastmod: "2025-07-10"
sitemap: 
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: التعامل مع الإجراءات في مستند PDF باستخدام بايثون
Abstract: تستكشف هذه المقالة كيفية التعامل مع الإجراءات في مستندات PDF باستخدام مكتبة Aspose.PDF، مع تغطية التفاعلات على مستوى المستند، مستوى الصفحة، ومستوى النموذج. إجراءات PDF هي محفزات معرفة مسبقًا أو قابلة للتخصيص تستجيب لأحداث المستخدم، مما يتيح التنقل، تنفيذ جافا سكريبت، تشغيل الوسائط المتعددة، إرسال النماذج، والمزيد. يوضح الدليل كيفية إضافة، تخصيص، وإزالة الإجراءات، مثل فتح عناوين URL عند أحداث المستند، إنشاء تنقل أو تأثيرات تكبير مخصصة للصفحات، إضافة أزرار تفاعلية للطباعة والتنقل، إخفاء عناصر النموذج ديناميكيًا، وإرسال بيانات النموذج إلى نقاط النهاية على الويب. من خلال أمثلة شاملة لكود بايثون، يتعلم القراء تعزيز تفاعل PDF، تبسيط سير العمل، ودمج ملفات PDF مع الأنظمة الخارجية مع فهم اعتبارات توافق عارض PDF.
---

الإجراءات في PDF هي مهام معرفة مسبقًا يتم تفعيلها بواسطة تفاعل المستخدم أو أحداث المستند. يمكن استخدامها لـ:

- الانتقال إلى صفحة محددة أو ملف خارجي
- فتح رابط ويب
- تشغيل محتوى وسائط متعددة
- تشغيل جافا سكريبت
- إرسال أو إعادة تعيين نموذج
- إظهار/إخفاء الحقول
- تغيير مستوى التكبير أو وضع العرض

تقريبًا جميع الإجراءات تستخدم معلمات مدمجة ولكن هناك بعض الإجراءات التي يمكن تخصيصها. على سبيل المثال - إجراءات جافا سكريبت.

## إجراءات على مستوى المستند

### إضافة إجراءات إلى مستند PDF

تدعم مستندات PDF عدة إجراءات على مستوى المستند، بما في ذلك الكود الذي يعمل عند فتح المستند أو استجابةً لأحداث معينة. استخدم خاصية `open_action` للإجراءات عند الفتح؛ تُدار باقي الإجراءات في مجموعة `actions`.

لننظر في كيفية استخدام `open_action`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/open');"
)
document.save(path_outfile)
```

في هذا المثال نستدعي طريقة `launchURL` من كائن `app` ونفتح موقع ويب (لأغراض العرض).

يمكن إضافة إجراءات أخرى بنفس الطريقة، ولكن مع تغييرات طفيفة:

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.actions.before_saving = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/save');"
)
document.actions.before_printing = ap.annotations.JavascriptAction(
    "app.launchURL('http://localhost:3000/print');"
)
```

يمكنك إضافة إجراءات للأحداث التالية: `before_saving`، `before_printing`، `before_closing`، `after_saving`، `after_printing`.

يوضح مقطع الشيفرة هذا كيفية إرفاق إجراءات جافا سكريبت بأحداث مختلفة على مستوى المستند في PDF. أولاً، يتم تحميل مستند PDF موجود من مسار ملف الإدخال المحدد. تُضبط خاصية `document.open_action` على إجراء جافا سكريبت يفتح عنوان URL عند فتح المستند، مما يدفع عارض PDF لفتح `http://localhost:3000/open` في متصفح المستخدم.

بعد ذلك، يتم تعيين إجراءين جافا سكريبت إضافيين إلى حدثي `before_saving` و `before_printing` في المستند. تُفعَّل هذه الإجراءات عندما يحاول المستخدم حفظ أو طباعة المستند، على التوالي، حيث يفتح كل مرة عنوان URL مختلف (`/save` أو `/print`) في المتصفح. يمكن أن يكون ذلك مفيدًا لتتبع تفاعلات المستخدم أو دمجه مع سير عمل قائم على الويب.

### إزالة إجراءات من مستند PDF

لإزالة (أو حذف) الإجراءات، قم فقط بتعيين المعالج إلى `None`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

document = ap.Document(path_infile)
document.open_action = None
document.actions.before_saving = None
document.actions.before_printing = None
document.save(path_outfile)
```

## إجراءات على مستوى الصفحة

### إضافة إجراءات إلى الصفحة في مستند PDF

توفر المشغلات المشابهة للصفحات: `on_open`، `on_close`.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_page_actions(self, infile, outfile):
    """
    Add actions to the third page of the PDF.

    Adds two actions to page 3:
    - On page open: Navigate to the top of the page with specific zoom
    - On page close: Launch a URL with page-specific information

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Raises:
        ValueError: If document has fewer than 3 pages

    Example:
        >>> actions.add_page_actions("multipage.pdf", "page_actions.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]

    # Add GoTo action on page open - navigate to top of page
    action = ap.annotations.GoToAction(page)
    action.destination = ap.annotations.XYZExplicitDestination(
        page, 0, page.page_info.height, 1
    )
    page.actions.on_open = action

    # Add JavaScript action on page close
    page.actions.on_close = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/page/3');"
    )

    document.save(path_outfile)

```

نضيف إجراءين إلى هذه الصفحة. أولاً، يتم إنشاء إجراء "GoTo" يتم تفعيله عندما تُفتح الصفحة. يستخدم هذا الإجراء هدفًا صريحًا للقفز إلى الزاوية العلوية اليسرى من الصفحة عند مستوى تكبير محدد. ثانيًا، يتم إرفاق إجراء جافا سكريبت يعمل عند إغلاق الصفحة، مُطالبًا عارض PDF بفتح عنوان URL محدد في المتصفح. أخيرًا، يتم حفظ المستند المعدل إلى مسار الإخراج المحدد.

نقطة دقيقة يجب الانتباه إليها هي فهرسة الصفحات، فاستخدام الفهرس الخاطئ قد يؤدي إلى سلوك غير متوقع أو أخطاء. بالإضافة إلى ذلك، قد لا يدعم جميع عارضي PDF إجراءات جافا سكريبت في ملفات PDF، لذا قد لا تعمل هذه الميزة في جميع الأماكن.

### إزالة إجراءات من صفحة PDF

استخدم `remove_actions` لإزالة الإجراء من الصفحة.

```python

import aspose.pdf as ap
from os import path

document = ap.Document(path_infile)

if len(document.pages) < 3:
    print("Error: The document does not have at least 3 pages.")
    return

page = document.pages[3]
page.actions.remove_actions()

document.save(path_outfile)

```

## إجراءات في AcroForms

### استخدام إجراءات التنقل

توفر معيار PDF مجموعة معينة من الإجراءات المسماة. يتم تحديد معنى هذه الإجراءات بناءً على أسمائها.
في الشيفرة التالية سنستخدم إجراءات للتنقل.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_navigation_buttons(self, infile, outfile):
    """
    Add navigation buttons to each page of the PDF.

    Creates four navigation buttons on each page:
    - First Page: Navigate to the first page
    - Previous Page: Navigate to the previous page
    - Next Page: Navigate to the next page
    - Last Page: Navigate to the last page

    Buttons are automatically disabled when not applicable (e.g.,
    "Previous" is disabled on the first page).

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_navigation_buttons("multipage.pdf", "nav_buttons.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    try:
        document = ap.Document(path_infile)
        total_pages = len(document.pages)

        # Add navigation buttons to each page
        for page in document.pages:
            page_number = page.number

            for name, x_pos, action, is_readonly_fn in button_config:
                # Create button rectangle
                rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
                button = ButtonField(page, rect)
                button.partial_name = name

                # Disable button when not applicable
                button.read_only = is_readonly_fn(page_number, total_pages)
                button.actions.on_release_mouse_btn = NamedAction(action)

                document.form.add(button)

        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding navigation buttons: {e}")

```

تضيف هذه الشيفرة أزرار تنقل إلى كل صفحة من مستند PDF، مما يسهل على المستخدمين الانتقال بين الصفحات. تبدأ بتحديد المسارات الكاملة لملفات الإدخال والإخراج باستخدام طريقة مساعدة. تُعرّف قائمة button_config أربعة أنواع من أزرار التنقل — الصفحة الأولى، الصفحة السابقة، الصفحة التالية، والصفحة الأخيرة — بالإضافة إلى مواقعها الأفقية، والإجراءات التنقلية المعرفة مسبقًا التي تُطلقها، ودالة lambda التي تحدد ما إذا كان يجب أن يكون كل زر للقراءة فقط في صفحة معينة (على سبيل المثال، أزرار "الصفحة الأولى" و"الصفحة السابقة" تُصبح للقراءة فقط في الصفحة الأولى).

بعد ذلك، تقوم الشيفرة بتحميل ملف PDF وتكرر عبر كل صفحة. لكل صفحة، تُعيد الدورة عبر إعدادات الأزرار، تُنشئ مساحة مستطيلة لكل زر وتُنشئ كائن ButtonField في ذلك الموقع. يُعطى كل زر اسمًا، وتُحدد حالة القراءة فقط بناءً على الصفحة الحالية، وتُعيَّن إجراء النقر إلى الإجراء التنقلي المقابل. ثم يُضاف الزر إلى حقول نموذج PDF.

بعد إضافة جميع الأزرار إلى جميع الصفحات، يتم حفظ المستند المعدل. إذا حدثت أي أخطاء أثناء هذه العملية، يتم التقاطها وطباعة رسالة بها. يضمن هذا النهج أن كل صفحة تحتوي على مجموعة متسقة من عناصر التحكم في التنقل، مما يحسن من قابلية استخدام ملفات PDF متعددة الصفحات. من النقاط الدقيقة هو استخدام الدالة is_readonly_fn lambda لتعطيل أزرار التنقل عندما لا تكون ذات معنى (مثل "الصفحة التالية" في الصفحة الأخيرة)، مما يساعد على تجنب ارتباك المستخدم.

### استخدام إجراءات الطباعة

عند استخدام نماذج PDF، غالبًا ما يكون هناك حاجة لطباعة هذه المستندات. يمكن تنفيذ هذا الإجراء باستخدام قارئ PDF، ولكن في بعض الأحيان يكون من الأنسب القيام به مباشرةً من المستند باستخدام زر خاص.

في الواقع، هذا مثال آخر على كيفية استخدام الإجراءات المسماة. سنستخدم `PredefinedAction.FILE_PRINT` (محاكاة لاستخدام عنصر القائمة ملف->طباعة)، ولكن يمكنك أيضًا استخدام `PredefinedAction.PRINT` أو `PredefinedAction.PRINT_DIALOG`، حسب احتياجاتك.

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_print(self, infile, outfile):
    """
    Add a print button to the first page of the PDF.

    Creates a button labeled "Print" that triggers the system print dialog
    when clicked. The button is positioned at the bottom-left corner of
    the first page with a 1-pixel border.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_print("input.pdf", "output.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    document = ap.Document(path_infile)
    page = document.pages[1]

    # Create print button with specific dimensions and position
    rect = Rectangle(10, 10, 100, 40, True)
    print_button = ButtonField(page, rect)
    print_button.partial_name = "printButton"
    print_button.value = "Print"
    print_button.actions.on_release_mouse_btn = NamedAction(PredefinedAction.FILE_PRINT)

    # Add border for better visibility
    border = ap.annotations.Border(print_button)
    border.width = 1
    print_button.border = border

    # Add button to the form on page 1
    document.form.add(print_button, 1)
    document.save(path_outfile)

```

يُظهر هذا المقتطف من الكود كيفية إضافة زر "Print" إلى الصفحة الأولى من مستند PDF. يبدأ بتحميل ملف PDF من مسار الملف الإدخالي المحدد واختيار الصفحة الأولى (document.pages[1]).

يتم تعريف مساحة مستطيلة لتحديد موضع وحجم الزر على الصفحة. ثم يتم إنشاء ButtonField في هذا الموقع، يُعطى الاسم "printButton," وتُضبط قيمته الظاهرة إلى "Print." يتم تكوين الزر بحيث عند النقر عليه (وبشكل محدد عند تحرير زر الفأرة)، يُنفّذ إجراء "Print File" المحدد مسبقًا، مما يُحرض عارض PDF على فتح مربع حوار الطباعة.

لتحسين مظهر الزر، يتم إنشاء إطار وتعيينه للزر، مع ضبط عرضه على وحدة واحدة. ثم يُضاف الزر إلى حقول نموذج PDF في الصفحة الأولى. أخيرًا، يُحفظ المستند المعدل إلى مسار ملف الإخراج. يوفر هذا النهج للمستخدمين طريقة مريحة لطباعة المستند مباشرةً من داخل PDF. لاحظ أن فعالية هذه الميزة تعتمد على دعم عارض PDF للحقول التفاعلية وإجراءات محددة مسبقًا.

### استخدام إجراء الإخفاء

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_named_action_hide(self, infile, outfile):
    """
    Add a hide button that toggles visibility of all checkbox fields.

    Creates a button labeled "Hide Checkboxes" that can hide or show
    all checkbox fields in the document. Useful for forms with many
    checkboxes that might clutter the interface.

    Args:
        infile (str): Input PDF filename
        outfile (str): Output PDF filename

    Example:
        >>> actions.add_named_action_hide("form.pdf", "form_with_hide.pdf")
    """
    path_infile, path_outfile = self._get_file_paths(infile, outfile)

    try:
        document = ap.Document(path_infile)
        # Collect all checkbox fields in the document
        checkboxes = [field for field in document.form if isinstance(field, ap.CheckboxField)]

        # Create the hide button
        rect = Rectangle(10, 510, 100, 540)
        hide_button = ButtonField(document.pages[1], rect)
        hide_button.partial_name = "HideButton"
        hide_button.value = "Hide Checkboxes"

        # Add HideAction to button - will hide all checkboxes when clicked
        hide_button.actions.on_release_mouse_btn = ap.HideAction(checkboxes, True)

        # Add button to the form on page 1
        document.form.add(hide_button, 1)

        # Save the modified PDF
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding hide button: {e}")

```

يضيف هذا المقتطف من الكود زرًا إلى الصفحة الأولى من ملف PDF حيث يقوم، عند النقر عليه، بإخفاء جميع حقول خانة الاختيار في المستند. يبدأ بحل مسارات الملفات الإدخال والإخراج الكاملة باستخدام طريقة مساعدة. يتم تحميل ملف PDF، ويتم جمع جميع حقول خانة الاختيار عن طريق تصفية حقول النموذج للعثور على نماذج من `ap.CheckboxField`.

يتم تعريف مساحة مستطيلة لتحديد موضع الزر الجديد بالقرب من أعلى الصفحة. يتم إنشاء ButtonField في هذا الموقع، يُسمى "HideButton," وموسوم بـ "Hide Checkboxes." يتم تكوين الزر بحيث عند النقر عليه (عند تحرير زر الفأرة)، يُفعل HideAction الذي يخفي جميع خانات الاختيار المجمعة.

ثم يُضاف الزر إلى حقول النموذج في الصفحة الأولى، ويُحفظ ملف PDF المعدل إلى ملف الإخراج. إذا حدثت أي أخطاء أثناء هذه العملية، يتم التقاطها وطباعةها. توفر هذه الميزة للمستخدمين طريقة سريعة لإخفاء جميع خانات الاختيار في PDF، وهو ما قد يكون مفيدًا لتخصيص مظهر المستند أو سير العمل.

### تطبيق إجراء الإرسال

```python

import aspose.pdf as ap
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField
from aspose.pdf.annotations import NamedAction, PredefinedAction
from os import path

# ...

def add_submit_action(self, infile, outfile):
    """
    Submit form.

    Parameters:
    - infile (str): The name of the input PDF file.
    - outfile (str): The name of the output PDF file.
    """
    path_infile = self.dataDir + infile
    path_outfile = self.dataDir + outfile

    try:
        document = ap.Document(path_infile)

        # Create the submit action
        submit_action = ap.SubmitFormAction()
        submit_action.url = FileSpecification("http://localhost:3000/submit")
        submit_action.flags = (
            SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
        )

        # Create the submit button
        rect = Rectangle(10, 10, 100, 40)
        submit_button = ButtonField(document.pages[1], rect)
        submit_button.partial_name = "SubmitButton"
        submit_button.value = "Submit"
        submit_button.actions.on_release_mouse_btn = submit_action

        # Add the button to the form on page 1
        document.form.add(submit_button, 1)

        # Save the document
        document.save(path_outfile)

    except Exception as e:
        print(f"Error adding submit button: {e}")

```

تضيف هذه الدالة زر "Submit" إلى الصفحة الأولى من نموذج PDF، مما يتيح للمستخدمين إرسال بيانات النموذج إلى نقطة نهاية ويب محددة. يبدأ ببناء المسارات الكاملة لملفات PDF الإدخال والإخراج، ثم يحمل ملف PDF الإدخال باستخدام مكتبة Aspose.PDF.

يتم إنشاء `SubmitFormAction` لتحديد السلوك عند النقر على الزر. يتم ضبط عنوان URL للإجراء باستخدام `FileSpecification` يشير إلى http://localhost:3000/submit، مما يعني أن بيانات النموذج ستُرسل إلى هذا العنوان. تجمع خاصية flags بين `EXPORT_FORMAT` و`SUBMIT_COORDINATES`، لضمان تصدير بيانات النموذج بتنسيق قياسي وإدراج إحداثيات نقرة الزر في الإرسال.

يتم تعريف مساحة مستطيلة لتحديد موضع وحجم الزر على الصفحة. يتم إنشاء ButtonField في هذا الموقع في الصفحة الأولى، يُعطى الاسم "SubmitButton," وتُضبط قيمته الظاهرة إلى "Submit." يُربط إجراء الإرسال بحدث تحرير زر الفأرة للزر، بحيث يُفعَّل الإجراء عندما ينقر المستخدم على الزر.

أخيرًا، يُضاف الزر إلى حقول النموذج في الصفحة الأولى، ويُحفظ ملف PDF المعدل إلى ملف الإخراج. إذا حدثت أي أخطاء أثناء هذه العملية، يتم التقاطها وطباعةها. يوفر هذا النهج طريقة سهلة الاستخدام لمستخدمي PDF لإرسال بيانات النموذج مباشرةً إلى نقطة النهاية على الخادم.

