---
title: Defina a cor de fundo para PDF com Go
linktitle: Definir cor de fundo
type: docs
weight: 80
url: /pt/go-cpp/set-background-color/
description: Defina a cor de fundo para o seu arquivo PDF com Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Defina a cor de fundo para PDF com Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C\u002B\u002B oferece funcionalidade para definir a cor de fundo das páginas PDF, permitindo que os desenvolvedores personalizem a aparência dos documentos. Esse recurso possibilita a aplicação de cores sólidas em todo o fundo da página, aprimorando a apresentação visual do document\u0027s. Os desenvolvedores podem especificar facilmente valores de cor usando modelos de cor padrão, como RGB ou CMYK. A documentação fornece instruções detalhadas e exemplos de código para ajudar os desenvolvedores a implementar a personalização da cor de fundo de forma eficaz em suas aplicações C\u002B\u002B.
SoftwareApplication: go-cpp
---

1. O trecho de código fornecido demonstra como definir uma cor de fundo para um arquivo PDF usando a biblioteca Aspose.PDF em Go.
1. O [Abrir](https://reference.aspose.com/pdf/go-cpp/core/open/) método carrega o arquivo PDF especificado na memória, permitindo manipulações adicionais, como modificar sua aparência ou conteúdo.
1. O [SetBackground](https://reference.aspose.com/pdf/go-cpp/organize/setbackground/) método aplica uma nova cor de fundo ao documento PDF. Os valores RGB permitem que os usuários personalizem o estilo visual do documento.
1. O [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) O método salva o PDF atualizado sob um novo nome.

Este código é ideal para aplicativos que precisam automatizar personalizações de PDF, como criar relatórios com marca, adicionar marcas d'água ou melhorar a consistência visual em vários documentos.

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
      // SetBackground(r, g, b int32) sets PDF-document background color
      err = pdf.SetBackground(200, 100, 101)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_SetBackground.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```