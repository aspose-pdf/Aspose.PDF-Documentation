---
title: Extrair texto de PDF usando Rust
linktitle: Extrair texto de PDF
type: docs
weight: 30
url: /pt/rust-cpp/extract-text-from-pdf/
description: Este artigo descreve várias maneiras de extrair texto de documentos PDF usando Aspose.PDF for Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Extrair texto com Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ fornece um método poderoso e eficiente para extrair texto de documentos PDF. A biblioteca suporta várias técnicas de extração, permitindo que os usuários recuperem texto de documentos inteiros, páginas específicas ou áreas predefinidas dentro de um PDF.
SoftwareApplication: rust-cpp
---

## Extrair texto de documento PDF

Extrair texto do documento PDF é uma tarefa muito comum e útil. PDFs frequentemente contêm informações críticas que precisam ser acessadas, analisadas ou processadas para diversos fins.

Extrair texto torna o conteúdo do PDF pesquisável, permitindo que os usuários localizem informações específicas rapidamente sem precisar revisar manualmente todo o documento.

Caso você queira extrair texto de um documento PDF, pode usar [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) função.
Por favor, veja o trecho de código a seguir para extrair texto de um arquivo PDF usando Rust.

1. Abra um documento PDF com o nome de arquivo fornecido.
1. [extract_text](https://reference.aspose.com/pdf/rust-cpp/core/extract_text/) extrai o conteúdo de texto do documento PDF.
1. Imprima o texto extraído no console.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Return the PDF-document contents as plain text
        let txt = pdf.extract_text()?;

        // Print extracted text
        println!("Extracted text:\n{}", txt);

        Ok(())
    }
```