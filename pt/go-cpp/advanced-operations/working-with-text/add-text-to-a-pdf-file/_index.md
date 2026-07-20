---
title: Adicionar Texto a PDF usando Go
linktitle: Adicionar Texto a PDF
type: docs
weight: 10
url: /pt/go-cpp/add-text-to-pdf-file/
description: Aprenda como adicionar texto a um documento PDF em Go usando Aspose.PDF para aprimoramento de conteúdo e edição de documentos.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Adicionar Texto em PDF usando Aspose.PDF para Go
Abstract: A seção Adicionar Texto ao Arquivo PDF da documentação do Aspose.PDF para C++ e Go fornece instruções passo a passo sobre como inserir texto em documentos PDF programaticamente. Ela abrange vários métodos para adicionar texto, incluindo posicionamento, personalização de fontes, ajustes de cor e opções de alinhamento de texto. O guia demonstra como adicionar texto a páginas e locais específicos dentro de um PDF, garantindo a colocação precisa do conteúdo. Com exemplos de código detalhados e explicações, os desenvolvedores podem integrar facilmente recursos de inserção de texto em suas aplicações para melhorar o gerenciamento de documentos PDF.
SoftwareApplication: go-cpp
---

Para adicionar texto a um arquivo PDF existente:

1. Abrir um arquivo PDF.
1. Adicionar o texto ao documento PDF com [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/) função.
1. Salva as modificações no mesmo arquivo.

## Adicionando Texto

O trecho de código a seguir mostra como adicionar texto em um arquivo PDF existente.

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
