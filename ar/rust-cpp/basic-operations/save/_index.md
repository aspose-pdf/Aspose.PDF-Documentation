---
title: حفظ مستند PDF برمجيًا
linktitle: حفظ PDF
type: docs
weight: 30
url: /ar/rust-cpp/save-pdf-document/
description: تعلم كيفية حفظ ملف PDF باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: حفظ مستند PDF باستخدام Aspose.PDF for Rust عبر C++
Abstract: Aspose.PDF for Rust عبر C++ يقدم وظيفة شاملة لحفظ مستندات PDF بصيغ ومواقع متعددة مع كفاءة عالية ومرونة. تسمح المكتبة للمطورين بحفظ ملفات PDF إلى أنظمة الملفات، وتدفقات الذاكرة، أو إخراجها بصيغ بديلة مثل DOCX و XLSX والصور. توفر خيارات لتخصيص معلمات الحفظ، تحسين حجم الملف، وضمان سلامة البيانات. يتضمن الوثائق تعليمات مفصلة وعينات كود لمساعدة المطورين على تنفيذ قدرات حفظ PDF بفعالية في تطبيقاتهم.
SoftwareApplication: rust-cpp
---

## حفظ مستند PDF إلى نظام الملفات

المثال يوضح [جديد](https://reference.aspose.com/pdf/rust-cpp/core/new/) طريقة لإنشاء مستند PDF جديد، وهي ميزة أساسية لتوليد المستندات بشكل ديناميكي، مثل التقارير أو الفواتير.

الكود بسيط ويمكن أن يكون كقالب للميزات المتقدمة مثل إضافة نص أو صور أو تعليقات توضيحية إلى ملف PDF.

هذا المثال يوضح الاستخدام السهل لمكتبة Aspose.PDF Rust، مظهرًا إمكاناتها لإنشاء وتعديل وحفظ المستندات.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```
