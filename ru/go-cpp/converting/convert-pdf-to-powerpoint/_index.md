---
title: Конвертировать PDF в PPTX на Go
linktitle: Конвертировать PDF в PowerPoint
type: docs
weight: 30
url: /ru/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF позволяет конвертировать PDF в формат PPTX, используя Go.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Инструмент Golang для конвертации PDF в PowerPoint
Abstract: Aspose.PDF для Go через C++ предоставляет надёжное решение для преобразования PDF‑документов в формат PowerPoint (PPTX) с сохранением оригинального макета, форматирования и структуры контента. Эта функция позволяет разработчикам без труда преобразовывать статические PDF‑файлы в динамичные, редактируемые презентации. Библиотека предлагает параметры настройки, позволяющие контролировать процесс конвертации, обеспечивая вывод высокого качества, подходящий для бизнес‑ и профессионального использования. Документация предоставляет пошаговые инструкции и образцы кода, помогающие разработчикам эффективно интегрировать конвертацию PDF‑в‑PowerPoint в свои приложения.
SoftwareApplication: go-cpp
---

## Конвертировать PDF в PPTX

Предоставленный фрагмент кода на Go демонстрирует, как конвертировать PDF‑документ в PPTX с использованием библиотеки Aspose.PDF:

1. Откройте PDF‑документ.
1. Преобразуйте PDF‑файл в PPTX с помощью функции [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/).
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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в PowerPoint онлайн**

Aspose.PDF представляет вам онлайн приложение [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), где вы можете попробовать изучить функциональность и качество, с которым он работает.

[![Aspose.PDF Конвертация PDF в PPTX с приложением](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}
