---
title: إنشاء روابط في ملف PDF باستخدام بايثون
linktitle: إنشاء روابط
type: docs
weight: 10
url: /ar/python-net/create-links/
description: يشرح هذا القسم كيفية إنشاء روابط في مستند PDF الخاص بك باستخدام بايثون.
lastmod: "2025-07-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إنشاء روابط في PDF
Abstract: يوفر دليل Aspose.PDF for Python عبر .NET حول إنشاء الروابط للمطورين إرشادات عملية لإضافة روابط تشعبية تفاعلية إلى مستندات PDF باستخدام بايثون. يغطي كيفية إنشاء أنواع مختلفة من الروابط، بما في ذلك تلك التي تشغل تطبيقات خارجية، أو تنتقل إلى صفحات محددة داخل نفس المستند، أو تفتح ملفات PDF أخرى. يشرح التوثيق كيفية استخدام كائنات LinkAnnotation، وتحديد المناطق القابلة للنقر باستخدام Rectangle، وتعيين إجراءات مثل LaunchAction أو GoToRemoteAction. من خلال أمثلة شفرة واضحة وإرشادات خطوة بخطوة، يساعد هذا المورد المطورين على تعزيز تنقل PDF وتفاعليته في تطبيقاتهم بايثون.
---

## الروابط في مستندات PDF

وفقًا لمواصفة PDF 1.7 (ISO 32000-1:2008)، يمكن لت **Link annotation** أن تُطلق عدة أنواع من الإجراءات التي تحدد ما يحدث عندما يتم تنشيط التعليق التوضيحي. إليكم الإجراءات الأساسية المدعومة:

1. **GoTo** – ينتقل إلى وجهة داخل نفس المستند.
1. **GoToR** – ينتقل إلى وجهة في ملف PDF آخر (انتقال عن بُعد).
1. **URI** – يفتح معرف مورد موحد، عادةً رابط ويب.
1. **Launch** – يُشغِّل تطبيقًا أو يفتح ملفًا (يعتمد على النظام وغالبًا ما يكون مقيدًا لأسباب أمنية).
1. **Named** – ينفذ إجراءً مسبق التعريف، مثل الانتقال إلى الصفحة التالية أو طباعة المستند.
1. **JavaScript** – ينفّذ شفرة JavaScript مدمجة (يُستخدم بحذر بسبب مخاوف أمنية).
1. **SubmitForm** – يرسل بيانات النموذج إلى عنوان URL محدد.
1. **ResetForm** – يعيد حقول النموذج إلى قيمها الافتراضية.
1. **ImportData** – يستورد البيانات إلى المستند من ملف خارجي.

من خلال إضافة رابط لتطبيق داخل مستند، يمكن ربط التطبيقات من داخل المستند. هذا مفيد عندما تريد من القُرّاء اتخاذ إجراء معين في نقطة محددة من الدرس، على سبيل المثال، أو لإنشاء مستند غني بالميزات.

لإنشاء رابط تطبيق باستخدام 'LaunchAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the input PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific dimensions and position
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Configure the link's border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width of 5 units
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link appearance
    link.color = ap.Color.green  # Green color for the link

    # Set the action to launch another PDF file
    # Note: Commented out system command demonstrates potential alternative launch actions
    # link.action = ap.annotations.LaunchAction(document, "start %windir%\explorer.exe")
    link.action = ap.annotations.LaunchAction(document, "sample.pdf")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

## إنشاء رابط مستند PDF في ملف PDF

### باستخدام GoToRemoteAction

توضح هذه الشريحة من الشيفرة كيفية إضافة تعليق توضيحي للرابط إلى صفحة محددة من مستند PDF باستخدام مكتبة PDF بايثون.

1. افتح مستند PDF
1. اختر الصفحة الثانية من المستند (الفهرس 1)
1. أنشئ تعليق توضيحي للرابط:
1. تموضع عند الإحداثيات (10, 580, 120, 600)
1. ملونة بالأخضر
1. تربط إلى 'sample.pdf' في صفحته الأولى
1. أضف التعليق التوضيحي للرابط إلى الصفحة
1. احفظ المستند المعدل إلى مسار ملف الإخراج

لإنشاء رابط مستند PDF باستخدام 'GoToRemoteAction':

```python

import aspose.pdf as ap
from os import path

path_infile = path.join(self.dataDir, infile)
path_outfile = path.join(self.dataDir, outfile)

# Load the input PDF document
document = ap.Document(path_infile)

# Access the first page of the document (Aspose uses 1-based indexing)
page = document.pages[1]

# Create a link annotation in the specified rectangle area on the page
link = ap.annotations.LinkAnnotation(
    page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
)

# Set the color of the link annotation to green
link.color = ap.Color.green

# Define a remote action to open "sample.pdf" and navigate to its first page
link.action = ap.annotations.GoToRemoteAction("sample.pdf", 1)

# Add the link annotation to the current page
page.annotations.append(link)

# Save the updated PDF to the specified output path
document.save(path_outfile)
```

### باستخدام GoToAction

تُظهر هذه الشفرة كيفية إضافة تعليق توضيحي للرابط إلى صفحة محددة من مستند PDF باستخدام Aspose.PDF for Python. يظهر الرابط كمستطيل أخضر محدد بخط منقط ويسمح للمستخدم بالانتقال إلى صفحة أخرى داخل نفس ملف PDF. لإنشاء رابط مستند PDF باستخدام 'GoToAction':

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Open the PDF document
    document = ap.Document(path_infile)

    # Select the second page (index 1)
    page = document.pages[1]

    # Create a link annotation with specific coordinates
    link = ap.annotations.LinkAnnotation(page, ap.Rectangle(10, 580, 120, 600, True))

    # Customize link annotation border
    border = ap.annotations.Border(link)
    border.width = 5  # Border width
    border.dash = ap.annotations.Dash(1, 1)  # Dashed border style

    # Set link color to green
    link.color = ap.Color.green

    # Set link destination
    if document.pages.count >= 4:
        # Link to 4th page if document has 4 or more pages
        link.action = ap.annotations.GoToAction(document.pages[4])
    else:
        # Fallback: link to the last page if less than 4 pages
        link.action = ap.annotations.GoToAction(document.pages[document.pages.count])

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified document
    document.save(path_outfile)
```

### تطبيق GoToURIAction

يوضح المثال التالي كيفية إضافة تعليق توضيحي للرابط إلى مستند PDF باستخدام Aspose.PDF for Python. يظهر الرابط كمنطقة خضراء قابلة للنقر في الصفحة الأولى، وعند النقر عليها، يفتح وثائق Aspose.PDF for Python في متصفح ويب عبر GoToURIAction.

هذه الوظيفة مفيدة لتضمين مراجع خارجية مفيدة أو توثيق أو روابط دعم مباشرة داخل ملفات PDF الخاصة بك.

1. حمّل مستند PDF. افتح ملف PDF الموجود باستخدام ap.Document.
1. الوصول إلى الصفحة الأولى. استخدم document.pages[1] للوصول إلى الصفحة الأولى (Aspose يستخدم فهرسة تبدأ من 1).
1. أنشئ تعليق توضيحي للرابط. أنشئ كائن LinkAnnotation وحدد المنطقة المستطيلة القابلة للنقر باستخدام ap.Rectangle.
1. ضبط مظهر التعليق التوضيحي. اضبط لون التعليق إلى الأخضر باستخدام link.color = ap.Color.green.
1. تعيين إجراء URI. استخدم GoToURIAction لربط التعليق التوضيحي بعنوان URL خارجي.
1. إضافة التعليق التوضيحي إلى الصفحة. أرفق تعليق الرابط المُكوَّن إلى مجموعة التعليقات التوضيحية للصفحة الأولى.
1. احفظ المستند المعدل. احفظ مستند PDF المحدث إلى مسار الإخراج المحدد.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.dataDir, infile)
    path_outfile = path.join(self.dataDir, outfile)

    # Load the input PDF document
    document = ap.Document(path_infile)

    # Access the first page (Aspose uses 1-based indexing)
    page = document.pages[1]

    # Create a link annotation at the specified rectangle position
    link = ap.annotations.LinkAnnotation(
        page, ap.Rectangle(10, 580, 120, 600, True)  # (left, bottom, right, top, isEmpty)
    )

    # Set the color of the link annotation to green
    link.color = ap.Color.green

    # Define a URI action that navigates to the Aspose.PDF Python documentation
    link.action = ap.annotations.GoToURIAction("https://docs.aspose.com/pdf/python")

    # Add the link annotation to the page
    page.annotations.append(link)

    # Save the modified PDF to the output path
    document.save(path_outfile)
```

