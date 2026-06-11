---
title: إنشاء ملف PDF متوافق مع PDF/3-A وإرفاق فاتورة ZugFerd بلغة Python
linktitle: قم بإرفاق ZugFerd إلى ملف PDF
type: docs
weight: 10
url: /ar/python-net/attach-zugferd/
description: تعرف على كيفية إنشاء مستند PDF باستخدام ZugFerd في Aspose.PDF لبيثون عبر .NET
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إرفاق ZugFerd بوثيقة PDF
Abstract: توفر المقالة دليلًا تفصيليًا حول كيفية إرفاق ZugFerd (تنسيق للفواتير الإلكترونية) بمستند PDF باستخدام مكتبة Aspose.PDF. يبدأ الإجراء باستيراد المكتبة الضرورية وإعداد مسارات الدليل لملفات الإدخال والإخراج. يتضمن تحميل ملف PDF الهدف إلى كائن المستند، وإنشاء كائن FileSpecification لملف بيانات تعريف فاتورة XML. تم تعيين الخصائص الرئيسية مثل `mime_type` و `af_relationship` لضمان التكامل الصحيح للبيانات الوصفية. ثم تتم إضافة ملف XML إلى مجموعة الملفات المضمنة في PDF، وإرفاقه بشكل فعال كبيانات وصفية. بعد ذلك، يتم تحويل مستند PDF إلى تنسيق PDF/A-3A، وهو مناسب لأرشفة المستندات الإلكترونية، قبل حفظ ملف PDF النهائي باستخدام ZugFerd المضمن. تختتم المقالة بمقتطف كود Python الذي يوضح تنفيذ هذه الخطوات، ويعرض تكامل ZugFerd مع PDF لإدارة المستندات المحسنة.
---

## قم بإرفاق ZugFerd إلى ملف PDF

نوصي باتباع الخطوات التالية لإرفاق ZugFerd بـ PDF:

1. قم باستيراد مكتبة Aspose.PDF وأعطها اسمًا مستعارًا للتطبيق من أجل الراحة.
1. حدد المسار إلى الدليل حيث توجد ملفات PDF المدخلة والمخرجة.
1. حدد المسار إلى ملف PDF الذي ستتم معالجته.
1. قم بتحميل ملف PDF من متغير المسار وإنشاء كائن مستند.
1. قم بإنشاء كائن FileSpecification لملف XML الذي يحتوي على بيانات تعريف الفاتورة. استخدم متغير المسار وسلسلة الوصف لإنشاء كائن FileSpecification.
1. قم بتعيين `mime_type` و ال `af_relationship` خصائص كائن تحديد الملف إلى `text/xml` و `ALTERNATIVE`، على التوالي.
1. أضف كائن FileSpecification إلى مجموعة الملفات المضمنة لكائن المستند. يؤدي هذا إلى إرفاق ملف XML بمستند PDF كملف بيانات تعريف الفاتورة.
1. قم بتحويل وثيقة PDF إلى صيغة PDF/A-3A. استخدم المسار لتسجيل الملف، `PdfFormat.PDF_A_3A` التعداد، و `ConvertErrorAction.DELETE` التعداد لتحويل كائن المستند.
1. احفظ مستند PDF مع ZugFerd المرفق.

```python
import sys
import os
import aspose.pdf as ap

def attach_invoice_zugferd_format(infile, invoice, outfile):
    document = ap.Document(infile)

    # Create a FileSpecification object for the XML file that contains the invoice metadata
    description = "Invoice metadata conforming to ZUGFeRD standard"
    file_specification = ap.FileSpecification(invoice, description)

    # Set the MIME type and the AFRelationship properties of the embedded file
    file_specification.mime_type = "text/xml"
    file_specification.af_relationship = ap.AFRelationship.ALTERNATIVE

    # Add the embedded file to the PDF document's embedded files collection
    document.embedded_files.add("factur", file_specification)

    # Convert the PDF document to the PDF/A-3A format
    log_path = outfile.replace(".pdf", "_log.xml")
    document.convert(log_path, ap.PdfFormat.PDF_A_3A, ap.ConvertErrorAction.DELETE)
    document.save(outfile)
```
