---
title: Rotacionar páginas PDF com Rust via C++
linktitle: Rotacionar páginas PDF
type: docs
weight: 50
url: /pt/rust-cpp/rotate-pages/
description: Este tópico descreve como rotacionar a orientação da página em um arquivo PDF existente programaticamente com Rust via C++
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Rotacionar páginas PDF com Aspose.PDF para Rust
Abstract: O Aspose.PDF for Rust via C++ fornece funcionalidade robusta para rotacionar páginas em documentos PDF, permitindo que os desenvolvedores modifiquem a orientação das páginas conforme necessário. A biblioteca suporta a rotação de páginas em 90, 180 ou 270 graus, possibilitando ajustes rápidos e eficientes no layout do documento. Esse recurso é útil para corrigir páginas mal orientadas ou alterar a apresentação do documento. A documentação inclui instruções passo a passo e exemplos de código para ajudar os desenvolvedores a integrar perfeitamente as capacidades de rotação de páginas em suas aplicações.
SoftwareApplication: rust-cpp
---

Esta seção descreve como alterar a orientação da página de paisagem para retrato e vice‑versa em um arquivo PDF existente usando Rust.

Rotacionar páginas garante o alinhamento adequado para impressão ou exibição de PDFs em ambientes profissionais

1. Abra o Documento PDF.
1. Rotacionar Páginas PDF. O [rotacionar](https://reference.aspose.com/pdf/rust-cpp/organize/rotate/) a função aplica uma rotação específica (neste caso, 180 graus) a uma página determinada.
1. Salvar Alterações para um Novo Arquivo. O [salvar_como](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) A função cria um novo arquivo PDF para preservar o original ao armazenar a versão atualizada.

Neste exemplo, você gira uma página específica em um documento PDF:

```rs

    use asposepdf::{Document, Rotation};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Rotate PDF-document
        pdf.rotate(Rotation::On270)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_rotate.pdf")?;

        Ok(())
    }
```