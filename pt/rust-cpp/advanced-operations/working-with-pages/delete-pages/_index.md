---
title: Excluir páginas PDF com Rust via C++
linktitle: Excluir páginas PDF
type: docs
weight: 30
url: /pt/rust-cpp/delete-pages/
description: Você pode excluir páginas do seu arquivo PDF usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Excluir páginas PDF com Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C++ oferece funcionalidade eficiente para excluir páginas de documentos PDF, permitindo que os desenvolvedores removam páginas indesejadas ou desnecessárias com facilidade. A biblioteca permite a exclusão de uma única página ou de várias páginas especificando números de página ou intervalos, garantindo modificações precisas no documento. Esse recurso ajuda a simplificar arquivos PDF ao eliminar conteúdo redundante e otimizar a estrutura do documento. A documentação fornece instruções passo a passo e exemplos de código para auxiliar os desenvolvedores a implementar a funcionalidade de exclusão de páginas de forma eficaz em suas aplicações.
SoftwareApplication: rust-cpp
---

Você pode excluir páginas de um arquivo PDF usando **Aspose.PDF for Rust via C++**. O próximo trecho de código demonstra como manipular um documento PDF excluindo uma página específica. Esse método é eficiente para tarefas de manipulação de documentos PDF, especificamente para remover páginas, salvar o documento modificado e garantir o gerenciamento adequado de recursos.

1. Abrindo um Arquivo PDF.
1. Excluindo uma Página Específica com [page_delete](https://reference.aspose.com/pdf/rust-cpp/core/page_delete/) função.
1. Salvando o Documento usando [save](https://reference.aspose.com/pdf/rust-cpp/core/save/) método.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document from file
        let pdf = Document::open("sample.pdf")?;

        // Delete specified page in PDF-document
        pdf.page_delete(1)?;

        // Save the previously opened PDF-document
        pdf.save()?;

        Ok(())
    }
```
