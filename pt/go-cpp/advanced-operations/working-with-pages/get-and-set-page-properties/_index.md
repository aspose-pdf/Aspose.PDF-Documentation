---
title: Obter e Definir Propriedades da Página
linktitle: Obter e Definir Propriedades da Página
type: docs
url: /pt/go-cpp/get-and-set-page-properties/
description: Aprenda como obter e definir propriedades de página para documentos PDF usando Aspose.PDF for Go, permitindo a formatação personalizada de documentos.
lastmod: "2026-07-04"
TechArticle: true
AlternativeHeadline: Obter e Definir Propriedades da Página com Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C\u002B\u002B oferece recursos abrangentes para obter e definir propriedades de página em documentos PDF, permitindo que os desenvolvedores acessem e modifiquem vários atributos da página, como tamanho, rotação, margens e metadados. Essas capacidades possibilitam controle preciso sobre o layout e a aparência do documento para atender a requisitos específicos da aplicação. A biblioteca garante personalização e otimização contínua das páginas PDF. A documentação oferece orientações detalhadas e exemplos de código para ajudar os desenvolvedores a recuperar e atualizar propriedades de página de forma eficiente em suas aplicações.
SoftwareApplication: go-cpp
---


Aspose.PDF for Go permite ler e definir propriedades das páginas em um arquivo PDF. Esta seção mostra como obter o número de páginas em um arquivo PDF, obter informações sobre as propriedades das páginas PDF, como cor, e definir propriedades de página.

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você costuma querer saber quantas páginas eles contêm. Com Aspose.PDF isso leva no máximo duas linhas de código.

**Aspose.PDF for Go via C++** permite contar páginas com [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) função.

O próximo trecho de código foi projetado para abrir um documento PDF, recuperar a contagem de páginas e, em seguida, imprimir o resultado.

O [PageCount](https://reference.aspose.com/pdf/go-cpp/core/pagecount/) O método é chamado para obter o número total de páginas no documento PDF. Isso é útil para tarefas que precisam conhecer o comprimento do documento, como ao extrair páginas específicas ou realizar operações em todas as páginas. Este método é uma maneira direta de consultar a estrutura do documento.

Para obter o número de páginas em um arquivo PDF:

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

## Definir tamanho da página

Neste exemplo, o método pdf.PageSetSize() altera o tamanho da primeira página do documento PDF. A constante PageSizeA1 garante que a primeira página seja definida para o tamanho de papel A1. Isso é útil ao converter documentos para um formato padronizado ou ao garantir que conteúdo específico se ajuste corretamente nas páginas.

1. Abrindo o documento PDF com [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) método.
1. Definindo o tamanho da página com [PageSetSize](https://reference.aspose.com/pdf/go-cpp/organize/pagesetsize/) função.
1. Salvando o Documento usando [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) método.

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