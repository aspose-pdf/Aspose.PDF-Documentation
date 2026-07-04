---
title: Поворот страниц PDF с помощью Go
linktitle: Поворот страниц PDF
type: docs
weight: 50
url: /ru/go-cpp/rotate-pages/
description: В этой статье описывается, как программно изменить ориентацию страниц в существующем файле PDF с помощью Go через C++
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Поворот страниц PDF с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go через C++ предоставляет мощный функционал для поворота страниц в PDF‑документах, позволяя разработчикам при необходимости изменять ориентацию страниц. Библиотека поддерживает поворот страниц на 90, 180 или 270 градусов, обеспечивая быстрые и эффективные коррективы макета документа. Эта возможность полезна для исправления неправильно ориентированных страниц или изменения представления документа. Документация включает пошаговые инструкции и примеры кода, помогающие разработчикам беспрепятственно интегрировать возможности поворота страниц в свои приложения.
SoftwareApplication: go-cpp
---

В этом разделе описывается, как изменить ориентацию страниц с альбомной на портретную и обратно в существующем файле PDF с использованием Go.

Поворот страниц обеспечивает правильное выравнивание при печати или отображении PDF в профессиональных условиях

1. Откройте PDF‑документ.
1. Поверните страницы PDF. Функция [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) применяет определённый поворот (в данном случае 180 градусов) к указанной странице.
1. Сохраните изменения в новый файл. Функция [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) создаёт новый файл PDF, чтобы сохранить оригинал и одновременно сохранить обновлённую версию.

В этом примере вы вращаете определённую страницу в PDF‑документе:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

У вас также есть возможность повернуть все страницы PDF в вашем документе:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```
