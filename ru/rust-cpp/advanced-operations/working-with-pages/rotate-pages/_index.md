---
title: Поворот страниц PDF с помощью Rust через C++
linktitle: Поворот страниц PDF
type: docs
weight: 50
url: /ru/rust-cpp/rotate-pages/
description: В этом разделе описывается, как программно изменить ориентацию страниц в существующем файле PDF с использованием Rust через C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поворот страниц PDF с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ предоставляет надёжный функционал для поворота страниц в PDF‑документах, позволяя разработчикам при необходимости изменять ориентацию страниц. Библиотека поддерживает поворот страниц на 90, 180 или 270 градусов, обеспечивая быстрые и эффективные коррекции макета документа. Эта функция полезна для исправления неправильно ориентированных страниц или изменения презентации документа. Документация включает пошаговые инструкции и примеры кода, помогающие разработчикам бесшовно интегрировать возможности поворота страниц в свои приложения.
SoftwareApplication: rust-cpp
---

В этом разделе описывается, как изменить ориентацию страниц с альбомной на портретную и наоборот в существующем файле PDF с использованием Rust.

Поворот страниц обеспечивает правильное выравнивание при печати или отображении PDF в профессиональных условиях

1. Откройте PDF Document.
1. Повернуть PDF Pages. The [повернуть](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) функция применяет конкретный поворот (в данном случае 180 градусов) к заданной странице.
1. Сохранить изменения в новый файл. The [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) Функция создаёт новый PDF‑файл, чтобы сохранить оригинал и одновременно хранить обновлённую версию.

В этом примере вы вращаете определённую страницу в PDF‑документе:

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```