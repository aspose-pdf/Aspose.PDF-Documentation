---
title: Converter PDF para documentos Word em Rust
linktitle: Converter PDF para Word
type: docs
weight: 10
url: /pt/rust-cpp/convert-pdf-to-doc/
lastmod: "2026-07-20"
description: Aprenda como escrever código Rust para conversão de PDF para DOC (DOCX).
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ferramenta para converter PDF para Word com Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ permite a conversão perfeita de documentos PDF para o formato DOC, preservando o texto original, imagens, tabelas e a estrutura geral do documento. Esse recurso permite que os desenvolvedores transformem PDFs estáticos em arquivos Word editáveis para modificação e processamento adicionais. A biblioteca oferece várias opções de personalização para controlar a saída da conversão, garantindo alta fidelidade e precisão. A documentação inclui instruções detalhadas e código de exemplo para ajudar os desenvolvedores a implementar de forma eficiente a conversão de PDF para DOC em suas aplicações.
SoftwareApplication: rust-cpp
---

Para editar o conteúdo de um arquivo PDF no Microsoft Word ou em outros processadores de texto que suportam os formatos DOC e DOCX. Arquivos PDF são editáveis, mas os arquivos DOC e DOCX são mais flexíveis e personalizáveis.

## Converter PDF para DOC

O snippet de código Rust fornecido demonstra como converter um documento PDF em DOC usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter um arquivo PDF em DOC usando [save_doc](https://reference.aspose.com/pdf/rust-cpp/convert/save_doc/) função.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Doc-document
      pdf.save_doc("sample.doc")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para DOC online**

Aspose.PDF for Rust apresenta a você um aplicativo gratuito online ["PDF para DOC"](https://products.aspose.app/pdf/conversion/pdf-to-doc), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Converter PDF para DOC](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-doc) 
{{% /alert %}}

## Converter PDF para DOCX

A API Aspose.PDF for Rust permite que você leia e converta documentos PDF para DOCX. DOCX é um formato bem conhecido para documentos Microsoft Word cuja estrutura foi alterada de binário simples para uma combinação de arquivos XML e binários. Arquivos Docx podem ser abertos com o Word 2007 e versões posteriores, mas não com as versões anteriores do MS Word que suportam extensões de arquivo DOC.

O trecho de código Rust fornecido demonstra como converter um documento PDF em DOCX usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter um arquivo PDF para DOCX usando [save_docx](https://reference.aspose.com/pdf/rust-cpp/convert/save_docx/) função.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document
      pdf.save_docx("sample.docx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para DOCX online**

Aspose.PDF for Rust apresenta a você um aplicativo gratuito online ["PDF para Word"](https://products.aspose.app/pdf/conversion/pdf-to-docx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Word App Gratuito](pdf_to_word.png)](https://products.aspose.app/pdf/conversion/pdf-to-docx)

{{% /alert %}}

## Converter PDF para DOCX com Modo de Reconhecimento Aprimorado

Converta um documento PDF para um arquivo Microsoft Word (DOCX) usando Aspose.PDF for Rust com Modo de Reconhecimento Aprimorado.

O Modo de Reconhecimento Avançado produz um DOCX totalmente editável, preservando:

 - Estrutura de parágrafo
 - Tabelas como tabelas nativas do Word
 - Fluxo lógico de texto e formatação

1. Abra o arquivo PDF de origem.
1. Salve o PDF como um arquivo DOCX com o reconhecimento avançado de layout ativado.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as DocX-document with Enhanced Recognition Mode (fully editable tables and paragraphs)
      pdf.save_docx_enhanced("sample_enhanced.docx")?;

      Ok(())
  }
```
