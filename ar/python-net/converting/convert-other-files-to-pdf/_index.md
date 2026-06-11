---
title: تحويل تنسيقات الملفات الأخرى إلى PDF في Python
linktitle: تحويل تنسيقات الملفات الأخرى إلى PDF
type: docs
weight: 80
url: /ar/python-net/convert-other-files-to-pdf/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل ملفات EPUB وMarkdown وPCL وXPS وPostScript وXML وLaTeX إلى PDF بلغة بايثون باستخدام Aspose.PDF لبيثون عبر .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: كيفية تحويل تنسيقات الملفات الأخرى إلى PDF في Python
Abstract: توفر هذه المقالة دليلًا شاملاً حول تحويل تنسيقات الملفات المختلفة إلى PDF باستخدام Python، والاستفادة من إمكانيات Aspose.PDF لـ Python عبر .NET. تحدد الوثيقة عمليات التحويل للعديد من التنسيقات، بما في ذلك EPUB وMarkdown وPCL والنص وXPS وPostScript وXML وXSL-FO وLaTEX/Tex. يوفر كل قسم مقتطفات شفرة محددة وإرشادات لتنفيذ هذه التحويلات. تؤكد المقالة على فائدة ميزات Aspose.PDF، مثل خيارات التحميل المصممة لكل نوع ملف، لضمان التحويل الدقيق والفعال. بالإضافة إلى ذلك، فإنه يسلط الضوء على توفر تطبيقات التحويل عبر الإنترنت للمستخدمين لاستكشاف الوظائف بشكل مباشر. يعمل الدليل كمورد عملي للمطورين الذين يسعون إلى دمج إمكانات تحويل PDF في تطبيقات Python الخاصة بهم.
---

تشرح هذه المقالة كيفية**تحويل أنواع أخرى مختلفة من تنسيقات الملفات إلى PDF باستخدام Python**. يغطي الموضوعات التالية.

## تحويل ملفات OFD إلى PDF

يرمز OFD إلى مستند مفتوح ذو تخطيط ثابت (يُسمى أيضًا تنسيق المستند الثابت المفتوح). إنه معيار وطني صيني (GB/T 33190-2016) للمستندات الإلكترونية، تم تقديمه كبديل لـ PDF.

خطوات تحويل OFD إلى PDF في بايثون:

1. قم بإعداد خيارات تحميل OFD باستخدام خيارات ofdloadOptions ().
1. قم بتحميل مستند OFD.
1. احفظ كملف PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_OFD_to_PDF(infile, outfile):
    load_options = ap.OfdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل لاتكس/تكس إلى PDF

تنسيق ملف LaTeX هو تنسيق ملف نصي مع ترميز في مشتق LaTeX من عائلة لغات TeX و LaTeX هو تنسيق مشتق من نظام TeX. LaTeX (ək.le550 tehk/lay-tek أو lah-tek) هو نظام لإعداد المستندات ولغة ترميز المستندات. يستخدم على نطاق واسع لتوصيل ونشر الوثائق العلمية في العديد من المجالات، بما في ذلك الرياضيات والفيزياء وعلوم الكمبيوتر. كما أنها تلعب دورًا رئيسيًا في إعداد ونشر الكتب والمقالات التي تحتوي على مواد معقدة متعددة اللغات، مثل الأحرف الكورية واليابانية والصينية والعربية، بما في ذلك الإصدارات الخاصة.

يستخدم LaTeX برنامج التنضيد TeX لتنسيق مخرجاته، وهو نفسه مكتوب بلغة ماكرو TeX.

{{% alert color="success" %}}
** حاول تحويل LaTEX/TEX إلى PDF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«لاتكس إلى PDF»](https://products.aspose.app/pdf/conversion/tex-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل اللاتكس/النص إلى PDF مع التطبيق](latex.png)](https://products.aspose.app/pdf/conversion/tex-to-pdf)
{{% /alert %}}

خطوات تحويل TEX إلى PDF في بايثون:

1. قم بإعداد خيارات تحميل LaTeX باستخدام LatexLoadOptions ().
1. قم بتحميل مستند LaTeX.
1. احفظ كملف PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TEX_to_PDF(infile, outfile):
    load_options = ap.LatexLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل EPUB إلى PDF

**Aspose.pdf لبايثون عبر .NET** يسمح لك ببساطة بتحويل ملفات EPUB إلى صيغة PDF.

EPUB (اختصار للنشر الإلكتروني) هو معيار مجاني ومفتوح للكتب الإلكترونية من المنتدى الدولي للنشر الرقمي (IDPF). تحتوي الملفات على الامتداد.epub. تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين.

<abbr title="electronic publication">النشر الإلكتروني</abbr> يدعم أيضًا محتوى التخطيط الثابت. الغرض من التنسيق هو التنسيق الوحيد الذي يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. إنه يحل محل معيار الكتاب الإلكتروني المفتوح. تم اعتماد الإصدار EPUB 3 أيضًا من قبل مجموعة دراسة صناعة الكتاب (BISG)، وهي جمعية رائدة في تجارة الكتب لأفضل الممارسات الموحدة والبحوث والمعلومات والأحداث، لتغليف المحتوى.

{{% alert color="success" %}}
** حاول تحويل EPUB إلى PDF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«EPUB إلى PDF»](https://products.aspose.app/pdf/conversion/epub-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل EPUB إلى PDF باستخدام التطبيق](epub.png)](https://products.aspose.app/pdf/conversion/epub-to-pdf)
{{% /alert %}}

خطوات تحويل EPUB إلى PDF في بايثون:

1. قم بتحميل مستند EPUB باستخدام خيارات تحميل ePubloadOptions ().
1. قم بتحويل EPUB إلى PDF.
1. تأكيد الطباعة.

يوضح لك مقتطف الشفرة التالي كيفية تحويل ملفات EPUB إلى تنسيق PDF باستخدام Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_EPUB_to_PDF(infile, outfile):
    load_options = ap.EpubLoadOptions()
    document = ap.Document(infile, load_options)

    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## تحويل تخفيض السعر إلى PDF

**هذه الميزة مدعومة بالإصدار 19.6 أو أحدث. **

{{% alert color="success" %}}
** حاول تحويل Markdown إلى PDF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«تخفيض السعر إلى PDF»](https://products.aspose.app/pdf/conversion/md-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![تخفيض قيمة تحويل Aspose.PDF إلى PDF باستخدام التطبيق](markdown.png)](https://products.aspose.app/pdf/conversion/md-to-pdf)
{{% /alert %}}

يساعد مقتطف الشفرة هذا من Aspose.PDF لـ Python عبر .NET على تحويل ملفات Markdown إلى ملفات PDF، مما يسمح بمشاركة المستندات بشكل أفضل والحفاظ على التنسيق وتوافق الطباعة. o

يوضح مقتطف الشفرة التالي كيفية استخدام هذه الوظيفة مع مكتبة Aspose.PDF:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_MD_to_PDF(infile, outfile):
    load_options = ap.MdLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## تحويل PCL إلى PDF

<abbr title="Printer Command Language">ثنائي الفينيل متعدد الكلور</abbr> (لغة أوامر الطابعة) هي لغة طابعة Hewlett-Packard تم تطويرها للوصول إلى ميزات الطابعة القياسية. مستويات PCL من 1 إلى 5e/5c هي لغات قائمة على الأوامر تستخدم تسلسلات التحكم التي تتم معالجتها وتفسيرها بالترتيب الذي تم استلامها به. على مستوى المستهلك، يتم إنشاء تدفقات بيانات PCL بواسطة برنامج تشغيل الطباعة. يمكن أيضًا إنشاء إخراج PCL بسهولة من خلال التطبيقات المخصصة.

{{% alert color="success" %}}
** حاول تحويل PCL إلى PDF عبر الإنترنت**

Aspose.PDF لـ .NET يقدم لك التطبيق عبر الإنترنت [«PCL إلى PDF»](https://products.aspose.app/pdf/conversion/pcl-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل ملفات PCL إلى PDF باستخدام التطبيق](pcl_to_pdf.png)](https://products.aspose.app/pdf/conversion/pcl-to-pdf)
{{% /alert %}}

للسماح بالتحويل من PCL إلى PDF، يحتوي Aspose.PDF على الفئة [`PclLoadOptions`](https://reference.aspose.com/pdf/net/aspose.pdf/pclloadoptions) والذي يتم استخدامه لتهيئة كائن LoadOptions. في وقت لاحق يتم تمرير هذا الكائن كوسيطة أثناء تهيئة كائن المستند ويساعد محرك عرض PDF على تحديد تنسيق الإدخال للمستند المصدر.

يعرض مقتطف الشفرة التالي عملية تحويل ملف PCL إلى تنسيق PDF.

خطوات تحويل PCL إلى PDF في بايثون:

1. خيارات التحميل لـ PCL باستخدام PclloadOptions ().
1. قم بتحميل المستند.
1. احفظ كملف PDF.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PCL_to_PDF(infile, outfile):
    load_options = ap.PclLoadOptions()
    load_options.supress_errors = True

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل النص المنسق مسبقًا إلى PDF

**Aspose.pdf لـ Python عبر .NET** يدعم ميزة تحويل النص العادي والملف النصي المنسق مسبقًا إلى تنسيق PDF.

تحويل النص إلى PDF يعني إضافة أجزاء نصية إلى صفحة PDF. أما بالنسبة للملفات النصية، فنحن نتعامل مع نوعين من النصوص: التنسيق المسبق (على سبيل المثال، 25 سطرًا بـ 80 حرفًا لكل سطر) والنص غير المنسق (النص العادي). اعتمادًا على احتياجاتنا، يمكننا التحكم في هذه الإضافة بأنفسنا أو تكليفها بخوارزميات المكتبة.

{{% alert color="success" %}}
** حاول تحويل TEXT إلى PDF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«تحويل النص إلى PDF»](https://products.aspose.app/pdf/conversion/txt-to-pdf)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل النص إلى PDF مع التطبيق](text_to_pdf.png)](https://products.aspose.app/pdf/conversion/txt-to-pdf)
{{% /alert %}}

خطوات تحويل TEXT إلى PDF في Python:

1. اقرأ ملف الإدخال النصي سطرًا بسطر.
1. قم بإعداد خط أحادي المسافة (Courier New) لمحاذاة النص المتسقة.
1. قم بإنشاء مستند PDF جديد وأضف الصفحة الأولى بهوامش مخصصة وإعدادات الخط.
1. قم بالتكرار من خلال أسطر الملف النصي لمحاكاة الآلة الكاتبة، نستخدم الخط 'monospace_font' والحجم 12.
1. حدد إنشاء الصفحة بـ 4 صفحات.
1. احفظ ملف PDF النهائي إلى المسار المحدد.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_TXT_to_PDF(infile, outfile):
    with open(infile, "r") as file:
        lines = file.readlines()

    monospace_font = ap.text.FontRepository.find_font("Courier New")

    document = ap.Document()
    page = document.pages.add()

    page.page_info.margin.left = 20
    page.page_info.margin.right = 10
    page.page_info.default_text_state.font = monospace_font
    page.page_info.default_text_state.font_size = 12
    count = 1
    for line in lines:
        if line != "" and line[0] == "\x0c":
            page = document.pages.add()
            page.page_info.margin.left = 20
            page.page_info.margin.right = 10
            page.page_info.default_text_state.font = monospace_font
            page.page_info.default_text_state.font_size = 12
            count = count + 1
        else:
            text = ap.text.TextFragment(line)
            page.paragraphs.add(text)

        if count == 4:
            break

    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل بوستسكريبت إلى PDF

يوضح هذا المثال كيفية تحويل ملف PostScript إلى مستند PDF باستخدام Aspose.PDF لـ Python عبر .NET.

1. قم بإنشاء مثيل من «psloAdOptions» لتفسير ملف PS بشكل صحيح.
1. قم بتحميل ملف «PostScript» إلى كائن مستند باستخدام خيارات التحميل.
1. احفظ المستند بصيغة PDF إلى مسار الإخراج المطلوب.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_PS_to_PDF(infile, outfile):
    load_options = ap.PsLoadOptions()

    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

## تحويل XPS إلى PDF

**aspose.pdf لبايثون عبر .NET** دعم تحويل الميزة <abbr title="XML Paper Specification">XPS</abbr> ملفات بصيغة PDF. راجع هذه المقالة لحل مهامك.

يرتبط نوع ملف XPS بشكل أساسي بمواصفات ورق XML من قبل شركة Microsoft Corporation. تعد مواصفات ورق XML (XPS)، التي كانت تُعرف سابقًا باسم Metro والتي تضم مفهوم تسويق مسار الطباعة من الجيل التالي (NGPP)، مبادرة Microsoft لدمج إنشاء المستندات وعرضها في نظام تشغيل Windows الخاص بها.

يعرض مقتطف الشفرة التالي عملية تحويل ملف XPS إلى تنسيق PDF باستخدام Python.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XPS_to_PDF(infile, outfile):
    load_options = ap.XpsLoadOptions()
    document = ap.Document(infile, load_options)
    document.save(outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل تنسيق XPS إلى PDF عبر الإنترنت**

Aspose.PDF لبيثون عبر.NET يقدم لك التطبيق عبر الإنترنت [«XPS إلى PDF»](https://products.aspose.app/pdf/conversion/xps-to-pdf/)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل XPS إلى PDF باستخدام التطبيق](xps_to_pdf.png)](https://products.aspose.app/pdf/conversion/xps-to-pdf/)
{{% /alert %}}

## تحويل XSL-FO إلى PDF

يمكن استخدام مقتطف الشفرة التالي لتحويل XSLFO إلى تنسيق PDF باستخدام Aspose.PDF لـ Python عبر .NET:

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## تحويل XML مع XSLT إلى PDF

يوضح هذا المثال كيفية تحويل ملف XML إلى PDF عن طريق تحويله أولاً إلى HTML باستخدام قالب XSLT ثم تحميل HTML إلى Aspose.PDF.

1. قم بإنشاء مثيل من «HtmlLoadOptions» لتكوين تحويل HTML إلى PDF.
1. قم بتحميل ملف HTML المحول إلى كائن مستند Aspose.PDF.
1. احفظ المستند كملف PDF في مسار الإخراج المحدد.
1. قم بإزالة ملف HTML المؤقت بعد التحويل الناجح.

```python
from os import path, remove
import aspose.pdf as ap
import sys

def convert_XSLFO_to_PDF(xsltfile, xmlfile, outfile):
    load_options = ap.XslFoLoadOptions(xsltfile)
    load_options.parsing_errors_handling_type = (
        ap.XslFoLoadOptions.ParsingErrorsHandlingTypes.THROW_EXCEPTION_IMMEDIATELY
    )
    document = ap.Document(xmlfile, load_options)
    document.save(outfile)

    print(xmlfile + " converted into " + outfile)
```

## التحويلات ذات الصلة

- [تحويل HTML إلى PDF](/pdf/ar/python-net/convert-html-to-pdf/) لسيناريوهات تحويل HTML و MHTML.
- [تحويل تنسيقات الصور إلى PDF](/pdf/ar/python-net/convert-images-format-to-pdf/) عندما تكون المدخلات الخاصة بك هي PNG أو JPEG أو TIFF أو SVG أو صور أخرى.
- [تحويل PDF إلى تنسيقات أخرى](/pdf/ar/python-net/convert-pdf-to-other-files/) إذا كنت بحاجة أيضًا إلى تحويلات عكسية مثل PDF إلى EPUB أو Markdown أو النص.
