---
title: تحويل ملفات PDF إلى مستندات Microsoft Word باستخدام بايثون
linktitle: تحويل PDF إلى Word 2003/2019
type: docs
weight: 10
url: /python-net/convert-pdf-to-word/
lastmod: "2022-12-23"
description: تعلم كيفية كتابة كود بايثون لتحويل تنسيقات PDF إلى Microsoft Word باستخدام Aspose.PDF لـ Python عبر .NET. وتحسين تحويل PDF إلى DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

تشرح هذه المقالة كيفية **تحويل PDF إلى مستندات Microsoft Word باستخدام بايثون**. وهي تغطي هذه المواضيع.

_تنسيق_: **DOC**
- [بايثون PDF إلى DOC](#python-pdf-to-doc)
- [بايثون تحويل PDF إلى DOC](#python-pdf-to-doc)
- [بايثون كيفية تحويل ملف PDF إلى DOC](#python-pdf-to-doc)

_تنسيق_: **DOCX**
- [بايثون PDF إلى DOCX](#python-pdf-to-docx)
- [بايثون تحويل PDF إلى DOCX](#python-pdf-to-docx)
- [بايثون كيفية تحويل ملف PDF إلى DOCX](#python-pdf-to-docx)

_تنسيق_: **Word**
- [بايثون PDF إلى Word](#python-pdf-to-docx)
- [بايثون تحويل PDF إلى Word](#python-pdf-to-doc)

- [بايثون كيفية تحويل ملف PDF إلى Word](#python-pdf-to-docx)

## تحويل PDF إلى DOC و DOCX باستخدام Python

من أكثر الميزات شهرة هي تحويل PDF إلى Microsoft Word DOC، مما يجعل إدارة المحتوى أسهل. **Aspose.PDF for Python** يتيح لك تحويل ملفات PDF ليس فقط إلى DOC بل أيضًا إلى تنسيق DOCX بسهولة وكفاءة.

## تحويل ملف PDF إلى DOC (Word 97-2003)

قم بتحويل ملف PDF إلى تنسيق DOC بسهولة وتحكم كامل. Aspose.PDF for Python مرن ويدعم مجموعة واسعة من التحويلات. تحويل الصفحات من مستندات PDF إلى صور، على سبيل المثال، هو ميزة شائعة جدًا.

تحويل طلبه العديد من عملائنا هو PDF إلى DOC: تحويل ملف PDF إلى مستند Microsoft Word. العملاء يرغبون في ذلك لأن ملفات PDF لا يمكن تحريرها بسهولة، بينما يمكن تحرير مستندات Word. بعض الشركات ترغب في أن يتمكن مستخدموها من التعامل مع النصوص والجداول والصور في ملفات بدأت بصيغة PDF.

مع الحفاظ على تقليد جعل الأمور بسيطة ومفهومة، يتيح لك Aspose.PDF for Python تحويل ملف PDF المصدر إلى ملف DOC بسطرين من التعليمات البرمجية.
 لإتمام هذه الميزة، قمنا بإدخال تعداد يسمى SaveFormat وقيمته .Doc تتيح لك حفظ الملف المصدر بتنسيق Microsoft Word.

يُظهر مقتطف الكود البايثون التالي عملية تحويل ملف PDF إلى تنسيق DOC.

<a name="csharp-pdf-to-doc"><strong>الخطوات: تحويل PDF إلى DOC في بايثون</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.
2. احفظه بتنسيق [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) عن طريق استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc.doc"
    # افتح مستند PDF
    document = ap.Document(input_pdf)
    # احفظ الملف بتنسيق مستند MS Word
    document.save(output_pdf, ap.SaveFormat.DOC)
```

### استخدام فئة DocSaveOptions

توفر فئة [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) العديد من الخصائص التي تحسن عملية تحويل ملفات PDF إلى تنسيق DOC. بين هذه الخصائص، تُمكنك وضعية Mode من تحديد وضع التعرف على محتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. لكل واحدة من هذه القيم فوائد وقيود محددة:

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC
    # قم بتعيين وضع التعرف كـ Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # قم بتعيين القرب الأفقي كـ 2.5
    save_options.relative_horizontal_proximity = 2.5
    # قم بتمكين القيمة للتعرف على النقاط أثناء عملية التحويل
    save_options.recognize_bullets = True

    # حفظ الملف بصيغة مستند MS Word
    document.save(output_pdf, save_options)
```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

تقدم Aspose.PDF for Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة استكشاف الوظيفة والجودة التي يعمل بها.
[![Convert PDF to DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك Aspose.PDF لـ Python API قراءة وتحويل مستندات PDF إلى DOCX باستخدام Python عبر .NET. DOCX هو تنسيق معروف لمستندات Microsoft Word الذي تم تغيير هيكله من ثنائي عادي إلى مزيج من ملفات XML وثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات الأحدث ولكن ليس مع الإصدارات السابقة من MS Word التي تدعم امتدادات ملفات DOC.

يوضح مقطع الكود التالي في Python عملية تحويل ملف PDF إلى تنسيق DOCX.

<a name="csharp-pdf-to-docx"><strong>الخطوات: تحويل PDF إلى DOCX في Python</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) مع مستند PDF المصدر.

2. احفظه بصيغة [SaveFormat](https://reference.aspose.com/pdf/python-net/aspose.pdf/saveformat/) عن طريق استدعاء طريقة [save()](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/#methods).

```python

    import aspose.pdf as ap

    input_pdf = DIR_INPUT + "sample.pdf"
    output_pdf = DIR_OUTPUT + "convert_pdf_to_docx_options.docx"
    # افتح مستند PDF
    document = ap.Document(input_pdf)

    save_options = ap.DocSaveOptions()
    save_options.format = ap.DocSaveOptions.DocFormat.DOC_X
    # عيّن وضع التعرف كـ Flow
    save_options.mode = ap.DocSaveOptions.RecognitionMode.FLOW
    # عيّن القرب الأفقي كـ 2.5
    save_options.relative_horizontal_proximity = 2.5
    # تمكين القيمة للتعرف على النقاط أثناء عملية التحويل
    save_options.recognize_bullets = True

    # احفظ الملف بصيغة مستند MS Word
    document.save(output_pdf, save_options)
```

تحتوي فئة [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) على خاصية تسمى Format والتي توفر القدرة على تحديد صيغة المستند الناتج، أي DOC أو DOCX.
 من أجل تحويل ملف PDF إلى تنسيق DOCX، يرجى تمرير قيمة Docx من تعداد DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

يقدم Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تطبيق Aspose.PDF لتحويل PDF إلى Word مجانًا](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## انظر أيضًا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما هو مذكور أعلاه.

_التنسيق_: **Word**
- [كود Python لتحويل PDF إلى Word](#python-pdf-to-docx)
- [واجهة برمجة تطبيقات Python لتحويل PDF إلى Word](#python-pdf-to-docx)
- [تحويل PDF إلى Word بواسطة Python برمجيًا](#python-pdf-to-docx)
- [مكتبة Python لتحويل PDF إلى Word](#python-pdf-to-docx)
- [حفظ PDF كملف Word بواسطة Python](#python-pdf-to-docx)
- [إنشاء Word من PDF بواسطة Python](#python-pdf-to-docx)
- [إنشاء ملف Word من PDF بواسطة Python](#python-pdf-to-docx)

- [محول PDF إلى Word بواسطة Python](#python-pdf-to-docx)
_Format_: **DOC**
- [كود بايثون لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [واجهة برمجة تطبيقات بايثون لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [برمجة بايثون لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [مكتبة بايثون لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [حفظ PDF كـ DOC باستخدام بايثون](#python-pdf-to-doc)
- [إنشاء DOC من PDF باستخدام بايثون](#python-pdf-to-doc)
- [إنشاء مستند DOC من PDF باستخدام بايثون](#python-pdf-to-doc)
- [محول بايثون من PDF إلى DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [كود بايثون لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [واجهة برمجة تطبيقات بايثون لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [برمجة بايثون لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [مكتبة بايثون لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [حفظ PDF كـ DOCX باستخدام بايثون](#python-pdf-to-docx)
- [إنشاء DOCX من PDF باستخدام بايثون](#python-pdf-to-docx)
- [إنشاء مستند DOCX من PDF باستخدام بايثون](#python-pdf-to-docx)
- [محول بايثون من PDF إلى DOCX](#python-pdf-to-docx)