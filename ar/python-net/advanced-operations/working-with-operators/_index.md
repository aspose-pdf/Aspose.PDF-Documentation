---
title: العمل مع المشغلات باستخدام بايثون
linktitle: العمل مع المشغلات
type: docs
weight: 90
url: /ar/python-net/working-with-operators/
description: تشرح هذه الموضوع كيفية استخدام المشغلات مع Aspose.PDF لـ Python عبر .NET. توفر فئات المشغلات ميزات رائعة لمعالجة ملفات PDF.
lastmod: "2025-05-16"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخدام المشغلات في PDF مع Aspose.PDF لـ Python عبر .NET
Abstract: توفر المقالة استكشافًا متعمقًا لمشغلات PDF وتطبيقاتها في تعديل تدفقات محتوى PDF. المشغلات هي كلمات رئيسية متخصصة في PDF توجه إجراءات معينة، مثل رسم العناصر الرسومية على صفحة، وتكون صالحة فقط داخل تدفقات المحتوى. تفصل المقالة طريقة للسيطرة الدقيقة على وضع الصور في ملفات PDF عن طريق تعديل تدفقات المحتوى مباشرةً باستخدام مشغلات الرسومات منخفضة المستوى. هذا النهج مفيد للمهام التي تتطلب تحديدًا دقيقًا لموقع الصورة، مثل إضافة العلامات المائية، محاذاة الطبقات، وإنشاء تخطيطات مخصصة. تُبرز مشغلات معينة مثل GSave و ConcatenateMatrix و Do و GRestore أدوارها في إدارة حالات الرسومات والتحولات، مما يضمن عرضًا دقيقًا دون التأثير على محتوى الصفحات الأخرى.
---

## مقدمة في مشغلات PDF واستخداماتها

المشغل هو كلمة مفتاح في PDF تحدد إجراءً ما يجب تنفيذه، مثل رسم شكل رسومي على الصفحة. يتم تمييز كلمة المشغل عن الكائن المسمى بغياب الحرف المائل الأول (2Fh). المشغلات ذات معنى فقط داخل تدفق المحتوى.

تدفق المحتوى هو كائن تدفق PDF تتكون بياناته من تعليمات تصف العناصر الرسومية التي سيتم رسمها على صفحة. يمكن العثور على المزيد من التفاصيل حول مشغلات PDF في [مواصفة PDF](https://opensource.adobe.com/dc-acrobat-sdk-docs/).

### تفاصيل التنفيذ

توفر هذه الطريقة تحكمًا دقيقًا في وضع الصورة داخل ملف PDF عن طريق تعديل تدفق المحتوى مباشرةً باستخدام مشغلات الرسومات منخفضة المستوى. إنها مفيدة بشكل خاص عندما يكون المطلوب تحديد موضع وتحويل الصور بدقة، مثل:

- إضافة علامات مائية أو شعارات في مواقع محددة.

- وضع صور فوق المحتوى الحالي مع محاذاة دقيقة.

- تنفيذ تخطيطات مخصصة لا يمكن تحقيقها باستخدام التجريديات عالية المستوى.

باستخدام مشغلات مثل GSave و ConcatenateMatrix و Do و GRestore، يمكن للمطورين ضمان أن يتم عرض الصور بدقة دون آثار جانبية غير مقصودة على محتوى الصفحات الأخرى.

- المشغل [GSave](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/gsave/) يحفظ الحالة الرسومية الحالية للـ PDF.
- المشغل [ConcatenateMatrix](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/concatenatematrix/) (دمج المصفوفة) يستخدم لتحديد كيفية وضع صورة على صفحة PDF.
- المشغل [Do](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/do/) يرسم الصورة على الصفحة.
- المشغل [GRestore](https://reference.aspose.com/pdf/python-net/aspose.pdf.operators/grestore/) يعيد الحالة الرسومية.

لإضافة صورة إلى ملف PDF:

1. فتح مستند PDF
1. تحديد إحداثيات وضع الصورة
1. الوصول إلى الصفحة المستهدفة
1. تحميل الصورة إلى تدفق
1. حفظ الحالة الرسومية الحالية
1. إنشاء مستطيل ومصفوفة تحويل
1. تطبيق مصفوفة التحويل
1. رسم الصورة
1. استعادة الحالة الرسومية السابقة
1. حفظ مستند PDF المعدل

يعرض الجزء البرمجي التالي كيفية استخدام مشغلات PDF:

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Set coordinates for the image placement
        lower_left_x = 100
        lower_left_y = 100
        upper_right_x = 200
        upper_right_y = 200

        # Get the page where the image needs to be added
        page = document.pages[1]

        # Load the image into a file stream
        with open(path_imagefile, "rb") as image_stream:
            # Add the image to the page's Resources collection
            page.resources.images.add(image_stream)

        # Save the current graphics state using the GSave operator
        page.contents.add(ap.operators.GSave())

        # Create a rectangle and matrix for positioning the image
        rectangle = ap.Rectangle(lower_left_x, lower_left_y, upper_right_x, upper_right_y)
        matrix = ap.Matrix([
            rectangle.urx - rectangle.llx, 0,
            0, rectangle.ury - rectangle.lly,
            rectangle.llx, rectangle.lly
        ])

        # Define how the image must be placed using the ConcatenateMatrix operator
        page.contents.add(ap.operators.ConcatenateMatrix(matrix))

        # Get the image from the Resources collection
        x_image = page.resources.images[page.resources.images.count]

        # Draw the image using the Do operator
        page.contents.add(ap.operators.Do(x_image.name))

        # Restore the graphics state using the GRestore operator
        page.contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## رسم XForm على الصفحة باستخدام المشغلات

استخدم هذا المثال قوة XForms ومشغلات الرسومات لإعادة استخدام المحتوى الرسومي داخل PDF بكفاءة. من خلال تغليف الصورة في XForm، يمكن رسمها عدة مرات دون تكرار بيانات الصورة، مما يؤدي إلى ملفات أصغر وأداء محسّن. هذا النهج مفيد بشكل خاص عندما:

- الحاجة إلى ظهور نفس الصورة أو الرسم عدة مرات في المستند.

- ضرورة التحكم الدقيق في وضع وتحويل الرسومات.

- تحسين PDF للأداء والحجم هو أولوية.

من خلال إدارة الحالة الرسومية باستخدام GSave و GRestore، واستخدام مصفوفات التحويل مع ConcatenateMatrix، تضمن هذه التقنية أن كل رسم يتم عرضه بشكل صحيح ومستقل.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        page_contents = document.pages[1].contents

        # Wrap existing contents with GSave/GRestore operators to preserve graphics state
        page_contents.insert(1, ap.operators.GSave())
        page_contents.add(ap.operators.GRestore())

        # Add GSave operator to start new graphics state
        page_contents.add(ap.operators.GSave())

        # Create an XForm
        form = ap.XForm.create_new_form(document.pages[1], document)
        document.pages[1].resources.forms.add(form)

        form.contents.add(ap.operators.GSave())
        # Define image width and height
        form.contents.add(ap.operators.ConcatenateMatrix(200, 0, 0, 200, 0, 0))

        # Load image into stream
        with open(path_imagefile, 'rb') as image_stream:
            # Add the image to the XForm's resources
            form.resources.images.add(image_stream)

        x_image = form.resources.images[form.resources.images.count]
        # Draw the image on the XForm
        form.contents.add(ap.operators.Do(x_image.name))
        form.contents.add(ap.operators.GRestore())

        # Place and draw the XForm at two different coordinates

        # Draw the XForm at (100, 500)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 500))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Draw the XForm at (100, 300)
        page_contents.add(ap.operators.GSave())
        page_contents.add(ap.operators.ConcatenateMatrix(1, 0, 0, 1, 100, 300))
        page_contents.add(ap.operators.Do(form.name))
        page_contents.add(ap.operators.GRestore())

        # Restore graphics state
        page_contents.add(ap.operators.GRestore())

        # Save PDF document
        document.save(path_outfile)
```

## إزالة كائنات الرسومات باستخدام فئات المشغلات

يعرض الجزء البرمجي التالي كيفية إزالة الرسومات. يرجى ملاحظة أنه إذا كان ملف PDF يحتوي على تسميات نصية للرسومات، فقد تبقى هذه التسميات في الملف عند استخدام هذه الطريقة. لذا ابحث عن مشغلات الرسومات للحصول على طريقة بديلة لحذف هذه الصور.

```python

    import aspose.pdf as ap

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Get the specific page (page 2 in this case)
        page = document.pages[2]

        # Get the operator collection from the page contents
        operator_collection = page.contents

        # Define the path-painting operators to be removed
        operators_to_remove = [
            ap.operators.Stroke(),
            ap.operators.ClosePathStroke(),
            ap.operators.Fill()
        ]

        # Delete the specified operators from the page contents
        operator_collection.delete(operators_to_remove)

        # Save PDF document
        document.save(path_outfile)
```


