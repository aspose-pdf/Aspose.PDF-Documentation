---
title: رخصة Aspose PDF
linktitle: الترخيص والقيود
type: docs
weight: 90
url: /ar/rust-cpp/licensing/
description: يدعو Aspose. PDF for Rust عملائه للحصول على Classic License. وكذلك استخدام رخصة محدودة لاستكشاف المنتج بشكل أفضل.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: الترخيص لـ Aspose.PDF for Rust عبر C++
Abstract: توضح صفحة الترخيص لـ Aspose.PDF for Rust عبر C++ خيارات الترخيص المتاحة للمنتج. يمكن للعملاء الاختيار بين Classic License، أو Metered License، أو رخصة محدودة لأغراض التقييم. تسلط الصفحة أيضًا الضوء على فوائد الحصول على رخصة صحيحة، مثل إتاحة الوظائف الكاملة وإزالة قيود التقييم.
SoftwareApplication: rust-cpp
---

## رخصة

- **كود مصدر Rust** مرخص بموجب رخصة MIT.
- **المكتبة المشتركة** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) هي مالكة وتتطلب رخصة تجارية. لاستخدام جميع الوظائف، يجب عليك الحصول على رخصة.

## نسخة تجريبية

يمكنك استخدام **Aspose.PDF for Rust via C++** مجانًا للتقييم. توفر نسخة التقييم تقريبًا جميع وظائف المنتج مع بعض القيود. تصبح نسخة التقييم نفسها مرخصة عندما تقوم بشراء رخصة وإضافة بضع أسطر من الشيفرة لتطبيق الرخصة.

- إذا كنت تريد اختبار Aspose.PDF for Rust بدون قيود نسخة التقييم، يمكنك أيضًا طلب رخصة مؤقتة لمدة 30 يومًا. يرجى الرجوع إلى [كيف تحصل على رخصة مؤقتة؟](https://purchase.aspose.com/temporary-license)?

### قيود النسخة التجريبية

نريد من عملائنا اختبار مكوناتنا بدقة قبل الشراء، لذلك تسمح النسخة التجريبية لك باستخدامها كما تفعل عادةً.

- **المستندات التي تم إنشاؤها بعلامة مائية تجريبية**. النسخة التجريبية من Aspose.PDF for Rust توفر كامل وظائف المنتج، لكن جميع الصفحات في الملفات المولدة تحمل علامة مائية بالنص "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." في الأعلى.
- **حد عدد الصفحات التي يمكن معالجتها**. في النسخة التجريبية، يمكنك معالجة أول أربع صفحات فقط من المستند.

### الاستخدام في بيئة الإنتاج

مفتاح ترخيص تجاري مطلوب في بيئة الإنتاج. يرجى الاتصال بنا لشراء ترخيص تجاري.

### تطبيق الترخيص

تطبيق ترخيص لتمكين الوظائف الكاملة لـ Aspose.PDF for Rust باستخدام ملف ترخيص (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```