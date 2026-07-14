---
title: Установить цвет фона для PDF с помощью Go
linktitle: Установить цвет фона
type: docs
weight: 80
url: /ru/go-cpp/set-background-color/
description: Установить цвет фона для вашего PDF‑файла с помощью Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Установить цвет фона для PDF с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предоставляет возможность задавать цвет фона страниц PDF, позволяя разработчикам настраивать внешний вид документов. Эта функция позволяет применять сплошные цвета ко всему фону страницы, улучшая визуальное представление документа. Разработчики могут легко указывать значения цвета, используя стандартные цветовые модели, такие как RGB или CMYK. Документация содержит подробные инструкции и примеры кода, помогающие разработчикам эффективно реализовать настройку цвета фона в их приложениях на C++.
SoftwareApplication: go-cpp
---

1. Приведённый фрагмент кода демонстрирует, как установить цвет фона для PDF‑файла с использованием библиотеки Aspose.PDF в Go.
1. Этот [Open](https://reference.aspose.com/pdf/go-cpp/core/open/) метод загружает указанный PDF‑файл в память, позволяя выполнять дальнейшие манипуляции, такие как изменение его внешнего вида или содержимого.
1. Этот [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) метод применяет новый цвет фона к PDF‑документу. Значения RGB позволяют пользователям настраивать визуальный стиль документа.
1. Этот [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) метод сохраняет обновлённый PDF под новым именем.

Этот код идеален для приложений, которым необходимо автоматизировать настройку PDF, например, создавать брендированные отчёты, добавлять водяные знаки или повышать визуальную согласованность нескольких документов.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```