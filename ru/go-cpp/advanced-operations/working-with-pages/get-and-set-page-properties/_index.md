---
title: Получить и установить свойства страниц
linktitle: Получить и установить свойства страниц
type: docs
url: /ru/go-cpp/get-and-set-page-properties/
description: Узнайте, как получать и устанавливать свойства страниц PDF‑документов с помощью Aspose.PDF for Go, что позволяет настраивать форматирование документов.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Получение и установка свойств страниц с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ предоставляет всесторонние возможности получения и установки свойств страниц в PDF‑документах, позволяя разработчикам получать доступ к различным атрибутам страниц, таким как размер, поворот, поля и метаданные, а также изменять их. Эти возможности обеспечивают точный контроль над макетом и внешним видом документа для удовлетворения конкретных требований приложения. Библиотека гарантирует бесшовную настройку и оптимизацию страниц PDF. Документация предлагает подробные руководства и примеры кода, помогающие разработчикам эффективно извлекать и обновлять свойства страниц в своих приложениях.
SoftwareApplication: go-cpp
---


Aspose.PDF for Go позволяет считывать и устанавливать свойства страниц в PDF‑файле. В этом разделе показано, как получить количество страниц в PDF‑файле, получить информацию о свойствах страниц PDF, таких как цвет, и установить свойства страниц.

## Получить количество страниц в PDF‑файле

Работая с документами, вы часто хотите знать, сколько страниц они содержат. С Aspose.PDF это занимает не более двух строк кода.

**Aspose.PDF for Go via C++** позволяет вам подсчитывать страницы с функцией [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/).

Следующий фрагмент кода предназначен для открытия PDF‑документа, получения количества его страниц и последующего вывода результата.

Этот [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) Метод вызывается, чтобы получить общее количество страниц в документе PDF. Это полезно для задач, которым необходимо знать длину документа, например при извлечении определённых страниц или выполнении операций над всеми страницами. Этот метод представляет собой простой способ запросить структуру документа.

Чтобы получить количество страниц в файле PDF:

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
      // PageCount() returns page count in PDF-document
      count, err := pdf.PageCount()
      if err != nil {
        log.Fatal(err)
      }
      // Print
      fmt.Println("Count:", count)
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

## Установить размер страницы

В этом примере метод pdf.PageSetSize() изменяет размер первой страницы PDF‑документа. Константа PageSizeA1 гарантирует, что первая страница будет установлена на размер бумаги A1. Это полезно при конвертации документов в стандартизированный формат или для обеспечения корректного размещения определённого содержимого на страницах.

1. Откройте PDF‑документ с помощью метода [Open](https://reference.aspose.com/pdf/go-cpp/core/open/).
1. Установка размера страницы с помощью [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) функция.
1. Сохраните документ с использованием метода [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/).

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
        // PageSetSize(num int32, pageSize int32) sets size of page
        err = pdf.PageSetSize(1, asposepdf.PageSizeA1)
        if err != nil {
            log.Fatal(err)
        }
        // SaveAs(filename string) saves previously opened PDF-document with new filename
        err = pdf.SaveAs("sample_page1_SetSize_A1.pdf")
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
