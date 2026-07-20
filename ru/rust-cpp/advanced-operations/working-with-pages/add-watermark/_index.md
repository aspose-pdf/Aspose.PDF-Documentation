---
title: Добавить водяной знак в PDF с использованием Rust
linktitle: Добавить водяной знак
type: docs
weight: 80
url: /ru/rust-cpp/add-watermarks/
description: В этом примере демонстрируется, как добавить настраиваемый текстовый водяной знак в PDF‑документ с использованием Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить текстовый водяной знак
Abstract: Aspose.PDF for Rust via C++ предоставляет гибкий способ добавлять текстовые водяные знаки в PDF‑документы. В этом примере демонстрируется, как вставить настраиваемый водяной знак, указав содержимое текста, Font, размер, цвет, позицию, угол вращения, поведение слоёв и прозрачность. Водяные знаки обычно используются для брендинга, меток конфиденциальности, пометок черновика или защиты документа.
SoftwareApplication: rust-cpp
---

Эта [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) Метод позволяет разработчикам программно применять текстовый водяной знак к существующему PDF‑документу. Водяной знак может быть полностью настроен, включая:

- Текст водяного знака
- Семейство шрифтов
- Размер шрифта
- Цвет текста (в формате HEX)
- Координаты позиции X и Y
- Угол поворота
- Размещение на переднем или заднем плане
- Прозрачность (уровень прозрачности)

В этом примере приложение открывает существующий PDF‑файл, применяет полупрозрачный повернутый водяной знак и сохраняет изменённый документ под новым именем файла.

Эта функция особенно полезна для маркировки документов как Draft, Confidential, Sample, или для добавления фирменных элементов перед распространением.

1. Откройте существующий PDF‑документ.
1. Вызовите метод add_watermark и настройте свойства водяного знака.
1. Сохраните обновлённый документ.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```