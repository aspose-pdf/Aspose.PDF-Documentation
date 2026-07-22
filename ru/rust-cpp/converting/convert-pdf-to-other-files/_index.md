---
title: Конвертировать PDF в EPUB, TeX, Text, XPS на Rust
linktitle: Конвертировать PDF в другие форматы
type: docs
weight: 90
url: /ru/rust-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-20"
description: В этой теме показывается, как с помощью Rust преобразовать файл PDF в другие форматы, такие как EPUB, LaTeX, Text, XPS и т.д.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Инструмент Rust для преобразования PDF в EPUB, TeX, Text и XPS
Abstract: Aspose.PDF for Rust via C++ предлагает мощные возможности для конвертации PDF‑документов в различные форматы файлов, включая DOCX, PPTX, HTML, EPUB, SVG и другие. Эта функциональность позволяет разработчикам без труда извлекать и повторно использовать содержимое PDF, сохраняя при этом форматирование, структуру и качество в разных выходных форматах. Библиотека предоставляет гибкие варианты настройки процесса конвертации в соответствии с конкретными требованиями. Документация включает всесторонние руководства и примеры кода, помогающие разработчикам эффективно внедрять конвертацию PDF в файл в своих приложениях.
SoftwareApplication: rust-cpp
---

## Конвертировать PDF в EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** является бесплатным и открытым стандартом электронных книг от International Digital Publishing Forum (IDPF). Файлы имеют расширение .epub.
EPUB разработан для текучего контента, что означает, что читалка EPUB может оптимизировать текст под конкретное устройство отображения. EPUB также поддерживает контент фиксированного макета. Формат предназначен как единый формат, который издатели и компании по конвертации могут использовать внутри компании, а также для распространения и продажи. Он заменил стандарт Open eBook.

Приведённый фрагмент кода на Rust демонстрирует, как преобразовать документ PDF в EPUB с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Конвертируйте файл PDF в EPUB с помощью [сохранить_epub](https://reference.aspose.com/pdf/rust-cpp/convert/save_epub/) функция.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Epub-document
      pdf.save_epub("sample.epub")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в EPUB онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), где вы можете попытаться исследовать функциональность и качество, как оно работает.

[![Aspose.PDF Конвертация PDF в EPUB с бесплатным приложением](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Конвертировать PDF в TeX

**Aspose.PDF for Rust** поддерживает конвертирование PDF в TeX.
Формат файлов LaTeX — это текстовый формат файлов со специальной разметкой, используемый в системе подготовки документов на основе TeX для высококачественной верстки.

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать документ PDF в TeX с помощью библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте PDF‑файл в TeX с помощью [save_tex](https://reference.aspose.com/pdf/rust-cpp/convert/save_tex/) функция.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as TeX-document
      pdf.save_tex("sample.tex")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в LaTeX/TeX онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), где вы можете попытаться исследовать функциональность и качество, как оно работает.

[![Aspose.PDF Конвертация PDF в LaTeX/TeX с бесплатным приложением](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Конвертировать PDF в TXT

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать PDF‑документ в TXT с помощью библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Конвертируйте PDF-файл в TXT с помощью [save_txt](https://reference.aspose.com/pdf/rust-cpp/convert/save_txt/) функция.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Txt-document
      pdf.save_txt("sample.txt")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в текст онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в Текст"](https://products.aspose.app/pdf/conversion/pdf-to-txt), где вы можете попытаться исследовать функциональность и качество, как оно работает.

[![Aspose.PDF преобразование PDF в текст с бесплатным приложением](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Конвертировать PDF в XPS

Тип файла XPS в первую очередь связан со спецификацией XML Paper Specification, разработанной корпорацией Microsoft. Спецификация XML Paper Specification (XPS), ранее имевшая кодовое название Metro и включающая маркетинговую концепцию Next Generation Print Path (NGPP), является инициативой Microsoft по интеграции создания и просмотра документов в операционную систему Windows.

**Aspose.PDF for Rust** предоставляет возможность конвертировать PDF‑файлы в <abbr title="XML Paper Specification">XPS</abbr> формат. Давайте попробуем использовать представленный фрагмент кода для конвертации PDF‑файлов в формат XPS на Rust.

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать документ PDF в XPS с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Конвертируйте PDF-файл в XPS, используя [save_xps](https://reference.aspose.com/pdf/rust-cpp/convert/save_xps/) функция.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Xps-document
      pdf.save_xps("sample.xps")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в XPS онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), где вы можете попытаться исследовать функциональность и качество, как оно работает.

[![Aspose.PDF Конвертация PDF в XPS с бесплатным приложением](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Преобразовать PDF в PDF в градациях серого

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в градационный PDF, используя библиотеку Aspose.PDF:

1. Откройте PDF-документ.
1. Конвертируйте страницу PDF в PDF в градациях серого с помощью [страница_оттенки_серого](https://reference.aspose.com/pdf/rust-cpp/organize/page_grayscale/) функция.

Этот пример преобразует определённую страницу вашего PDF в градации серого:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Convert page to black and white
      pdf.page_grayscale(1)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_page1_grayscale.pdf")?;

      Ok(())
  }
```

## Преобразовать PDF в Markdawn

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать PDF‑документ в файл Markdown (.md) с использованием Aspose.PDF for Rust.

1. Откройте исходный PDF-файл.
1. Конвертируйте PDF в Markdown.
1. Сохраните открытый PDF‑документ как файл Markdown.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Markdown-document
      pdf.save_markdown("sample.md")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в MD онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в MD"](https://products.aspose.app/pdf/conversion/md), где вы можете попытаться исследовать функциональность и качество, как оно работает.

[![Aspose.PDF Конвертация PDF в MD с бесплатным приложением](pdf_to_md.png)](https://products.aspose.app/pdf/conversion/md)
{{% /alert %}}
