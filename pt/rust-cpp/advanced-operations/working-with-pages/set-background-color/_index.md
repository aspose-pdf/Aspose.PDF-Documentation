---
title: Defina a cor de fundo para PDF com Rust via C++
linktitle: Defina a cor de fundo
type: docs
weight: 80
url: /pt/rust-cpp/set-background-color/
description: Defina a cor de fundo para o seu arquivo PDF com Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Defina a cor de fundo para PDF com Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ oferece funcionalidade para definir a cor de fundo das páginas de PDF, permitindo que os desenvolvedores personalizem a aparência dos documentos. Esse recurso permite a aplicação de cores sólidas em todo o fundo da página, aprimorando a apresentação visual do documento. Os desenvolvedores podem especificar facilmente valores de cor usando modelos de cor padrão, como RGB ou CMYK. A documentação fornece instruções detalhadas e exemplos de código para ajudar os desenvolvedores a implementar a personalização da cor de fundo de forma eficaz em suas aplicações C++.
SoftwareApplication: rust-cpp
---

1. O trecho de código fornecido demonstra como definir uma cor de fundo para um arquivo PDF usando a biblioteca Aspose.PDF em Rust.
1. O [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) O método carrega o arquivo PDF especificado na memória, permitindo manipulações adicionais, como modificar sua aparência ou conteúdo.
1. O [definir_fundo](https://reference.aspose.com/pdf/rust-cpp/organize/set_background/) O método aplica uma nova cor de fundo ao documento PDF. Os valores RGB permitem que os usuários personalizem o estilo visual do documento.
1. O [salvar_como](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método salva o PDF atualizado com um novo nome.

Este código é ideal para aplicações que precisam automatizar personalizações de PDF, como criar relatórios com marca, adicionar marcas d'água ou melhorar a consistência visual em vários documentos.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Set PDF-document background color using RGB values
      pdf.set_background(200, 100, 101)?;

      // Save the previously opened PDF-document with new filename
      pdf.save_as("sample_set_background.pdf")?;

      Ok(())
  }
```