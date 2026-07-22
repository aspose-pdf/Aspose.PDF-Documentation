---
title: Salvar documento PDF programaticamente
linktitle: Salvar PDF
type: docs
weight: 30
url: /pt/rust-cpp/save-pdf-document/
description: Aprenda como salvar arquivo PDF com Aspose.PDF for Rust via C\u002B\u002B.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Salvar documento PDF com Aspose.PDF for Rust via C\u002B\u002B
Abstract: Aspose.PDF for Rust via C\u002B\u002B oferece funcionalidade abrangente para salvar documentos PDF em diversos formatos e locais com alta eficiência e flexibilidade. A biblioteca permite que desenvolvedores salvem PDFs em sistemas de arquivos, fluxos de memória ou os exportem em formatos alternativos como DOCX, XLSX e imagens. Ela fornece opções para personalizar parâmetros de salvamento, otimizar o tamanho do arquivo e garantir a integridade dos dados. A documentação inclui instruções detalhadas e exemplos de código para ajudar os desenvolvedores a implementar de forma eficiente recursos de salvamento de PDF em suas aplicações.
SoftwareApplication: rust-cpp
---

## Salvar documento PDF no sistema de arquivos

O exemplo demonstra o [novo](https://reference.aspose.com/pdf/rust-cpp/core/new/) método para criar um novo documento PDF, que é um recurso fundamental para gerar documentos dinamicamente, como relatórios ou faturas.

O código é simples e pode servir como um modelo para recursos mais avançados, como adicionar texto, imagens ou anotações ao PDF.

Este exemplo demonstra o uso direto da biblioteca Aspose.PDF Rust, exibindo seu potencial para criar, modificar e salvar documentos.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Create a new PDF-document
        let pdf = Document::new()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_new.pdf")?;

        Ok(())
    }
```
