---
title: Преобразовать PDF в форматы изображений на Rust
linktitle: Преобразовать PDF в изображения
type: docs
weight: 70
url: /ru/rust-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-20"
description: В этой теме показано, как использовать Aspose.PDF for Rust для преобразования PDF в различные форматы изображений, например TIFF, BMP, JPEG, PNG, SVG, с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Инструмент для преобразования PDF в форматы изображений с Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ обеспечивает бесшовное преобразование PDF‑документов в различные форматы изображений, включая JPEG, PNG, BMP и TIFF. Эта функция позволяет разработчикам рендерить изображения высокого качества, сохраняя содержание, макет и разрешение оригинального документа. Библиотека предоставляет гибкие параметры выходных настроек, такие как разрешение, качество изображения и глубина цвета. Документация предлагает пошаговые инструкции и примеры кода, чтобы помочь разработчикам эффективно интегрировать преобразование PDF в изображение в свои приложения.
SoftwareApplication: rust-cpp
---

## Преобразуйте PDF в изображение

В этой статье мы покажем вам варианты конвертации PDF в форматы изображений.

Ранее отсканированные документы часто сохраняются в формате PDF. Однако вам нужно отредактировать их в графическом редакторе или отправить дальше в формате изображения? У нас есть универсальный инструмент, позволяющий конвертировать PDF в изображения с использованием **Aspose.PDF for Rust via C++**.
Самая распространённая задача — когда необходимо сохранить весь PDF‑документ или отдельные страницы документа в виде набора изображений. **Aspose.PDF for Rust via C++** позволяет конвертировать PDF в форматы JPG и PNG, упрощая шаги, необходимые для получения изображений из конкретного PDF‑файла.

**Aspose.PDF for Rust via C++** поддерживает конвертацию различных форматов PDF в изображения. Пожалуйста, проверьте раздел. [Поддерживаемые форматы файлов Aspose.PDF](https://docs.aspose.com/pdf/rust-cpp/supported-file-formats/).

### Конвертируйте PDF в JPEG

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в изображение JPEG с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Конвертируйте страницу в JPEG с помощью функции [page_to_jpg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_jpg/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Jpg-image
      pdf.page_to_jpg(1, 100, "sample_page1.jpg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в JPEG онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), где вы можете попытаться исследовать функциональность и качество его работы.

[![Конвертация PDF в JPEG с бесплатным приложением Aspose.PDF](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

### Конвертируйте PDF в TIFF

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в изображение TIFF с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Конвертируйте страницу в TIFF с помощью функции [page_to_tiff](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_tiff/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Tiff-image
      pdf.page_to_tiff(1, 100, "sample_page1.tiff")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попытаться исследовать функциональность и качество его работы.

[![Конвертация PDF в TIFF с бесплатным приложением Aspose.PDF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

### Конвертируйте PDF в PNG

Приведённый фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в изображение PNG с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Конвертируйте страницу в PNG с помощью функции [page_to_png](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_png/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Png-image
      pdf.page_to_png(1, 100, "sample_page1.png")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, проверьте следующую функцию.

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попытаться исследовать функциональность и качество его работы.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций XML‑основанного формата файлов для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается World Wide Web Consortium (W3C) с 1999 года.

### Конвертируйте PDF в SVG

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в SVG‑изображение с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Преобразуйте страницу в SVG с помощью функции [page_to_svg](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_svg/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Svg-image
      pdf.page_to_svg(1, "sample_page1.svg")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Попробуйте преобразовать PDF в SVG онлайн**

Aspose.PDF for Rust представляет вам онлайн бесплатное приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попытаться исследовать функциональность и качество его работы.

[![Aspose.PDF Конвертация PDF в SVG с бесплатным приложением](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

### Конвертируйте PDF в ZIP‑архив SVG

Следующий пример преобразует PDF‑документ в SVG‑архив, где каждая страница сохраняется как отдельный SVG‑файл внутри ZIP‑контейнера.

1. Откройте исходный документ PDF.
1. Сохраните документ как ZIP-архив, содержащий SVG-файлы.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as SVG-archive
      pdf.save_svg_zip("sample_svg.zip")?;

      Ok(())
  }
```

### Преобразуйте PDF в DICOM

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в изображение DICOM с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Конвертируйте страницу в DICOM с помощью функции [page_to_dicom](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_dicom/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as DICOM-image
      pdf.page_to_dicom(1, 100, "sample_page1.dcm")?;

      Ok(())
  }
```

### Преобразуйте PDF в BMP

Предоставленный фрагмент кода на Rust демонстрирует, как преобразовать первую страницу PDF‑документа в изображение BMP с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Конвертируйте страницу в BMP с помощью функции [page_to_bmp](https://reference.aspose.com/pdf/rust-cpp/convert/page_to_bmp/).

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the specified page as Bmp-image
      pdf.page_to_bmp(1, 100, "sample_page1.bmp")?;

      Ok(())
  }
```
