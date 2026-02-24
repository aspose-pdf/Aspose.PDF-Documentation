---
title: تحويل PDF إلى EPUB، LaTeX، نص، XPS باستخدام بايثون
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /ar/python-net/convert-pdf-to-other-files/
lastmod: "2025-09-27"
description: يظهر هذا الموضوع لك كيفية تحويل ملف PDF إلى صيغ ملفات أخرى مثل EPUB، LaTeX، نص، XPS وغيرها باستخدام بايثون.
sitemap: 
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى صيغ أخرى باستخدام بايثون
Abstract: توفر المقالة دليلًا شاملاً حول تحويل ملفات PDF إلى صيغ مختلفة باستخدام Aspose.PDF للبايثون. تغطي عملية تحويل ملفات PDF إلى صيغ EPUB، LaTeX/TeX، نص، XPS، وXML. يبدأ كل قسم بدعوة لتجربة التطبيقات المجانية عبر الإنترنت التي تقدمها Aspose لتحويل ملفات PDF إلى الصيغ المعنية، مع إبراز سهولة الاستخدام وجودة هذه الأدوات.
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**جرّب تحويل PDF إلى EPUB عبر الإنترنت**

تقدم لك Aspose.PDF للبايثون تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك تجربة الوظيفة والجودة.

[![تحويل Aspose.PDF PDF إلى EPUB مع التطبيق المجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

<abbr title="Electronic Publication">EPUB</abbr> هو معيار مجاني ومفتوح للكتب الإلكترونية من المنتدى الدولي للنشر الرقمي (IDPF). الملفات لها الامتداد .epub.
تم تصميم EPUB للمحتوى القابل لإعادة التدفق، أي أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. يدعم EPUB أيضًا المحتوى ذو التخطيط الثابت. يهدف هذا التنسيق إلى أن يكون تنسيقًا واحدًا يمكن للناشرين ومكاتب التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. وهو يحل محل معيار Open eBook.

يدعم Aspose.PDF للبايثون أيضًا إمكانية تحويل مستندات PDF إلى صيغة EPUB. يحتوي Aspose.PDF للبايثون على فئة تسمى 'EpubSaveOptions' يمكن استخدامها كمعامل ثانٍ لطريقة [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لإنشاء ملف EPUB.
يرجى تجربة استخدام مقتطف الشيفرة التالي لتحقيق هذا المتطلب باستخدام بايثون.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.EpubSaveOptions()
    save_options.content_recognition_mode = (
        ap.EpubSaveOptions.RecognitionMode.FLOW
    )
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى LaTeX/TeX

**يدعم Aspose.PDF للبايثون عبر .NET تحويل PDF إلى LaTeX/TeX**
تنسيق ملف LaTeX هو تنسيق ملف نصي يحتوي على علامات خاصة ويُستخدم في نظام إعداد المستندات القائم على TeX لتحقيق تنضيد عالي الجودة.

{{% alert color="success" %}}
**جرّب تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

تقدم لك Aspose.PDF للبايثون تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك تجربة الوظيفة والجودة.

[![تحويل Aspose.PDF PDF إلى LaTeX/TeX مع التطبيق المجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

لتحويل ملفات PDF إلى TeX، يمتلك Aspose.PDF الفئة [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/latexsaveoptions/) التي توفر الخاصية OutDirectoryPath لحفظ الصور المؤقتة أثناء عملية التحويل.

يُظهر مقتطف الشيفرة التالي عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام بايثون.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.LaTeXSaveOptions()

    document.save(path_outfile, save_options)
    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى نص

**يدعم Aspose.PDF للبايثون** تحويل مستند PDF كامل أو صفحة واحدة إلى ملف نص. يمكنك تحويل مستند PDF إلى ملف TXT باستخدام الفئة 'TextDevice'. يشرح مقتطف الشيفرة التالي كيفية استخراج النصوص من جميع الصفحات.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    device = ap.devices.TextDevice()
    device.process(document.pages[1], path_outfile)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرّب تحويل PDF إلى نص عبر الإنترنت**

تقدم لك Aspose.PDF للبايثون تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى نص"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك تجربة الوظيفة والجودة.

[![تحويل Aspose.PDF PDF إلى نص مع التطبيق المجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى XPS

**يمنح Aspose.PDF للبايثون** إمكانية تحويل ملفات PDF إلى صيغة XPS. دعنا نجرب استخدام مقتطف الشيفرة المعروض لتحويل ملفات PDF إلى صيغة XPS باستخدام بايثون.

{{% alert color="success" %}}
**جرّب تحويل PDF إلى XPS عبر الإنترنت**

تقدم لك Aspose.PDF للبايثون تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك تجربة الوظيفة والجودة.

[![تحويل Aspose.PDF PDF إلى XPS مع التطبيق المجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

نوع ملف XPS مرتبط أساسًا بمواصفة الورق XML من شركة مايكروسوفت. مواصفة الورق XML (XPS)، التي كان اسمها الرمزي السابق Metro وتضم مفهوم مسار الطباعة الجيل التالي (NGPP)، هي مبادرة مايكروسوفت لدمج إنشاء المستندات وعرضها في نظام تشغيل Windows.

لتحويل ملفات PDF إلى XPS، يمتلك Aspose.PDF الفئة [XpsSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/xpssaveoptions/) التي تُستخدم كمعامل ثانٍ لطريقة [document.save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods) لإنشاء ملف XPS.

يُظهر مقتطف الشيفرة التالي عملية تحويل ملف PDF إلى صيغة XPS.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.XpsSaveOptions()
    save_options.use_new_imaging_engine = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

## تحويل PDF إلى MD

تحتوي Aspose.PDF على الفئة 'MarkdownSaveOptions()'، التي تقوم بتحويل مستند PDF إلى تنسيق Markdown (MD) مع الحفاظ على الصور والموارد.

1. احمل ملف PDF المصدر باستخدام 'ap.Document'.
1. أنشئ مثيلاً من 'MarkdownSaveOptions'.
1. عين 'resources_directory_name' إلى 'images' – سيتم تخزين الصور المستخرجة في هذا المجلد.
1. احفظ مستند Markdown المحوَّل باستخدام الخيارات المُكوَّنة.
1. اطبع رسالة تأكيد بعد التحويل.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    save_options = ap.MarkdownSaveOptions()
    # save_options.extract_vector_graphics = True
    save_options.resources_directory_name = "images"
    save_options.use_image_html_tag = True
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

ملف Markdown يحتوي على نص وصور مرتبطة مخزنة في مجلد الصور المحدد.

## تحويل PDF إلى MobiXML

هذه الطريقة تحوِّل مستند PDF إلى تنسيق MOBI (MobiXML)، والذي يُستخدم عادةً للكتب الإلكترونية على أجهزة Kindle.

1. احمل مستند PDF المصدر باستخدام 'ap.Document'.
1. احفظ المستند بالتنسيق 'ap.SaveFormat.MOBI_XML'.
1. اطبع رسالة تأكيد بمجرد اكتمال التحويل.

```python

    from os import path
    import aspose.pdf as ap

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = ap.Document(path_infile)
    document.save(path_outfile, ap.SaveFormat.MOBI_XML)

    print(infile + " converted into " + outfile)
```
