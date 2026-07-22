---
title: Converter PDF para EPUB, TeX, Texto, XPS em Rust
linktitle: Converter PDF para outros formatos
type: docs
weight: 90
url: /pt/rust-cpp/convert-pdf-to-other-files/
lastmod: "2026-07-20"
description: Este tópico mostra como converter um arquivo PDF para outros formatos de arquivo, como EPUB, LaTeX, Texto, XPS etc., usando Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.8
TechArticle: true
AlternativeHeadline: Ferramenta Rust para converter PDF em EPUB, TeX, Texto e XPS
Abstract: Aspose.PDF for Rust via C++ oferece recursos poderosos para converter documentos PDF em vários formatos de arquivo, incluindo DOCX, PPTX, HTML, EPUB, SVG e mais. Essa funcionalidade permite que os desenvolvedores extraiam e reutilizem o conteúdo PDF de maneira contínua, mantendo a formatação, a estrutura e a qualidade em diferentes formatos de saída. A biblioteca fornece opções flexíveis para personalizar o processo de conversão de acordo com requisitos específicos. A documentação inclui diretrizes abrangentes e exemplos de código para auxiliar os desenvolvedores a implementar de forma eficiente a conversão de PDF para arquivo em suas aplicações.
SoftwareApplication: rust-cpp
---

## Converter PDF para EPUB

**<abbr title="Electronic Publication">EPUB</abbr>** é um padrão de e-book livre e aberto do International Digital Publishing Forum (IDPF). Arquivos têm a extensão .epub.
EPUB é projetado para conteúdo refluível, o que significa que um leitor EPUB pode otimizar o texto para um dispositivo de exibição específico. O EPUB também suporta conteúdo de layout fixo. O formato foi concebido como um único formato que editores e casas de conversão podem usar internamente, bem como para distribuição e venda. Ele substitui o padrão Open eBook.

O trecho de código Rust fornecido demonstra como converter um documento PDF em um EPUB usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter um arquivo PDF para EPUB usando [save_epub](https://reference.aspose.com/pdf/rust-cpp/convert/save_epub/) função.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Epub-document
      pdf.save_epub("sample.epub")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para EPUB online**

Aspose.PDF for Rust apresenta a você um aplicativo online gratuito ["PDF para EPUB"](https://products.aspose.app/pdf/conversion/pdf-to-epub), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para EPUB com Aplicativo Gratuito](pdf_to_epub.png)](https://products.aspose.app/pdf/conversion/pdf-to-epub)
{{% /alert %}}

## Converter PDF para TeX

**Aspose.PDF for Rust** suporta a conversão de PDF para TeX.
O formato de arquivo LaTeX é um formato de arquivo de texto com marcação especial e é usado em sistemas de preparação de documentos baseados em TeX para tipografia de alta qualidade.

O trecho de código Rust fornecido demonstra como converter um documento PDF em TeX usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter um arquivo PDF para TeX usando [save_tex](https://reference.aspose.com/pdf/rust-cpp/convert/save_tex/) função.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as TeX-document
      pdf.save_tex("sample.tex")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para LaTeX/TeX online**

Aspose.PDF for Rust apresenta a você um aplicativo online gratuito ["PDF para LaTeX"](https://products.aspose.app/pdf/conversion/pdf-to-tex), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para LaTeX/TeX com Aplicativo Gratuito](pdf_to_latex.png)](https://products.aspose.app/pdf/conversion/pdf-to-tex)
{{% /alert %}}

## Converter PDF para TXT

O trecho de código Rust fornecido demonstra como converter um documento PDF em TXT usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter um arquivo PDF para TXT usando [save_txt](https://reference.aspose.com/pdf/rust-cpp/convert/save_txt/) função.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Txt-document
      pdf.save_txt("sample.txt")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para Texto online**

Aspose.PDF for Rust apresenta a você um aplicativo online gratuito ["PDF para Texto"](https://products.aspose.app/pdf/conversion/pdf-to-txt), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para Texto com Aplicativo Gratuito](pdf_to_text.png)](https://products.aspose.app/pdf/conversion/pdf-to-txt)
{{% /alert %}}

## Converter PDF para XPS

O tipo de arquivo XPS está principalmente associado à XML Paper Specification da Microsoft Corporation. A XML Paper Specification (XPS), anteriormente codinome Metro e que engloba o conceito de marketing Next Generation Print Path (NGPP), é a iniciativa da Microsoft para integrar a criação e visualização de documentos ao sistema operacional Windows.

**Aspose.PDF for Rust** oferece a possibilidade de converter arquivos PDF para <abbr title="XML Paper Specification">XPS</abbr> formato. Vamos tentar usar o trecho de código apresentado para converter arquivos PDF para o formato XPS com Rust.

O trecho de código Rust fornecido demonstra como converter um documento PDF em XPS usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter um arquivo PDF para XPS usando [save_xps](https://reference.aspose.com/pdf/rust-cpp/convert/save_xps/) função.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Xps-document
      pdf.save_xps("sample.xps")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para XPS online**

Aspose.PDF for Rust apresenta a você um aplicativo online gratuito ["PDF para XPS"](https://products.aspose.app/pdf/conversion/pdf-to-xps), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para XPS com Aplicativo Gratuito](pdf_to_xps.png)](https://products.aspose.app/pdf/conversion/pdf-to-xps)
{{% /alert %}}

## Converter PDF para PDF em tons de cinza

O trecho de código Rust fornecido demonstra como converter a primeira página de um documento PDF em um PDF em escala de cinza usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converter uma página PDF para PDF em escala de cinza usando [pagina_escala_de_cinza](https://reference.aspose.com/pdf/rust-cpp/organize/page_grayscale/) função.

Este exemplo converte uma página específica do seu PDF para escala de cinza:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Convert page to black and white
      pdf.page_grayscale(1)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_page1_grayscale.pdf")?;

      Ok(())
  }
```

## Converter PDF para Markdown

O trecho de código Rust fornecido demonstra como converter um documento PDF em um arquivo Markdown (.md) usando Aspose.PDF for Rust.

1. Abra o arquivo PDF de origem.
1. Converter PDF para Markdown.
1. Salve o documento PDF aberto como um arquivo Markdown.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as Markdown-document
      pdf.save_markdown("sample.md")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para MD online**

Aspose.PDF for Rust apresenta a você um aplicativo online gratuito ["PDF para MD"](https://products.aspose.app/pdf/conversion/md), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão PDF para MD com aplicativo gratuito](pdf_to_md.png)](https://products.aspose.app/pdf/conversion/md)
{{% /alert %}}
