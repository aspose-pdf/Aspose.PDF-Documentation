---
title: Компоновка PDF с использованием Aspose.PDF for Rust via C++
linktitle: Компоновка PDF
type: docs
weight: 30
url: /ru/rust-cpp/pdf-imposition/
description: В этой статье объясняется, как переставлять страницы PDF для печатных оптимизированных макетов с использованием Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Как создать буклет или N-Up из PDF‑файлов
Abstract: Aspose.PDF for Rust via C++ предоставляет мощные инструменты для реструктуризации PDF‑документов в соответствии с требованиями печати и макетирования. В этой статье демонстрируется, как преобразовать обычный PDF в буклет, обеспечивая правильный порядок страниц для складывания, и как создать PDF в формате N-Up, объединяя несколько страниц в один лист. С помощью лаконичных примеров кода на Rust разработчики могут быстро реализовать трансформации PDF, готовые к печати, для документации, публикации и архивных рабочих процессов.
SoftwareApplication: rust-cpp
---

## Создайте N-Up PDF

PDF с N-Up размещает несколько исходных страниц на одной результирующей странице. В этом примере используется макет 2 × 2, поэтому четыре оригинальные страницы комбинируются в каждую страницу выходного документа.

1. Откройте исходный PDF‑документ.
1. Сохраните документ, используя макет N-Up с указанным числом строк и столбцов.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## Создайте брошюру из PDF

Aspose.PDF for Rust via C++ объясняет, как преобразовать стандартный PDF‑документ в PDF‑документ в формате буклета.
Формат буклета переупорядочивает страницы так, чтобы при печати и складывании документ образовывал правильный буклет с страницами в правильном порядке.

1. Откройте исходный PDF‑документ.
1. Сохраните документ как PDF‑буклет.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**Обратите внимание, что для полной функциональности требуется лицензия Free Trial.**

Исследуйте результат создания буклета из 4 страниц.

![Пример буклета из 4 страниц](sample_4.png)

Исследуйте результат создания буклета из 3 страниц.

![Пример буклета из 3 страниц](sample_3.png)
