---
title: العمل مع النماذج باستخدام Python
linktitle: النماذج في مستند PDF
type: docs
weight: 60
url: /ar/python-java/forms/
lastmod: "2023-05-19"
description: تحتوي هذه القسم على مقالات تتعلق بالعمل مع النماذج في مستندات PDF باستخدام واجهة برمجة التطبيقات Python.
sitemap:
    changefreq: "monthly"
    priority: 0.8
---

النماذج هي ملفات تحتوي على مناطق لتمكين المستخدمين من تحديد أو ملء المعلومات بغرض جمع وتخزين المعلومات.

AcroForms هي ملفات PDF تحتوي على حقول نماذج. يمكن إدخال البيانات في هذه الحقول (يدويًا أو من خلال عملية مؤتمتة) بواسطة المستخدمين النهائيين أو مؤلف النموذج. داخليًا، تعتبر AcroForms تعليقات توضيحية أو حقول تُطبق على مستند PDF.

تصف هذه القسم نهجًا سريعًا وبسيطًا لإكمال مستند PDF برمجيًا باستخدام Aspose.PDF. كما تناقش القسم كيفية استخدام Aspose.PDF لـ Java لاكتشاف وتعيين الحقول المتاحة داخل مستند PDF موجود مع AcroForms.

**مكتبة Aspose.PDF لـ Python عبر Java** الخاصة بنا تتيح لك العمل بنجاح وسرعة وسهولة مع النماذج في مستندات PDF.

  
- **AcroForms** - إنشاء نموذج، تعبئة حقل النموذج، استخراج البيانات من النموذج، تعديل الحقول في ملف PDF الخاص بك باستخدام مكتبة Java.
- **XFA Forms** - تعبئة حقول XFA، تحويل XFA، الحصول على خصائص حقول XFA.

## الوظائف التالية متاحة:

- تصدير/استيراد fdf
- تصدير/استيراد xfdf
- تصدير/استيراد xml
- تصدير/تعيين XfaData
- تعبئة الحقول
- تسطيح الحقول
- تحديد قيم زر الراديو الصحيحة
- الحصول على أسماء الحقول، العلامات، الأنواع، القيم
- إعادة تسمية الحقول

```python

from asposepdf import Api, Forms


# تهيئة الترخيص
documentName = "testdata/license/Aspose.PDF.PythonviaJava.lic"
licenseObject = Api.License()
licenseObject.setLicense(documentName)

DIR_INPUT = baseDir+"testdata/forms/"
DIR_OUTPUT = baseDir+"testout/"

# مثال على تعبئة الحقل

input_pdf1 = DIR_INPUT + "Testing.pdf"
output_pdf = DIR_OUTPUT + "test5_1.pdf"

form = Forms.Form(sourceFileName=input_pdf1)
print(form.getFieldType("form1[0].Page1[0].fldBarCode1[0]"))
form.fillField("form1[0].Page1[0].fldBarCode1[0]", "54321")

form.save(output_pdf)
```