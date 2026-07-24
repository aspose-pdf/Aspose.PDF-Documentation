---
title: Extrair Dados de AcroForm usando Rust
linktitle: Extrair Dados de AcroForm
type: docs
weight: 50
url: /pt/rust-cpp/extract-data-from-acroform/
description: Aspose.PDF facilita a extração de dados de campos de formulário de arquivos PDF. Saiba como extrair dados de AcroForms e salvá‑los nos formatos XML, FDF ou XFDF.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como Extrair Dados de AcroForm via Rust
Abstract: Este artigo explica como extrair dados AcroForm de arquivos PDF usando Aspose.PDF for Rust via C++. Ele exporta esses dados para formatos de troca amplamente usados – XML, FDF e XFDF. Demonstra como abrir um documento PDF que contém campos de formulário interativos e exportar programaticamente os nomes e valores dos campos de formulário para reutilização fora do PDF original. Fornecendo exemplos práticos em Rust para cada formato de exportação, o artigo destaca fluxos de trabalho comuns, incluindo processamento de dados, submissão de formulários, integração de sistemas e armazenamento de dados a longo prazo, ajudando desenvolvedores a gerenciar e reutilizar eficientemente os dados de formulários PDF em suas aplicações.
---

## Exportar Dados para XML a partir de um Arquivo PDF

Este trecho de código mostra como exportar dados AcroForm de um documento PDF para um arquivo XML usando Aspose.PDF for Rust.
O processo envolve abrir um arquivo PDF existente com campos de formulário, em seguida exportar esses campos e seus valores para um documento XML para processamento adicional, armazenamento ou troca de dados.

1. Abra o documento PDF.
1. Chame o método 'export_xml' para extrair os dados dos campos de formulário e salvá-los como um arquivo XML.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XML-document
        pdf.export_xml("sample.xml")?;

        Ok(())
    }
```

## Exportar Dados para FDF de um Arquivo PDF

Aspose.PDF for Rust via C++ permite exportar dados AcroForm de um documento PDF para um arquivo FDF. O arquivo Forms Data Format (FDF) armazena nomes e valores dos campos de formulário separadamente do PDF, sendo útil para troca de dados, fluxos de envio de formulários e arquivamento de dados de formulário sem incorporá‑los no documento original.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to FDF-document
        pdf.export_fdf("sample.fdf")?;

        Ok(())
    }
```

## Exportar dados para XFDF de um arquivo PDF

XFDF (XML Forms Data Format) é um formato baseado em XML que representa os dados dos campos de formulário separadamente do arquivo PDF, tornando-o ideal para intercâmbio de dados, envios de formulários e integração com fluxos de trabalho baseados na web.
Aspose.PDF for Rust via C++ ajuda a exportar os dados do AcroForm de um documento PDF para um arquivo XFDF.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Export from the previously opened PDF-document with AcroForm to XFDF-document
        pdf.export_xfdf("sample.xfdf")?;

        Ok(())
    }
```
