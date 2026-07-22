---
title: Извлечь текст из PDF с использованием Rust
linktitle: Извлечь текст из PDF
type: docs
weight: 30
url: /ru/rust-cpp/extract-text-from-pdf/
description: В этой статье описываются различные способы извлечения текста из PDF‑документов с помощью Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечь текст с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ предоставляет мощный и эффективный способ извлечения текста из PDF‑документов. Библиотека поддерживает несколько методов извлечения, позволяя пользователям получать текст из целых документов, определённых страниц или предопределённых областей внутри PDF.
SoftwareApplication: rust-cpp
---

## Извлеките текст из PDF‑документа

Извлечение текста из PDF‑документа — очень распространённая и полезная задача. PDF‑файлы часто содержат критически важную информацию, к которой необходимо получить доступ, проанализировать её или обработать для различных целей. Извлечение текста упрощает повторное использование в базах данных, отчётах или других документах.

Извлечение текста делает содержимое PDF доступным для поиска, позволяя пользователям быстро находить конкретную информацию без необходимости вручную просматривать весь документ.

Если вам нужно извлечь текст из PDF‑документа, вы можете использовать [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) функцию.
Пожалуйста, ознакомьтесь со следующим фрагментом кода, чтобы извлечь текст из PDF‑файла с помощью Rust.

1. Откройте PDF‑документ с указанным именем файла.
1. Вызовите [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/), чтобы извлечь текстовое содержимое из PDF‑документа.
1. Выведите извлечённый текст в консоль.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```
