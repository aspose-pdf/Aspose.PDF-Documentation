---
title: Exemplo de Hello World usando a linguagem Rust
linktitle: Exemplo Hello World
type: docs
weight: 40
url: /pt/rust-cpp/hello-world-example/
description: Este exemplo demonstra como criar um documento PDF simples com o texto Hello World usando Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Hello World via Aspose.PDF for Rust
Abstract: O guia de Introdução ao Aspose.PDF for Rust via C++ fornece uma introdução ao uso da biblioteca, cobrindo as etapas básicas para criar e manipular documentos PDF. Ele inclui um exemplo 'Hello World' que demonstra como gerar um arquivo PDF simples com conteúdo de texto, ajudando os desenvolvedores a entender rapidamente a funcionalidade central da API.
SoftwareApplication: rust-cpp
---

Um exemplo "Hello World" é tradicionalmente usado para introduzir recursos de uma linguagem de programação ou software com um caso de uso simples.

**Aspose.PDF for Rust** é uma API PDF rica em recursos que permite aos desenvolvedores incorporar a criação, manipulação e conversão de documentos PDF com Rust. Ela suporta muitos formatos de arquivo populares, incluindo PDF, TXT, XLSX, EPUB, TEX, DOC, DOCX, PPTX, formatos de imagem etc. Neste artigo, estamos criando um documento PDF contendo o texto "Hello World!" After installing Aspose.PDF for Rust in your environment, you can execute the code sample to see how the Aspose.PDF API works.
O trecho de código abaixo segue estas etapas:

1. Crie uma nova instância de documento PDF.
1. Adicione uma nova página ao documento PDF usando [page_add](https://reference.aspose.com/pdf/rust-cpp/core/page_add/) função.
1. Defina o tamanho da página usando [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/).
1. Adicione o texto "Hello World!" à primeira página usando [page_add_text](https://reference.aspose.com/pdf/rust-cpp/organize/page_add_text/).
1. Salve o documento PDF usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método.

O trecho de código a seguir é um programa Hello World para demonstrar o funcionamento da API Aspose.PDF for Rust.

```rs

    use asposepdf::{Document, PageSize};
    use std::error::Error;

    fn main() -> Result<(), Box<dyn Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Add a new page
        pdf.page_add()?;

        // Set the size of the first page to A4
        pdf.page_set_size(1, PageSize::A4)?;

        // Add "Hello World!" text to the first page
        pdf.page_add_text(1, "Hello World!")?;

        // Save the PDF-document as "hello.pdf"
        pdf.save_as("hello.pdf")?;

        println!("Saved PDF-document: hello.pdf");

        Ok(())
}
```
