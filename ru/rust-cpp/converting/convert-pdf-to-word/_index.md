---
title: Конвертировать PDF в документы Word на Rust
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/rust-cpp/convert-pdf-to-doc/
lastmod: "2026-07-20"
description: Узнайте, как написать код на Rust для конвертации PDF в DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Инструмент для конвертации PDF в Word с Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ обеспечивает бесшовное преобразование PDF‑документов в формат DOC при сохранении оригинального текста, изображений, таблиц и общей структуры документа. Эта функция позволяет разработчикам преобразовывать статические PDF в редактируемые файлы Word для дальнейшего изменения и обработки. Библиотека предоставляет различные параметры настройки, позволяющие контролировать результат конвертации, обеспечивая высокую точность и достоверность. Документация включает подробные инструкции и пример кода, помогающие разработчикам эффективно реализовать преобразование PDF в DOC в их приложениях.
SoftwareApplication: rust-cpp
---

Для редактирования содержимого PDF‑файла в Microsoft Word или других текстовых процессорах, поддерживающих форматы DOC и DOCX. PDF‑файлы редактируемы, но файлы DOC и DOCX более гибкие и настраиваемые.

## Преобразуйте PDF в DOC

Предоставленный фрагмент кода Rust демонстрирует, как преобразовать PDF-документ в DOC с помощью библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Конвертируйте PDF-файл в DOC с помощью функции [save_doc](https://reference.aspose.com/pdf/rust-cpp/convert/save_doc/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Doc-document
      pdf.save_doc("sample.doc")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc)", где вы можете попытаться исследовать функциональность и качество его работы."

[![Преобразовать PDF в DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc)
{{% /alert %}}

## Конвертируйте PDF в DOCX

Aspose.PDF for Rust API позволяет читать и конвертировать PDF‑документы в DOCX. DOCX — это широко известный формат документов Microsoft Word, структура которого была изменена от простого бинарного к комбинации XML и бинарных файлов. Файлы DOCX можно открывать в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, поддерживающих расширения файлов DOC.

Приведенный фрагмент кода на Rust демонстрирует, как конвертировать PDF‑документ в DOCX с помощью библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Конвертируйте PDF‑файл в DOCX с помощью функции [save_docx](https://reference.aspose.com/pdf/rust-cpp/convert/save_docx/).

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document
      pdf.save_docx("sample.docx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx)", где вы можете попытаться исследовать функциональность и качество его работы."

[![Aspose.PDF Конвертация PDF в Word Бесплатное приложение](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Конвертируйте PDF в DOCX с улучшенным режимом распознавания

Конвертировать PDF‑документ в файл Microsoft Word (DOCX), используя Aspose.PDF for Rust с улучшенным режимом распознавания.

Режим расширенного распознавания создает полностью редактируемый DOCX, сохраняющий:

- Структура абзацев
- Таблицы как нативные таблицы Word
- Логический поток текста и форматирование

1. Откройте исходный PDF-файл.
1. Сохраните PDF как файл DOCX с включённым расширенным распознаванием разметки.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document with Enhanced Recognition Mode (fully editable tables and paragraphs)
      pdf.save_docx_enhanced("sample_enhanced.docx")?;

      Ok(())
  }
```
