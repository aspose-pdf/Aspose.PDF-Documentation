---
title: Otimizar recursos de PDF usando Go
linktitle: Otimizar recursos de PDF
type: docs
weight: 15
url: /pt/go-cpp/optimize-pdf-resources/
description: Otimizar recursos de arquivos PDF usando a ferramenta Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Otimizar recursos de PDF usando Aspose.PDF para Go
Abstract: Aspose.PDF for Go via C\u002B\u002B oferece recursos avançados para otimizar recursos de PDF, aprimorando a eficiência do documento e reduzindo o tamanho do arquivo. A biblioteca permite que os desenvolvedores otimizem fontes, imagens e metadados removendo dados redundantes e comprimindo recursos sem comprometer a qualidade do documento. Essas técnicas de otimização melhoram o desempenho do documento, tornando os PDFs mais adequados para compartilhamento e armazenamento. A documentação fornece orientações detalhadas e exemplos de código para ajudar os desenvolvedores a implementar efetivamente a otimização de recursos em suas aplicações.
SoftwareApplication: go-cpp
---

## Otimizar recursos de PDF

Otimizar recursos no documento:

  1. Recursos que não são usados nas páginas do documento são removidos.
  1. Recursos iguais são unidos em um único objeto.
  1. Objetos não utilizados são excluídos.

A otimização pode incluir compressão de imagens, remoção de objetos não utilizados e otimização de fontes para reduzir o tamanho do arquivo e melhorar o desempenho. Qualquer erro durante esta operação é registrado e termina o programa.  
 
1. O [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) method carrega o arquivo PDF especificado (sample.pdf) na memória.
1. Optimiza os recursos dentro do PDF para eficiência usando [OptimizeResource](https://reference.aspose.com/pdf/go-cpp/organize/optimizeresource/) método.
1. O [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) method salva o PDF otimizado em um novo arquivo.

O seguinte fragmento de código mostra como otimizar um documento PDF.

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
      // OptimizeResource() optimizes resources of PDF-document
      err = pdf.OptimizeResource()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_OptimizeResource.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```