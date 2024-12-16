---
title: مثال لـ Hello World باستخدام لغة Python
linktitle: مثال Hello World
type: docs
weight: 20
url: /ar/python-cpp/hello-world-example/
description: يوضح هذا المثال كيفية إنشاء مستند PDF بسيط "Hello, World!" باستخدام Aspose.PDF لـ Python
lastmod: "2023-07-27"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "TechArticle",
    "headline": "مثال لـ Hello World باستخدام لغة Python",
    "alternativeHeadline": "مثال Aspose.PDF Python (عبر C++)",
    "author": {
        "@type": "Person",
        "givenName": "Andriy",
        "familyName": "Andrukhovskiy",
        "url":"https://www.linkedin.com/in/andruhovski/"
    },
    "genre": "توليد مستندات PDF",
    "keywords": "pdf, Python, توليد مستندات",
    "wordcount": "302",
    "proficiencyLevel":"مبتدئ",
    "publisher": {
        "@type": "Organization",
        "name": "فريق مستندات Aspose.PDF",
        "url": "https://products.aspose.com/pdf",
        "logo": "https://www.aspose.cloud/templates/aspose/img/products/pdf/aspose_pdf-for-python-cpp.svg",
        "alternateName": "Aspose",
        "sameAs": [
            "https://facebook.com/aspose.pdf/",
            "https://twitter.com/asposepdf",
            "https://https://www.youtube.com/@AsposePDF",
            "https://www.linkedin.com/company/aspose",
            "https://stackoverflow.com/questions/tagged/aspose",
            "https://aspose.quora.com/",
            "https://aspose.github.io/"
        ],
        "contactPoint": [
            {
                "@type": "ContactPoint",
                "telephone": "+1 903 306 1676",
                "contactType": "sales",
                "areaServed": "US",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+44 141 628 8900",
                "contactType": "sales",
                "areaServed": "GB",
                "availableLanguage": "en"
            },
            {
                "@type": "ContactPoint",
                "telephone": "+61 2 8006 6987",
                "contactType": "sales",
                "areaServed": "AU",
                "availableLanguage": "en"
            }
        ]
    },
    "url": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "http://docs.aspose.com/pdf/python-cpp/hello-world-example/"
    },
    "dateModified": "2022-02-04",
    "description": "يوضح هذا المثال كيفية إنشاء مستند PDF بسيط باستخدام Aspose.PDF لـ Python.",
    "articleBody": "يمكن أن يساعد استخدام حالة بسيطة في توضيح ميزات لغة البرمجة أو البرنامج. يتم ذلك عادةً باستخدام مثال "Hello World".\n\nAspose.PDF لـ Python عبر C++ هو API قوي يمكّن المطورين من إنشاء وتعديل وتحويل مستندات PDF في تطبيقاتهم باستخدام Python. يدعم العمل مع تنسيقات ملفات مختلفة مثل PDF, XFA, TXT, HTML, PCL, XML, XPS, EPUB, TEX وصيغ ملفات الصور. في هذه المقالة، سنوضح لك كيفية إنشاء مستند PDF يحتوي على النص "Hello World!" باستخدام Aspose.PDF API. تحتاج إلى تثبيت Aspose.PDF لـ Python عبر C++ في بيئتك قبل تشغيل نموذج الكود التالي.\n1. استيراد وحدة AsposePdfPython.\n2. إنشاء كائن مستند PDF جديد باستخدام وظيفة document_create.\n3. الحصول على مجموعة الصفحات للمستند باستخدام وظيفة document_get_pages.\n4. إضافة صفحة جديدة إلى مجموعة الصفحات باستخدام وظيفة page_collection_add_page.\n5. الحصول على مجموعة الفقرات للصفحة باستخدام وظيفة page_get_paragraphs.\n6. إنشاء كائن صورة جديد باستخدام وظيفة image_create.\n7. تعيين اسم ملف كائن الصورة إلى "sample.jpg" باستخدام وظيفة image_set_file.\n8. إضافة كائن الصورة إلى مجموعة الفقرات باستخدام وظيفة paragraphs_add_image.\n9. حفظ المستند في ملف باسم "document.pdf" باستخدام وظيفة document_save.\n10. إغلاق مقبض المستند باستخدام وظيفة close_handle."
}
</script>


حالة استخدام بسيطة يمكن أن تساعد في توضيح ميزات لغة البرمجة أو البرنامج. يتم ذلك عادةً بمثال "Hello World".

Aspose.PDF لـ Python عبر C++ هو API PDF قوي يمكّن المطورين من إنشاء وتعديل وتحويل مستندات PDF في تطبيقات Python الخاصة بهم. يدعم العمل مع تنسيقات ملفات مختلفة مثل PDF وXFA وTXT وHTML وPCL وXML وXPS وEPUB وTEX وتنسيقات ملفات الصور. في هذه المقالة، سنوضح لك كيفية إنشاء مستند PDF بالنص "Hello World!" باستخدام Aspose.PDF API. تحتاج إلى تثبيت Aspose.PDF لـ Python عبر C++ في بيئتك قبل تشغيل نموذج الشيفرة التالي.

1. استيراد الوحدة `AsposePdfPython`.
1. إنشاء كائن مستند PDF جديد باستخدام الدالة `document_create`.
1. الحصول على مجموعة الصفحات للمستند باستخدام الدالة `document_get_pages`.
1. إضافة صفحة جديدة إلى مجموعة الصفحات باستخدام الدالة `page_collection_add_page`.

1. الحصول على مجموعة الفقرات من الصفحة باستخدام الدالة `page_get_paragraphs`.
1. إنشاء كائن صورة جديد باستخدام الدالة `image_create`.
1. تعيين اسم ملف كائن الصورة إلى "sample.jpg" باستخدام الدالة `image_set_file`.
1. إضافة كائن الصورة إلى مجموعة الفقرات باستخدام الدالة `paragraphs_add_image`.
1. حفظ المستند إلى ملف باسم "document.pdf" باستخدام الدالة `document_save`.
1. إغلاق مقبض المستند باستخدام الدالة `close_handle`.

مقتطف الشيفرة التالي هو برنامج Hello World يوضح كيفية عمل Aspose.PDF لـ Python عبر C++.

```python
from AsposePdfPython import *
 
doc = document_create()
pages = document_get_pages(doc)
page = page_collection_add_page(pages)
paragraphs = page_get_paragraphs(page)
image = image_create()
image_set_file(image,"sample.jpg")
paragraphs_add_image(paragraphs,image)
 
document_save(doc, "document.pdf")
close_handle(doc)
```