---
title: Converter PDF para PPTX em Rust
linktitle: Converter PDF para PowerPoint
type: docs
weight: 30
url: /pt/rust-cpp/convert-pdf-to-powerpoint/
lastmod: "2026-07-20"
description: Aspose.PDF permite que você converta PDF para formato PPTX usando Rust.
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Ferramenta Rust para Converter PDF para PowerPoint
Abstract: Aspose.PDF for Rust via C++ fornece uma solução confiável para converter documentos PDF para o formato PowerPoint (PPTX), preservando o layout original, a formatação e a estrutura do conteúdo. Essa funcionalidade permite que os desenvolvedores transformem arquivos PDF estáticos em apresentações dinâmicas e editáveis de forma contínua. A biblioteca oferece opções de personalização para controlar o processo de conversão, garantindo uma saída de alta qualidade adequada para uso empresarial e profissional. A documentação fornece instruções passo a passo e exemplos de código para ajudar os desenvolvedores a integrar eficientemente a conversão de PDF para PowerPoint em suas aplicações.
SoftwareApplication: rust-cpp
---

## Converter PDF para PPTX

O trecho de código Rust fornecido demonstra como converter um documento PDF em um PPTX usando a biblioteca Aspose.PDF:

1. Abra um documento PDF.
1. Converta um arquivo PDF em PPTX usando [save_pptx](https://reference.aspose.com/pdf/rust-cpp/convert/save_pptx/) função.

```rust

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as PptX-document
      pdf.save_pptx("sample.pptx")?;

      Ok(())
  }
```

{{% alert color="success" %}}
**Tente converter PDF para PowerPoint online**

Aspose.PDF for Rust apresenta a você um aplicativo online gratuito [“PDF to PPTX”](https://products.aspose.app/pdf/conversion/pdf-to-pptx), onde você pode tentar investigar a funcionalidade e a qualidade com que funciona.

[![Aspose.PDF Conversão de PDF para PPTX com App Gratuito](pdf_to_pptx.png)](https://products.aspose.app/pdf/conversion/pdf-to-pptx)
{{% /alert %}}