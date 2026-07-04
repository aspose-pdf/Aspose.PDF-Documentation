---
title: Converter PDF para EPUB, TeX, Texto, XPS em Go
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/go-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-04"
description: Este tópico mostra como converter um arquivo PDF para outros formatos de arquivo, como EPUB, LaTeX, Texto, XPS etc., usando Go.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Ferramenta Golang para converter PDF para EPUB, TeX, Texto e XPS
Abstract: Aspose.PDF for Go via C++ oferece recursos poderosos para converter documentos PDF em vários formatos de arquivo, incluindo DOCX, PPTX, HTML, EPUB, SVG e mais. Essa funcionalidade permite que os desenvolvedores extraiam e reutilizem o conteúdo PDF de forma contínua, mantendo a formatação, a estrutura e a qualidade em diferentes formatos de saída. A biblioteca fornece opções flexíveis para personalizar o processo de conversão de acordo com requisitos específicos. A documentação inclui diretrizes abrangentes e exemplos de código para auxiliar os desenvolvedores a implementar de forma eficiente a conversão de PDF para arquivo em suas aplicações.
SoftwareApplication: go-cpp
---

## Converter PDF para EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** é um padrão de e-book livre e aberto do International Digital Publishing Forum (IDPF). Os arquivos têm a extensão .epub.
EPUB foi projetado para conteúdo refluível, o que significa que um leitor de EPUB pode otimizar o texto para um dispositivo de exibição específico. O EPUB também suporta conteúdo de layout fixo. O formato destina-se a ser um formato único que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

O trecho de código Go fornecido demonstra como converter um documento PDF em um EPUB usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter um arquivo PDF para EPUB usando [SalvarEpub]() função.
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
      // SaveEpub(filename string) saves previously opened PDF-document as Epub-document with filename
      err = pdf.SaveEpub("sample.epub")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF for Go apresenta-lhe uma aplicação online gratuita ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para EPUB com aplicativo gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Converter PDF para TeX

**Aspose.PDF for Go** suporta a conversão de PDF para TeX.
O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e é usado em sistemas de preparação de documentos baseados em TeX para composição tipográfica de alta qualidade.

O trecho de código Go fornecido demonstra como converter um documento PDF em TeX usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter um arquivo PDF para TeX usando [SaveTeX](https://reference.aspose.com/pdf/go-cpp/convert/savetex/) função.
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
      // SaveTeX(filename string) saves previously opened PDF-document as TeX-document with filename
      err = pdf.SaveTeX("sample.tex")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF for Go apresenta-lhe uma aplicação online gratuita ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para LaTeX/TeX com App Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para TXT

O trecho de código Go fornecido demonstra como converter um documento PDF em um TXT usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter um arquivo PDF para TXT usando [SalvarTxt](https://reference.aspose.com/pdf/go-cpp/convert/savetxt/) função.
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
      // SaveTxt(filename string) saves previously opened PDF-document as Txt-document with filename
      err = pdf.SaveTxt("sample.txt")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF for Go apresenta-lhe uma aplicação online gratuita ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

O tipo de arquivo XPS está principalmente associado à XML Paper Specification da Microsoft Corporation. A XML Paper Specification (XPS), anteriormente com o codinome Metro e que subsume o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos ao sistema operacional Windows.

**Aspose.PDF for Go** oferece a possibilidade de converter arquivos PDF para <abbr title="XML Paper Specification">XPS</abbr> formato. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Go.

O trecho de código Go fornecido demonstra como converter um documento PDF em XPS usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter um arquivo PDF para XPS usando [SalvarXps](https://reference.aspose.com/pdf/go-cpp/convert/savexps/) função.
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
      // SaveXps(filename string) saves previously opened PDF-document as Xps-document with filename
      err = pdf.SaveXps("sample.xps")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF for Go apresenta-lhe uma aplicação online gratuita ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para XPS com App Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Converter PDF para PDF em escala de cinza

O trecho de código Go fornecido demonstra como converter a primeira página de um documento PDF em um PDF em escala de cinza usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter uma página PDF para PDF em tons de cinza usando [Página em escala de cinza](https://reference.aspose.com/pdf/go-cpp/organize/pagegrayscale/) função.
1. Feche o documento PDF e libere quaisquer recursos alocados.

Este exemplo converte uma página específica do seu PDF para tons de cinza:

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
      // PageGrayscale(num int32) converts page to black and white
      err = pdf.PageGrayscale(1)
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_page1_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

Este exemplo converterá todo o documento PDF para tons de cinza:

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
      // Grayscale() converts PDF-document to black and white
      err = pdf.Grayscale()
      if err != nil {
        log.Fatal(err)
      }
      // SaveAs(filename string) saves previously opened PDF-document with new filename
      err = pdf.SaveAs("sample_Grayscale.pdf")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```