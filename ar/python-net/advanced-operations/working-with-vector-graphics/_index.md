---
title: العمل مع الرسومات المتجهة باستخدام بايثون
linktitle: العمل مع الرسومات المتجهة
type: docs
weight: 100
url: /ar/python-net/working-with-vector-graphics/
description: هذه المقالة تصف ميزات العمل بأداة GraphicsAbsorber باستخدام بايثون.
lastmod: "2025-05-17"
TechArticle: true
AlternativeHeadline: استخدام أداة GraphicsAbsorber في PDF مع بايثون
Abstract: توفر وثائق Aspose.PDF للبايثون عبر .NET الخاصة بمقالة العمل مع الرسومات المتجهة دليلًا شاملاً للمطورين الراغبين في تعديل الرسومات المتجهة داخل مستندات PDF باستخدام فئة GraphicsAbsorber. تسهل هذه الفئة استخراج، ونقل، وإزالة، وتكرار عناصر الرسومات المتجهة عبر صفحات PDF.
---

في هذا الفصل، سوف نستكشف كيفية استخدام فئة `GraphicsAbsorber` القوية للتفاعل مع الرسومات المتجهة داخل مستندات PDF. سواء احتجت إلى نقل أو إزالة أو إضافة رسومات، سيوضح لك هذا الدليل كيفية تنفيذ هذه المهام بفعالية.

## مقدمة

الرسومات المتجهة هي مكون حاسم في العديد من مستندات PDF، تُستخدم لتمثيل الصور والأشكال والعناصر الرسومية الأخرى. توفر Aspose.PDF فئة `GraphicsAbsorber`، التي تسمح للمطورين بالوصول إلى هذه الرسومات ومعالجتها برمجيًا. باستخدام طريقة `Visit` في `GraphicsAbsorber`، يمكنك استخراج الرسومات المتجهة من صفحة محددة وأداء عمليات مختلفة، مثل نقلها أو إزالتها أو نسخها إلى صفحات أخرى.

## استخراج الرسومات

الخطوة الأولى في العمل مع الرسومات المتجهة هي استخراجها من مستند PDF. إليك كيفية القيام بذلك باستخدام فئة `GraphicsAbsorber`:

1. فتح مستند PDF.
1. تهيئة GraphicsAbsorber.
1. اختيار الصفحة المستهدفة.
1. استخراج الرسومات من الصفحة.
1. تكرار وعرض العناصر المستخرجة.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create an instance of GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Use the `Visit` method to extract graphics from the page
            graphics_absorber.visit(page)
            # Display information about the extracted elements
            for element in graphics_absorber.elements:
                print(f"Page Number: {element.source_page.number}")
                print(f"Position: ({element.position.x}, {element.position.y})")
                print(f"Number of Operators: {element.operators.length}")
```

فئة GraphicsAbsorber هي جزء من مساحة الاسم aspose.pdf.vector وصممت خصيصًا للتفاعل مع الرسومات المتجهة داخل مستندات PDF.

## نقل الرسومات

بعد استخراج الرسومات، يمكنك نقلها إلى موقع مختلف على نفس الصفحة. إليك كيفية تحقيق ذلك:

1. فتح مستند PDF.
1. تهيئة GraphicsAbsorber.
1. اختيار الصفحة المستهدفة.
1. استخراج عناصر الرسومات.
1. إيقاف التحديثات لتحسين الأداء.
1. تعديل مواضع عناصر الرسومات.
1. استئناف التحديثات وتطبيق التغييرات.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create a GraphicsAbsorber instance
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Select the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Temporarily suspend updates to improve performance
            graphics_absorber.suppress_update()
            # Loop through each extracted graphic element and shift its position
            for element in graphics_absorber.elements:
                position = element.position
                # Move graphics by shifting its X and Y coordinates
                element.position = ap.Point(position.x + 150, position.y - 10)
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## إزالة الرسومات

هناك سيناريوهات قد ترغب فيها بإزالة رسومات معينة من صفحة. توفر Aspose.PDF للبايثون طريقتين لتحقيق ذلك:

### الطريقة 1: استخدام حدود المستطيل

يوضح المثال التالي كيفية إزالة عناصر الرسومات المتجهة الموجودة داخل مساحة مستطيلة محددة في الصفحة الأولى من مستند PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET. تتضمن هذه العملية تحديد عناصر الرسومات داخل المستطيل المحدد وإزالتها لتنظيف أو تعديل محتوى PDF.

1. فتح مستند PDF.
1. تهيئة GraphicsAbsorber.
1. اختيار الصفحة المستهدفة.
1. استخراج عناصر الرسومات.
1. تعريف المستطيل المستهدف.
1. إيقاف التحديثات لتحسين الأداء.
1. إزالة عناصر الرسومات داخل المستطيل.
1. استئناف التحديثات وتطبيق التغييرات.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Temporarily suspend updates for better performance
            graphics_absorber.suppress_update()
            # Iterate through the extracted graphic elements and remove elements inside the rectangle
            for element in graphics_absorber.elements:
                # Check if the graphic's position falls within the rectangle
                if rectangle.contains(element.position, False):
                    # Remove the graphic element
                    element.remove()
            # Resume updates and apply changes
            graphics_absorber.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### الطريقة 2: استخدام مجموعة من العناصر التي تم إزالتها

يوضح المثال التالي كيفية إزالة عناصر الرسومات المتجهة الموجودة داخل مساحة مستطيلة محددة في الصفحة الأولى من مستند PDF باستخدام مكتبة Aspose.PDF للبايثون عبر .NET. تتضمن هذه العملية تحديد عناصر الرسومات داخل المستطيل المحدد وإزالتها لتنظيف أو تعديل محتوى PDF.

1. فتح مستند PDF.
1. تهيئة GraphicsAbsorber.
1. اختيار الصفحة المستهدفة.
1. تعريف المستطيل المستهدف.
1. استخراج عناصر رسومية.
1. إنشاء مجموعة للإزالة.
1. تحديد العناصر داخل المستطيل.
1. إيقاف التحديثات لتحقيق الأداء.
1. إزالة العناصر الرسومية.
1. استئناف التحديثات وتطبيق التغييرات.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first page of the document
            page = document.pages[1]
            # Define the rectangle where graphics will be removed
            rectangle = ap.Rectangle(70, 248, 170, 252, True)
            # Extract graphic elements from the page
            graphics_absorber.visit(page)
            # Create a collection for the removed elements
            removed_elements_collection = ap.vector.GraphicElementCollection()
            # Add elements within the rectangle to the collection
            for element in graphics_absorber.elements:
                if rectangle.contains(element.position,False):
                    removed_elements_collection.add(item)
            # Temporarily suppress updates for better performance
            page.contents.suppress_update()
            # Delete the selected graphic elements
            page.delete_graphics(removed_elements_collection)
            # Resume updates and apply changes
            page.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

## إضافة رسومات إلى صفحة أخرى

يمكن إضافة الرسومات الممتصة من صفحة إلى صفحة أخرى داخل نفس المستند.
إليك طريقتان لتحقيق ذلك:

### الطريقة 1: إضافة الرسومات بصورة فردية

المثال التالي لنسخ عناصر الرسومات المتجهية من الصفحة الأولى لمستند PDF ولصقها على الصفحة الثانية. يتم تسهيل هذه العملية بواسطة فئة GraphicsAbsorber، التي تسمح باستخراج ومعالجة الرسومات المتجهية داخل مستندات PDF.

1. فتح مستند PDF.
1. تهيئة GraphicsAbsorber.
1. اختيار الصفحة المستهدفة.
1. استخراج عناصر رسومية من الصفحة الأولى.
1. إيقاف التحديثات على الصفحة الثانية لتحسين الأداء.
1. إضافة العناصر الرسومية المستخرجة إلى الصفحة الثانية.
1. استئناف التحديثات وتطبيق التغييرات.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add each graphic element from the first page to the second page
            for element in graphics_absorber.elements:
                element.add_on_page(page_2) # Add each graphic element to the second page.
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```

### الطريقة 2: إضافة الرسومات كمجموعة

المثال التالي لتكرار عناصر الرسومات المتجهية من الصفحة الأولى لمستند PDF ووضعها في الصفحة الثانية. يتم ذلك من خلال استخدام فئة GraphicsAbsorber، التي تسهل استخراج ومعالجة الرسومات المتجهية داخل مستندات PDF.

1. فتح مستند PDF.
1. تهيئة GraphicsAbsorber.
1. اختيار الصفحة المستهدفة.
1. استخراج عناصر رسومية من الصفحة الأولى.
1. إيقاف التحديثات على الصفحة الثانية لتحسين الأداء.
1. إضافة العناصر الرسومية المستخرجة إلى الصفحة الثانية.
1. استئناف التحديثات وتطبيق التغييرات.
1. حفظ المستند المحدث.

```python

    import aspose.pdf as ap

    path_infile = self.data_dir + infile
    path_outfile = self.data_dir + outfile

    # Open PDF document
    with ap.Document(path_infile) as document:
        # Create GraphicsAbsorber
        with ap.vector.GraphicsAbsorber() as graphics_absorber:
            # Get the first and second pages
            page_1 = document.pages[1]
            page_2 = document.pages[2]
            # Extract graphic elements from the first page
            graphics_absorber.visit(page_1)
            # Temporarily suppress updates for better performance
            page_2.contents.suppress_update()
            # Add all graphics at once from the first page to the second page
            page_2.add_graphics(graphics_absorber.elements, None)
            # Resume updates and apply changes
            page_2.contents.resume_update()
        # Save PDF document
        document.save(path_outfile)
```
