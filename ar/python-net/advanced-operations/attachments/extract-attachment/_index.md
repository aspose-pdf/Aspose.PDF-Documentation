---
title: استخراج المرفقات من PDF
linktitle: استخراج المرفقات
type: docs
weight: 50
url: /ar/python-net/extract-attachment/
description: تعرف على كيفية التعامل مع مرفقات PDF باستخدام Python و Aspose.PDF.
lastmod: "2026-06-11"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: "الدليل الكامل لإدارة مرفقات PDF في Python: إضافة الملفات المضمنة واستخراجها ومعالجتها"
Abstract: تستخدم مرفقات PDF على نطاق واسع لتخزين المستندات الداعمة والتقارير والصور والموارد الأخرى مباشرة داخل ملف PDF. تقدم هذه المقالة نظرة عامة كاملة على التعامل مع مرفقات PDF باستخدام Python باستخدام Aspose.PDF. يشرح كيفية تضمين ملفات خارجية في ملفات PDF الحالية، واستخراج مرفقات محددة أو كلها، وفحص البيانات الوصفية مثل حجم الملف والطوابع الزمنية، واستعادة الملفات المخزنة كتعليقات توضيحية لـ FileAttachment. يوضح كل مثال التقنيات العملية لأتمتة عمليات سير عمل المرفقات، وتحسين قابلية نقل المستندات، وتبسيط إدارة الملفات. سواء كان إنشاء أنظمة مستندات المؤسسة أو البرامج النصية المخصصة للتشغيل الآلي، يمكن للمطورين استخدام هذه الأساليب لإدارة الملفات المضمنة بكفاءة داخل مستندات PDF.
---

## استخراج مرفق محدد من PDF

قم باستخراج ملف مضمن واحد من مستند PDF باستخدام Python و Aspose.PDF. يبحث عن مرفق بالاسم، ويسترد محتواه، ويحفظه كملف منفصل. هذا مفيد للوصول إلى المستندات المضمنة مثل التقارير أو السجلات أو الملفات الداعمة المخزنة داخل PDF.

1. تعريف الوظيفة «extract_single_attachment ()».
1. افتح مستند PDF.
1. ابحث عن المرفق.
1. استخراج محتوى المرفقات.

```python
import aspose.pdf as ap

def extract_single_attachment(infile, attachment_name, outfile):
    with ap.Document(infile) as document:
        print(f"Extracting attachment: {attachment_name}")

        attachment_found = False
        for file_spec in document.embedded_files:
            if file_spec.name == attachment_name:
                with open(outfile, "wb") as f:
                    f.write(file_spec.contents.read())
                print("Attachment extracted successfully")
                attachment_found = True
                break

        if not attachment_found:
            raise ValueError(f"Attachment '{attachment_name}' not found in PDF")
```

## عرض البيانات الوصفية لمرفق الملف

تقوم وظيفة المساعد هذه بطباعة معلومات البيانات الأولية من كائن مواصفات الملف. يتم استخدامه عادةً عند العمل مع مرفقات الملفات المضمنة في ملفات PDF باستخدام Aspose.PDF، مما يسمح للمطورين بفحص التفاصيل مثل المجموع الاختباري وتاريخ الإنشاء وتاريخ التعديل وحجم الملف.

```python
def _print_file_params(params):
    """Helper to print file specification parameters."""
    if params:
        print(f"CheckSum: {params.check_sum}")
        print(f"Creation Date: {params.creation_date}")
        print(f"Modification Date: {params.mod_date}")
        print(f"Size: {params.size}")
```

## قم باستخراج وفحص جميع مرفقات PDF

يوضح مقتطف الشفرة هذا كيفية استخراج جميع الملفات المضمنة من مستند PDF باستخدام Python و Aspose.PDF. لا يقتصر الأمر على حفظ كل مرفق في مجلد محدد فحسب، بل يقوم أيضًا بطباعة البيانات الوصفية التفصيلية مثل اسم الملف والوصف ونوع MIME والمجموع الاختباري والطوابع الزمنية. هذا مفيد لتدقيق أو تصدير أو معالجة المحتوى المضمن في ملفات PDF.

```python
from os import path
import aspose.pdf as ap

def extract_attachments(infile, output_dir):
    with ap.Document(infile) as document:
        print(f"Total files: {len(document.embedded_files)}")

        for file_spec in document.embedded_files:
            print(f"Name: {file_spec.name}")
            print(f"Description: {file_spec.description}")
            print(f"Mime Type: {file_spec.mime_type}")
            _print_file_params(file_spec.params)

            output_path = path.join(output_dir, file_spec.name)
            with open(output_path, "wb") as f:
                f.write(file_spec.contents.read())
```

## استخراج الملفات من التعليقات التوضيحية لمرفقات PDF

قم باستخراج ملف مضمن من التعليق التوضيحي لـ FileAttachment في ملف PDF باستخدام Python و Aspose.PDF. وهي تبحث في الصفحة الأولى عن التعليق التوضيحي للمرفق الأول، وتسترد الملف المضمن، وتحفظه في دليل الإخراج المحدد. يكون هذا مفيدًا عندما تحتوي ملفات PDF على رموز مرفقات الملفات القابلة للنقر بدلاً من مجموعات الملفات المضمنة القياسية.

```python
from os import path
import aspose.pdf as ap
from aspose.pycore import cast

def extract_file_attachment_annotation(infile, output_dir):
    # Open PDF document
    with ap.Document(infile) as document:

        # Get first page
        page = document.pages[1]

        # Find first FileAttachment annotation
        file_attachment = next(
            (
                annot
                for annot in page.annotations
                if annot.annotation_type == ap.annotations.AnnotationType.FILE_ATTACHMENT
            ),
            None,
        )

        if file_attachment is None:
            print("No FileAttachment annotation found on the first page.")
            return

        # Cast to FileAttachmentAnnotation
        faa = cast(ap.annotations.FileAttachmentAnnotation, file_attachment)

        # Access embedded file
        file_spec = faa.file
        print(f"File name: {file_spec.name}")

        # Save embedded file to disk
        output_path = path.join(output_dir, f"extracted-{file_spec.name}")
        with open(output_path, "wb") as f:
            f.write(file_spec.contents.read())

        print(f"Extracted to: {output_path}")
```