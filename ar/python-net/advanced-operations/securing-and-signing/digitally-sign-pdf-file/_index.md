---
title: إضافة توقيع رقمي أو توقيع PDF رقمياً في بايثون
linktitle: توقيع PDF رقمياً
type: docs
weight: 10
url: /ar/python-net/digitally-sign-pdf-file/
description: قم بتوقيع مستندات PDF رقمياً، والتحقق منها، أو تصديق ملفات PDF الموقعة رقمياً باستخدام بايثون.
lastmod: "2025-06-07"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: توقيع ملفات PDF رقمياً باستخدام بايثون
Abstract: يشرح هذا الدليل كيفية توقيع مستندات PDF رقمياً باستخدام Aspose.PDF لبايثون عبر .NET. يوضح عملية تطبيق التوقيعات الرقمية القياسية والمتقدمة، باستخدام الشهادات (PFX و PKCS#12)، وتخصيص مظهر التوقيع وسلوكه. تشمل الوثائق أمثلة على الشيفرة تُظهر كيفية توقيع ملفات PDF الموجودة، إضافة طوابع زمنية، والتحقق من صلاحية التوقيع. يتيح ذلك للمطورين ضمان أصالة المستند، سلامته، والامتثال لمعايير التوقيع الرقمي في تطبيقاتهم ببايثون.
---

## توقيع PDF باستخدام التوقيعات الرقمية

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    ppath_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 object for sign
            pkcs = ap.forms.PKCS7(path_pfxfile, "12345")
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

تضيف **توقيع PKCS#7 المنفصل** توقيعًا رقميًا إلى مستند دون دمج المحتوى داخل كتلة التوقيع.

في المثال التالي يتم توقيع مستند PDF باستخدام توقيع رقمي PKCS#7 منفصل، مع تطبيق التوقيع على الصفحة الأولى في منطقة مستطيلة محددة.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Instantiate PdfFileSignature object using the opened document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create PKCS#7 detached object for sign
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)
            # Sign PDF file
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)
            #  Save PDF document
            signature.save(path_outfile)
```

يقوم هذا المقتطف من كود بايثون بالتحقق من توقيع رقمي في ملف PDF باستخدام طريقة 'file_sign.verify_signature()'.

1. إنشاء كائن من PdfFileSignature يتيح لك التفاعل مع التوقيعات في PDF.
1. الحصول على قائمة بأسماء التوقيع `get_signature_names(True)`.
1. فحص التوقيع الأول في القائمة `verify_signature` للتأكد من توافقه مع الشهادة المحددة.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Create an instance of PdfFileSignature for working with signatures in the document
    with ap.facades.PdfFileSignature(path_infile) as file_sign:
        # Get a list of signatures
        signature_names = file_sign.get_signature_names(True)
        # Verify the signature with the given name.
        return file_sign.verify_signature(signature_names[0], certificate)
```

## إضافة طابع زمني إلى التوقيع الرقمي

### كيفية توقيع PDF رقمياً مع طابع زمني

يدعم Aspose.PDF لبايثون توقيع PDF رقمياً باستخدام خادم طوابع زمنية أو خدمة ويب.

من أجل تحقيق هذا المتطلب، تم إضافة الفئة [TimestampSettings](https://reference.aspose.com/pdf/python-net/aspose.pdf/timestampsettings/) إلى مساحة الأسماء Aspose.PDF. يرجى إلقاء نظرة على المقتطف التالي من الشيفرة الذي يحصل على الطابع الزمني ويضيفه إلى مستند PDF:

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature for working with signatures in the document
        with ap.facades.PdfFileSignature(document) as signature:
            pkcs = ap.forms.PKCS7(path_pfxfile, password)
            # Create TimestampSettings settings
            timestamp_settings = ap.TimestampSettings("https://freetsa.org/tsr",
                                                                "", ap.DigestHashAlgorithm.SHA256)  # User/Password can be omitted
            pkcs.timestamp_settings = timestamp_settings
            rect = drawing.Rectangle(100, 100, 200, 100)  # Creating a rectangle for the signature
            # Create any of the three signature types
            signature.sign(1, "Signature Reason", "Contact", "Location", True, rect, pkcs)
            # Save PDF document
                signature.save(path_outfile)
```

## توقيع مستندات PDF باستخدام ECDSA

يتضمن توقيع مستندات PDF باستخدام ECDSA (خوارزمية التوقيع الرقمي للمنحنى الإهليلجي) الاستفادة من تشفير المنحنى الإهليلجي لإنشاء توقيعات رقمية.

يوضح المقتطف أعلاه كيفية تطبيق توقيع رقمي PKCS#7 منفصل على مستند PDF باستخدام Aspose.PDF لبايثون. من خلال تحميل المستند، تكوين مظهر التوقيع وإعدادات الأمان، وحفظ النتيجة، يبين هذا المثال سير عمل كامل وموثوق لتوقيع ملفات PDF رقمياً.

تضمن هذه الطريقة أصالة المستند وسلامته عن طريق تضمين توقيع آمن وقابل للتحقق على الصفحة الأولى. استخدام SHA-256 كخوارزمية تجزئة يلتزم بالمعايير التشفيرية الحديثة، بينما توفر القدرة على التحكم في موضع التوقيع مرونة للعلامات المرئية للموافقة.

```python

    import aspose.pdf as ap
    import aspose.pydrawing as drawing

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile
    path_pfxfile = self.data_dir + pfxfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of PdfFileSignature to sign the document
        with ap.facades.PdfFileSignature(document) as signature:
            # Create a PKCS7Detached object using the provided certificate and password
            pkcs = ap.forms.PKCS7Detached(path_pfxfile, password, ap.DigestHashAlgorithm.SHA256)

            # Sign the first page of the document, setting the signature's appearance at the specified location
            signature.sign(1, True, drawing.Rectangle(300, 100, 400, 200), pkcs)

            # Save PDF document
            signature.save(path_outfile)
```
