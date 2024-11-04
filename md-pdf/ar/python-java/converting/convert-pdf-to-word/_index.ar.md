---
title: تحويل PDF إلى مستندات Microsoft Word باستخدام Python
linktitle: تحويل PDF إلى Word 2003/2019
type: docs
weight: 10
url: /python-java/convert-pdf-to-word/
lastmod: "2023-04-06"
description: تعلم كيفية كتابة كود بايثون لتحويل صيغة PDF إلى مستندات Microsoft Word باستخدام Aspose.PDF for Python via .NET. وتحسين تحويل PDF إلى DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## نظرة عامة

توضح هذه المقالة كيفية **تحويل PDF إلى مستندات Microsoft Word باستخدام Python**. وتغطي هذه المواضيع.

_صيغة_: **DOC**
- [Python PDF إلى DOC](#python-pdf-to-doc)
- [Python تحويل PDF إلى DOC](#python-pdf-to-doc)
- [Python كيفية تحويل ملف PDF إلى DOC](#python-pdf-to-doc)

_صيغة_: **DOCX**
- [Python PDF إلى DOCX](#python-pdf-to-docx)
- [Python تحويل PDF إلى DOCX](#python-pdf-to-docx)
- [Python كيفية تحويل ملف PDF إلى DOCX](#python-pdf-to-docx)

_صيغة_: **Word**
- [Python PDF إلى Word](#python-pdf-to-docx)
- [Python تحويل PDF إلى Word](#python-pdf-to-doc)

- [Python كيفية تحويل ملف PDF إلى Word](#python-pdf-to-docx)

## تحويل PDF إلى DOC و DOCX باستخدام Python

إحدى الميزات الأكثر شيوعًا هي تحويل PDF إلى مستند Microsoft Word DOC، مما يجعل إدارة المحتوى أسهل. **Aspose.PDF for Python** يتيح لك تحويل ملفات PDF ليس فقط إلى DOC ولكن أيضًا إلى تنسيق DOCX، بسهولة وكفاءة.

## تحويل ملف PDF إلى DOC (Word 97-2003)

قم بتحويل ملف PDF إلى تنسيق DOC بسهولة وتحكم كامل. Aspose.PDF for Python مرن ويدعم مجموعة واسعة من التحويلات. تحويل الصفحات من مستندات PDF إلى صور، على سبيل المثال، هو ميزة شائعة جدًا.

تحويل يطلبه العديد من عملائنا هو PDF إلى DOC: تحويل ملف PDF إلى مستند Microsoft Word. العملاء يريدون هذا لأن ملفات PDF لا يمكن تحريرها بسهولة، بينما يمكن تحرير مستندات Word. بعض الشركات تريد أن يتمكن مستخدموها من التلاعب بالنصوص والجداول والصور في الملفات التي بدأت كـ PDF.

مواصلة تقليد جعل الأمور بسيطة ومفهومة، Aspose.PDF for Python يتيح لك تحويل ملف PDF المصدر إلى ملف DOC بسطرين من الشيفرة.
 لتحقيق هذه الميزة، قمنا بتقديم تعداد باسم SaveFormat وقيمته .Doc تسمح لك بحفظ الملف المصدر بصيغة Microsoft Word.

يوضح مقطع الشيفرة البرمجية التالي بلغة Python عملية تحويل ملف PDF إلى صيغة DOC.

<a name="csharp-pdf-to-doc"><strong>الخطوات: تحويل PDF إلى DOC في Python</strong></a>

1. قم بإنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) مع مستند PDF المصدر.
2. احفظه بصيغة [SaveFormat.Doc](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) عن طريق استدعاء طريقة [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python

from asposepdf import Api

documentName = "testdata/Hello.pdf"
doc = Api.Document(documentName)
documentOutName = "testout/out.doc"
doc.save(documentOutName, Api.SaveFormat.Doc)
```

### استخدام فئة DocSaveOptions

توفر فئة [DocSaveOptions](https://reference.aspose.com/pdf/python-java/aspose.pdf/docsaveoptions/) العديد من الخصائص التي تحسن عملية تحويل ملفات PDF إلى صيغة DOC. بين هذه الخصائص، تُمَكِّنك وضعية التعرف من تحديد وضع التعرف على محتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. كل من هذه القيم لها فوائد وحدود محددة:

```python

from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.doc"
# افتح مستند PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Doc
# عين وضعية التعرف كـ Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# عين القرب الأفقي كـ 2.5
save_options.relative_horizontal_proximity = 2.5
# فعّل القيمة للتعرف على النقاط أثناء عملية التحويل
save_options.recognize_bullets = True

# احفظ الملف في تنسيق مستند MS Word
document.save(output_pdf, save_options)

```

{{% alert color="success" %}}
**حاول تحويل PDF إلى DOC عبر الإنترنت**

Aspose.PDF لـ Python يقدم لك تطبيق مجاني عبر الإنترنت ["PDF إلى DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.
[![تحويل PDF إلى DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) {{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك Aspose.PDF لواجهة برمجة التطبيقات في بايثون قراءة وتحويل مستندات PDF إلى DOCX باستخدام بايثون عبر .NET. DOCX هو تنسيق معروف لمستندات Microsoft Word الذي تم تغيير هيكله من ثنائي بسيط إلى مجموعة من ملفات XML وثنائية. يمكن فتح ملفات Docx باستخدام Word 2007 والإصدارات الأحدث ولكن ليس مع الإصدارات السابقة من MS Word التي تدعم امتدادات ملفات DOC.

يظهر مقتطف الشيفرة البرمجية التالي في بايثون عملية تحويل ملف PDF إلى تنسيق DOCX.

<a name="csharp-pdf-to-docx"><strong>الخطوات: تحويل PDF إلى DOCX في بايثون</strong></a>

1. إنشاء مثيل لكائن [Document](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/) مع مستند PDF المصدر.

2. احفظه بتنسيق [SaveFormat.DocX](https://reference.aspose.com/pdf/python-java/aspose.pdf/saveformat/) عن طريق استدعاء أسلوب [Document.Save()](https://reference.aspose.com/pdf/python-java/aspose.pdf/document/#methods).

```python


from asposepdf import Api

DIR_INPUT = "testdata/"
DIR_OUTPUT = "testout/"

input_pdf = DIR_INPUT + "Hello.pdf"
output_pdf = DIR_OUTPUT + "convert_pdf_to_doc_with_options.docx"
# افتح مستند PDF
document = Api.Document(input_pdf)

save_options = Api.DocSaveOptions()
save_options.format = Api.DocSaveOptions.DocFormat.Docx
# ضبط وضع التعرف كـ Flow
save_options.mode = Api.DocSaveOptions.RecognitionMode.Flow
# ضبط القرب الأفقي كـ 2.5
save_options.relative_horizontal_proximity = 2.5
# تمكين القيمة للتعرف على الرموز النقطية أثناء عملية التحويل
save_options.recognize_bullets = True

# احفظ الملف بتنسيق مستند MS Word
document.save(output_pdf, save_options)
```

تمتلك فئة [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) خاصية اسمها Format التي توفر القدرة على تحديد تنسيق المستند الناتج، أي DOC أو DOCX.
 من أجل تحويل ملف PDF إلى تنسيق DOCX، يرجى تمرير قيمة Docx من تعداد DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**حاول تحويل PDF إلى DOCX عبر الإنترنت**

يقدم Aspose.PDF لـ Python تطبيقًا مجانيًا عبر الإنترنت ["PDF إلى Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك محاولة استكشاف الوظائف والجودة التي يعمل بها.

[![تطبيق Aspose.PDF لتحويل PDF إلى Word مجانًا](/pdf/java/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## انظر أيضًا

تغطي هذه المقالة أيضًا هذه المواضيع. الأكواد هي نفسها كما هو مذكور أعلاه.

_التنسيق_: **Word**
- [كود Python لتحويل PDF إلى Word](#python-pdf-to-docx)
- [واجهة برمجة تطبيقات Python لتحويل PDF إلى Word](#python-pdf-to-docx)
- [تحويل PDF إلى Word برمجيًا باستخدام Python](#python-pdf-to-docx)
- [مكتبة Python لتحويل PDF إلى Word](#python-pdf-to-docx)
- [حفظ PDF كـ Word باستخدام Python](#python-pdf-to-docx)
- [إنشاء Word من PDF باستخدام Python](#python-pdf-to-docx)
- [إنشاء Word من PDF باستخدام Python](#python-pdf-to-docx)

- [محول PDF إلى Word باستخدام Python](#python-pdf-to-docx)
_Format_: **DOC**
- [كود Python لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [API Python لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [Python لتحويل PDF إلى DOC برمجياً](#python-pdf-to-doc)
- [مكتبة Python لتحويل PDF إلى DOC](#python-pdf-to-doc)
- [Python لحفظ PDF كـ DOC](#python-pdf-to-doc)
- [Python لتوليد DOC من PDF](#python-pdf-to-doc)
- [Python لإنشاء DOC من PDF](#python-pdf-to-doc)
- [محول Python من PDF إلى DOC](#python-pdf-to-doc)

_Format_: **DOCX**
- [كود Python لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [API Python لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [Python لتحويل PDF إلى DOCX برمجياً](#python-pdf-to-docx)
- [مكتبة Python لتحويل PDF إلى DOCX](#python-pdf-to-docx)
- [Python لحفظ PDF كـ DOCX](#python-pdf-to-docx)
- [Python لتوليد DOCX من PDF](#python-pdf-to-docx)
- [Python لإنشاء DOCX من PDF](#python-pdf-to-docx)
- [محول Python من PDF إلى DOCX](#python-pdf-to-docx)