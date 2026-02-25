---
title: تحرير وسوم ملفات PDF باستخدام بايثون
linktitle: تحرير الوسوم
type: docs
weight: 70
url: /ar/python-net/edit-pdf-file-tags/
description: تشرح هذه المقالة كيفية تحرير الوسوم في مستندات PDF باستخدام مكتبة Aspose.PDF لبايثون عبر .NET.
lastmod: "2025-06-17"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
---

تم تصميم ملفات PDF الموسومة لضمان إمكانية الوصول عن طريق وضع وسوم على كل عنصر — مثل النصوص والصور والروابط — تُحدد هدفه ودوره في المستند. عند تحرير هذه الـ PDF، من الضروري الحفاظ على هذه الوسوم لضمان الامتثال لمعايير إمكانية الوصول.

توفر أدوات مثل Aspose.PDF لبايثون عبر .NET وظائف قوية للتعامل مع المحتوى الموسوم، ولكن يجب الحذر للحفاظ على بنية المستند وإمكانية الوصول. من خلال إضافة نص بديل للصور أو تنسيق الفقرات بشكل منهجي، تظل ملفات PDF الموسومة قابلة للوصول وسهلة الاستخدام.

الأساليب:

- tag (إضافة وسوم إلى عوامل محددة مثل الصور والنصوص والروابط).
- insert_child.
- remove_child.
- clear_childs.

تسمح لك هذه الأساليب بتحرير وسوم ملفات PDF، على سبيل المثال:

- البحث وتغليف المحتوى باستخدام مشغلات BDC
- وضع وسوم على الفقرة بالنص
- وضع وسم على صورة بعنصر Figure
- تنسيق ووضع وسوم على مقطعين نصيين
- إنشاء ووضع وسوم على عناصر الرابط
- حذف عنصر الهيكل الطفل الأول (من المحتمل أنه قديم وغير مستخدم).
- حفظ ملف PDF المحدث

```python

    import aspose.pdf as ap
    from aspose.pycore import *
    import uuid

    #  Open PDF document
    with (ap.Document(path_infile) as document):
        # Get first page
        page = document.pages[1]
        # The marked content operator on page for the text.
        text_1_bdc = None
        link_2_bdc = None
        link_1_bdc = None
        # Find the marked content operators for the elements on the page.
        for i in range(1, page.contents.length + 1):
            op = page.contents[i]
            if is_assignable(op, ap.operators.BDC):
                bdc = cast(ap.operators.BDC, op)
                # The text operator with marked content id = 0 was found.
                if bdc.properties.mcid == 0:
                    hello_bdc = bdc
            if is_assignable(op, ap.operators.Do):
                do_x_obj = cast(ap.operators.Do, op)
                # Wrap the image XObject with marked content operator.
                image_bdc = ap.operators.BDC("Figure")
                page.contents.insert(i - 2, image_bdc)
                i += 1
                page.contents.insert(i + 1, ap.operators.EMC())
                i += 1
            if is_assignable(op, ap.operators.TextShowOperator):
                tx = cast(ap.operators.TextShowOperator, op)
                # Wrap the text operator on page with marked content operator.
                if "efter Ukendt forfatter er licenseret under" in tx.text:
                    text_1_bdc = ap.operators.BDC("P")
                    page.contents.insert(i - 1, text_1_bdc)
                    i += 1
                    page.contents.insert(i + 1, ap.operators.EMC())
                    i += 1
                # Wrap the text operator on page with marked content operator.
                if "CC" in tx.text:
                    link_1_bdc = ap.operators.BDC("Link")
                    page.contents.insert(i - 1, link_1_bdc)
                    i += 1
                    page.contents.insert(i + 1, ap.operators.EMC())
                    i += 1
                # Wrap the text operator on page with marked content operator.
                if "Dette billede" in tx.text:
                    link_2_bdc = ap.operators.BDC("Link")
                    page.contents.insert(i - 1, link_2_bdc)
                    i += 1
                    page.contents.insert(i + 1, ap.operators.EMC())
                    i += 1

        tagged = document.tagged_content
        # Find exist struct element in document.
        hello_paragraph = tagged.root_element.child_elements[1]
        # Clear the subtree of an existing structure tree element.
        hello_paragraph.clear_childs()
        # Tag paragraph struct element to text on page.
        hello_mcr = hello_paragraph.tag(hello_bdc)
        # Fill the paragraph struct element spaceAfter attribute.
        hello_space_after = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.SPACE_AFTER)
        hello_space_after.set_number_value(30.625)
        # Create a figure element and place it to root element in second position.
        figure = tagged.create_figure_element()
        tagged.root_element.insert_child(figure, 2, True)
        # Set an alternative text for the figure.
        figure.alternative_text = "A fly."
        # Tag figure struct element to image element on page.
        figure_mcr = figure.tag(image_bdc)
        # Find exist struct element in document.
        p2 = cast(ap.logicalstructure.StructureElement,tagged.root_element.child_elements[3])
        # Clear the subtree of an existing structure tree element.
        p2.clear_childs()
        # Create the span struct element.
        span1 = tagged.create_span_element()
        # Get the span1 struct element attributes.
        span1_attrs = span1.attributes.create_attributes(ap.logicalstructure.AttributeOwnerStandard.LAYOUT)
        # Fill the span1 struct element textDecorationType attribute.
        span1_text_decoration_type = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_TYPE)
        span1_text_decoration_type.set_name_value(ap.logicalstructure.AttributeName.TEXT_DECORATION_TYPE_UNDERLINE)
        span1_attrs.set_attribute(span1_text_decoration_type)
        # Fill the span1 struct element textDecorationThickness attribute.
        span1_text_decoration_thickness = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_THICKNESS)
        span1_text_decoration_thickness.set_number_value(0)
        span1_attrs.set_attribute(span1_text_decoration_thickness)
        # Fill the span1 struct element textDecorationColor attribute.
        span1_text_decoration_color = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_COLOR)
        span1_text_decoration_color.set_array_number_value([0.0196075, 0.384308, 0.756866 ])
        span1_attrs.set_attribute(span1_text_decoration_color)
        # Append the span element to the paragraph element in the struct tree.
        p2.append_child(span1, True)
        # Create the span struct element.
        span2 = tagged.create_span_element()
        # Get the span2 struct element attributes.
        span2_attrs = span2.attributes.create_attributes(ap.logicalstructure.AttributeOwnerStandard.LAYOUT)
        # Fill the span2 struct element textDecorationType attribute.
        text_decoration_type = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_TYPE)
        text_decoration_type.set_name_value(ap.logicalstructure.AttributeName.TEXT_DECORATION_TYPE_UNDERLINE)
        span2_attrs.set_attribute(text_decoration_type)
        # Fill the span2 struct element textDecorationThickness attribute.
        text_decoration_thickness = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_THICKNESS)
        text_decoration_thickness.set_number_value(0)
        span2_attrs.set_attribute(text_decoration_thickness)
        # Fill the span2 struct element textDecorationColor attribute.
        text_decoration_color = ap.logicalstructure.StructureAttribute(ap.logicalstructure.AttributeKey.TEXT_DECORATION_COLOR)
        text_decoration_color.set_array_number_value([ 0.0196075, 0.384308, 0.756866 ])
        span2_attrs.set_attribute(text_decoration_color)
        # Append the span struct element to the struct element tree.
        p2.append_child(span2, True)
        # Create the link struct element.
        link2 = tagged.create_link_element()
        # Set an id attribute of struct element.
        link2.set_id(str(uuid.uuid4()))
        # Append the link struct element to the struct element tree.
        span2.append_child(link2, True)
        # Tag link struct element to the page annotation element.
        link2.tag(page.annotations[1])
        # Tag link struct element to text element on page.
        link2.tag(link_2_bdc)
        # Create the link struct element.
        link1 = tagged.create_link_element()
        # Set an id attribute of struct element.
        link1.set_id(str(uuid.uuid4()))
        # Append the link struct element to the struct element tree.
        span1.append_child(link1, True)
        # Tag link struct element to the page annotation element.
        link1.tag(page.annotations[2])
        # Tag link struct element to text element on page.
        link1.tag(link_1_bdc)
        # Remove the struct element at index 0 from the struct tree.
        tagged.root_element.remove_child(0)
        # Save PDF document
        document.save(path_outfile)
```

