---
title: Пример Hello World с использованием языка Rust
linktitle: Пример Hello World
type: docs
weight: 40
url: /ru/rust-cpp/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF‑документ с текстом Hello World с использованием Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World через Aspose.PDF for Rust
Abstract: Руководство «Начало работы» для Aspose.PDF for Rust через C++ предоставляет вводную информацию по работе с библиотекой, охватывая базовые шаги по созданию и манипулированию PDF‑документами. Оно включает пример «Hello World», демонстрирующий, как сгенерировать простой PDF‑файл с текстовым содержимым, помогая разработчикам быстро понять основную функциональность API.
SoftwareApplication: rust-cpp
---

Пример «Hello World» традиционно используется для представления возможностей языка программирования или программного обеспечения на простом примере.

**Aspose.PDF for Rust** — это полнофункциональный API для PDF, позволяющий разработчикам внедрять возможности создания, манипулирования и конвертации PDF‑документов с помощью Rust. Он поддерживает многие популярные форматы файлов, включая PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, форматы изображений и т.д. В этой статье мы создаём PDF‑документ, содержащий текст "Hello World!". После установки Aspose.PDF for Rust в вашей среде вы можете выполнить пример кода, чтобы увидеть, как работает API Aspose.PDF.
Следующий фрагмент кода выполняет такие шаги:

1. Создайте новый экземпляр PDF‑документа.
1. Добавьте новую страницу в PDF‑документ с помощью функции [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/).
1. Установите размер страницы с помощью [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. Добавьте текст "Hello World!" на первую страницу с помощью [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. Сохраните PDF‑документ с помощью метода [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

Следующий фрагмент кода — это программа Hello World, демонстрирующая работу API Aspose.PDF for Rust.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
