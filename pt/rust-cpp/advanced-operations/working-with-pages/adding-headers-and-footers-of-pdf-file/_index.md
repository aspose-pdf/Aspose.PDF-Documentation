---
title: Adicionando Cabeçalho e Rodapé ao PDF usando Rust
linktitle: Adicionando Cabeçalho e Rodapé ao PDF
type: docs
weight: 90
url: /pt/rust-cpp/add-headers-and-footers-of-pdf-file/
description:
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como adicionar Cabeçalho e Rodapé ao PDF usando Rust
Abstract: Este artigo demonstra como adicionar cabeçalhos e rodapés de texto a documentos PDF usando a biblioteca asposepdf Rust. Ele explica como abrir um PDF existente, inserir texto consistente no cabeçalho ou rodapé de cada página e salvar o documento modificado como um novo arquivo. Os exemplos apresentam um fluxo de trabalho simples e à prova de erros que pode ser usado para tarefas como adicionar números de página, títulos ou branding programaticamente em aplicações Rust.
SoftwareApplication: rust-cpp
---

## Adicionando Cabeçalhos e Rodapés como Fragmentos de Texto

### Adicionar texto no Rodapé de um PDF-document

Nossa ferramenta permite que você abra um PDF existente, adicione um rodapé de texto a todas as páginas e salve o PDF modificado como um novo arquivo usando a biblioteca asposepdf Rust. Ela lida com erros de forma elegante usando o tipo Result do Rust.

1. Abra um documento PDF existente.
1. Adicione texto ao rodapé com [add_text_footer](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_footer/).
1. Salve o PDF modificado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Footer of a PDF-document
        pdf.add_text_footer("FOOTER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_footer.pdf")?;

        Ok(())
    }
```

### Adicionar texto no cabeçalho de um PDF-documento

Este trecho de código demonstra como abrir um arquivo PDF existente, adicionar um cabeçalho de texto a todas as páginas e salvar o documento modificado como um novo arquivo usando a biblioteca asposepdf. Ele fornece uma maneira simples e automatizada de inserir cabeçalhos consistentes em PDFs.

1. Abrir um PDF existente.
1. Adicionar texto ao cabeçalho com ajuda [add_text_header](https://reference.aspose.com/pdf/rust-cpp/organize/add_text_header/).
1. Salve o PDF modificado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add text in Header of a PDF-document
        pdf.add_text_header("HEADER")?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_text_header.pdf")?;

        Ok(())
    }
```