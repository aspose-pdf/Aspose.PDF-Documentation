---
title: كيفية التوقيع الرقمي على PDF
linktitle: التوقيع الرقمي على PDF
type: docs
weight: 10
url: /cpp/digitally-sign-pdf-file/
description: التوقيع الرقمي على مستندات PDF باستخدام C++. تحقق أو تحقق من صحة التوقيعات الرقمية على ملفات PDF باستخدام C++.
lastmod: "2021-12-15"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## التوقيع الرقمي على PDF

يمكنك توقيع مستند PDF لتأكيد محتواه، أو يمكنك الموافقة على المستند باستخدام Aspose.PDF.

يدعم Aspose.PDF لـ C++ ميزة التوقيع الرقمي على ملفات PDF باستخدام فئة SignatureField. يمكنك أيضًا توثيق ملف PDF بشهادة PKCS12. شيء مشابه لـ [إضافة التوقيعات والأمان في Adobe Acrobat](https://www.adobepress.com/articles/article.asp?p=1272495&seqNum=6).

استخدم فئة [PdfFileSignature](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.facades.pdf_file_signature) لتوقيع PDF الخاص بك.

```cpp
using namespace System;
using namespace Aspose::Pdf;
using namespace Aspose::Pdf::Facades;

void SecuringAndSigning::SignDocument() {

// String for path name.

String _dataDir("C:\\Samples\\");


String inFile = _dataDir + u"DigitallySign.pdf";

String outFile = _dataDir + u"DigitallySign_out.pdf";


auto document = MakeObject<Document>(inFile);


auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020"); // Use PKCS7/PKCS7Detached
























// objects

System::Drawing::Rectangle rect(300, 100, 400, 200);

signature->Sign(1, true, rect, pkcs);

// Save output PDF file

signature->Save(outFile);
}
```

## إضافة طابع زمني إلى التوقيع الرقمي

### كيفية التوقيع الرقمي على ملف PDF مع طابع زمني

يدعم Aspose.PDF لـ C++ التوقيع الرقمي لملف PDF باستخدام خادم الطوابع الزمنية أو خدمة الويب.

تُستخدم الطوابع الزمنية للإشارة إلى التاريخ والوقت الذي قمت فيه بتوقيع المستند. يثبت الطابع الزمني الموثوق به أن محتوى ملفات PDF الخاصة بك كان موجودًا في نقطة زمنية معينة ولم يتغير منذ ذلك الحين.

استخدم فئة [TimestampSettings](https://reference.aspose.com/pdf/cpp/class/aspose.pdf.timestamp_settings) لإضافة طابع زمني موثوق به للتوقيعات الرقمية أو المستندات.

يرجى إلقاء نظرة على مقتطف الشيفرة التالي الذي يحصل على الطابع الزمني ويضيفه إلى مستند PDF:

```cpp
void SecuringAndSigning::SignWithTimeStampServer() {


// String for path name.

String _dataDir("C:\\Samples\\");

auto document = MakeObject<Document>(_dataDir + u"SimpleResume.pdf");

auto signature = MakeObject<PdfFileSignature>(document);


auto pkcs = MakeObject<Aspose::Pdf::Forms::PKCS7>(_dataDir + u"test.pfx", u"Pa$$w0rd2020");


auto timestampSettings = MakeObject<TimestampSettings>(u"https://freetsa.org/tsr", String::Empty); // User/Password can
























// be omitted

pkcs->set_TimestampSettings(timestampSettings);


System::Drawing::Rectangle rect(100, 100, 200, 100);

// Create any of the three signature types

signature->Sign(1, u"Signature Reason", u"Contact", u"Location", true, rect, pkcs);

// Save output PDF file

signature->Save(_dataDir + u"DigitallySignWithTimeStamp_out.pdf");
}
```