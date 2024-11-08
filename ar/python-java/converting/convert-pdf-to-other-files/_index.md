---
title: تحويل PDF إلى EPUB وLaTeX ونص وXPS في بايثون
linktitle: تحويل PDF إلى صيغ أخرى
type: docs
weight: 90
url: /ar/python-java/convert-pdf-to-other-files/
lastmod: "2023-04-06"
keywords: تحويل, PDF, EPUB, LaText, نص, XPS, بايثون
description: يوضح هذا الموضوع كيفية تحويل ملف PDF إلى صيغ ملفات أخرى مثل EPUB وLaTeX ونص وXPS وغيرها باستخدام بايثون.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

## تحويل PDF إلى EPUB

{{% alert color="success" %}}
**جرب تحويل PDF إلى EPUB عبر الإنترنت**

تقدم Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى EPUB باستخدام تطبيق مجاني](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

**<abbr title="Electronic Publication">EPUB</abbr>** هو معيار كتاب إلكتروني مجاني ومفتوح من المنتدى الدولي للنشر الرقمي (IDPF).
 ملفات لها الامتداد .epub.  
تم تصميم EPUB للمحتوى القابل لإعادة التدفق، مما يعني أن قارئ EPUB يمكنه تحسين النص لجهاز عرض معين. كما يدعم EPUB محتوى التخطيط الثابت. يهدف التنسيق ليكون تنسيقًا فرديًا يمكن للناشرين وبيوت التحويل استخدامه داخليًا، وكذلك للتوزيع والبيع. إنه يحل محل معيار Open eBook.

يدعم Aspose.PDF لـ Python أيضًا ميزة تحويل مستندات PDF إلى تنسيق EPUB. يحتوي Aspose.PDF لـ Python على فئة باسم 'EpubSaveOptions' التي يمكن استخدامها كحجة ثانية في طريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods)، لإنشاء ملف EPUB. يرجى محاولة استخدام جزء الشيفرة التالي لتحقيق هذا المتطلب باستخدام Python.

```python

from asposepdf import Api

# تهيئة الرخصة
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

# التحويل إلى Epub
documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.epub"
doc.save(documentOutName, Api.SaveFormat.Epub)
```

## تحويل PDF إلى LaTeX/TeX

**Aspose.PDF for Python عبر Java** يدعم تحويل PDF إلى LaTeX/TeX. 
تنسيق ملف LaTeX هو تنسيق ملف نصي مع علامات خاصة ويُستخدم في نظام إعداد المستندات القائم على TeX للطباعة عالية الجودة.

{{% alert color="success" %}}
**جرب تحويل PDF إلى LaTeX/TeX عبر الإنترنت**

تقدم لك Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex)، حيث يمكنك تجربة استكشاف الوظائف والجودة التي يعمل بها.

[![Aspose.PDF تحويل PDF إلى LaTeX/TeX مع تطبيق مجاني](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

لتحويل ملفات PDF إلى TeX، لدى Aspose.PDF الفئة [LaTeXSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/latexsaveoptions/) التي توفر الخاصية OutDirectoryPath لحفظ الصور المؤقتة أثناء عملية التحويل.

يوضح المقتطف التالي عملية تحويل ملفات PDF إلى تنسيق TEX باستخدام Python.

```python
from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "testout/out.tex"
doc.save(documentOutName, Api.SaveFormat.TeX)
```

## تحويل PDF إلى نص

**Aspose.PDF for Python** يدعم تحويل مستند PDF بالكامل وصفحة واحدة إلى ملف نصي.

### تحويل مستند PDF إلى ملف نصي

يمكنك تحويل مستند PDF إلى ملف TXT باستخدام فئة 'TextDevice'.

يشرح جزء الشيفرة التالي كيفية استخراج النصوص من جميع الصفحات.

```python

from asposepdf import Api, Device

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "source.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_text"
# فتح مستند PDF
document = Api.Document(input_pdf)

device = Device.TextDevice()

for i in range(0, document.getPages.size):
    imageFileName = output_pdf + "_page_" + str(i + 1) + "_out.txt"
    # تحويل صفحة معينة وحفظها كملف نصي
    device.process(document.getPages.getPage(i + 1), imageFileName)
```

{{% alert color="success" %}}
**حاول تحويل تحويل PDF إلى نص عبر الإنترنت**

تقدم لك Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى نص"](https://products.aspose.app/pdf/conversion/pdf-to-txt)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى نص باستخدام التطبيق المجاني](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## تحويل PDF إلى XPS

**Aspose.PDF لـ Python** يتيح إمكانية تحويل ملفات PDF إلى تنسيق <abbr title="تحديد ورقة XML">XPS</abbr>. دعونا نحاول استخدام الكود المقدم لتحويل ملفات PDF إلى تنسيق XPS باستخدام Python.

{{% alert color="success" %}}
**حاول تحويل PDF إلى XPS عبر الإنترنت**

تقدم لك Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تحويل Aspose.PDF من PDF إلى XPS باستخدام التطبيق المجاني](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

نوع ملف XPS مرتبط بشكل أساسي بمواصفات ورق XML من قبل شركة Microsoft Corporation. مواصفات ورق XML (XPS)، التي كانت تُعرف سابقاً بالاسم الرمزي Metro وتتضمن مفهوم التسويق Next Generation Print Path (NGPP)، هي مبادرة من مايكروسوفت لدمج إنشاء وعرض المستندات في نظام تشغيل Windows.

لتحويل ملفات PDF إلى XPS، تحتوي Aspose.PDF على الفئة [XpsSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/xpssaveoptions/) التي تُستخدم كوسيط ثانٍ للطريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods) لإنشاء ملف XPS.

يوضح مقتطف الشفرة التالي عملية تحويل ملف PDF إلى تنسيق XPS.

```python

from asposepdf import Api

documentName = "../../testdata/Hello.pdf"
doc = Api.Document(documentName, None)
documentOutName = "../../testout/out.xps"
doc.save(documentOutName, Api.SaveFormat.Xps)

```