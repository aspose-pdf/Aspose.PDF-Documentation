---
title: Добавление заголовка и нижнего колонтитула в PDF с использованием Rust
linktitle: Добавление заголовка и нижнего колонтитула в PDF
type: docs
weight: 90
url: /ru/rust-cpp/add-headers-and-footers-of-pdf-file/
description:
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как добавить заголовок и нижний колонтитул в PDF с помощью Rust
Abstract: В этой статье показано, как добавить текстовые заголовки и нижние колонтитулы в PDF‑документы с использованием библиотеки asposepdf для Rust. Описано, как открыть существующий PDF, вставить одинаковый текст в заголовок или нижний колонтитул каждой страницы и сохранить изменённый документ в виде нового файла. Примеры демонстрируют простой, надёжный от ошибок рабочий процесс, который можно использовать для таких задач, как добавление номеров страниц, заголовков или фирменного брендинга программно в приложениях на Rust.
SoftwareApplication: rust-cpp
---

## Добавление заголовков и нижних колонтитулов в виде текстовых фрагментов

### Добавить текст в нижний колонтитул PDF‑документа

Наш инструмент позволяет открыть существующий PDF, добавить текстовый нижний колонтитул на все страницы и сохранить изменённый PDF как новый файл, используя библиотеку asposepdf Rust. Он обрабатывает ошибки корректно с помощью типа Result в Rust.

1. Откройте существующий PDF‑документ.
1. Добавьте текст в нижний колонтитул с помощью [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. Сохраните изменённый PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### Добавить текст в заголовок PDF-документа

Этот фрагмент кода демонстрирует, как открыть существующий PDF‑файл, добавить текстовый заголовок на все страницы и сохранить изменённый документ как новый файл с использованием библиотеки asposepdf. Он предоставляет простой автоматизированный способ вставки одинаковых заголовков в PDF‑документы.

1. Открыть существующий PDF.
1. Добавить текст в заголовок с помощью подсказок [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. Сохраните изменённый PDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```