---
title: Otimizar recursos de PDF usando Rust via C++
linktitle: Otimizar recursos de PDF
type: docs
weight: 15
url: /pt/rust-cpp/optimize-pdf-resources/
description: Otimizar recursos de arquivos PDF usando ferramenta Rust.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Otimizar recursos de PDF usando Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ fornece recursos avançados para otimizar recursos de PDF, aprimorando a eficiência do documento e reduzindo o tamanho do arquivo. A biblioteca permite que os desenvolvedores otimizem fontes, imagens e metadados, removendo dados redundantes e comprimindo recursos sem comprometer a qualidade do documento. Essas técnicas de otimização melhoram o desempenho do documento, tornando os PDFs mais adequados para compartilhamento e armazenamento. A documentação oferece orientações detalhadas e exemplos de código para ajudar os desenvolvedores a implementar eficazmente a otimização de recursos em suas aplicações.
SoftwareApplication: rust-cpp
---

## Otimizar recursos de PDF

Otimizar recursos no documento:

  1. Recursos que não são usados nas páginas do documento são removidos.
  1. Recursos iguais são unidos em um único objeto.
  1. Objetos não utilizados são excluídos.

A otimização pode incluir compactação de imagens, remoção de objetos não utilizados e otimização de fontes para reduzir o tamanho do arquivo e melhorar o desempenho. Qualquer erro durante esta operação é registrado e encerra o programa.  
 
1. O [abrir](https://reference.aspose.com/pdf/rust-cpp/core/open/) método carrega o arquivo PDF especificado (sample.pdf) na memória.
1. Otimiza os recursos dentro do PDF para eficiência usando [optimize_resource](https://reference.aspose.com/pdf/rust-cpp/organize/optimize_resource/) método.
1. O [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método salva o PDF otimizado em um novo arquivo.

O seguinte trecho de código mostra como otimizar um documento PDF.

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