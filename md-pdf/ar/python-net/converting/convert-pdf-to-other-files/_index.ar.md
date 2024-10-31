---
title: تحويل PDF إلى EPUB، LaTeX، نص، XPS باستخدام بايثون
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /python-net/convert-pdf-to-other-files/
lastmod: "2022-12-23"
keywords: تحويل، PDF، EPUB، LaTeX، نص، XPS، بايثون
description: يوضح لك هذا الموضوع كيفية تحويل ملف PDF إلى صيغ ملفات أخرى مثل EPUB، LaTeX، نص، XPS إلخ باستخدام بايثون.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**جرب تحويل PDF إلى EPUB عبر الإنترنت**

تقدم Aspose.PDF لبايثون تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك تجربة استكشاف الوظيفة والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى EPUB مع تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** هو معيار مفتوح ومجاني للكتب الإلكترونية من منتدى النشر الرقمي الدولي (IDPF).
 الملفات لها الامتداد .epub.  
تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. كما يدعم EPUB المحتوى ذو التخطيط الثابت. يهدف التنسيق ليكون تنسيقًا واحدًا يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. يحل محل المعيار Open eBook.

يدعم Aspose.PDF for Python أيضًا إمكانية تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF for Python على فئة تسمى 'EpubSaveOptions' والتي يمكن استخدامها كالحجة الثانية لطريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)، لإنشاء ملف EPUB.  
يرجى محاولة استخدام مقطع الشفرة التالي لتحقيق هذا المتطلب باستخدام بايثون.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_epub.epub"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء خيارات حفظ EPUB
    save_options = ap.EpubSaveOptions()

    # تحديد التخطيط للمحتويات
    save_options.content_recognition_mode = ap.EpubSaveOptions.RecognitionMode.FLOW

    # احفظ مستند ePUB
    document.save(output_pdf, save_options)
```

## تحويل PDF إلى LaTeX/TeX

**Aspose.PDF for Python عبر .NET** يدعم تحويل PDF إلى LaTeX/TeX. 
تنسيق ملف LaTeX هو تنسيق ملف نصي مع ترميز خاص ويُستخدم في نظام إعداد الوثائق المستند إلى TeX لتنسيق عالي الجودة.

{{% alert color="success" %}}
**حاول تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

يقدم لك Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى LaTeX/TeX باستخدام تطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

لتحويل ملفات PDF إلى TeX، يحتوي Aspose.PDF على الفئة [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) التي توفر الخاصية OutDirectoryPath لحفظ الصور المؤقتة أثناء عملية التحويل.

يوضح الجزء التالي من الكود عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام Python.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_tex.tex"
    # فتح مستند PDF
    document = ap.Document(input_pdf)
    # إنشاء كائن من LaTeXSaveOptions
    saveOptions = ap.LaTeXSaveOptions()
    document.save(output_pdf, saveOptions)
```

## تحويل PDF إلى نص

**Aspose.PDF for Python** يدعم تحويل مستند PDF بالكامل وصفحة واحدة إلى ملف نصي.

### تحويل مستند PDF إلى ملف نص

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام فئة 'TextDevice'.

يوضح مقتطف الشيفرة التالي كيفية استخراج النصوص من كل الصفحات.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf =  DIR_OUTPUT + "convert_pdf_to_txt.txt"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء جهاز نصي
    textDevice = ap.devices.TextDevice()

    # تحويل صفحة معينة وحفظها
    textDevice.process(document.pages[1], output_pdf)

**حاول تحويل PDF إلى نص عبر الإنترنت**

يقدم لك Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to Text"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى نص باستخدام تطبيق مجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى XPS

يوفر **Aspose.PDF لـ Python** إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="XML Paper Specification">XPS</abbr>. دعنا نحاول استخدام مقتطف الشفرة المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام Python.

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

يقدم لك Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى XPS باستخدام تطبيق مجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

نوع ملف XPS مرتبط بشكل أساسي بمواصفات ورق XML من قبل شركة Microsoft Corporation. مواصفات ورق XML (XPS)، التي كانت تحمل الاسم الرمزي Metro سابقًا وتشمل مفهوم التسويق Next Generation Print Path (NGPP)، هي مبادرة من Microsoft لدمج إنشاء المستندات وعرضها في نظام التشغيل Windows.

لتحويل ملفات PDF إلى XPS، يتوافر في Aspose.PDF الفئة [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) التي تُستخدم كحجة ثانية لطريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لتوليد ملف XPS.

يظهر مقطع الشيفرة التالي عملية تحويل ملف PDF إلى تنسيق XPS.

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_xps.xps"
    # فتح مستند PDF
    document = ap.Document(input_pdf)

    # إنشاء خيارات الحفظ لـ XPS
    save_options = ap.XpsSaveOptions()

    # حفظ مستند XPS
    document.save(output_pdf, save_options)
```

## تحويل PDF إلى XML

{{% alert color="success" %}}
**حاول تحويل PDF إلى XML عبر الإنترنت**

يقدم Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to XML"](https://products.aspose.app/pdf/conversion/pdf-to-xml)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى XML مع تطبيق مجاني](pdf_to_xml.png)](https://products.aspose.app/pdf/conversion/pdf-to-xml)
{{% /alert %}}

<abbr title="لغة الترميز الموسعة">XML</abbr> هي لغة ترميز وصيغة ملف لتخزين ونقل وإعادة بناء البيانات العشوائية.

يدعم Aspose.PDF لـ Python أيضًا ميزة تحويل مستندات PDF إلى صيغة XML. يحتوي Aspose.PDF لـ Python على فئة تُسمى 'XmlSaveOptions' والتي يمكن استخدامها كوسيط ثاني لطريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods)، لإنشاء ملف XML. يرجى محاولة استخدام الجزء التالي من الشيفرة البرمجية لتحقيق هذا المتطلب باستخدام Python.

```python

    import aspose.pdf as ap

    def convert_pdf_to_xml(self, infile, outfile):
        path_infile = self.dataDir + infile
        path_outfile = self.dataDir + outfile

        # فتح مستند PDF

        document = ap.Document(path_infile)

        # إنشاء خيارات حفظ XML
        save_options = ap.XmlSaveOptions()

        # حفظ مستند XML
        document.save(path_outfile, save_options)
        print(infile + " تم تحويله إلى " + outfile)
```