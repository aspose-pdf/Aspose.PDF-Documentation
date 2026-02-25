---
title: استخراج التفاصيل من التوقيع
linktitle: استخراج التفاصيل من التوقيع
type: docs
weight: 20
url: /ar/python-net/extract-image-and-signature-information/
description: كيفية استخراج الصورة من التوقيع الرقمي في مستندات PDF باستخدام Aspose.PDF للغة Python.
lastmod: "2025-06-22"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: احصل على تفاصيل التوقيع في ملفات PDF باستخدام Python
Abstract: توضح هذه المقالة كيفية استخراج الصور ومعلومات التوقيع الرقمي من مستندات PDF باستخدام Aspose.PDF للغة Python. وتوفر تعليمات خطوة بخطوة وعينات من الشيفرة لتحديد الصور المضمنة والوصول إليها وحفظها، وكذلك لاسترجاع البيانات الوصفية وحالة التحقق من التواقيع الرقمية.
---

## استخراج الصورة من حقل التوقيع

Aspose.PDF for Python via .NET supports the feature to digitally sign the PDF files using the [حقل_التوقيع](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) class.

يوضح هذا المقطع البرمجي كيفية استخراج صور التوقيع الرقمي من مستند PDF باستخدام Aspose.PDF للغة Python.

الخطوات:

1. فتح مستند PDF.
1. التكرار عبر حقول النموذج لتحديد أي كائنات SignatureField.
1. استخراج الصورة المرتبطة بكل توقيع (إن وجدت).
1. حفظ صورة التوقيع المستخرجة كملف JPEG.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue

            image_stream = signature_field.extract_image()
            if image_stream is None:
                continue

            image = drawing.Bitmap.from_stream(image_stream)
            # Save the image
            image.save(path_outfile, drawing.imaging.ImageFormat.jpeg)
```

## استخراج معلومات التوقيع

يدعم Aspose.PDF للغة Python عبر .NET ميزة التوقيع الرقمي لملفات PDF باستخدام فئة SignatureField. حاليًا، يمكننا أيضًا تحديد صحة الشهادة ولكن لا يمكننا استخراج الشهادة بالكامل. المعلومات التي يمكن استخراجها هي المفتاح العمومي، البصمة، الجهة المُصدرة، إلخ.

To extract signature information, we have introduced the [ExtractCertificate](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/#methods) method to the [SignatureField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/signaturefield/) class. Please take a look at the following code snippet which demonstrates the steps to extract the certificate from SignatureField object:

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Searching for signature fields
        for field in document.form:
            signature_field = field if isinstance(field, ap.forms.SignatureField) else None
            if signature_field is None:
                continue
            # Extract certificate
            certificate_stream = signature_field.extract_certificate()
            if certificate_stream is None:
                continue
            # Save certificate
            with certificate_stream:
                bytes_data = bytearray(certificate_stream.length)
                with open(path_outfile, "wb") as file_stream:
                    certificate_stream.read(bytes_data, 0, len(bytes_data))
                    file_stream.write(bytes_data)
```

يمكنك الحصول على معلومات حول خوارزميّات توقيع المستند.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        with ap.facades.PdfFileSignature(document) as signature:
            # Get signature names
            signature_names = signature.get_signature_names(True)
            signatures_info_list = signature.get_signatures_info()
            for sig_info in signatures_info_list:
                print(sig_info.DIGEST_HASH_ALGORITHM)
                print(sig_info.ALGORITHM_TYPE)
                print(sig_info.CRYPTOGRAPHIC_STANDARD)
                    print(sig_info.signature_name)
```

## فحص التواقيع لاكتشاف الاختراق

يوضح هذا المقطع البرمجي كيفية كشف التواقيع الرقمية المخترقة في مستند PDF باستخدام Aspose.PDF للغة Python.

تشمل الخطوات:

1. فتح مستند PDF.
1. إنشاء مثيل 'SignaturesCompromiseDetector' لتحليل المستند.
1. التحقق من أي تواقيع مخترقة (غير صالحة أو تم تعديلها).
1. طباعة أسماء أي تواقيع مخترقة تم العثور عليها.
1. الإبلاغ عن تغطية التوقيع—مما يشير إلى مقدار المستند المحمي بالتواقيع الصالحة.

هذه الميزة حاسمة في الحالات التي يجب فيها التحقق من أصالة المستند وسلامته، مثل البيئات القانونية والمالية والامتثالية. وتتيح للمطورين اكتشاف التلاعب أو الفساد في ملفات PDF الموقّعة تلقائيًا.

يوفر Aspose.PDF مجموعة شاملة من الأدوات للتحقق من صحة التوقيع الرقمي، مما يسهل بناء تطبيقات آمنة وواعية للتوقيع تحافظ على موثوقية المستندات.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create the compromise detector instance
        detector = ap.SignaturesCompromiseDetector(document)
        result = []

        # Check for compromise
        if detector.check(result):
            print("No signature compromise detected")
            return

        # Get information about compromised signatures
        if result[0].has_compromised_signatures:
            print(f"Count of compromised signatures: {len(result[0].COMPROMISED_SIGNATURES)}")
            for signature_name in result[0].COMPROMISED_SIGNATURES:
                print(f"Signature name: {signature_name.FULL_NAME}")

        # Get info about signatures coverage
        print(result[0].signatures_coverage)
```

