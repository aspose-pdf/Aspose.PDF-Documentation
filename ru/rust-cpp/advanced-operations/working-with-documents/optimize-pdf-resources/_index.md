---
title: Оптимизировать ресурсы PDF с помощью Rust через C++
linktitle: Оптимизировать ресурсы PDF
type: docs
weight: 15
url: /ru/rust-cpp/optimize-pdf-resources/
description: Оптимизировать ресурсы PDF‑файлов с помощью инструмента Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Оптимизировать ресурсы PDF с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust через C++ предоставляет расширенные возможности для оптимизации ресурсов PDF, повышая эффективность документа и уменьшая размер файла. Библиотека позволяет разработчикам оптимизировать шрифты, изображения и метаданные, удаляя избыточные данные и сжимая ресурсы без ущерба для качества документа. Эти методы оптимизации улучшают производительность документа, делая PDF более удобными для обмена и хранения. Документация предлагает подробные рекомендации и примеры кода, помогающие разработчикам эффективно реализовать оптимизацию ресурсов в своих приложениях.
SoftwareApplication: rust-cpp
---

## Оптимизировать ресурсы PDF

Оптимизировать ресурсы в документе:

1. Ресурсы, которые не используются на страницах документа, удаляются.
1. Идентичные ресурсы объединяются в один объект.
1. Неиспользуемые объекты удаляются.

Оптимизация может включать сжатие изображений, удаление неиспользуемых объектов и оптимизацию шрифтов для уменьшения размера файла и повышения производительности. Любая ошибка во время этой операции журналируется и завершает работу программы.  
 
1. Откройте указанный PDF‑файл (sample.pdf) с помощью метода [открыть](https://reference.aspose.com/pdf/rust-cpp/core/open/).
1. Оптимизируйте ресурсы PDF с помощью метода [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/).
1. Сохраните оптимизированный PDF в новый файл с помощью метода [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/).

Следующий фрагмент кода показывает, как оптимизировать PDF‑документ.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document named "sample.pdf"
      let pdf = Document::open("sample.pdf")?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_open.pdf")?;

      Ok(())
  }
```
