---
title: إنشاء PDF متوافق مع PDF/3-A وإرفاق فاتورة ZUGFeRD في بايثون
linktitle: إرفاق ZUGFeRD إلى PDF
type: docs
weight: 10
url: /ar/python-net/attach-zugferd/
description: تعلم كيفية إنشاء مستند PDF مع ZUGFeRD باستخدام Aspose.PDF للبايثون عبر .NET
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إرفاق ZUGFeRD إلى مستند PDF
Abstract: تقدم المقالة دليلًا خطوة بخطوة حول كيفية إرفاق ZUGFeRD (تنسيق للفواتير الإلكترونية) إلى مستند PDF باستخدام مكتبة Aspose.PDF. تبدأ العملية باستيراد المكتبة اللازمة وإعداد مسارات الأدلة للملفات المدخلة والمخرجة. تتضمن تحميل ملف PDF المستهدف في كائن Document، وإنشاء كائن FileSpecification لملف XML الذي يحتوي على بيانات الفاتورة الوصفية. يتم ضبط الخصائص الرئيسية مثل `mime_type` و `af_relationship` لضمان دمج البيانات الوصفية بشكل صحيح. ثم يُضاف ملف XML إلى مجموعة الملفات المدمجة في PDF، مما يرفقه كبيانات وصفية. بعد ذلك، يتم تحويل مستند PDF إلى تنسيق PDF/A-3A، المناسب لأرشفة المستندات الإلكترونية، قبل حفظ PDF النهائي مع ZUGFeRD المدمج. تختتم المقالة بمقتطف شفرة بايثون يُظهر تنفيذ هذه الخطوات، مبرزًا دمج ZUGFeRD مع PDF لتحسين إدارة المستندات.
---

## إرفاق ZUGFeRD إلى PDF

نوصي باتباع الخطوات التالية لإرفاق ZUGFeRD إلى PDF:

1. استورد مكتبة Aspose.PDF ومنحها الاسم المختصر ap للسهولة.
1. حدد المسار إلى الدليل الذي توجد فيه ملفات PDF المدخلات والمخرجات.
1. حدد المسار إلى ملف PDF الذي سيتم معالجته.
1. حمّل ملف PDF من المتغير path وأنشئ كائن Document.
1. أنشئ كائن FileSpecification للملف XML الذي يحتوي على بيانات الفاتورة الوصفية. استخدم المتغير path وسلسلة الوصف لإنشاء كائن FileSpecification.
1. اضبط خصائص `mime_type` و`af_relationship` لكائن FileSpecification إلى `text/xml` و`ALTERNATIVE` على التوالي.
1. أضف كائن fileSpecification إلى مجموعة الملفات المدمجة لكائن المستند. يرفق هذا ملف XML إلى مستند PDF كملف بيانات وصفية للفاتورة.
1. حوّل مستند PDF إلى تنسيق PDF/A-3A. استخدم مسار ملف السجل، وتعداد `PdfFormat.PDF_A_3A`، وتعداد `ConvertErrorAction.DELETE` لتحويل كائن المستند.
1. احفظ مستند PDF مع ZUGFeRD المرفق.

```python
import aspose.pdf as ap

# Define the path to the directory where the input and output PDF files are located
_dataDir = "./"

# Load the PDF file that will be processed
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# Create a FileSpecification object for the XML file that contains the invoice metadata
description = "Invoice metadata conforming to ZUGFeRD standard"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# Set the MIME type and the AFRelationship properties of the embedded file
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# Add the embedded file to the PDF document's embedded files collection
document.embedded_files.add("factur",fileSpecification)

# Convert the PDF document to the PDF/A-3A format
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# Save the PDF document with the attached ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```

