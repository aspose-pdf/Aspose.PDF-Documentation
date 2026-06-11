---
title: العمل مع إجراءات PDF في بايثون
linktitle: الإجراءات
type: docs
weight: 20
url: /ar/python-net/actions/
description: تعرف على كيفية إضافة إجراءات المستند والصفحة والنموذج وتحديثها وإزالتها في ملفات PDF باستخدام Python.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: إضافة إجراءات المستند والصفحة والنموذج إلى ملفات PDF في Python
Abstract: تستكشف هذه المقالة كيفية التعامل مع الإجراءات في مستندات PDF باستخدام مكتبة Aspose.PDF، والتي تغطي التفاعلات على مستوى المستند ومستوى الصفحة ومستوى النموذج. إجراءات PDF هي مشغلات محددة مسبقًا أو قابلة للتخصيص تستجيب لأحداث المستخدم، وتتيح التنقل، وتنفيذ JavaScript، وتشغيل الوسائط المتعددة، وتقديم النماذج، والمزيد. يوضح الدليل كيفية إضافة الإجراءات وتخصيصها وإزالتها، مثل فتح عناوين URL في أحداث المستند، وإنشاء التنقل الخاص بالصفحة أو تأثيرات التكبير/التصغير، وإضافة أزرار تفاعلية للطباعة والتنقل، وإخفاء عناصر النموذج ديناميكيًا، وإرسال بيانات النموذج إلى نقاط نهاية الويب. من خلال أمثلة كود Python المفصلة، يتعلم القراء تحسين تفاعل PDF وتبسيط سير العمل ودمج ملفات PDF مع الأنظمة الخارجية مع فهم اعتبارات توافق المشاهد.
---

الإجراءات في PDF هي مهام محددة مسبقًا يتم تشغيلها من خلال تفاعل المستخدم أو أحداث المستند. يمكن استخدامها من أجل:

- انتقل إلى صفحة محددة أو ملف خارجي
- افتح رابط ويب
- تشغيل محتوى الوسائط المتعددة
- قم بتشغيل جافا سكريبت
- إرسال نموذج أو إعادة تعيينه
- إظهار/إخفاء الحقول
- تغيير مستوى التكبير/التصغير أو وضع العرض

تستخدم جميع الإجراءات تقريبًا المعلمات المضمنة ولكن هناك بعض الإجراءات التي يمكن تخصيصها. على سبيل المثال - إجراءات جافا سكريبت.

## إضافة إجراءات تشغيل PDF

أضف إجراءات التشغيل المستندة إلى جافا سكريبت إلى مستند PDF باستخدام Python و Aspose.PDF. يقوم بتعيين إجراءات لأحداث المستندات الرئيسية مثل الفتح والحفظ والطباعة، مما يسمح بتشغيل عناوين URL تلقائيًا عند حدوث هذه الأحداث في برامج عرض PDF المدعومة.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_launch_actions(infile, outfile):
    """Add JavaScript launch actions for document events.

    Adds JavaScript actions that launch URLs when specific document events occur:
    - On document open: launches http://localhost:3000/open
    - Before saving: launches http://localhost:3000/save
    - Before printing: launches http://localhost:3000/print

    Args:
        infile (str): Path to the input PDF file.
        outfile (str): Path to save the output PDF with document actions.

    Returns:
        None

    Example:
        >>> add_launch_actions("sample_data/input/add_launch_actions_in.pdf", "sample_data/output/add_launch_actions_out.pdf")

    Notes:
        - Uses `ap.annotations.JavascriptAction` with `app.launchURL()`.
        - URLs are opened in the default browser depending on viewer support.
    """

    document = ap.Document(infile)

    # Add JavaScript actions for document events
    document.open_action = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/open');"
    )
    document.actions.before_saving = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/save');"
    )
    document.actions.before_printing = ap.annotations.JavascriptAction(
        "app.launchURL('http://localhost:3000/print');"
    )

    document.save(outfile)
```

## إزالة الإجراءات من مستند PDF

لتنظيف (أو إزالة) الإجراءات، ما عليك سوى تعيين المعالج على `None`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def remove_page_actions(infile, outfile):
    document = ap.Document(infile)

    if len(document.pages) < 3:
        print("Error: The document does not have at least 3 pages.")
        return

    page = document.pages[3]
    page.actions.remove_actions()

    document.save(outfile)
```

## إضافة إجراءات إلى الصفحة في مستند PDF

يتم توفير المشغلات المماثلة للصفحات: `on_open`, `on_close`.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_page_actions(infile, outfile):
    document = ap.Document(infile)

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

    document.save(outfile)
```

## الإجراءات في أكروفورمز

### استخدام إجراءات التنقل

يوفر معيار PDF مجموعة معينة من الإجراءات المسماة. يتم تحديد معنى هذه الإجراءات من خلال اسمها.
في التعليمة البرمجية التالية، سنستخدم إجراءات التنقلات.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_navigation_buttons(infile, outfile):
    # Configuration for each navigation button
    button_config = [
        ("First Page", 10.0, PredefinedAction.FIRST_PAGE, lambda p, t: p == 1),
        ("Previous Page", 120.0, PredefinedAction.PREV_PAGE, lambda p, t: p == 1),
        ("Next Page", 230.0, PredefinedAction.NEXT_PAGE, lambda p, t: p == t),
        ("Last Page", 340.0, PredefinedAction.LAST_PAGE, lambda p, t: p == t),
    ]

    document = ap.Document(infile)
    total_pages = len(document.pages)

    # Add navigation buttons to each page
    for page in document.pages:
        for name, x_pos, action, is_readonly_fn in button_config:
            # Create button rectangle
            rect = Rectangle(x_pos, 10.0, x_pos + 100, 40.0, True)
            button = ButtonField(page, rect)
            button.partial_name = name
            button.value = name
            button.characteristics.border = ap.Color.red.to_rgb()
            button.characteristics.background = ap.Color.orange.to_rgb()
            # Disable button when not applicable
            button.read_only = is_readonly_fn(page.number, total_pages)
            button.actions.on_release_mouse_btn = NamedAction(action)
            document.form.add(button)

    document.save(outfile)
```

يضيف هذا الرمز أزرار التنقل إلى كل صفحة من وثيقة PDF، مما يسهل على المستخدمين التنقل بين الصفحات. يبدأ بتحديد مسارات الملفات الكاملة لملفات الإدخال والإخراج باستخدام طريقة مساعدة. تحدد قائمة button_config أربعة أنواع من أزرار التنقل - الصفحة الأولى والصفحة السابقة والصفحة التالية والصفحة الأخيرة - إلى جانب مواضعها الأفقية وإجراءات التنقل المحددة مسبقًا التي تقوم بتشغيلها ووظيفة lambda التي تحدد ما إذا كان يجب قراءة كل زر فقط على صفحة معينة (على سبيل المثال، زري «الصفحة الأولى» و «الصفحة السابقة» للقراءة فقط في الصفحة الأولى).

يقوم الكود بعد ذلك بتحميل ملف PDF وتكراره من خلال كل صفحة. بالنسبة لكل صفحة، يتم التنقل بين تكوينات الأزرار، مما يؤدي إلى إنشاء منطقة مستطيلة لكل زر وإنشاء مثيل لـ ButtonField في هذا الموقع. يتم إعطاء كل زر اسمًا، ويتم تعيين حالة القراءة فقط استنادًا إلى الصفحة الحالية، ويتم تعيين إجراء النقر الخاص به لإجراء التنقل المقابل. ثم تتم إضافة الزر إلى حقول نموذج PDF.

بعد إضافة جميع الأزرار إلى جميع الصفحات، يتم حفظ المستند المعدل. في حالة حدوث أي أخطاء أثناء هذه العملية، يتم اكتشافها وطباعتها. يضمن هذا الأسلوب أن تحتوي كل صفحة على مجموعة متسقة من عناصر التحكم في التنقل، مما يحسن قابلية استخدام ملفات PDF متعددة الصفحات. إحدى التفاصيل الدقيقة هي استخدام is_readonly_fn lambda لتعطيل أزرار التنقل عندما لا تكون منطقية (على سبيل المثال، «الصفحة التالية» في الصفحة الأخيرة)، مما يساعد على منع ارتباك المستخدم.

### استخدام إجراءات الطباعة

عند استخدام نماذج PDF، غالبًا ما تكون هناك حاجة لطباعة مستندات PDF هذه. يمكن تنفيذ هذا الإجراء باستخدام قارئ PDF، ولكن في بعض الأحيان يكون من الأنسب القيام بذلك مباشرة من المستند باستخدام زر خاص.

في الواقع، هذا مثال آخر على كيفية استخدام الإجراءات المسماة. سوف نستخدم `PredefinedAction.FILE_PRINT` (محاكاة استخدام عنصر قائمة File->Print)، ولكن يمكنك أيضًا استخدامه `PredefinedAction.PRINT` أو `PredefinedAction.PRINT_DIALOG`، اعتمادًا على أغراضك الخاصة.

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_print(infile, outfile):
    document = ap.Document(infile)
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
    document.save(outfile)
```

يوضح مقتطف الشفرة هذا كيفية إضافة زر «طباعة» إلى الصفحة الأولى من مستند PDF. يبدأ بتحميل PDF من مسار ملف الإدخال المحدد وتحديد الصفحة الأولى (document.pages [1]).

يتم تحديد منطقة مستطيلة لموضع الزر وحجمه على الصفحة. يتم بعد ذلك إنشاء ButtonField في هذا الموقع، مع إعطاء الاسم «PrintButton»، ويتم تعيين قيمة العرض الخاصة به إلى «Print». تم تكوين الزر بحيث عند النقر عليه (على وجه التحديد، عند تحرير زر الماوس)، فإنه يقوم بتشغيل إجراء «طباعة ملف» المحدد مسبقًا، مما يدفع عارض PDF إلى فتح مربع حوار الطباعة.

لتحسين مظهر الزر، يتم إنشاء حد وتعيينه للزر، مع ضبط عرضه على وحدة واحدة. ثم تتم إضافة الزر إلى حقول نموذج PDF في الصفحة الأولى. أخيرًا، يتم حفظ المستند المعدل في مسار ملف الإخراج. يوفر هذا الأسلوب للمستخدمين طريقة ملائمة لطباعة المستند مباشرة من داخل PDF. لاحظ أن فعالية هذه الميزة تعتمد على دعم عارض PDF لحقول النماذج التفاعلية والإجراءات المحددة مسبقًا.

### استخدام إجراء الإخفاء

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_named_action_hide(infile, outfile):
    document = ap.Document(infile)
    # Collect all checkbox fields in the document
    checkboxes = [
        field for field in document.form if is_assignable(field, CheckboxField)
    ]

    # Create the hide button
    rect = Rectangle(10, 410, 140, 440, True)
    hide_button = ButtonField(document.pages[1], rect)
    hide_button.partial_name = "HideButton"
    hide_button.value = "Hide Checkboxes"

    # Add HideAction to button - will hide all checkboxes when clicked
    hide_button.actions.on_release_mouse_btn = HideAction(checkboxes, True)

    # Add button to the form on page 1
    document.form.add(hide_button, 1)

    # Save the modified PDF
    document.save(outfile)
```

يضيف مقتطف الشفرة هذا زرًا إلى الصفحة الأولى من PDF يخفي، عند النقر عليه، جميع حقول مربع الاختيار في المستند. يبدأ بحل مسارات ملفات الإدخال والإخراج الكاملة باستخدام طريقة مساعدة. يتم تحميل ملف PDF، ويتم تجميع جميع حقول مربع الاختيار عن طريق تصفية حقول النموذج لمثيلات `ap.CheckboxField`.

يتم تحديد منطقة مستطيلة لموضع الزر الجديد بالقرب من أعلى الصفحة. يتم إنشاء حقل ButtonField في هذا الموقع، باسم «HideButton»، ويُسمى «إخفاء مربعات الاختيار». تم تكوين الزر بحيث عند النقر عليه (عند تحرير زر الماوس)، فإنه يقوم بتشغيل HideAction الذي يخفي جميع مربعات الاختيار المجمعة.

ثم تتم إضافة الزر إلى حقول النموذج في الصفحة الأولى، ويتم حفظ ملف PDF المعدل في ملف الإخراج. في حالة حدوث أي أخطاء أثناء هذه العملية، يتم اكتشافها وطباعتها. توفر هذه الميزة للمستخدمين طريقة لإخفاء جميع مربعات الاختيار بسرعة في PDF، والتي يمكن أن تكون مفيدة لتخصيص مظهر المستند أو سير العمل.

### تطبيق إجراء الإرسال

```python
import aspose.pdf as ap
from aspose.pycore import is_assignable
from aspose.pdf import Rectangle
from aspose.pdf.forms import ButtonField, CheckboxField
from aspose.pdf.annotations import (
    NamedAction,
    PredefinedAction,
    HideAction,
    SubmitFormAction,
)
from os import path
import sys

def add_submit_action(infile, outfile):
    document = ap.Document(infile)

    # Create the submit action
    submit_action = SubmitFormAction()
    submit_action.url = ap.FileSpecification("http://localhost:3000/submit")
    submit_action.flags = (
        SubmitFormAction.EXPORT_FORMAT | SubmitFormAction.SUBMIT_COORDINATES
    )

    # Create the submit button
    rect = Rectangle(10, 10, 100, 40, True)
    submit_button = ButtonField(document.pages[1], rect)
    submit_button.partial_name = "SubmitButton"
    submit_button.value = "Submit"
    submit_button.actions.on_release_mouse_btn = submit_action

    # Add the button to the form on page 1
    document.form.add(submit_button, 1)

    # Save the document
    document.save(outfile)
```

تضيف هذه الوظيفة زر «إرسال» إلى الصفحة الأولى من نموذج PDF، مما يسمح للمستخدمين بإرسال بيانات النموذج إلى نقطة نهاية ويب محددة. يبدأ بإنشاء المسارات الكاملة لملفات PDF المدخلة والمخرجة، ثم يقوم بتحميل ملف PDF المُدخل باستخدام مكتبة Aspose.PDF.

أ `SubmitFormAction` تم إنشاؤه لتحديد السلوك عند النقر فوق الزر. تم تعيين عنوان url الخاص بالإجراء باستخدام `FileSpecification` مشيرا إلى http://localhost:3000/submit, مما يعني أنه سيتم إرسال بيانات النموذج إلى عنوان URL هذا. تجمع خاصية الأعلام `EXPORT_FORMAT` و `SUBMIT_COORDINATES`، مما يضمن تصدير بيانات النموذج بتنسيق قياسي وإدراج إحداثيات النقر على الزر في الإرسال.

يتم تحديد منطقة مستطيلة لموضع الزر وحجمه على الصفحة. يتم إنشاء ButtonField في هذا الموقع على الصفحة الأولى، مع إعطاء الاسم «SubmitButton»، ويتم تعيين قيمة العرض الخاصة به على «Submit». يتم تعيين إجراء الإرسال لحدث تحرير الماوس الخاص بالزر، بحيث يتم تشغيل الإجراء عندما ينقر المستخدم على الزر.

أخيرًا، تتم إضافة الزر إلى حقول النموذج في الصفحة الأولى، ويتم حفظ ملف PDF المعدل في ملف الإخراج. في حالة حدوث أي أخطاء أثناء هذه العملية، يتم اكتشافها وطباعتها. يوفر هذا الأسلوب طريقة سهلة الاستخدام لمستخدمي PDF لإرسال بيانات النموذج مباشرة إلى نقطة نهاية الخادم.

## موضوعات التنقل ذات الصلة

- [التنقل والتفاعل في PDF باستخدام Python](/pdf/ar/python-net/navigation-and-interaction/)
- [العمل مع الإشارات المرجعية في PDF باستخدام Python](/pdf/ar/python-net/bookmarks/)
- [العمل مع الروابط في PDF باستخدام Python](/pdf/ar/python-net/links/)
