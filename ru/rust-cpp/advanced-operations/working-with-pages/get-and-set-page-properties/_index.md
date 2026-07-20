---
title: Получить и установить свойства страниц
linktitle: Получить и установить свойства страниц
type: docs
url: /ru/rust-cpp/get-and-set-page-properties/
description: Узнайте, как получить и установить свойства страниц PDF‑документов с помощью Aspose.PDF for Rust, позволяя настраивать форматирование документа.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Получить и установить свойства страниц с помощью Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C\u002B\u002B предоставляет комплексные возможности для получения и установки свойств страниц в PDF‑документах, позволяя разработчикам получать доступ и изменять различные атрибуты страниц, такие как размер, поворот, поля и метаданные. Эти возможности обеспечивают точный контроль над макетом и внешним видом документа в соответствии с конкретными требованиями приложения. Библиотека гарантирует бесшовную настройку и оптимизацию страниц PDF. Документация предлагает подробные руководства и примеры кода, помогающие разработчикам эффективно получать и обновлять свойства страниц в своих приложениях.
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust позволяет читать и устанавливать свойства страниц в PDF‑файле. Этот раздел показывает, как получить количество страниц в PDF‑файле, получить информацию о свойствах страницы PDF, таких как цвет, и установить свойства страниц.

## Получить количество страниц в PDF‑файле

При работе с документами часто требуется узнать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

**Aspose.PDF for Rust via C++** позволяет подсчитать количество страниц с помощью [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) функции.

Следующий фрагмент кода предназначен для открытия PDF‑документа, получения количества его страниц и последующего вывода результата.

The [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) Метод вызывается для получения общего количества страниц в PDF‑документе. Это полезно для задач, которым необходимо знать длину документа, например при извлечении определённых страниц или выполнении операций на всех страницах. Этот метод — простой способ запросить структуру документа.

Чтобы получить количество страниц в PDF‑файле:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## Установить размер страницы

В этом примере метод pdf.PageSetSize() изменяет размер первой страницы PDF‑документа. Константа PageSizeA1 гарантирует, что первая страница будет установлена на размер бумаги A1. Это полезно при конвертации документов в стандартизированный формат или при обеспечении того, чтобы конкретный контент правильно помещался на страницах.

1. Открытие PDF‑документа с помощью [открыть](https://reference.aspose.com/pdf/rust-cpp/core/open/) метод.
1. Установка размера страницы с помощью [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) функции.
1. Сохранение документа с использованием [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) метод.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```