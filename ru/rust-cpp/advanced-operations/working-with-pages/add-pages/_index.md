---
title: Добавить страницы в PDF‑документ
linktitle: Добавить страницы
type: docs
weight: 10
url: /ru/rust-cpp/add-pages/
description: Узнайте, как добавить страницы в существующий PDF на Rust с помощью Aspose.PDF for Rust для улучшения и расширения ваших документов.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавление страниц PDF с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ предоставляет мощный функционал для добавления страниц в PDF‑документы, позволяя разработчикам динамически создавать новые страницы и настраивать их в соответствии с конкретными требованиями. Библиотека поддерживает вставку пустых страниц или копирование страниц из существующих документов, при этом предлагая варианты определения размера страницы, ориентации и содержимого. Эти возможности обеспечивают бесшовное расширение и настройку документов. Документация содержит подробные инструкции и примеры кода, помогающие разработчикам эффективно реализовать функции добавления страниц в своих приложениях.
SoftwareApplication: rust-cpp
---

## Добавить страницу в PDF‑файл

Предоставленный фрагмент кода на Rust демонстрирует, как выполнить операцию Add Page в конце PDF, используя библиотеку Aspose.PDF.

1. Откройте существующий PDF‑файл (sample.pdf) с помощью [open](https://reference.aspose.com/pdf/rust-cpp/core/open/).
1. Добавьте новую пустую страницу с помощью [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/).
1. Сохраните изменения с помощью [сохранить](https://reference.aspose.com/pdf/rust-cpp/core/save/).

Этот фрагмент кода представляет собой краткий и эффективный пример того, как использовать библиотеку Aspose.PDF для Rust для базовых задач манипуляции PDF.

Aspose.PDF for Rust позволяет вставлять страницу в документ PDF в любой позиции файла, а также добавлять страницы в конец PDF‑файла.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add new page in PDF-document
        pdf.page_add()?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```

## Вставить страницу в PDF‑файл

Этот [page_insert](https://reference.aspose.com/pdf/rust-cpp/core/page_insert/) метод вставляет новую страницу в указанную позицию. Эта функция полезна, когда необходимо добавить дополнительные страницы в существующий документ, например, добавить новый раздел или содержание в отчет или презентацию.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Insert new page at the specified position in PDF-document
        pdf.page_insert(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
