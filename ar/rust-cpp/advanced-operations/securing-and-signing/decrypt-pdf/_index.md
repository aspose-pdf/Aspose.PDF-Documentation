---
title: فك تشفير PDF باستخدام Rust
linktitle: فك تشفير ملف PDF
type: docs
weight: 40
url: /ar/rust-cpp/decrypt-pdf/
description: فك تشفير ملف PDF باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## فك تشفير ملف PDF باستخدام كلمة مرور المالك

يمكنك فتح ملف PDF محمي بكلمة مرور، فك تشفيره، وحفظه باستخدام Aspose.PDF for Rust عبر C++.
يتم فتح ملف PDF باستخدام كلمة مرور المالك، فك تشفيره لإزالة جميع القيود الأمنية، ثم حفظه كملف PDF جديد غير محمي.

1. استخدم [open_with_password](https://reference.aspose.com/pdf/rust-cpp/security/open_with_password/) لتحميل ملف PDF محمي بكلمة مرور عن طريق توفير مسار الملف وكلمة مرور المالك.
1. استدعِ [decrypt](https://reference.aspose.com/pdf/rust-cpp/security/decrypt/) طريقة لإزالة حماية كلمة المرور وجميع القيود الأمنية المرتبطة بالمستند.
1. حفظ ملف PDF المفكك باستخدام [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a password-protected PDF-document
      let pdf = Document::open_with_password("sample_with_password.pdf", "ownerpass")?;

      // Decrypt PDF-document
      pdf.decrypt()?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_decrypt.pdf")?;

      Ok(())
  }
```