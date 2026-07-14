---
title: Оптимизировать PDF с помощью Aspose.PDF for Go via C++
linktitle: Оптимизировать PDF‑файл
type: docs
weight: 10
url: /ru/go-cpp/optimize-pdf/
description: Оптимизировать и сжимать PDF‑файлы с помощью инструмента Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Оптимизировать и сжимать PDF‑файлы с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предлагает мощные функции оптимизации, позволяющие уменьшить размер и повысить производительность PDF‑документов. Библиотека предоставляет различные варианты оптимизации, включая сжатие изображений, удаление неиспользуемых объектов, уменьшение размеров шрифтов и оптимизацию потоков контента. Эти функции помогают повысить эффективность хранения документов и обеспечить более быструю обработку и загрузку. Документация содержит пошаговые инструкции и примеры кода, которые помогают разработчикам эффективно внедрять оптимизацию PDF в своих приложениях.
SoftwareApplication: go-cpp
---

## Оптимизировать PDF‑документ

Набор инструментов Aspose.PDF for Go via C++ позволяет оптимизировать PDF‑документ.

Этот фрагмент кода полезен для приложений, где критично уменьшение размера или повышение эффективности PDF‑файлов, например для загрузки в веб, архивирования или передачи по ограниченной пропускной способности.

1. Эта [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) метод загружает указанный PDF‑файл (sample.pdf) в память.
1. Эта [Метод Optimize](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) уменьшает размер файла, выполняя оптимизацию, такую как удаление неиспользуемых объектов, сжатие изображений, уплощение аннотаций, извлечение шрифтов и включение повторного использования контента. Эти шаги помогают снизить требования к хранилищу и повысить скорость обработки PDF‑документа.
1. Эта [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) метод сохраняет оптимизированный PDF в новый файл.

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```