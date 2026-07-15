---
title: Лицензия Aspose PDF
linktitle: Лицензирование и ограничения
type: docs
weight: 90
url: /ru/go-cpp/licensing/
description: Aspose. PDF for Go приглашает своих клиентов получить Классическую лицензию. Также использовать ограниченную лицензию для более детального изучения продукта.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Лицензирование Aspose.PDF для Go через C++
Abstract: Страница лицензирования для Aspose.PDF для Go через C++ объясняет доступные варианты лицензирования продукта. Клиенты могут выбрать между Классической лицензией, Metered License или ограниченной лицензией для целей оценки. Страница также подчёркивает преимущества получения полноценной лицензии, такие как разблокировка полной функциональности и снятие ограничений оценки.
SoftwareApplication: go-cpp
---


## Ограничения версии для оценки

Мы хотим, чтобы наши клиенты тщательно тестировали наши компоненты перед покупкой, поэтому версия оценки позволяет использовать её так же, как обычно.

- **Документы, созданные с оценочным водяным знаком.** Оценочная версия Aspose.PDF for Go предоставляет полноценный набор функций продукта, но все страницы в создаваемых файлах имеют водяной знак с текстом "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." в верхней части.

- **Ограничить количество страниц, которые могут быть обработаны.**
В оценочной версии вы можете обрабатывать только первые четыре страницы документа.

>Если вы хотите протестировать Aspose.PDF for Go без ограничений оценочной версии, вы также можете запросить 30‑дневную временную лицензию. Пожалуйста, обратитесь к [Как получить временную лицензию?](https://purchase.aspose.com/temporary-license)

## Классическая лицензия

Применение лицензии для включения полной функциональности библиотеки Aspose.PDF с использованием файла лицензии (Aspose.PDF.GoViaCPP.lic).

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
