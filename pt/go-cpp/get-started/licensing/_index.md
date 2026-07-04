---
title: Licença Aspose PDF
linktitle: Licenciamento e limitações
type: docs
weight: 90
url: /pt/go-cpp/licensing/
description: Aspose. PDF for Go convida seus clientes a obter uma Classic License. Também pode usar uma licença limitada para explorar melhor o produto.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamento do Aspose.PDF for Go via C++
Abstract: A página de Licenciamento do Aspose.PDF for Go via C++ explica as opções de licenciamento disponíveis para o produto. Os clientes podem escolher entre uma Classic License, uma Metered License ou uma licença limitada para fins de avaliação. A página também destaca os benefícios de obter uma licença adequada, como desbloquear a funcionalidade completa e remover as limitações de avaliação.
SoftwareApplication: go-cpp
---


## Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes de forma completa antes de comprar, portanto a versão de avaliação permite que você a use como normalmente faria.

- **Documentos criados com marca d'água de avaliação.** A versão de avaliação do Aspose.PDF for Go fornece funcionalidade completa do produto, mas todas as páginas nos arquivos gerados são marcadas com a marca d'água contendo o texto \u0022Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd.\u0022 no topo.

- **Limite o número de páginas que podem ser processadas.**
Na versão de avaliação, você só pode processar as quatro primeiras páginas de um documento.

>Se você quiser testar o Aspose.PDF for Go sem as limitações da versão de avaliação, também pode solicitar uma Licença Temporária de 30 dias. Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)

## Licença clássica

Aplicando uma licença para habilitar a funcionalidade completa da biblioteca Aspose.PDF usando um arquivo de licença (Aspose.PDF.GoViaCPP.lic).

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
        // SetLicense(filename string) licenses with filename
        err = pdf.SetLicense("Aspose.PDF.GoViaCPP.lic")
        if err != nil {
            log.Fatal(err)
        }
        // Working with PDF-document
        // ...
        // Close() releases allocated resources for PDF-document
        defer pdf.Close()
    }
```
