---
title: Optimizar PDF usando Aspose.PDF for Rust via C++
linktitle: Optimizar Arquivo PDF
type: docs
weight: 10
url: /pt/rust-cpp/optimize-pdf/
description: Optimizar e comprimir arquivos PDF usando a ferramenta Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Optimizar e comprimir arquivos PDF usando Aspose.PDF for Rust
Abstract: O Aspose.PDF for Rust via C++ oferece recursos poderosos de otimização para reduzir o tamanho e melhorar o desempenho de documentos PDF. A biblioteca fornece diversas opções de otimização, incluindo compressão de imagens, remoção de objetos não utilizados, redução do tamanho de fontes e otimização de fluxos de conteúdo. Esses recursos ajudam a melhorar a eficiência de armazenamento de documentos e garantem tempos de processamento e carregamento mais rápidos. A documentação fornece instruções passo a passo e exemplos de código para auxiliar os desenvolvedores a implementar a otimização de PDF de forma eficaz em suas aplicações.
SoftwareApplication: rust-cpp
---

## Optimizar Documento PDF

O Toolkit com Aspose.PDF for Rust via C++ permite otimizar um documento PDF.

Este trecho é útil para aplicações onde reduzir o tamanho ou melhorar a eficiência de arquivos PDF é crítico, como para uploads na web, arquivamento ou compartilhamento em largura de banda limitada.

1. O [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) O método carrega o arquivo PDF especificado (sample.pdf) na memória.
1. O [otimizar](https://reference.aspose.com/pdf/rust-cpp/organize/optimize/) reduz o tamanho do arquivo ao realizar otimizações como a remoção de objetos não utilizados, compressão de imagens, achatamento de anotações, desincorporação de fontes e habilitação da reutilização de conteúdo. Essas etapas ajudam a reduzir os requisitos de armazenamento e melhorar a velocidade de processamento do documento PDF.
1. O [salvar_como](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) o método salva o PDF otimizado em um novo arquivo.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Optimize PDF-document content
        pdf.optimize()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_optimize.pdf")?;

        Ok(())
    }
```