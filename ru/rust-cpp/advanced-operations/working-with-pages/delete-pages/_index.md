---
title: Удалить страницы PDF с помощью Rust через C\u002B\u002B
linktitle: Удалить страницы PDF
type: docs
weight: 30
url: /ru/rust-cpp/delete-pages/
description: Вы можете удалять страницы из вашего PDF‑файла, используя Aspose.PDF for Rust via C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить страницы PDF с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C\u002B\u002B предлагает эффективную функциональность для удаления страниц из PDF‑документов, позволяя разработчикам с лёгкостью удалять нежелательные или лишние страницы. Библиотека поддерживает удаление отдельных или нескольких страниц путём указания номеров страниц или диапазонов, обеспечивая точные изменения документа. Эта функция помогает оптимизировать PDF‑файлы, устраняя избыточный контент и улучшая структуру документа. Документация содержит пошаговые инструкции и примеры кода, помогающие разработчикам эффективно внедрять функциональность удаления страниц в своих приложениях.
SoftwareApplication: rust-cpp
---

Вы можете удалять страницы из PDF‑файла, используя **Aspose.PDF for Rust via C\u002B\u002B**. Следующий фрагмент кода демонстрирует, как манипулировать PDF‑документом, удаляя конкретную страницу. Этот метод эффективен для задач манипуляции PDF‑документами, в частности для удаления страниц, сохранения изменённого документа и обеспечения надлежащего управления ресурсами.

1. Откройте PDF‑файл.
1. Удалите нужную страницу с помощью функции [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/).
1. Сохраните документ с помощью метода [save](https://reference.aspose.com/pdf/rust-cpp/core/save/).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
