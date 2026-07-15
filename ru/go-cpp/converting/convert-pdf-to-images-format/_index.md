---
title: Конвертация PDF в форматы изображений на Go
linktitle: Конвертация PDF в изображения
type: docs
weight: 70
url: /ru/go-cpp/convert-pdf-to-images-format/
lastmod: "2026-07-04"
description: Эта тема показывает, как использовать Aspose.PDF for Go для преобразования PDF в различные форматы изображений, например TIFF, BMP, JPEG, PNG, SVG, с помощью нескольких строк кода.
sitemap:
    changefreq: "monthly"
    priority: 0.5
TechArticle: true
AlternativeHeadline: Инструмент для преобразования PDF в формат изображений с помощью Aspose.PDF for Go.
Abstract: Aspose.PDF for Go via C++ обеспечивает бесшовное преобразование PDF‑документов в различные форматы изображений, включая JPEG, PNG, BMP и TIFF. Эта функция позволяет разработчикам создавать изображения высокого качества, сохраняющие содержимое, макет и разрешение исходного документа. Библиотека предоставляет гибкие параметры вывода, такие как разрешение, качество изображения и глубина цвета. Документация содержит пошаговые инструкции и примеры кода, помогающие разработчикам эффективно интегрировать преобразование PDF в изображение в свои приложения.
SoftwareApplication: go-cpp
---

## Go: преобразование PDF в изображение

В этой статье мы покажем вам варианты преобразования PDF в форматы изображений.

Ранее отсканированные документы часто сохраняются в формате PDF. Однако, нужно ли вам редактировать их в графическом редакторе или отправлять дальше в формате изображения? У нас есть универсальный инструмент для конвертации PDF в изображения с помощью **Aspose.PDF for Go via C++**.
Самой распространённой задачей является необходимость сохранить весь PDF‑документ или отдельные страницы документа в виде набора изображений. **Aspose.PDF for Go via C++** позволяет конвертировать PDF в форматы JPG и PNG, упрощая шаги, необходимые для получения изображений из конкретного PDF‑файла.

**Aspose.PDF for Go via C++** поддерживает конвертацию различных форматов PDF в изображения. Пожалуйста, проверьте раздел [Поддерживаемые форматы файлов Aspose.PDF](https://docs.aspose.com/pdf/go-cpp/supported-file-formats/).

## Конвертация PDF в JPEG

Предоставленный фрагмент кода на Go демонстрирует, как преобразовать первую страницу PDF‑документа в изображение JPEG с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте страницу в JPEG с помощью функции [PageToJpg](https://reference.aspose.com/pdf/go-cpp/convert/pagetojpg/).
1. Закройте PDF‑документ и освободите все выделенные ресурсы.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToJpg(num int32, resolution_dpi int32, filename string) saves the specified page as Jpg-image file
      err = pdf.PageToJpg(1, 100, "sample_page1.jpg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в JPEG онлайн**

Aspose.PDF представляет вам онлайн приложение ["PDF в JPEG"](https://products.aspose.app/pdf/conversion/pdf-to-jpg), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Конвертация Aspose.PDF PDF в JPEG с приложением](pdf_to_jpg.png)](https://products.aspose.app/pdf/conversion/pdf-to-jpg)
{{% /alert %}}

## Конвертировать PDF в TIFF

Предоставленный фрагмент кода на Go демонстрирует, как преобразовать первую страницу PDF‑документа в изображение TIFF с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте страницу в TIFF с помощью функции [PageToTiff](https://reference.aspose.com/pdf/go-cpp/convert/pagetotiff/).
1. Закройте PDF‑документ и освободите все выделенные ресурсы.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToTiff(num int32, resolution_dpi int32, filename string) saves the specified page as Tiff-image file
      err = pdf.PageToTiff(1, 100, "sample_page1.tiff")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в TIFF онлайн**

Aspose.PDF представляет вам онлайн приложение ["PDF в TIFF"](https://products.aspose.app/pdf/conversion/pdf-to-tiff), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Конвертация PDF в TIFF с приложением Aspose.PDF](pdf_to_tiff.png)](https://products.aspose.app/pdf/conversion/pdf-to-tiff)
{{% /alert %}}

## Конвертировать PDF в PNG

Предоставленный фрагмент кода на Go демонстрирует, как преобразовать первую страницу PDF‑документа в PNG‑изображение с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте страницу в PNG с помощью функции [PageToPng](https://reference.aspose.com/pdf/go-cpp/convert/pagetopng/).
1. Закройте PDF‑документ и освободите все выделенные ресурсы.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToPng(num int32, resolution_dpi int32, filename string) saves the specified page as Png-image file
      err = pdf.PageToPng(1, 100, "sample_page1.png")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PNG онлайн**

В качестве примера того, как работают наши бесплатные приложения, пожалуйста, проверьте следующую функцию.

Aspose.PDF представляет вам онлайн приложение ["PDF в PNG"](https://products.aspose.app/pdf/conversion/pdf-to-png), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Как конвертировать PDF в PNG с помощью бесплатного приложения](pdf_to_png.png)](https://products.aspose.app/pdf/conversion/pdf-to-png)
{{% /alert %}}

**Scalable Vector Graphics (SVG)** — это семейство спецификаций формата файла на основе XML для двумерной векторной графики, как статической, так и динамической (интерактивной или анимированной). Спецификация SVG является открытым стандартом, который разрабатывается World Wide Web Consortium (W3C) с 1999 года.

## Конвертировать PDF в SVG

Предоставленный фрагмент кода на Go демонстрирует, как преобразовать первую страницу PDF‑документа в изображение SVG с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте страницу в SVG с помощью функции [PageToSvg](https://reference.aspose.com/pdf/go-cpp/convert/pagetosvg/).
1. Закройте PDF‑документ и освободите все выделенные ресурсы.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToSvg(num int32, filename string) saves the specified page as Svg-image file
      err = pdf.PageToSvg(1, "sample_page1.svg")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в SVG онлайн**

Aspose.PDF представляет вам онлайн приложение ["PDF в SVG"](https://products.aspose.app/pdf/conversion/pdf-to-svg), где вы можете попытаться исследовать, как работает функциональность и качество.

[![Конвертация PDF в SVG с приложением Aspose.PDF](pdf_to_svg.png)](https://products.aspose.app/pdf/conversion/pdf-to-svg)
{{% /alert %}}

## Преобразовать PDF в DICOM

Предоставленный фрагмент кода на Go демонстрирует, как преобразовать первую страницу PDF‑документа в изображение DICOM с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте страницу в DICOM, используя функцию [PageToDICOM](https://reference.aspose.com/pdf/go-cpp/convert/pagetodicom/).
1. Закройте PDF‑документ и освободите все выделенные ресурсы.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToDICOM(num int32, resolution_dpi int32, filename string) saves the specified page as DICOM-image file
      err = pdf.PageToDICOM(1, 100, "sample_page1.dcm")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Конвертировать PDF в BMP

Предоставленный фрагмент кода на Go демонстрирует, как преобразовать первую страницу PDF‑документа в BMP‑изображение с использованием библиотеки Aspose.PDF:

1. Откройте PDF-документ.
1. Преобразуйте страницу в BMP, используя функцию [PageToBmp](https://reference.aspose.com/pdf/go-cpp/convert/pagetobmp/).
1. Закройте PDF‑документ и освободите все выделенные ресурсы.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
      // Open(filename string) opens a PDF-document with filename
      pdf, err := asposepdf.Open("sample.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // PageToBmp(num int32, resolution_dpi int32, filename string) saves the specified page as Bmp-image file
      err = pdf.PageToBmp(1, 100, "sample_page1.bmp")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
