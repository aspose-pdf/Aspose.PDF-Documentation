---
title: قم بتحويل ملفات PDF إلى EPUB والنص وXPS والمزيد في بايثون
linktitle: تحويل PDF إلى تنسيقات أخرى
type: docs
weight: 90
url: /ar/python-net/convert-pdf-to-other-files/
lastmod: "2026-06-11"
description: تعرف على كيفية تحويل ملفات PDF إلى ملفات EPUB وLaTeX وMarkdown والنص وXPS وMobiXML بلغة بايثون باستخدام Aspose.PDF لبيثون عبر .NET.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى تنسيقات أخرى في Python
Abstract: توفر المقالة دليلًا شاملاً حول تحويل ملفات PDF إلى تنسيقات مختلفة باستخدام Aspose.PDF لـ Python. وهو يغطي تحويل ملفات PDF إلى تنسيقات EPUB وLaTEX/TEX والنص وXPS وXML. يبدأ كل قسم بدعوة لتجربة التطبيقات عبر الإنترنت التي تقدمها Aspose لتحويل ملفات PDF إلى التنسيقات المعنية، مع إبراز سهولة استخدام وجودة هذه الأدوات.
---

## تحويل ملفات PDF إلى EPUB

{{% alert color="success" %}}
** حاول تحويل PDF إلى EPUB عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«من PDF إلى EPUB»](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل ملف PDF إلى EPUB باستخدام التطبيق](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">النشر الإلكتروني</abbr> هو معيار الكتاب الإلكتروني المجاني والمفتوح من المنتدى الدولي للنشر الرقمي (IDPF). تحتوي الملفات على الامتداد.epub.
تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. يدعم EPUB أيضًا محتوى التخطيط الثابت. الغرض من التنسيق هو التنسيق الوحيد الذي يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. إنه يحل محل معيار الكتاب الإلكتروني المفتوح.

يدعم Aspose.PDF لـ Python أيضًا ميزة تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF لبيثون على فئة تسمى «ePubSaveOptions» والتي يمكن استخدامها كوسيطة ثانية لـ [حفظ المستند ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) الطريقة، لإنشاء ملف EPUB.
يرجى محاولة استخدام مقتطف الشفرة التالي لإنجاز هذا المطلب باستخدام Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_EPUB(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## التحويلات ذات الصلة

- [تحويل ملفات PDF إلى وورد](/pdf/ar/python-net/convert-pdf-to-word/) لإخراج مستندات مكتبية قابلة للتحرير.
- [تحويل ملفات PDF إلى HTML](/pdf/ar/python-net/convert-pdf-to-html/) للإخراج الموجه للمتصفح.
- [تحويل ملفات PDF إلى ملفات PDF/A وPDF/E وPDF/X](/pdf/ar/python-net/convert-pdf-to-pdf_x/) لعمليات سير عمل التحويل الأرشيفية والمتوافقة مع المعايير.

## تحويل PDF إلى لاتكس/تكس

**Aspose.pdf لبيثون عبر .NET** يدعم تحويل PDF إلى لاتكس/تكس.
تنسيق ملف LaTeX هو تنسيق ملف نصي بترميز خاص ويستخدم في نظام إعداد المستندات المستند إلى TEX لتنضيد عالي الجودة.

{{% alert color="success" %}}
** حاول تحويل PDF إلى LaTEX/TEX عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«PDF إلى LaTeX»](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF - تحويل ملفات PDF إلى مادة اللاتكس/النص باستخدام التطبيق](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

لتحويل ملفات PDF إلى TeX، يحتوي Aspose.PDF على الفصل [خيارات حفظ اللاتكس](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) الذي يوفر الخاصية outDirectoryPath لحفظ الصور المؤقتة أثناء عملية التحويل.

يعرض مقتطف الشفرة التالي عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام Python.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TeX(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.LaTeXSaveOptions()
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى نص

**Aspose.pdf لـ Python** يدعم تحويل مستند PDF بالكامل وصفحة واحدة إلى ملف نصي. يمكنك تحويل مستند PDF إلى ملف TXT باستخدام فئة «TextDevice». يشرح مقتطف الشفرة التالي كيفية استخراج النصوص من جميع الصفحات.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_TXT(infile, outfile):
    document = ap.Document(infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
** حاول تحويل ملف PDF إلى نص عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«تحويل ملف PDF إلى نص»](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![Aspose.PDF تحويل PDF إلى نص باستخدام التطبيق](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل ملفات PDF إلى XPS

**aspose.pdf لبيثون** يتيح إمكانية تحويل ملفات PDF إلى صيغة XPS. دعنا نحاول استخدام مقتطف الشفرة المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام Python.

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

Aspose.PDF لبيثون يقدم لك التطبيق عبر الإنترنت [«من PDF إلى XPS»](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة التحقق من الوظائف والجودة التي تعمل بها.

[![تحويل ملف Aspose.PDF إلى ملفات PDF إلى XPS باستخدام التطبيق](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

يرتبط نوع ملف XPS بشكل أساسي بمواصفات ورق XML من قبل شركة Microsoft Corporation. تعد مواصفات ورق XML (XPS)، التي كانت تُعرف سابقًا باسم Metro والتي تضم مفهوم تسويق مسار الطباعة من الجيل التالي (NGPP)، مبادرة Microsoft لدمج إنشاء المستندات وعرضها في نظام تشغيل Windows.

لتحويل ملفات PDF إلى XPS، يحتوي Aspose.PDF على الفئة [خيارات الحفظ في XPS](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) يتم استخدامها كحجة ثانية لـ [حفظ المستند ()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) طريقة لإنشاء ملف XPS.

يعرض مقتطف الشفرة التالي عملية تحويل ملف PDF إلى تنسيق XPS.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_XPS(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل ملفات PDF إلى MD

يحتوي Aspose.PDF على فئة «MarkdownSaveOptions ()»، والتي تقوم بتحويل مستند PDF إلى تنسيق Markdown (MD) مع الحفاظ على الصور والموارد.

1. قم بتحميل ملف PDF المصدر باستخدام «AP.document».
1. قم بإنشاء مثيل لـ «خيارات MarkdownSaveOptions».
1. قم بتعيين «resources_directory_name» إلى «الصور» - سيتم تخزين الصور المستخرجة في هذا المجلد.
1. احفظ مستند Markdown المحول باستخدام الخيارات التي تم تكوينها.
1. اطبع رسالة تأكيد بعد التحويل.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MD(infile, outfile):
    document = ap.Document(infile)
    save_options = ap.MarkdownSaveOptions()
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(outfile, save_options)

    print(infile + " converted into " + outfile)
```

ملف Markdown يحتوي على نص وصور مرتبطة مخزنة في مجلد الصور المحدد.

## تحويل ملفات PDF إلى موبيكسمل

تقوم هذه الطريقة بتحويل مستند PDF إلى تنسيق MOBI (MobiXML)، والذي يشيع استخدامه للكتب الإلكترونية على أجهزة Kindle.

1. قم بتحميل مستند PDF المصدر باستخدام «AP.document».
1. احفظ المستند بالتنسيق «AP.SaveFormat.mobi_XML».
1. اطبع رسالة تأكيد بمجرد اكتمال التحويل.

```python
import aspose.pdf as ap
from os import path
import sys

def convert_PDF_to_MobiXML(infile, outfile):
    document = ap.Document(infile)
    document.save(outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
