---
title: إنشاء PDF متوافق مع PDF/3-A وإرفاق فاتورة ZUGFeRD في بايثون
linktitle: إرفاق ZUGFeRD إلى PDF
type: docs
weight: 10
url: ar/python-net/attach-zugferd/
description: تعلم كيفية إنشاء مستند PDF مع ZUGFeRD في Aspose.PDF لبايثون عبر .NET
lastmod: "2024-01-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## إرفاق ZUGFeRD إلى PDF

نوصي باتباع الخطوات التالية لإرفاق ZUGFeRD إلى PDF:

1. استيراد مكتبة Aspose.PDF وإعطائها اختصار ap للراحة.
2. تعريف المسار إلى الدليل حيث توجد ملفات PDF المدخلة والمخرجة.
3. تعريف المسار إلى ملف PDF الذي سيتم معالجته.
4. تحميل ملف PDF من متغير المسار وإنشاء كائن Document.
5. إنشاء كائن FileSpecification لملف XML الذي يحتوي على بيانات الفاتورة الوصفية. استخدم متغير المسار وسلسلة وصف لإنشاء كائن FileSpecification.

1. قم بتعيين خصائص `mime_type` و `af_relationship` لكائن FileSpecification إلى `text/xml` و `ALTERNATIVE` على التوالي.  
1. أضف كائن fileSpecification إلى مجموعة الملفات المضمنة لكائن الوثيقة. هذا يرفق ملف XML بوثيقة الـ PDF كملف بيانات الفاتورة.  
1. قم بتحويل وثيقة الـ PDF إلى تنسيق PDF/A-3A. استخدم المسار إلى ملف السجل، وتعداد `PdfFormat.PDF_A_3A`، وتعداد `ConvertErrorAction.DELETE` لتحويل كائن الوثيقة.  
1. احفظ وثيقة الـ PDF مع مرفق ZUGFeRD.

```python
import aspose.pdf as ap

# تحديد المسار إلى الدليل حيث توجد ملفات PDF المدخلات والمخرجات
_dataDir = "./"

# تحميل ملف PDF الذي سيتم معالجته
path = _dataDir + "ZUGFeRD/ZUGFeRD-test.pdf"
document = ap.Document(path)

# إنشاء كائن FileSpecification لملف XML الذي يحتوي على بيانات الفاتورة
description = "بيانات الفاتورة المتوافقة مع معيار ZUGFeRD"
path = _dataDir + "ZUGFeRD/factur-x.xml"
fileSpecification = ap.FileSpecification(path, description)

# تعيين نوع MIME وخصائص AFRelationship للملف المضمن
fileSpecification.mime_type = "text/xml"
fileSpecification.af_relationship = ap.AFRelationship.ALTERNATIVE

# إضافة الملف المضمن إلى مجموعة ملفات الـ PDF المضمنة
document.embedded_files.add("factur",fileSpecification)

# تحويل وثيقة الـ PDF إلى تنسيق PDF/A-3A
path = _dataDir + "ZUGFeRD/log.xml"
document.convert(path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)

# احفظ وثيقة الـ PDF مع المرفق ZUGFeRD
path = _dataDir + "ZUGFeRD/ZUGFeRD-res.pdf"
document.save(path)
```