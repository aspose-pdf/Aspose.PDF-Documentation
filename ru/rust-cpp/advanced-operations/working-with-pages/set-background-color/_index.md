---
title: Установите цвет фона для PDF с помощью Rust через C\u002B\u002B
linktitle: Установить цвет фона
type: docs
weight: 80
url: /ru/rust-cpp/set-background-color/
description: Установите цвет фона для вашего PDF‑файла с помощью Rust через C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установите цвет фона для PDF с Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C\u002B\u002B предлагает возможность задавать цвет фона страниц PDF, позволяя разработчикам настраивать внешний вид документов. Эта функция позволяет применять сплошные цвета ко всему фону страницы, улучшая визуальное представление документа. Разработчики могут легко указывать значения цветов, используя стандартные цветовые модели, такие как RGB или CMYK. Документация предоставляет подробные инструкции и примеры кода, помогающие разработчикам эффективно внедрять настройку цвета фона в своих C\u002B\u002B приложениях.
SoftwareApplication: rust-cpp
---

1. Откройте указанный PDF‑файл с помощью метода [открыть](https://reference.aspose.com/pdf/rust-cpp/core/open/).
1. Установите новый цвет фона с помощью метода [set_background](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/), указав значения RGB.
1. Сохраните обновлённый PDF под новым именем с помощью метода [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

Этот код идеально подходит для приложений, которым необходимо автоматизировать настройку PDF, например, создавать фирменные отчёты, добавлять водяные знаки или улучшать визуальную согласованность в нескольких документах.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```
