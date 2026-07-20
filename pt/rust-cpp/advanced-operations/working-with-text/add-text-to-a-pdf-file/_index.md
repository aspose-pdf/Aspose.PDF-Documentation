---
title: Adicionar texto a PDF usando Rust
linktitle: Adicionar texto a PDF
type: docs
weight: 10
url: /pt/rust-cpp/add-text-to-pdf-file/
description: Aprenda como adicionar texto a um documento PDF em Rust usando Aspose.PDF para aprimoramento de conteúdo e edição de documentos.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
AlternativeHeadline: Adicionar texto ao PDF usando Aspose.PDF para Rust
Abstract: A seção Add Text to PDF File da documentação do Aspose.PDF para C\u002B\u002B e Rust fornece instruções passo a passo sobre como inserir texto em documentos PDF programaticamente. Ela abrange diversos métodos para adicionar texto, incluindo posicionamento, personalização de fontes, ajustes de cor e opções de alinhamento de texto. O guia demonstra como adicionar texto a páginas e locais específicos dentro de um PDF, garantindo a colocação precisa do conteúdo. Com exemplos de código detalhados e explicações, os desenvolvedores podem integrar facilmente recursos de inserção de texto em suas aplicações para melhorar o gerenciamento de documentos PDF.
SoftwareApplication: rust-cpp
---

Para adicionar texto a um arquivo PDF existente:

1. Abra um arquivo PDF.
1. Adicione o texto ao documento PDF com [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/) função.
1. Salva as modificações no mesmo arquivo.

## Adicionando Texto

O trecho de código a seguir mostra como adicionar texto em um arquivo PDF existente.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Add text on page
        pdf.page_add_text(1, "added text")?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
