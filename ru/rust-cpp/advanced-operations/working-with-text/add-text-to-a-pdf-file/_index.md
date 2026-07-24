---
title: Добавить текст в PDF с помощью Rust
linktitle: Добавить текст в PDF
type: docs
weight: 10
url: /ru/rust-cpp/add-text-to-pdf-file/
description: Узнайте, как добавить текст в PDF‑документ на Rust с использованием Aspose.PDF для улучшения содержимого и редактирования документов.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Добавить текст в PDF с использованием Aspose.PDF для Rust
Abstract: Раздел "Add Text to PDF File" документации Aspose.PDF for C++ и Rust предоставляет пошаговые инструкции по программному вставлению текста в PDF‑документы. Он охватывает различные методы добавления текста, включая позиционирование, настройку Font, регулировку цвета и параметры выравнивания текста. Руководство демонстрирует, как добавить текст на конкретные страницы и в определённые места внутри PDF, обеспечивая точное размещение содержимого. С подробными примерами кода и объяснениями разработчики могут легко интегрировать функции вставки текста в свои приложения для улучшенного управления PDF‑документами.
SoftwareApplication: rust-cpp
---

Чтобы добавить текст в существующий PDF‑файл:

1. Откройте PDF‑файл.
1. Добавьте текст в PDF‑документ с помощью [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) функция.
1. Сохраните изменения в тот же файл.

## Добавление текста

Следующий фрагмент кода показывает, как добавить текст в существующий PDF‑файл.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
