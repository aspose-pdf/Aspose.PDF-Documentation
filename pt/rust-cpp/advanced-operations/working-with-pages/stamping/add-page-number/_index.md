---
title: Adicionando número de página ao PDF com Rust
linktitle: Adicionando número de página
type: docs
weight: 10
url: /pt/rust-cpp/add-page-number/
description: Este artigo demonstra como adicionar números de página a um documento PDF existente usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Adicionando números de página
Abstract: Aspose.PDF for Rust via C++ permite que desenvolvedores melhorem documentos PDF existentes com numeração automática de páginas em apenas algumas linhas de código. Este exemplo demonstra como abrir um arquivo PDF, inserir números de página em todas as páginas e salvar o documento atualizado como um novo arquivo. Automatizar a paginação garante uma estrutura de documento consistente e é particularmente útil para relatórios, contratos, manuais e outras saídas de várias páginas preparadas para distribuição ou impressão.
SoftwareApplication: rust-cpp
---

Aspose.PDF for Rust via C++ oferece funcionalidade integrada para modificar documentos PDF programaticamente. Neste exemplo, a aplicação abre um arquivo PDF existente, aplica numeração automática de página a cada página e salva o documento modificado com um novo nome.

Esta abordagem é útil ao gerar documentos finalizados para distribuição, impressão ou fins de arquivamento. O processo requer apenas algumas linhas de código e não altera o arquivo original, a menos que seja explicitamente sobrescrito.

A paginação é uma exigência comum para relatórios, faturas, contratos, manuais e outros documentos de várias páginas. O [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) O método insere automaticamente números de página em todas as páginas do documento, garantindo paginação consistente em todo o arquivo.

Após adicionar os números de página, o documento atualizado é salvo como um novo arquivo PDF.

1. Abra o documento PDF existente.
1. Adicionar números de página com [add_page_num()](https://reference.aspose.com/pdf/rust-cpp/organize/add_page_num/) método.
1. Salvar o documento atualizado.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Add page number to a PDF-document
        pdf.add_page_num()?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_add_page_num.pdf")?;

        Ok(())
    }
```