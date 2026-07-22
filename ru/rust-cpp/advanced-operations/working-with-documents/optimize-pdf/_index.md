---
title: Оптимизировать PDF с помощью Aspose.PDF for Rust via C++
linktitle: Оптимизировать PDF‑файл
type: docs
weight: 10
url: /ru/rust-cpp/optimize-pdf/
description: Оптимизировать и сжать PDF‑файлы с помощью инструмента Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Оптимизировать и сжать PDF‑файлы с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ предлагает мощные функции оптимизации для уменьшения размера и повышения производительности PDF‑документов. Библиотека предоставляет различные варианты оптимизации, включая сжатие изображений, удаление неиспользуемых объектов, уменьшение размеров шрифтов и оптимизацию потоков содержимого. Эти функции помогают улучшить эффективность хранения документов и обеспечивают более быструю обработку и загрузку. Документация содержит пошаговые инструкции и примеры кода, помогающие разработчикам эффективно реализовать оптимизацию PDF в своих приложениях.
SoftwareApplication: rust-cpp
---

## Оптимизировать PDF‑документ

Набор инструментов Aspose.PDF для Rust via C++ позволяет оптимизировать PDF‑документ.

Этот фрагмент кода полезен для приложений, где критически важны уменьшение размера или повышение эффективности PDF‑файлов, например при загрузке в веб, архивировании или обмене при ограниченной пропускной способности.

1. Откройте указанный PDF‑файл (sample.pdf) с помощью метода [открыть](https://reference.aspose.com/pdf/rust-cpp/core/open/).
1. Уменьшите размер файла с помощью [оптимизировать](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/). Метод удаляет неиспользуемые объекты, сжимает изображения, уплощает аннотации, удаляет встроенные шрифты и включает повторное использование контента.
1. Сохраните оптимизированный PDF в новый файл с помощью метода [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```
