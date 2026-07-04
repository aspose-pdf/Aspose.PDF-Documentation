---
title: Конвертировать PDF в Excel на Go
linktitle: Конвертировать PDF в Excel
type: docs
weight: 20
url: /ru/go-cpp/convert-pdf-to-xlsx/
lastmod: "2026-07-04"
description: Aspose.PDF for Go позволяет конвертировать PDF в формат XLSX.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Инструмент Golang для конвертации PDF в документы Excel
Abstract: Библиотека Aspose.PDF for Go через C++ предоставляет надёжное решение для конвертации PDF‑документов в формат XLSX с высокой точностью и эффективностью. Эта функция позволяет разработчикам извлекать табличные данные из PDF, при этом сохранять оригинальное расположение, структуру и форматирование таблиц Excel. Документация предлагает подробные рекомендации по реализации процесса конвертации, включая пример кода и пошаговые инструкции, чтобы облегчить бесшовную интеграцию в приложения на Go.
SoftwareApplication: go-cpp
---

**Aspose.PDF for Go** поддерживает возможность конвертировать PDF‑файлы в формат Excel.

## Конвертировать PDF в XLSX

Excel предоставляет продвинутые инструменты для сортировки, фильтрации и анализа данных, упрощая выполнение таких задач, как анализ тенденций или финансовое моделирование, которые трудно выполнить со статическими PDF‑файлами. Ручное копирование данных из PDF‑файлов в Excel отнимает много времени и подвержено ошибкам. Конвертация автоматизирует этот процесс, экономя значительное время при работе с большими наборами данных.

Aspose.PDF for Go использует [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/) для конвертации загруженного PDF‑файла в электронную таблицу Excel и сохранения её.

1. Импортировать необходимые пакеты.
1. Откройте PDF-файл.
1. Преобразуйте PDF в XLSX с помощью [SaveXlsX](https://reference.aspose.com/pdf/go-cpp/convert/savexlsx/).
1. Закройте PDF-документ.

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
    // SaveXlsX(filename string) saves previously opened PDF-document as XlsX-document with filename
    err = pdf.SaveXlsX("sample.xlsx")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в Excel онлайн**

Aspose.PDF for Go представляет вам онлайн бесплатное приложение ["PDF в XLSX"](https://products.aspose.app/pdf/conversion/pdf-to-xlsx), где вы можете попробовать исследовать функциональность и качество его работы.

[![Конвертация Aspose.PDF PDF в Excel с бесплатным приложением](pdf_to_xlsx.png)](https://products.aspose.app/pdf/conversion/pdf-to-xlsx)
{{% /alert %}}
