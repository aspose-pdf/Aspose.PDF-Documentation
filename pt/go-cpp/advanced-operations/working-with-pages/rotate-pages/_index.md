---
title: Rotacionar páginas PDF com Go
linktitle: Rotacionar páginas PDF
type: docs
weight: 50
url: /pt/go-cpp/rotate-pages/
description: Este tópico descreve como rotacionar a orientação da página em um arquivo PDF existente programaticamente com Go via C++
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotacionar páginas PDF com Aspose.PDF for Go
Abstract: O Aspose.PDF for Go via C++ oferece funcionalidade robusta para rotacionar páginas em documentos PDF, permitindo que os desenvolvedores modifiquem a orientação das páginas conforme necessário. A biblioteca suporta a rotação de páginas em 90, 180 ou 270 graus, possibilitando ajustes rápidos e eficientes no layout do documento. Esse recurso é útil para corrigir páginas desorientadas ou alterar a apresentação do documento. A documentação inclui instruções passo a passo e exemplos de código para ajudar os desenvolvedores a integrar perfeitamente as capacidades de rotação de páginas em suas aplicações.
SoftwareApplication: go-cpp
---

Esta seção descreve como mudar a orientação da página de paisagem para retrato e vice‑versa em um arquivo PDF existente usando Go.

Rotacionar páginas garante o alinhamento adequado para impressão ou exibição de PDFs em ambientes profissionais

1. Abrir o Documento PDF.
1. Rotacionar Páginas PDF. O [PageRotate](https://reference.aspose.com/pdf/go-cpp/organize/rotate/) A função aplica uma rotação específica (neste caso, 180 graus) a uma página dada.
1. Salvar Alterações em um Novo Arquivo. O [SaveAs](https://reference.aspose.com/pdf/go-cpp/core/saveas/) A função cria um novo arquivo PDF para preservar o original enquanto armazena a versão atualizada.

Neste exemplo, você gira uma página específica em um documento PDF:

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
    // PageRotate(num int32, rotation int32) rotates page
    err = pdf.PageRotate(1, asposepdf.RotationOn180)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_page1_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```

Você também tem a opção de girar todas as páginas PDF no seu documento:

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
    // Rotate(rotation int32) rotates PDF-document
    err = pdf.Rotate(asposepdf.RotationOn270)
    if err != nil {
      log.Fatal(err)
    }
    // SaveAs(filename string) saves previously opened PDF-document with new filename
    err = pdf.SaveAs("sample_Rotate.pdf")
    if err != nil {
      log.Fatal(err)
    }
    // Close() releases allocated resources for PDF-document
    defer pdf.Close()
  }
```