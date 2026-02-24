---
title: كيفية إضافة توقيع بطاقة ذكية إلى PDF
linktitle: توقيع PDF باستخدام بطاقة ذكية
type: docs
weight: 30
url: /ar/python-net/sign-pdf-document-from-smart-card/
description: تتيح لك Aspose.PDF for Python عبر .NET توقيع مستندات PDF من بطاقة ذكية باستخدام حقل التوقيع.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: توقيع مستندات PDF من بطاقة ذكية باستخدام Python
Abstract: يشرح هذا الدليل كيفية توقيع مستندات PDF رقمياً باستخدام بطاقة ذكية مع Aspose.PDF for Python عبر .NET. يوضح كيفية الوصول إلى الشهادات المخزنة على الأجهزة الصلبة (مثل رموز USB أو البطاقات الذكية) عبر مخزن شهادات Windows وتطبيقها لتوقيع ملفات PDF. تتضمن الوثائق أمثلة على الشيفرة تُظهر كيفية العثور على الشهادة المناسبة، وتكوين خصائص التوقيع، وتضمين التوقيع الرقمي في ملف PDF. يتيح ذلك توقيعاً آمناً مدعومًا بالأجهزة وفقاً لمعايير التوقيع الرقمي، وهو مناسب لسير عمل المؤسسات القانونية ذات الثقة العالية.
---

يوفر Aspose.PDF إمكانات قوية لدمج مكونات التوقيع البصري والتشفيري، مما يضمن الأصالة والعرض الاحترافي في مستندات PDF الموقعة رقمياً.

## التوقيع باستخدام بطاقة ذكية عبر حقل التوقيع

يوضح هذا المثال كيفية توقيع مستند PDF رقمياً باستخدام شهادة خارجية مع Aspose.PDF for Python وتطبيق صورة مظهر توقيع مخصصة:

1. فتح مستند PDF.
1. إنشاء كائن PdfFileSignature وربطه بالمستند.
1. استرجاع شهادة رقمية محلية باستخدام طريقة مخصصة `get_local_certificate()`.
1. إعداد ExternalSignature بناءً على الشهادة المختارة.
1. تطبيق صورة مظهر توقيع مخصصة (مثل شعار الشركة أو توقيع مكتوب بخط اليد).
1. توقيع الصفحة الأولى من المستند رقمياً مع بيانات وصفية محددة (السبب، جهة الاتصال، الموقع).
1. حفظ المستند الموقع في ملف إخراج جديد.

هذه الطريقة مثالية للحالات التي يجب فيها تطبيق التوقيعات برمجياً باستخدام شهادات خارجية—مثل الرموز الصلبة، مخازن الشهادات، أو المزودين الموثوقين—وعرضها بتصميم بصري مخصص.

فيما يلي مقتطفات الشيفرة لتوقيع مستند PDF من بطاقة ذكية:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pngfile = self.data_dir + pngfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature() as pdf_signature:
            # Bind PDF document
            pdf_signature.bind_pdf(document)
            selected_certificates = self.get_local_certificate()
            # Set an external signature settings
            external_signature = ap.forms.ExternalSignature(selected_certificates)
            pdf_signature.signature_appearance = path_pngfile
            # Sign the document
            pdf_signature.sign(1, "Reason", "Contact", "Location", True, drawing.Rectangle(100, 100, 200, 200),
                                external_signature)
            # Save PDF document
            pdf_signature.save(path_outfile)
```

## التحقق من التوقيعات الرقمية

يوضح هذا المقتطف من الشيفرة كيفية التحقق من التوقيعات الرقمية في مستند PDF باستخدام Aspose.PDF for Python:

1. فتح ملف PDF.
1. إنشاء كائن 'PdfFileSignature' وربطه بالمستند.
1. استرجاع قائمة بجميع أسماء حقول التوقيع باستخدام 'get_signature_names()'.
1. التنقل عبر كل توقيع والتحقق من صلاحيته باستخدام 'verify_signature()'.
1. رفع استثناء إذا فشل أي توقيع في التحقق.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as pdf_signature:
            signature_names = pdf_signature.get_signature_names(True)
            for index in range(len(signature_names)):
                if not pdf_signature.verify_signature(signature_names[index]):
                    raise Exception("Not verified")
```

## التوقيع باستخدام شهادة خارجية

يوضح هذا المقتطف من الشيفرة كيفية إضافة وتوقيع حقل توقيع رقمي في مستند PDF باستخدام Aspose.PDF for Python مع شهادة خارجية:

1. فتح ملف PDF كتيار ثنائي.
1. إنشاء حقل SignatureField ووضعه في الصفحة الأولى من المستند في موضع محدد.
1. استرجاع شهادة رقمية محلية باستخدام طريقة مخصصة `get_local_certificate()`.
1. إعداد ExternalSignature مع بيانات وصفية مثل الجهة، السبب، ومعلومات الاتصال.
1. تعيين اسم حقل فريد لحقل التوقيع (partial_name = "sig1").
1. إضافة حقل التوقيع إلى حقول النموذج في PDF.
1. توقيع الحقل باستخدام الشهادة الخارجية.
1. حفظ المستند الموقع في ملف إخراج.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open a document stream
    with open(path_infile, "rb+") as file_stream:
        # Open PDF document from stream
        document = ap.Document(file_stream)

        # Create a signature field
        signature_field = ap.forms.SignatureField(document.pages[1], ap.Rectangle(100, 400, 10, 10, True))
        selected_certificate = self.get_local_certificate()

        # Set external signature settings
        external_signature = ap.forms.ExternalSignature(selected_certificate)
        external_signature.authority = "Me"
        external_signature.reason = "Reason"
        external_signature.contact_info = "Contact"

        # Set a name of signature field
        signature_field.partial_name = "sig1"

        # Add the signature field to the document
        document.form.add(signature_field, 1)

        # Sign the document
        signature_field.sign(external_signature)

        # Save PDF document
        document.save(path_outfile)
```


