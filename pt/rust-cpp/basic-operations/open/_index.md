---
title: Abrir documento PDF programaticamente
linktitle: Abrir PDF
type: docs
weight: 20
url: /pt/rust-cpp/open-pdf-document/
description: Aprenda como abrir um arquivo PDF com Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Abrir documento PDF com Aspose.PDF for Rust via C++
Abstract: Aspose.PDF for Rust via C++ fornece funcionalidades poderosas para abrir e carregar documentos PDF programaticamente, permitindo que os desenvolvedores acessem e manipulem o conteúdo PDF com facilidade. A biblioteca suporta a abertura de arquivos PDF a partir de várias fontes, como caminhos de arquivos e fluxos de memória, garantindo processamento eficiente e gerenciamento de recursos. Ela oferece recursos para inspecionar propriedades do documento, extrair texto e imagens, e realizar outras operações em PDFs carregados. A documentação inclui instruções detalhadas e exemplos de código para ajudar os desenvolvedores a integrar recursos de abertura de PDF em suas aplicações de forma fluida.
SoftwareApplication: rust-cpp
---

## Abrir documento PDF existente

O trecho de código demonstra operações essenciais para trabalhar com PDFs usando Aspose.PDF for Rust. São abrir um arquivo, salvar alterações e fechar recursos adequadamente. Isso o torna um exemplo fundamental para desenvolvedores que manipulam documentos PDF.

O exemplo é direto, facilitando a compreensão e modificação. É ideal para iniciantes ou como um modelo para aplicações mais complexas.

A capacidade de abrir e salvar documentos PDF é um requisito básico em muitos cenários, como gerar relatórios, modificar documentos ou criar fluxos de trabalho automatizados.

Este exemplo demonstra a facilidade de uso da API para manipulação simples de PDF, que pode ser expandida para incluir recursos avançados como extração de texto, anotação ou preenchimento de formulários.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document named "sample.pdf"
        let pdf = Document::open("sample.pdf")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_open.pdf")?;

        Ok(())
    }
```
