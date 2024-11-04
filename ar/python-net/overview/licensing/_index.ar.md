---
title: Aspose PDF License
linktitle: Licensing and limitations
type: docs
weight: 50
url: /python-net/licensing/
description: تدعو Aspose. PDF for Python عملاءها للحصول على ترخيص كلاسيكي. وكذلك استخدام ترخيص محدود لاستكشاف المنتج بشكل أفضل.
lastmod: "2022-12-21"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## قيود النسخة التجريبية

نريد من عملائنا اختبار مكوناتنا بشكل كامل قبل الشراء لذا تسمح النسخة التجريبية لك باستخدامها كما تفعل عادة.

- **تم إنشاء PDF بعلامة مائية للتقييم.** توفر النسخة التجريبية من Aspose.PDF for Python الوظائف الكاملة للمنتج، لكن جميع الصفحات في مستندات PDF المولدة تحمل علامة مائية "للتقييم فقط. تم الإنشاء بواسطة Aspose.PDF. حقوق النشر 2002-2020 Aspose Pty Ltd" في الأعلى.

>إذا كنت ترغب في اختبار Aspose.PDF دون قيود النسخة التجريبية، يمكنك أيضًا طلب ترخيص مؤقت لمدة 30 يومًا.
 ## رخصة الكلاسيكية

يمكن تحميل الرخصة من ملف أو كائن تدفق. أسهل طريقة لتعيين الرخصة هي وضع ملف الرخصة في نفس المجلد مع ملف Aspose.PDF.dll وتحديد اسم الملف بدون مسار، كما هو موضح في المثال أدناه.

إذا كنت تستخدم أي مكون آخر من Aspose لـ Python إلى جانب Aspose.PDF لـ Python، يرجى تحديد مساحة الأسماء لـ License مثل [فئة Aspose.Pdf.License]().

```python

    license_file = LICENSE_FILE
    license = ap.License()
    license.set_license(license_file)
```