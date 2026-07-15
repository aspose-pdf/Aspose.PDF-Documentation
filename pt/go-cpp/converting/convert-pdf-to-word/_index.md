---
title: Converter PDF para documentos Word em Go
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /pt/go-cpp/convert-pdf-to-doc/
lastmod: "2026-07-04"
description: Aprenda como escrever código Go para conversão de PDF para DOC(DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ferramenta para converter PDF para Word com Aspose.PDF for Go
Abstract: Aspose.PDF for Go via C++ permite a conversão perfeita de documentos PDF para o formato DOC, preservando o texto original, imagens, tabelas e a estrutura geral do documento. Esse recurso permite que os desenvolvedores transformem PDFs estáticos em arquivos Word editáveis para modificação e processamento adicionais. A biblioteca oferece várias opções de personalização para controlar a saída da conversão, garantindo alta fidelidade e precisão. A documentação inclui instruções detalhadas e código de exemplo para ajudar os desenvolvedores a implementar de forma eficiente a conversão de PDF para DOC em suas aplicações.
SoftwareApplication: go-cpp
---

Para editar o conteúdo de um arquivo PDF no Microsoft Word ou em outros processadores de texto que suportam os formatos DOC e DOCX. Arquivos PDF são editáveis, mas os arquivos DOC e DOCX são mais flexíveis e personalizáveis.

## Converter PDF para DOC

O trecho de código Go fornecido demonstra como converter um documento PDF em DOC usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter um arquivo PDF para DOC usando [SaveDoc](https://reference.aspose.com/pdf/go-cpp/convert/savedoc/) função.
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
      // SaveDoc(filename string) saves previously opened PDF-document as Doc-document with filename
      err = pdf.SaveDoc("sample.doc")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF for Go apresenta a você um aplicativo gratuito online [“PDF para DOC”](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Converter PDF para DOCX

A API Aspose.PDF for Go permite que você leia e converta documentos PDF para DOCX. DOCX é um formato bem conhecido para documentos do Microsoft Word cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivos DOC.

O trecho de código Go fornecido demonstra como converter um documento PDF em DOCX usando a biblioteca Aspose.PDF:

1. Abrir um documento PDF.
1. Converter um arquivo PDF para DOCX usando [SaveDocX](https://reference.aspose.com/pdf/go-cpp/convert/savedocx/) função.
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
      // SaveDocX(filename string) saves previously opened PDF-document as DocX-document with filename
      err = pdf.SaveDocX("sample.docx")
      if err != nil {
        log.Fatal(err)
      }
      // Close() releases allocated resources for PDF-document
      defer pdf.Close()
    }
```

{{% alert color="success" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF for Go apresenta a você um aplicativo gratuito online [“PDF para Word”](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para Word App Gratuito](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}