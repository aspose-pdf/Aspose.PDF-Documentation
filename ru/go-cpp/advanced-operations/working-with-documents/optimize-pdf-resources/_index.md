---
title: Оптимизировать ресурсы PDF с помощью Go
linktitle: Оптимизировать ресурсы PDF
type: docs
weight: 15
url: /ru/go-cpp/optimize-pdf-resources/
description: Оптимизировать ресурсы PDF‑файлов с помощью инструмента Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Оптимизировать ресурсы PDF с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предоставляет расширенные возможности оптимизации ресурсов PDF, повышая эффективность документа и уменьшая размер файла. Библиотека позволяет разработчикам оптимизировать шрифты, изображения и метаданные, удаляя избыточные данные и сжимая ресурсы без ущерба качеству документа. Эти методы оптимизации улучшают производительность документа, делая PDF более удобными для обмена и хранения. Документация предлагает подробные рекомендации и примеры кода, помогающие разработчикам эффективно реализовать оптимизацию ресурсов в своих приложениях.
SoftwareApplication: go-cpp
---

## Оптимизировать ресурсы PDF

Оптимизировать ресурсы в документе:

  1. Ресурсы, которые не используются на страницах документа, удаляются.
  1. Равные ресурсы объединяются в один объект.
  1. Неиспользуемые объекты удаляются.

Оптимизация может включать сжатие изображений, удаление неиспользуемых объектов и оптимизацию шрифтов для уменьшения размера файла и повышения производительности. Любая ошибка во время этой операции регистрируется и завершает работу программы.  
 
1. Откройте указанный PDF‑файл (sample.pdf) с помощью метода [Open](https://reference.aspose.com/pdf/go-cpp/core/open/).
1. Оптимизирует ресурсы внутри PDF для повышения эффективности, используя [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) метод.
1. Сохраните оптимизированный PDF в новый файл с помощью метода [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

В следующем фрагменте кода показано, как оптимизировать PDF‑документ.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```
