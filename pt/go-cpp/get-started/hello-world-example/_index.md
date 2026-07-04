---
title: Exemplo de Hello World usando a linguagem Go
linktitle: Exemplo Hello World
type: docs
weight: 40
url: /pt/go-cpp/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando o Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World via Aspose.PDF for Go
Abstract: O guia Get Started para Aspose.PDF for Go via C++ fornece uma introdução ao trabalho com a biblioteca, cobrindo as etapas básicas para criar e manipular documentos PDF. Ele inclui um exemplo 'Hello World' demonstrando como gerar um arquivo PDF simples com conteúdo de texto, ajudando os desenvolvedores a entender rapidamente a funcionalidade central da API.
SoftwareApplication: go-cpp
---

Um exemplo "Hello World" é tradicionalmente usado para apresentar recursos de uma linguagem de programação ou software com um caso de uso simples.

**Aspose.PDF for Go** é uma API PDF rica em recursos que permite aos desenvolvedores incorporar criação, manipulação e conversão de documentos PDF com Go. Ela suporta muitos formatos de arquivo populares, incluindo PDF, TXT, XPS, EPUB, TEX, DOC, DOCX, PPTX, formatos de imagem etc. Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!". Após instalar o Aspose.PDF for Go em seu ambiente, você pode executar o exemplo de código para ver como a API Aspose.PDF funciona.
O trecho de código abaixo segue estas etapas:

1. Crie uma nova instância de documento PDF.
1. Adicione uma nova página ao documento PDF usando [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) função.
1. Defina o tamanho da página usando [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/).
1. Adicione o texto \"Hello World!\" à primeira página usando [PageAddText](https://reference.aspose.com/pdf/go-cpp/organize/pageaddtext/).
1. Salve o documento PDF reparado usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) método.
1. Feche o documento PDF e libere quaisquer recursos alocados.

O seguinte trecho de código é um programa Hello World para demonstrar o funcionamento da API Aspose.PDF para Go.

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
