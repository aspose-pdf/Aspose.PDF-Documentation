---
title: Adicionar marca d'água ao PDF usando Rust
linktitle: Adicionar marca d'água
type: docs
weight: 80
url: /pt/rust-cpp/add-watermarks/
description: Este exemplo demonstra como adicionar uma marca d'água de texto personalizável a um documento PDF usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionar marca d'água de texto
Abstract: Aspose.PDF for Rust via C++ fornece uma maneira flexível de adicionar marcas d'água de texto a documentos PDF. Este exemplo demonstra como inserir uma marca d'água personalizável especificando o conteúdo do texto, fonte, tamanho, cor, posição, ângulo de rotação, comportamento de camadas e transparência. As marcas d'água são comumente usadas para branding, rótulos de confidencialidade, marcações de rascunho ou proteção de documentos.
SoftwareApplication: rust-cpp
---

O [add_watermark](https://reference.aspose.com/pdf/rust-cpp/organize/add_watermark/) método permite que desenvolvedores apliquem programaticamente uma marca d'água de texto a um documento PDF existente. A marca d'água pode ser totalmente personalizada, incluindo:

- Texto da marca d'água
- Família da fonte
- Tamanho da fonte
- Cor do texto (formato HEX)
- Coordenadas de posição X e Y
- Ângulo de rotação
- Posicionamento em primeiro plano ou plano de fundo
- Opacidade (nível de transparência)

Neste exemplo, a aplicação abre um arquivo PDF existente, aplica uma marca d'água girada semitransparente e salva o documento modificado com um novo nome de arquivo.

Esta funcionalidade é particularmente útil para marcar documentos como Rascunho, Confidencial, Exemplo, ou para adicionar elementos de marca antes da distribuição.

1. Abra o documento PDF existente.
1. Chame o método add_watermark e configure as propriedades da marca d'água.
1. Salve o documento atualizado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add watermark to PDF-document
        pdf.add_watermark(
            "WATERMARK",
            "Arial",
            16.0,
            "#010101",
            100,
            100,
            45,
            true,
            0.5,
        )?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_watermark.pdf")?;

        Ok(())
    }
```