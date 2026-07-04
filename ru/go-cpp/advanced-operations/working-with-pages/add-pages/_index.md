---
title: Добавить страницы в PDF‑документ
linktitle: Добавить страницы
type: docs
weight: 10
url: /ru/go-cpp/add-pages/
description: Изучите, как добавить страницы в существующий PDF на Go с помощью Aspose.PDF для улучшения и расширения ваших документов.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Добавить страницы PDF с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предоставляет мощный функционал для добавления страниц в PDF‑документы, позволяя разработчикам динамически создавать новые страницы и настраивать их в соответствии с конкретными требованиями. Библиотека поддерживает вставку пустых страниц или копирование страниц из существующих документов, предлагая варианты определения размера страницы, ориентации и содержимого. Эти возможности обеспечивают бесшовное расширение и настройку документов. Документация содержит подробные инструкции и примеры кода, помогающие разработчикам эффективно реализовать функции добавления страниц в своих приложениях.
SoftwareApplication: go-cpp
---

## Добавить страницу в PDF‑файл

Предоставленный фрагмент кода на Go демонстрирует, как выполнить операцию Add Page в конце PDF с использованием библиотеки Aspose.PDF. 

1. Откройте существующий PDF файл (sample.pdf) с помощью функции [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) для манипуляций. Это необходимо для любых операций, связанных с PDF, таких как редактирование, добавление контента или чтение данных.
1. Вставьте новую пустую страницу в существующий PDF документ с помощью метода [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/). Это полезно для расширения документа или подготовки его к дополнительному контенту.
1. Сохраните изменения PDF обратно в файл с помощью метода [Save](https://reference.aspose.com/pdf/go-cpp/core/save/). Этот шаг критически важен для сохранения изменений, таких как добавление новых страниц.
1. Вызовите метод [Close](https://reference.aspose.com/pdf/go-cpp/core/close/) с помощью defer для освобождения любых ресурсов, выделенных во время операций с PDF. Это важно для предотвращения утечек памяти и обеспечения эффективного использования ресурсов.

Этот фрагмент кода — краткий и эффективный пример того, как использовать библиотеку Aspose.PDF Go для базовых задач манипуляции PDF.

Aspose.PDF for Go позволяет вставлять страницу в документ PDF в любое место файла, а также добавлять страницы в конец PDF‑файла.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## Вставить страницу в PDF‑файл

The [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) метод вставляет новую страницу в указанную позицию. Эта функция полезна, когда необходимо добавить дополнительные страницы в существующий документ, например, добавить новый раздел или содержимое в отчет или презентацию.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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
