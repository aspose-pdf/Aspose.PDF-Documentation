---
title: Конвертировать PDF в документы Word на Go
linktitle: Конвертировать PDF в Word
type: docs
weight: 10
url: /ru/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: Узнайте, как писать код на Go для преобразования PDF в DOC (DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Инструмент для конвертации PDF в Word с помощью Aspose.PDF for Go
Abstract: Aspose.PDF for Go через C++ обеспечивает бесшовное преобразование PDF‑документов в формат DOC, сохраняя оригинальный текст, изображения, таблицы и общую структуру документа. Эта функция позволяет разработчикам преобразовывать статические PDF в редактируемые файлы Word для дальнейшего изменения и обработки. Библиотека предоставляет различные параметры настройки для контроля результата конвертации, обеспечивая высокую точность и достоверность. Документация содержит подробные инструкции и примеры кода, помогающие разработчикам эффективно внедрять конвертацию PDF‑в‑DOC в своих приложениях.
SoftwareApplication: go-cpp
---

Редактировать содержимое PDF‑файла в Microsoft Word или других текстовых процессорах, поддерживающих форматы DOC и DOCX. PDF‑файлы можно редактировать, но файлы DOC и DOCX более гибкие и настраиваемые.

## Конвертировать PDF в DOC

Приведённый фрагмент кода на Go демонстрирует, как конвертировать документ PDF в DOC с использованием библиотеки Aspose.PDF:

1. Откройте документ PDF.
1. Преобразуйте файл PDF в DOC с помощью функции [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/).
1. Закройте PDF документ и освободите любые выделенные ресурсы.

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
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOC онлайн**

Aspose.PDF for Go представляет вам бесплатное онлайн‑приложение [“PDF в DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), где вы можете попытаться исследовать функциональность и качество того, как он работает.

[![Конвертировать PDF в DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Конвертировать PDF в DOCX

Aspose.PDF for Go API позволяет читать и конвертировать PDF‑документы в DOCX. DOCX — это широко известный формат документов Microsoft Word, структура которого была изменена с простого двоичного на комбинацию XML и двоичных файлов. Файлы DOCX можно открывать в Word 2007 и более поздних версиях, но не в более ранних версиях MS Word, поддерживающих расширения файлов DOC.

Приведённый фрагмент кода на Go демонстрирует, как конвертировать PDF‑документ в DOCX с использованием библиотеки Aspose.PDF:

1. Откройте документ PDF.
1. Преобразуйте PDF‑файл в DOCX с помощью функции [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/).
1. Закройте PDF документ и освободите любые выделенные ресурсы.

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
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Попробуйте конвертировать PDF в DOCX онлайн**

Aspose.PDF for Go представляет вам бесплатное онлайн‑приложение ["PDF в Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), где вы можете попытаться исследовать функциональность и качество того, как он работает.

[![Бесплатное приложение Aspose.PDF для конвертации PDF в Word](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}
