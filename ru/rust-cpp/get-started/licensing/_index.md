---
title: Лицензия Aspose PDF
linktitle: Лицензирование и ограничения
type: docs
weight: 90
url: /ru/rust-cpp/licensing/
description: Aspose. PDF for Rust приглашает своих клиентов получить Classic License. Также можно использовать limited license, чтобы лучше изучить продукт.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Лицензирование Aspose.PDF для Rust via C++
Abstract: Страница лицензирования Aspose.PDF для Rust via C++ объясняет доступные варианты лицензирования продукта. Клиенты могут выбрать Classic License, Metered License или limited license для целей оценки. Страница также подчеркивает преимущества получения полной лицензии, такие как разблокировка полной функциональности и снятие ограничений оценки.
SoftwareApplication: rust-cpp
---

## Лицензия

- **Исходный код Rust** лицензирован под лицензией MIT.
- **Общая библиотека** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) является проприетарной и требует коммерческой лицензии. Чтобы использовать весь набор функций, необходимо получить лицензию.

## Оценочная версия

Вы можете использовать **Aspose.PDF for Rust via C++** бесплатно для оценки. Оценочная версия предоставляет почти всю функциональность продукта с некоторыми ограничениями. Та же оценочная версия становится лицензированной, когда вы приобретаете лицензию и добавляете несколько строк кода для её применения.

- Если вы хотите протестировать Aspose.PDF for Rust без ограничений оценочной версии, вы также можете запросить 30‑дневную временную лицензию. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)?

### Ограничения версии оценки

Мы хотим, чтобы наши клиенты тщательно тестировали наши компоненты перед покупкой, поэтому оценочная версия позволяет использовать её так же, как обычно.

- **Документы, созданные с водяным знаком оценки**. Оценочная версия Aspose.PDF for Rust предоставляет полный функционал продукта, но все страницы в сгенерированных файлах помечены водяным знаком с текстом "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." в верхней части.
- **Ограничьте количество страниц, которые могут быть обработаны**. В оценочной версии вы можете обработать только первые четыре страницы документа.

### Использование в продакшене

В производственной среде требуется коммерческий лицензионный ключ. Пожалуйста, свяжитесь с нами для покупки коммерческой лицензии.

### Применить лицензию

Применение лицензии для включения полной функциональности Aspose.PDF для Rust с использованием файла лицензии (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```