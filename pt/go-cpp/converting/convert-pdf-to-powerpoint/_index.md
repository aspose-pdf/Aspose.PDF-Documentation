---
title: Converter PDF para PPTX em Go
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /pt/go-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-04"
description: Aspose.PDF permite converter PDF para formato PPTX usando Go.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ferramenta Golang para Converter PDF para PowerPoint
Abstract: Aspose.PDF for Go via C++ fornece uma solução confiável para converter documentos PDF para o formato PowerPoint (PPTX) enquanto preserva o layout original, a formatação e a estrutura de conteúdo. Essa funcionalidade permite que os desenvolvedores transformem de forma contínua arquivos PDF estáticos em apresentações dinâmicas e editáveis. A biblioteca oferece opções de personalização para controlar o processo de conversão, garantindo uma saída de alta qualidade adequada para uso empresarial e profissional. A documentação fornece instruções passo a passo e exemplos de código para ajudar os desenvolvedores a integrar eficientemente a conversão PDF-to-PowerPoint em suas aplicações.
SoftwareApplication: go-cpp
---

## Converter PDF para PPTX

O trecho de código Go fornecido demonstra como converter um documento PDF em um PPTX usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converta um arquivo PDF para PPTX usando [SavePptx](https://reference.aspose.com/pdf/go-cpp/convert/savepptx/) função.
1. Feche o documento PDF e libere quaisquer recursos alocados.

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
      // SavePptX(filename string) saves previously opened PDF-document as PptX-document with filename
      err = pdf.SavePptX("sample.pptx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF for Go apresenta-lhe um aplicativo gratuito online [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode experimentar a funcionalidade e a qualidade com que ele funciona.

[![Aspose.PDF Conversão de PDF para PPTX com Aplicativo Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}