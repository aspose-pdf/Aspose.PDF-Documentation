---
title: استخراج الروابط
linktitle: استخراج الروابط
type: docs
weight: 70
url: /ar/python-net/extract-links/
description: يقوم هذا المثال بربط ملف PDF للإدخال، واستخراج جميع الروابط، وطباعة الإحداثيات وعناوين URL الخاصة بها (إذا كانت متوفرة).
lastmod: "2026-06-11"
sitemap:
    changefreq: "weekly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: استخراج الروابط من ملف PDF باستخدام محرر محتوى PDF في بايثون
Abstract: يوضح هذا المثال كيفية استخراج جميع الروابط من مستند PDF باستخدام Aspose.PDF لـ Python عبر واجهة برمجة تطبيقات الواجهات. يوضح كيفية تحديد واسترداد روابط الويب أو الروابط الأخرى القابلة للتنفيذ المضمنة في PDF.
---

غالبًا ما يحتوي PDF على عناصر تفاعلية مثل روابط الويب وروابط المستندات والإجراءات المخصصة. استخدام [محرر محتوى PDF](https://reference.aspose.com/pdf/python-net/aspose.pdf.facades/pdfcontenteditor/)، يمكنك استخراج جميع التعليقات التوضيحية للروابط من ملف PDF برمجيًا. يتيح لك ذلك فحص الروابط أو معالجتها، على سبيل المثال، للتحقق من عناوين URL أو تحليل أنماط التنقل في المستند.

1. قم بإنشاء مثيل محرر محتوى PDF.
1. قم بربط وثيقة PDF المدخلة.
1. استخرج جميع الروابط باستخدام 'extract_link () '.
1. قم بالتكرار من خلال الروابط المستخرجة.
1. تحقق مما إذا كان الرابط هو LinkAnNotation وما إذا كان الإجراء الخاص به هو GoTouriAction.
1. اطبع إحداثيات المستطيل وURI.
1. اعرض رسالة إذا لم يتم العثور على روابط.

```python
import aspose.pdf.facades as pdf_facades
from aspose.pycore import cast, is_assignable
import aspose.pydrawing as apd
import aspose.pdf as ap

import sys
from os import path

sys.path.append(path.join(path.dirname(__file__), ".."))

from config import set_license, initialize_data_dir


def extract_links(infile):
    # Create PdfContentEditor object
    content_editor = pdf_facades.PdfContentEditor()
    # Bind document to PdfContentEditor
    content_editor.bind_pdf(infile)
    # Extract links from the document
    links = content_editor.extract_link()

    count = 0
    for link in links:
        count += 1
        print(f"Link {count}: {link.rect}")
        if is_assignable(link, ap.annotations.LinkAnnotation):
            annotation = cast(ap.annotations.LinkAnnotation, link)
            if is_assignable(annotation.action, ap.annotations.GoToURIAction):
                action = cast(ap.annotations.GoToURIAction, annotation.action)
                print(f"  URI: {action.uri}")

    if count == 0:
        print("No links found")
```
