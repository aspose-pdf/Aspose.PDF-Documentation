---
title: Abrir documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /pt/go-cpp/open-pdf-document/
description: Aprenda como abrir um arquivo PDF com Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documento PDF com Aspose.PDF for Go via C++
Abstract: Aspose.PDF for Go via C++ oferece funcionalidade poderosa para abrir e carregar documentos PDF programaticamente, permitindo que desenvolvedores acessem e manipulem o conteúdo PDF com facilidade. A biblioteca suporta a abertura de arquivos PDF a partir de várias fontes, como caminhos de arquivos e fluxos de memória, garantindo processamento eficiente e gerenciamento de recursos. Ela oferece recursos para inspecionar propriedades do documento, extrair texto e imagens, e executar outras operações em PDFs carregados. A documentação inclui instruções detalhadas e exemplos de código para ajudar os desenvolvedores a integrar capacidades de abertura de PDF em suas aplicações de forma contínua.
SoftwareApplication: go-cpp
---

## Abrir documento PDF existente

O snippet de código demonstra operações essenciais para trabalhar com PDFs usando Aspose.PDF for Go. Estas são abrir um arquivo, salvar alterações e fechar recursos corretamente. Isso o torna um exemplo fundamental para desenvolvedores que manipulam documentos PDF.

O exemplo é direto, facilitando sua compreensão e modificação. É ideal para iniciantes ou como modelo para aplicações mais complexas.

A capacidade de abrir e salvar documentos PDF é uma exigência central em diversos cenários, como geração de relatórios, modificação de documentos ou criação de fluxos de trabalho automatizados.

Este exemplo mostra a facilidade de uso da API para manipulação simples de PDF, que pode ser expandida para incluir recursos avançados como extração de texto, anotação ou preenchimento de formulários.

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
        // Save() saves previously opened PDF-document
        err = pdf.Save()
        if err != nil {
            log.Fatal(err)
        }
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
