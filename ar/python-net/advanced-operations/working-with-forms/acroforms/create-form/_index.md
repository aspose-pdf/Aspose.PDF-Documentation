---
title: إنشاء AcroForm - إنشاء PDF قابل للتعبئة في Python
linktitle: إنشاء AcroForm
type: docs
weight: 10
url: /ar/python-net/create-form/
description: مع Aspose.PDF للبايثون يمكنك إنشاء نموذج من الصفر في ملف PDF الخاص بك
lastmod: "2025-02-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية إنشاء AcroForm في PDF باستخدام Python
Abstract: توفر المقالة دليلًا حول كيفية إنشاء حقل نموذج في مستند PDF باستخدام مكتبة Aspose.PDF للبايثون. تُقدم فئة `Document` التي تحتوي على مجموعة `Form` لإدارة حقول النماذج. تتضمن عملية إضافة حقل نموذج إنشاء الحقل المطلوب واستخدام طريقة `add` من مجموعة `Form`. يتم تقديم مثال محدد لتوضيح إضافة `TextBoxField` إلى مستند PDF. يتضمن المثال شفرة تفصيلية تُظهر إنشاء `TextBoxField` وتعيين خصائصه مثل الموقع والاسم والقيمة والحد واللون، ثم إضافته إلى المستند. ثم يُحفظ ملف PDF المعدّل مع حقل النموذج المضاف حديثًا.
---

## إنشاء نموذج من الصفر

### إضافة حقل نموذج في مستند PDF

الفئة [Document](https://reference.aspose.com/pdf/python-net/aspose.pdf/document/) توفر مجموعة تسمى [Form](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/) تساعدك على إدارة حقول النماذج في مستند PDF.

لإضافة حقل نموذج:

1. أنشئ حقل النموذج الذي تريد إضافته.
1. استدعِ طريقة [add](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/form/#methods) لمجموعة Form.

### إضافة TextBoxField

المثال أدناه يوضح كيفية إضافة [TextBoxField](https://reference.aspose.com/pdf/python-net/aspose.pdf.forms/textboxfield/).

```python

    import aspose.pdf as ap

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Open document
    pdfDocument = ap.Document(path_infile)

    # Create a field
    textBoxField = ap.forms.TextBoxField(pdfDocument.pages[1], ap.Rectangle(100, 200, 300, 300, True))
    textBoxField.partial_name = "textbox1"
    textBoxField.value = "Text Box"

    border = ap.annotations.Border(textBoxField)
    border.width = 5
    border.dash = ap.annotations.Dash(1, 1)
    textBoxField.border = border

    textBoxField.color = ap.Color.green

    # Add field to the document
    pdfDocument.form.add(textBoxField, 1)

    # Save modified PDF
    pdfDocument.save(path_outfile)
```


