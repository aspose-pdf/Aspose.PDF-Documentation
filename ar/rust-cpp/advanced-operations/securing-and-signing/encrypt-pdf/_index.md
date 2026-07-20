---
title:  تشفير PDF باستخدام Rust
linktitle: تشفير ملف PDF
type: docs
weight: 10
url: /ar/rust-cpp/encrypt-pdf/
description: تشفير ملف PDF باستخدام Aspose.PDF for Rust عبر C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
---

## تشفير ملف PDF باستخدام باستخدام كلمة مرور المستخدم أو المالك

لتشفير المستندات بسهولة وأمان، يمكنك استخدام Aspose.PDF for Rust عبر C++.

- **user_password**، إذا تم تعيينها، هي ما تحتاج إلى تقديمه لفتح ملف PDF. سيطلب Acrobat/Reader من المستخدم إدخال كلمة مرور المستخدم. إذا لم تكن صحيحة، لن يفتح المستند.
- الـ **owner_password**، إذا تم تعيينه، يتحكم في الأذونات، مثل الطباعة، التحرير، الاستخراج، التعليق، إلخ. سيمنع Acrobat/Reader هذه الأشياء بناءً على إعدادات الأذونات. سيطلب Acrobat هذه الكلمة السرية إذا أردت تعيين/تغيير الأذونات.

تم حماية PDF بكلمات سر المستخدم والمالك، مع أذونات وصول محددة، وتشفير AES-128 متوافق مع معايير PDF 2.0. بمجرد تشفيره، يتم حفظ المستند على القرص، مما يضمن وصولًا محكمًا وتعاملًا آمنًا مع ملف PDF.

1. إنشاء مستند PDF جديد.
1. تشفير مستند PDF باستخدام [تشفير](https://reference.aspose.com/pdf/rust-cpp/security/encrypt/) طريقة.
1. حدد كلمة مرور للمستخدم لتقييد فتح المستند.
1. حدد كلمة مرور للمالك للتحكم في الأذونات.
1. عرّف الإجراءات المسموح بها باستخدام علم بتات الأذونات.
1. اختر AES-128 كخوارزمية التشفير.
1. فعّل تشفير PDF 2.0 للامتثال لأمان حديث.
1. احفظ ملف PDF المشفر باستخدام [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/). 

```rs

  use asposepdf::{CryptoAlgorithm, Document, Permissions};

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Create a new PDF-document
      let pdf = Document::new()?;

      // Encrypt PDF-document
      pdf.encrypt(
          "userpass",  // User password
          "ownerpass", // Owner password
          Permissions::PRINT_DOCUMENT | Permissions::MODIFY_CONTENT | Permissions::FILL_FORM, // Permissions bitflag
          CryptoAlgorithm::AESx128, // Encryption algorithm
          true,                     // Use PDF 2.0 encryption
      )?;

      // Save the encrypted PDF-document
      pdf.save_as("sample_with_password.pdf")?;

      Ok(())
  }
```