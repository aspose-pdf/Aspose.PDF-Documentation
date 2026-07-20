---
title: Конвертировать PDF в PPTX на Rust
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 30
url: /ru/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF позволяет конвертировать PDF в формат PPTX с использованием Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Инструмент Rust для конвертации PDF в PowerPoint
Abstract: Aspose.PDF for Rust через C\u002B\u002B предоставляет надёжное решение для конвертации PDF‑документов в формат PowerPoint (PPTX) с сохранением исходного макета, форматирования и структуры содержимого. Эта функция позволяет разработчикам бесшовно преобразовывать статические PDF‑файлы в динамичные, редактируемые презентации. Библиотека предлагает параметры настройки для контроля процесса конвертации, обеспечивая высококачественный результат, подходящий для бизнес‑ и профессионального использования. Документация содержит пошаговые инструкции и примеры кода, помогающие разработчикам эффективно интегрировать конвертацию PDF‑в‑PowerPoint в свои приложения.
SoftwareApplication: rust-cpp
---

## Конвертировать PDF в PPTX

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать PDF‑документ в PPTX с помощью библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Преобразовать PDF‑файл в PPTX с помощью [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) функция.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF for Rust представляет вам бесплатное онлайн‑приложение ["PDF to PPTX"](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать изучить функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в PPTX с бесплатным приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}