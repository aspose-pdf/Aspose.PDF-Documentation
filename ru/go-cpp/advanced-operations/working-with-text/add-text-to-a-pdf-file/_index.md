---
title: Добавить текст в PDF с использованием Go
linktitle: Добавить текст в PDF
type: docs
weight: 10
url: /ru/go-cpp/add-text-to-pdf-file/
description: Узнайте, как добавить текст в PDF‑документ на Go с помощью Aspose.PDF для улучшения контента и редактирования документов.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Добавить текст в PDF с помощью Aspose.PDF для Go
Abstract: Раздел «Add Text to PDF File» документации Aspose.PDF для C++ и Go предоставляет пошаговые инструкции по программному вставлению текста в PDF‑документы. Описываются различные методы добавления текста, включая позиционирование, настройку шрифтов, регулирование цветов и варианты выравнивания текста. Руководство демонстрирует, как добавлять текст на конкретные страницы и в определённые места внутри PDF, обеспечивая точное размещение контента. С подробными примерами кода и объяснениями разработчики могут легко интегрировать функции вставки текста в свои приложения для улучшенного управления PDF‑документами.
SoftwareApplication: go-cpp
---

Чтобы добавить текст в существующий PDF‑файл:

1. Откройте PDF‑файл.
1. Добавьте текст в PDF‑документ с помощью [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) функция.
1. Сохраняет изменения в тот же файл.

## Добавление текста

Следующий фрагмент кода показывает, как добавить текст в существующий PDF‑файл.

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
        // PageAddText(num int32, addText string) adds text on page
        err = pdf.PageAddText(1, "added text")
        if err != nil {
            log.Fatal(err)
        }
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
