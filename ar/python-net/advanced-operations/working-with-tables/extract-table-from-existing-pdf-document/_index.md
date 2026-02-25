---
title: استخراج جدول من مستند PDF
linktitle: استخراج جدول
type: docs
weight: 20
url: /ar/python-net/extracting-table/
description: يتيح Aspose.PDF for Python عبر .NET إمكانية إجراء عمليات متعددة على الجداول الموجودة في مستند PDF الخاص بك.
lastmod: "2025-09-27"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: كيفية استخراج جدول من PDF باستخدام بايثون
Abstract: هذا المقال يناقش عملية استخراج الجداول من مستندات PDF باستخدام بايثون، مع الاستفادة من مكتبة Aspose.PDF for Python عبر .NET. يقدم مثالًا برمجيًا يوضح كيفية تحميل مستند PDF، وتكرار صفحاته، واستخدام الفئة `TableAbsorber` لتحديد واستخراج بيانات الجداول. يتنقل الكود عبر كل جدول، صف، وخلية، يجمع مقاطع النص ويطبع النص المستخرج. تُبرز هذه الطريقة كأداة قوية لاستخراج البيانات وتحليل المهام التي تتضمن بيانات جدولة داخل ملفات PDF.
---

## استخراج جدول من PDF

استخراج الجداول من ملفات PDF باستخدام بايثون يمكن أن يكون مفيدًا جدًا لاستخراج البيانات والتحليل. مع مكتبة Aspose.PDF for Python عبر .NET، يمكنك العمل بفعالية مع الجداول المدمجة في مستندات PDF لمهام مختلفة متعلقة بالبيانات.

هذا المقتطف البرمجي يفتح ملف PDF موجود، يفحص كل صفحة بحثًا عن الجداول، ويستخرج محتوى نص الخلايا. يستخدم 'TableAbsorber' لاكتشاف الجداول ثم يتنقل عبر الصفوف والخلايا لطباعة النص الموجود داخلها.

١. يقوم بتحميل PDF إلى كائن ap.Document.
١. التكرار عبر الصفحات.
١. إنشاء كائن TableAbsorber.
١. التكرار عبر الجداول.
١. التكرار عبر الصفوف والخلايا.
١. استخراج وطباعة النص من الخلايا.

هذا المثال يقرأ ملف PDF، يجد جميع الجداول، ويطبع محتويات خلاياه صفًا بصف.

```python

    import aspose.pdf as ap
    from os import path

    path_infile = path.join(self.data_dir, infile)
    document = ap.Document(path_infile)
    for page in document.pages:
        absorber = ap.text.TableAbsorber()
        absorber.visit(page)
        for table in absorber.table_list:
            print("Table ----")
            for row in table.row_list:
                print("Row")
                for cell in row.cell_list:
                    text_fragment_collection = cell.text_fragments
                    for fragment in text_fragment_collection:
                        txt = ""
                        for seg in fragment.segments:
                            txt += seg.text
                        print(txt)
```


