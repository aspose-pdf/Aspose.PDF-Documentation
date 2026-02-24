---
title: تحويل PDF إلى مستندات Microsoft Word في بايثون
linktitle: تحويل PDF إلى Word
type: docs
weight: 10
url: /ar/python-net/convert-pdf-to-word/
lastmod: "2025-09-27"
description: تعلم كيفية تحويل مستندات PDF إلى تنسيق Word في بايثون باستخدام Aspose.PDF لتسهيل تحرير المستندات.
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية تحويل PDF إلى Word في بايثون
Abstract: توفر هذه المقالة دليلًا شاملًا حول تحويل ملفات PDF إلى صيغ Microsoft Word (DOC و DOCX) باستخدام بايثون، مع الاستفادة من مكتبة Aspose.PDF. وتستعرض مزايا تحويل ملفات PDF إلى مستندات Word قابلة للتحرير، مما يسهل تعديل المحتوى مثل النصوص والجداول والصور. تفصل المقالة عملية التحويل إلى DOC (صيغة Word 97-2003) و DOCX، مع مقاطع كود توضح هذه التحويلات عبر بايثون. تشمل العملية إنشاء كائن `Document` من ملف PDF وحفظه بالصيغ المطلوبة باستخدام طريقة `save()` وتعداد `SaveFormat`. بالإضافة إلى ذلك، تُقدم فئة `DocSaveOptions` التي تسمح بمزيد من تخصيص عملية التحويل، مثل تحديد أوضاع التعرف. كما تُسلط المقالة الضوء على التطبيقات الإلكترونية التي توفرها Aspose.PDF لاختبار جودة ووظيفة التحويل. يحتوي المحتوى على نظرة عامة منظمة وروابط للأقسام المقابلة لكل صيغة.
---

## تحويل PDF إلى DOC

إحدى أكثر الميزات شهرة هي تحويل PDF إلى Microsoft Word DOC، مما يجعل إدارة المحتوى أسهل. **Aspose.PDF for Python via .NET** يتيح لك تحويل ملفات PDF ليس فقط إلى DOC بل أيضًا إلى صيغة DOCX بسهولة وكفاءة.

توفر فئة [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) العديد من الخصائص التي تحسن عملية تحويل ملفات PDF إلى صيغة DOC. من بين هذه الخصائص، يتيح لك الوضع (Mode) تحديد وضع التعرف لمحتوى PDF. يمكنك تحديد أي قيمة من تعداد RecognitionMode لهذه الخاصية. كل من هذه القيم لها فوائد وقيود معينة:

الخطوات: تحويل PDF إلى DOC في بايثون

1. تحميل ملف PDF في كائن 'ap.Document'.
1. إنشاء مثيل من 'DocSaveOptions'.
1. تعيين خاصية format إلى 'DocFormat.DOC' لضمان أن يكون الإخراج بصيغة .doc (صيغة Word القديمة).
1. حفظ PDF كمستند Word باستخدام خيارات الحفظ المحددة.
1. طباعة رسالة تأكيد.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

{{% alert color="success" %}}
**جرّب تحويل PDF إلى DOC عبر الإنترنت**

تقدم لك Aspose.PDF for Python تطبيقًا مجانيًا على الإنترنت ["PDF to DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)، حيث يمكنك تجربة الوظيفة وجودتها.

[![تحويل PDF إلى DOC](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## تحويل PDF إلى DOCX

تتيح لك Aspose.PDF for Python API قراءة وتحويل مستندات PDF إلى DOCX باستخدام بايثون عبر .NET. DOCX هي صيغة معروفة لمستندات Microsoft Word تم تغيير هيكلها من ثنائي بسيط إلى مزيج من ملفات XML والثنائية. يمكن فتح ملفات DOCX باستخدام Word 2007 والإصدارات اللاحقة لكنها غير مدعومة في الإصدارات الأقدم من MS Word التي تدعم امتدادات ملفات DOC.

تظهر مقطع كود بايثون التالي عملية تحويل ملف PDF إلى صيغة DOCX.

الخطوات: تحويل PDF إلى DOCX في بايثون

1. تحميل ملف PDF المصدر باستخدام 'ap.Document'.
1. إنشاء مثيل من 'DocSaveOptions'.
1. تعيين خاصية format إلى 'DocFormat.DOC_X' لإنشاء ملف .docx (صيغة Word الحديثة).
1. حفظ PDF كملف DOCX باستخدام خيارات الحفظ المُكوَّنة.
1. طباعة رسالة تأكيد بعد التحويل.

```python

    from os import path
    import aspose.pdf as apdf

    path_infile = path.join(self.data_dir, infile)
    path_outfile = path.join(self.data_dir, "python", outfile)

    document = apdf.Document(path_infile)
    save_options = apdf.DocSaveOptions()
    save_options.format = apdf.DocSaveOptions.DocFormat.DOC_X
    document.save(path_outfile, save_options)

    print(infile + " converted into " + outfile)
```

تحتوي فئة [DocSaveOptions](https://reference.aspose.com/pdf/python-net/aspose.pdf/docsaveoptions/) على خاصية تسمى Format توفر القدرة على تحديد صيغة المستند الناتج، إما DOC أو DOCX. لتحويل ملف PDF إلى صيغة DOCX، يرجى تمرير القيمة Docx من تعداد DocSaveOptions.DocFormat.

{{% alert color="warning" %}}
**جرّب تحويل PDF إلى DOCX عبر الإنترنت**

تقدم لك Aspose.PDF for Python تطبيقًا مجانيًا على الإنترنت ["PDF to Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)، حيث يمكنك تجربة الوظيفة وجودتها.

[![تطبيق Aspose.PDF للتحويل من PDF إلى Word المجاني](/pdf/net/images/pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

