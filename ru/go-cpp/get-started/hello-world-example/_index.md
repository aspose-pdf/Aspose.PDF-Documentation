---
title: Пример Hello World с использованием языка Go
linktitle: Пример Hello World
type: docs
weight: 40
url: /ru/go-cpp/hello-world-example/
description: Этот пример демонстрирует, как создать простой PDF‑документ с текстом Hello World с использованием Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World через Aspose.PDF for Go
Abstract: Руководство «Get Started» для Aspose.PDF for Go via C++ предоставляет введение в работу с библиотекой, охватывая базовые шаги по созданию и манипулированию PDF‑документами. Оно включает пример 'Hello World', демонстрирующий, как сгенерировать простой PDF‑файл с текстовым содержимым, помогая разработчикам быстро понять основную функциональность API.
SoftwareApplication: go-cpp
---

Пример "Hello World" традиционно используется для представления возможностей языка программирования или программного обеспечения с простым примером.

**Aspose.PDF for Go** — это многофункциональный PDF API, который позволяет разработчикам внедрять создание, манипуляцию и преобразование PDF‑документов с помощью Go. Он поддерживает множество популярных форматов файлов, включая PDF, TXT, XPS, EPUB, TEX, DOC, DOCX, PPTX, форматы изображений и т.д. В этой статье мы создаём PDF‑документ, содержащий текст "Hello World!" После установки Aspose.PDF for Go в вашей среде вы можете выполнить пример кода, чтобы увидеть, как работает API Aspose.PDF.
Ниже приведённый фрагмент кода следует этим шагам:

1. Создайте новый экземпляр PDF‑документа.
1. Добавьте новую страницу в PDF‑документ с помощью [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) функции.
1. Установите размер страницы с помощью [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. Добавьте текст "Hello World!" на первую страницу с помощью [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. Сохраните восстановленный PDF‑документ с помощью метода [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).
1. Закройте документ PDF и освободите все выделенные ресурсы.

Следующий фрагмент кода — это программа Hello World, демонстрирующая работу Aspose.PDF for Go API.

```go

    package main

    import "github.com/aspose-pdf/aspose-pdf-go-cpp"
    import "log"

    func main() {
        // Create new PDF-document
        pdf, err := asposepdf.New()
        if err != nil {
                log.Fatal(err)
        }
        // Add new page
        err = pdf.PageAdd()
        if err != nil {
                log.Fatal(err)
        }
        // Set page size A4
        err = pdf.PageSetSize(1, asposepdf.PageSizeA4)
        if err != nil {
                log.Fatal(err)
        }
        // Add text on first page
        err = pdf.PageAddText(1, "Hello World!")
        if err != nil {
                log.Fatal(err)
        }
        // Save PDF-document with "hello.pdf" name
        err = pdf.SaveAs("hello.pdf")
        if err != nil {
                log.Fatal(err)
        }
        // Release allocated resources
        defer pdf.Close()
    }
```
