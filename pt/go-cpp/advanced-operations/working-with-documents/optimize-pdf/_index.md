---
title: Otimizar PDF usando Aspose.PDF for Go via C++
linktitle: Otimizar arquivo PDF
type: docs
weight: 10
url: /pt/go-cpp/optimize-pdf/
description: Otimizar e compactar arquivos PDF usando a ferramenta Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Otimizar e compactar arquivos PDF usando Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ oferece recursos poderosos de otimização para reduzir o tamanho e melhorar o desempenho de documentos PDF. A biblioteca fornece várias opções de otimização, incluindo compressão de imagens, remoção de objetos não utilizados, redução de tamanhos de Font e otimização de fluxos de conteúdo. Esses recursos ajudam a melhorar a eficiência de armazenamento de documentos e garantem tempos de processamento e carregamento mais rápidos. A documentação fornece instruções passo a passo e exemplos de código para auxiliar desenvolvedores a implementar a otimização de PDF de forma eficaz em suas aplicações.
SoftwareApplication: go-cpp
---

## Otimizar documento PDF

O Toolkit com Aspose.PDF for Go via C++ permite otimizar um documento PDF.

Este trecho de código é útil para aplicações onde reduzir o tamanho ou melhorar a eficiência de arquivos PDF é crítico, como para uploads na web, arquivamento ou compartilhamento em largura de banda limitada.

1. O [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) método carrega o arquivo PDF especificado (sample.pdf) na memória.
1. O [Método Optimize](https://reference.aspose.com/pdf/go-cpp/organize/optimize/) reduz o tamanho do arquivo ao realizar otimizações como remover objetos não utilizados, comprimir imagens, achatar anotações, desincorporar fontes e permitir a reutilização de conteúdo. Essas etapas ajudam a reduzir os requisitos de armazenamento e melhorar a velocidade de processamento do documento PDF.
1. O [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) método salva o PDF otimizado em um novo arquivo.

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
      // Optimize() optimizes PDF-document content
      err = pdf.Optimize()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Optimize.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```