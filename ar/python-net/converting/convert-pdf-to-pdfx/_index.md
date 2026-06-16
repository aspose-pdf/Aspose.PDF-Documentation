---
title: تحويل ملفات PDF إلى ملفات PDF/A وPDF/E وPDF/X بلغة بايثون
linktitle: تحويل ملفات PDF إلى ملفات PDF/A وPDF/E وPDF/X
type: docs
weight: 120
url: /ar/python-net/convert-pdf-to-pdf_x/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل ملفات PDF إلى PDF/A و PDF/E و PDF/X في Python باستخدام Aspose.PDF لـ Python عبر .NET للأرشفة وإمكانية الوصول وعمليات سير عمل الطباعة.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى تنسيقات PDF/x
Abstract: توفر المقالة دليلًا شاملاً حول تحويل PDF إلى تنسيقات PDF/A و PDF/E و PDF/X باستخدام Aspose.PDF لبيثون.
---

** صيغة PDF إلى PDF/x تعني القدرة على تحويل PDF إلى تنسيقات إضافية، وهي PDF/A و PDF/E و PDF/X.**

## تحويل ملفات PDF إلى PDF/A

**aspose.pdf لبيثون** يسمح لك بتحويل ملف PDF إلى ملف <abbr title="Portable Document Format / A">ملف PDF\ A</abbr> ملف PDF متوافق. قبل القيام بذلك، يجب التحقق من صحة الملف. يشرح هذا الموضوع كيفية القيام بذلك.

{{% alert color="primary" %}}

يرجى ملاحظة أننا نتبع Adobe Preflight للتحقق من توافق PDF/A. جميع الأدوات الموجودة في السوق لها «تمثيل» خاص بها لتوافق PDF/A. يرجى مراجعة هذه المقالة حول أدوات التحقق من PDF/A كمرجع. لقد اخترنا منتجات Adobe للتحقق من كيفية إنتاج Aspose.PDF لملفات PDF لأن Adobe هي مركز كل شيء متصل بـ PDF.

{{% /alert %}}

قم بتحويل الملف باستخدام طريقة تحويل فئة المستند. قبل تحويل PDF إلى ملف متوافق مع PDF/A، تحقق من صحة PDF باستخدام طريقة التحقق. يتم تخزين نتيجة التحقق في ملف XML ثم يتم تمرير هذه النتيجة أيضًا إلى طريقة التحويل. يمكنك أيضًا تحديد الإجراء للعناصر التي لا يمكن تحويلها باستخدام تعداد ConverterRorAction.

{{% alert color="success" %}}
** حاول تحويل PDF إلى PDF/A عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«PDF إلى PDF/A-1A»](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل ملفات PDF إلى PDF/A مع التطبيق](pdf_to_pdfa.png)](https://products.aspose.app/pdf/conversion/pdf-to-pdfa1a)
{{% /alert %}}

تقوم طريقة 'document.validate () 'بالتحقق مما إذا كان ملف PDF يتوافق مع معيار PDF/A-1B (إصدار معياري من ISO من PDF مصمم للأرشفة طويلة الأجل). يتم حفظ نتائج التحقق في ملف سجل.

### تحويل ملفات PDF إلى PDF/A-1B

يوضح مقتطف الشفرة التالي كيفية تحويل ملفات PDF إلى تنسيق PDF/A-1B:

1. قم بتحميل مستند PDF باستخدام «AP.document».
1. اتصل بطريقة التحويل باستخدام المعلمات التالية:
    - مسار ملف السجل - يخزن تفاصيل عملية التحويل وفحوصات الامتثال.
    - التنسيق الهدف - 'AP.pdfformat.pdf_a_1b' (معيار أرشيفي).
    - إجراء الخطأ - 'AP.Converterroraction.delete' - يزيل تلقائيًا العناصر التي تمنع الامتثال.
1. احفظ الملف المحول المتوافق مع PDF/A إلى مسار الإخراج.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA(infile, outfile):
    """Convert PDF to PDF/A-1B format."""

    document = ap.Document(infile)
    document.convert(
        outfile.replace(".pdf", "-log.xml"),
        ap.PdfFormat.PDF_A_1B,
        ap.ConvertErrorAction.DELETE,
    )
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

### تحويل ملفات PDF إلى PDF 2.0 وPDF/A-4

يوضح هذا المثال كيفية تحويل مستند PDF إلى تنسيقات قياسية جديدة: PDF 2.0 و PDF/A-4.
يساعد كلا التحويلين على ضمان الامتثال للمواصفات الحديثة ومتطلبات الأرشفة.

1. قم بتحميل مستند الإدخال باستخدام AP.document.
1. قم بإجراء التحويل الأول إلى PDF 2.0 عن طريق استدعاء document.convert باستخدام:
    - مسار ملف السجل للحصول على تفاصيل التحويل.
    - التنسيق المستهدف - 'AP.pdfformat.v_2_0'.
    - إجراء الخطأ - 'AP.ConverterRoraction.delete' لإزالة العناصر غير المتوافقة.
1. قم بإجراء تحويل ثانٍ إلى PDF/A-4 باستخدام نفس الطريقة، مع التأكد من أن الملف متوافق أيضًا مع معايير الأرشفة.
1. احفظ المستند الناتج في مسار الإخراج المحدد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA4(infile, outfile):
    logfile = outfile.replace(".pdf", "_log.xml")

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.V_2_0, ap.ConvertErrorAction.DELETE)
    document.convert(logfile, ap.PdfFormat.PDF_A_4, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### تحويل PDF إلى PDF/A-3A باستخدام الملفات المضمنة

يوضح مقتطف الشفرة التالي كيفية تضمين الملفات الخارجية في PDF ثم تحويل PDF إلى تنسيق PDF/A-3A، والذي يدعم المرفقات ومناسب للأرشفة طويلة المدى مع المحتوى المضمن.

1. قم بتحميل ملف PDF المُدخل باستخدام «AP.document».
1. قم بإنشاء كائن «FileEspecification» يشير إلى الملف لتضمينه (على سبيل المثال، "aspose-logo.jpg «) مع الوصف.
1. أضف مواصفات الملف إلى مجموعة «embedded_files» الخاصة بـ PDF.
1. قم بتحويل المستند إلى PDF/A-3A باستخدام «document.convert»، مع تحديد:
    - مسار ملف السجل.
    - التنسيق المستهدف - 'AP.pdfformat.pdf_a_3a'.
    - إجراء الخطأ - 'AP.ConverterRoraction.delete' لإزالة العناصر غير المتوافقة.
1. احفظ ملف PDF المحول إلى مسار الإخراج.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_attachment(infile, attachement_file, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    document = ap.Document(infile)

    fileSpecification = ap.FileSpecification(attachement_file, "Large Image file")
    document.embedded_files.add(fileSpecification)
    document.convert(
        logfile, ap.PdfFormat.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE
    )
    document.save(outfile)
```

### تحويل PDF إلى PDF/A-1B مع استبدال الخط

تقوم هذه الوظيفة بتحويل PDF إلى تنسيق PDF/A-1B أثناء معالجة الخطوط المفقودة عن طريق استبدالها بالخطوط المتاحة. هذا يضمن بقاء ملف PDF المحول متسقًا بصريًا ومتوافقًا مع معايير الأرشفة.

1. قم بتحميل ملف PDF باستخدام «AP.document».
1. قم بتحويل ملف PDF إلى PDF/A-1B باستخدام «document.convert»، مع تحديد:
    - مسار ملف السجل.
    - التنسيق المستهدف - 'AP.pdfformat.pdf_a_1b'.
    - إجراء الخطأ - 'AP.ConverterRoraction.delete' لإزالة العناصر غير المتوافقة.
1. احفظ ملف PDF المحول إلى مسار الإخراج.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_replace_missing_fonts(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")
    try:
        ap.text.FontRepository.find_font("AgencyFB")

    except ap.FontNotFoundException:
        font_substitution = ap.text.SimpleFontSubstitution("AgencyFB", "Arial")
        ap.text.FontRepository.Substitutions.append(font_substitution)

    document = ap.Document(infile)
    document.convert(logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```

### تحويل PDF إلى PDF/A-1B مع وضع العلامات التلقائي

تقوم هذه الوظيفة بتحويل مستند PDF إلى تنسيق PDF/A-1B مع وضع علامات على المحتوى تلقائيًا لإمكانية الوصول والاتساق الهيكلي. يعمل وضع العلامات التلقائي على تحسين قابلية استخدام المستندات لقارئات الشاشة ويضمن البنية الدلالية المناسبة.

1. قم بتحميل ملف PDF باستخدام «AP.document».
1. قم بإنشاء «خيارات تحويل تنسيق PDF» مع تحديد:
    - مسار ملف السجل.
    - التنسيق المستهدف - 'AP.pdfformat.pdf_a_1b'.
    - إجراء الخطأ - 'AP.ConverterRoraction.delete' لإزالة العناصر غير المتوافقة.
1. تكوين «إعدادات وضع العلامات التلقائية»:
    - تمكين «enable_auto_tagging = صحيح».
    - قم بتعيين 'heading_recognition_strategy = AUTO' لاكتشاف العناوين تلقائيًا.
1. قم بتعيين إعدادات وضع العلامات التلقائية لخيارات التحويل.
1. قم بتحويل ملف PDF باستخدام «document.convert (خيارات)».
1. احفظ ملف PDF المحول إلى مسار الإخراج.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDFA_with_automatic_tagging(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_A_1B, ap.ConvertErrorAction.DELETE
    )

    auto_tagging_settings = ap.AutoTaggingSettings()
    auto_tagging_settings.enable_auto_tagging = True

    auto_tagging_settings.heading_recognition_strategy = (
        ap.HeadingRecognitionStrategy.AUTO
    )

    options.auto_tagging_settings = auto_tagging_settings
    document.convert(options)
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## تحويل ملفات PDF إلى PDF/E

يوضح مقتطف الشفرة هذا كيفية تحويل مستند PDF إلى تنسيق PDF/E-1، وهو معيار ISO مصمم للتوثيق الهندسي والتقني. يحافظ هذا التنسيق على التخطيط الدقيق والرسومات والبيانات الوصفية المطلوبة لسير العمل الهندسي.

1. قم بتحميل ملف PDF المصدر باستخدام «AP.document».
1. قم بإنشاء «خيارات تحويل تنسيق PDF» مع تحديد:
    - مسار ملف السجل لتتبع مشكلات التحويل.
    - التنسيق المستهدف - 'AP.pdfformat.pdf_e_1'.
    - إجراء الخطأ - 'AP.ConverterRoraction.delete' لإزالة العناصر غير المتوافقة.
1. قم بتحويل ملف PDF باستخدام «document.convert (خيارات)».
1. احفظ ملف PDF المحول إلى مسار الإخراج المحدد.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_E(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_E_1, ap.ConvertErrorAction.DELETE
    )

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## تحويل ملفات PDF إلى PDF/X

يقوم مقتطف الشفرة التالي بتحويل مستند PDF إلى تنسيق PDF/X-4، وهو معيار ISO شائع الاستخدام في صناعة الطباعة والنشر. يضمن PDF/X-4 دقة الألوان ويحافظ على الشفافية ويدمج ملفات تعريف ICC للحصول على إخراج متسق عبر الأجهزة.

1. قم بتحميل ملف PDF المصدر باستخدام «AP.document».
1. قم بإنشاء «خيارات تحويل تنسيق PDF» مع تحديد:
    - مسار ملف السجل.
    - التنسيق المستهدف - 'AP.pdfformat.pdf_x_4'.
    - إجراء الخطأ - 'AP.ConverterRoraction.delete' لإزالة العناصر غير المتوافقة.
1. قم بتوفير ملف تعريف ICC** لإدارة الألوان عبر «icc_profile_file_name».
1. حدد **outputIntent** بمعرف الشرط (على سبيل المثال، «FOGRA39") لمتطلبات الطباعة.
1. قم بتحويل ملف PDF باستخدام «document.convert ()».
1. احفظ ملف PDF المحول إلى مسار الإخراج المحدد.
1. اطبع رسالة تأكيد.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_PDF_X(infile, outfile):
    logfile = outfile.replace(".pdf", "-log.xml")

    document = ap.Document(infile)
    options = ap.PdfFormatConversionOptions(
        logfile, ap.PdfFormat.PDF_X_4, ap.ConvertErrorAction.DELETE
    )

    # Provide the name of the external ICC profile file (optional)
    options.icc_profile_file_name = path.join(
        path.dirname(infile), "ISOcoated_v2_eci.icc"
    )
    # Provide an output condition identifier and other necessary OutputIntent properties (optional)
    options.output_intent = ap.OutputIntent("FOGRA39")

    document.convert(options)

    # Save PDF document
    document.save(outfile)
    print(infile + " converted into " + outfile)
```

## التحويلات ذات الصلة

- [تحويل ملفات PDF إلى وورد](/pdf/ar/python-net/convert-pdf-to-word/) لسير عمل المحتوى القابل للتحرير بعد التحقق من المعايير.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) عندما يكون الإخراج المستهدف جاهزًا للويب بدلاً من PDF المستند إلى المعايير.
