---
title: تعديل AcroForm
linktitle: تعديل AcroForm
type: docs
weight: 45
url: /ar/python-net/modifying-form/
description: تعديل النموذج في ملف PDF الخاص بك باستخدام مكتبة Aspose.PDF للـ Python عبر .NET. يمكنك إضافة أو إزالة الحقول في النموذج الموجود، الحصول على حد الحقل وتعيينه، إلخ.
lastmod: "2025-02-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: إدارة وتخصيص حقول نموذج PDF
Abstract: ت展示 مجموعة من الأمثلة تقنيات مختلفة لإدارة وتخصيص حقول نماذج PDF باستخدام Aspose.PDF للـ Python عبر .NET. يتضمن طرقًا لمسح النص من حقول النموذج من نوع Typewriter باستخدام TextFragmentAbsorber، تعيين واسترجاع حدود الأحرف باستخدام FormEditor، تطبيق خطوط وتنسيقات مخصصة على حقول صندوق النص، وإزالة حقول نموذج معينة بالاسم. تمكّن هذه العمليات المطورين من تنقية، تنسيق، وتخصيص نماذج PDF لإعادة التوزيع، العلامة التجارية، أو أغراض التحقق من البيانات، داعمةً كلاً من التحسين الجمالي والوظيفي في سير عمل المستندات الآلي.
---

## مسح النص في النموذج

يوضح هذا المثال كيفية مسح النص من حقول النموذج من نوع Typewriter في ملف PDF باستخدام Aspose.PDF للـ Python عبر .NET. يقوم بمسح الصفحة الأولى من PDF، يحدد نماذج Typewriter، يزيل محتواها، ويحفظ المستند المحدث. هذا النهج مفيد لإعادة تعيين أو تنقية حقول النموذج قبل إعادة توزيع PDF.

1. تحميل مستند PDF المدخل.
1. الوصول إلى النماذج في الصفحة الأولى.
1. التكرار على كل نموذج والتحقق مما إذا كان نموذج `Typewriter`.
1. استخدام TextFragmentAbsorber للعثور على قطع النص في النموذج.
1. مسح نص كل قطعة.
1. حفظ ملف PDF المعدل إلى ملف الإخراج.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    dataDir = "path/to/your/data/dir/"
    path_infile = dataDir + infile
    path_outfile = dataDir + outfile
    document = ap.Document(path_infile)

    # Get the forms from the first page
    forms = document.pages[1].resources.forms

    for form in forms:
        # Check if the form is of type "Typewriter" and subtype "Form"
        if (form.it == "Typewriter" and form.subtype == "Form"):
            # Create a TextFragmentAbsorber to find text fragments
            absorber = ap.Text.TextFragmentAbsorber()
            absorber.visit(form)

            # Clear the text in each fragment
            for fragment in absorber.text_fragments:
                fragment.Text = ""

    # Save PDF document
    document.save(path_outfile)
```

## الحصول على حد الحقل أو تعيينه

تتيح طريقة set_field_limit(field, limit) في فئة FormEditor تعيين حد للحقول، وهو الحد الأقصى لعدد الأحرف التي يمكن إدخالها في حقل.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    # Create FormEditor instance
    form = ap.facades.FormEditor()

    # Bind PDF document
    form.bind_pdf(path_infile)

    # Set field limit for "First Name"
    form.set_field_limit("First Name", 15)

    # Save PDF document
    form.save(path_outfile)
```

وبالمثل، يحتوي Aspose.PDF على طريقة تحصل على حد الحقل.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    # The path to the documents directory
    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        print(f"Limit: {textBoxField.max_len}")
```

## تعيين خط مخصص لحقل النموذج

يمكن تكوين حقول النماذج في ملفات PDF من Adobe لاستخدام خطوط افتراضية محددة. في الإصدارات الأولية من Aspose.PDF، كانت الخطوط الافتراضية الـ14 فقط مدعومة. سمحت الإصدارات اللاحقة للمطورين بتطبيق أي خط.

يقوم هذا الكود بتحديث مظهر حقل صندوق النص في نموذج PDF عن طريق تعيين خط مخصص، وحجم، ولون، ثم يحفظ المستند المعدل باستخدام Aspose.PDF للـ Python عبر .NET.

يظهر مقطع الكود التالي كيفية تعيين الخط الافتراضي لحقول نموذج PDF.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    if is_assignable(document.form[1], ap.forms.TextBoxField):
        textBoxField = cast(ap.forms.TextBoxField, document.form[1])
        font = ap.text.FontRepository.find_font("Calibri")
        textBoxField.default_appearance = ap.annotations.DefaultAppearance(font, 10, ap.Color.black.to_rgb())

    document.save(path_outfile)
```

## إزالة الحقول في نموذج موجود

يقوم هذا الكود بإزالة حقل نموذج معين (باسمه) من مستند PDF ويحفظ الملف المحدث باستخدام Aspose.PDF للـ Python عبر .NET.

1. تحميل مستند PDF.
1. حذف حقل نموذج بالاسم.
1. حفظ PDF المحدث.

```python

    import aspose.pdf as ap
    from aspose.pycore import cast, is_assignable

    data_dir = "/path/to/your/pdf/files/"
    path_infile = os.path.join(work_dir, infile)
    path_outfile = os.path.join(work_dir, outfile)

    document = ap.Document(path_infile)
    # Delete a particular field by name
    document.form.delete("First Name")
    # Save PDF document
    document.save(path_outfile)
```

