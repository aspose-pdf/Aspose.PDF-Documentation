---
title: Extrair Texto de PDF usando Go
linktitle: Extrair Texto de PDF
type: docs
weight: 30
url: /pt/go-cpp/extract-text-from-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF para Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair Texto com Aspose.PDF para Go
Abstract: Aspose.PDF para Go via C\u002B\u002B fornece uma maneira poderosa e eficiente de extrair texto de documentos PDF. A biblioteca suporta várias técnicas de extração, permitindo que os usuários recuperem texto de documentos inteiros, de páginas específicas ou de áreas predefinidas dentro de um PDF.
SoftwareApplication: go-cpp
---

## Extrair Texto de Documento PDF

Extrair texto do documento PDF é uma tarefa muito comum e útil. Os PDFs frequentemente contêm informações críticas que precisam ser acessadas, analisadas ou processadas para vários fins. Extrair texto permite reutilização mais fácil em bancos de dados, relatórios ou outros documentos.

Extrair texto torna o conteúdo PDF pesquisável, permitindo que os usuários localizem informações específicas rapidamente sem revisar manualmente o documento inteiro.

Caso você queira extrair texto de um documento PDF, pode usar [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) função.
Por favor, verifique o trecho de código a seguir para extrair texto de um arquivo PDF usando Go.

1. Abra um documento PDF com o nome de arquivo fornecido.
1. [ExtractText](https://reference.aspose.com/pdf/go-cpp/core/extracttext/) extrai o conteúdo de texto do documento PDF.
1. Imprime o texto extraído no console.

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