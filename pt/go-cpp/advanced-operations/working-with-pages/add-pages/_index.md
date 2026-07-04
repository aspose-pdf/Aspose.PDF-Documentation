---
title: Adicionar páginas ao documento PDF
linktitle: Adicionar páginas
type: docs
weight: 10
url: /pt/go-cpp/add-pages/
description: Explore como adicionar páginas a um PDF existente em Go com Aspose.PDF para aprimorar e expandir seus documentos.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar páginas PDF com Aspose.PDF para Go
Abstract: Aspose.PDF for Go via C\u002B\u002B oferece funcionalidade poderosa para adicionar páginas a documentos PDF, permitindo que desenvolvedores criem novas páginas dinamicamente e as personalizem de acordo com requisitos específicos. A biblioteca suporta a inserção de páginas em branco ou a cópia de páginas de documentos existentes, oferecendo opções para definir tamanho da página, orientação e conteúdo. Esses recursos permitem expansão e personalização de documentos de forma contínua. A documentação inclui instruções detalhadas e exemplos de código para ajudar os desenvolvedores a implementar de maneira eficiente os recursos de adição de páginas em suas aplicações.
SoftwareApplication: go-cpp
---

## Adicionar página em um arquivo PDF

O trecho de código Go fornecido demonstra como executar a operação Add Page ao final do PDF usando a biblioteca Aspose.PDF. 

1. O [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) A função permite que o programa carregue um arquivo PDF existente (sample.pdf) para manipulação. Isso é essencial para quaisquer operações relacionadas a PDF, como edição, adição de conteúdo ou leitura de dados.
1. O [PageAdd](https://reference.aspose.com/pdf/go-cpp/core/pageadd/) O método é usado para inserir uma nova página em branco no documento PDF existente. Isso é útil para expandir um documento ou prepará-lo para conteúdo adicional.
1. O [Salvar](https://reference.aspose.com/pdf/go-cpp/core/save/) O método garante que as modificações no PDF sejam gravadas de volta no arquivo. Esta etapa é crucial para persistir as alterações, como a adição de novas páginas.
1. O [Fechar](https://reference.aspose.com/pdf/go-cpp/core/close/) O método é chamado usando defer para liberar quaisquer recursos alocados durante as operações de PDF. Isso é importante para prevenir vazamentos de memória e garantir o uso eficiente de recursos.

Este trecho é um exemplo conciso e eficiente de como usar a biblioteca Aspose.PDF Go para tarefas básicas de manipulação de PDF.

Aspose.PDF for Go permite inserir uma página em um documento PDF em qualquer local do arquivo, bem como adicionar páginas ao final de um arquivo PDF.

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
        // PageAdd() adds new page in PDF-document
        err = pdf.PageAdd()
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

## Inserir página em um arquivo PDF

O [PageInsert](https://reference.aspose.com/pdf/go-cpp/core/pageinsert/) O método insere uma nova página na posição especificada. Esse recurso é útil quando você precisa inserir páginas adicionais em um documento existente, por exemplo, adicionando uma nova seção ou conteúdo a um relatório ou apresentação.

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
        // PageInsert(num int32) inserts new page at the specified position in PDF-document
        err = pdf.PageInsert(1)
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