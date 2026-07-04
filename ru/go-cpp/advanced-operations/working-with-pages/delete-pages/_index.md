---
title: Удалить страницы PDF с помощью Go
linktitle: Удалить страницы PDF
type: docs
weight: 30
url: /ru/go-cpp/delete-pages/
description: Вы можете удалить страницы из вашего PDF‑файла, используя Aspose.PDF for Go через C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Удалить страницы PDF с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предлагает эффективную функциональность для удаления страниц из PDF‑документов, позволяя разработчикам легко удалять нежелательные или ненужные страницы. Библиотека позволяет удалять одну или несколько страниц, указывая номера страниц или диапазоны, обеспечивая точные изменения документа. Эта возможность помогает оптимизировать PDF‑файлы, устраняя избыточный контент и оптимизируя структуру документа. Документация предоставляет пошаговые инструкции и примеры кода, чтобы помочь разработчикам эффективно реализовать функцию удаления страниц в своих приложениях.
SoftwareApplication: go-cpp
---

Вы можете удалить страницы из PDF‑файла, используя **Aspose.PDF for Go via C++**. Следующий фрагмент кода демонстрирует, как манипулировать PDF‑документом, удаляя определённую страницу. Этот метод эффективен для задач манипуляции PDF‑документами, в частности для удаления страниц, сохранения изменённого документа и обеспечения надлежащего управления ресурсами.

1. Откройте PDF-файл.
1. Удаление конкретной страницы с помощью [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) функция.
1. Сохраните документ с использованием метода [Save](https://reference.aspose.com/pdf/go-cpp/core/save/).

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
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
