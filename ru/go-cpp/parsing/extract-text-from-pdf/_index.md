---
title: Извлечение текста из PDF с помощью Go
linktitle: Извлечение текста из PDF
type: docs
weight: 30
url: /ru/go-cpp/extract-text-from-pdf/
description: В этой статье описаны различные способы извлечения текста из PDF‑документов с использованием Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Извлечение текста с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предоставляет мощный и эффективный способ извлечения текста из PDF‑документов. Библиотека поддерживает несколько методов извлечения, позволяя пользователям получать текст из целых документов, определённых страниц или заранее заданных областей в PDF.
SoftwareApplication: go-cpp
---

## Извлечение текста из PDF‑документа

Извлечение текста из PDF‑документа — очень распространённая и полезная задача. PDF‑файлы часто содержат критически важную информацию, к которой необходимо получить доступ, проанализировать её или обработать в разных целях. Извлечение текста упрощает повторное использование в базах данных, отчётах или других документах.

Извлечение текста делает содержимое PDF доступным для поиска, позволяя пользователям быстро находить конкретную информацию без необходимости вручную просматривать весь документ.

Если вы хотите извлечь текст из PDF‑документа, вы можете использовать [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) функцию.
Пожалуйста, проверьте следующий фрагмент кода, чтобы извлечь текст из PDF‑файла с помощью Go.

1. Откройте PDF‑документ с указанным именем файла.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) извлекает текстовое содержимое из PDF‑документа.
1. Выведите извлечённый текст на консоль.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"
    import "fmt"

    func main() {
        // Open(filename string) opens a PDF-document with filename
        pdf, err := asposepdf.Open("sample.pdf")
        if err != nil {
            log.Fatal(err)

        }
        // ExtractText() returns PDF-document contents as plain text
        txt, err := pdf.ExtractText()
        if err != nil {
            log.Fatal(err)
        }
        // Print
        fmt.Println("Extracted text:\n", txt)
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```