---
title: Excluir páginas PDF com Go
linktitle: Excluir páginas PDF
type: docs
weight: 30
url: /pt/go-cpp/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando Aspose.PDF for Go via C++.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir páginas PDF com Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ oferece funcionalidade eficiente para excluir páginas de documentos PDF, permitindo que os desenvolvedores removam páginas indesejadas ou desnecessárias com facilidade. A biblioteca permite a exclusão de uma ou várias páginas especificando números de página ou intervalos, garantindo modificações precisas no documento. Esse recurso ajuda a simplificar arquivos PDF ao eliminar conteúdo redundante e otimizar a estrutura do documento. A documentação fornece instruções passo a passo e exemplos de código para auxiliar os desenvolvedores na implementação eficaz da funcionalidade de exclusão de páginas em suas aplicações.
SoftwareApplication: go-cpp
---

Você pode excluir páginas de um arquivo PDF usando **Aspose.PDF for Go via C++**. O próximo trecho de código demonstra como manipular um documento PDF excluindo uma página específica. Este método é eficiente para tarefas de manipulação de documentos PDF, especificamente para remover páginas, salvar o documento modificado e garantir o gerenciamento adequado de recursos.

1. Abrindo um arquivo PDF.
1. Excluindo uma página específica com [PageDelete](https://reference.aspose.com/pdf/go-cpp/core/pagedelete/) função.
1. Salvando o documento usando [Salvar](https://reference.aspose.com/pdf/go-cpp/core/save/) método.

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
      // PageDelete(num int32) deletes specified page in PDF-document
      err = pdf.PageDelete(1)
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
