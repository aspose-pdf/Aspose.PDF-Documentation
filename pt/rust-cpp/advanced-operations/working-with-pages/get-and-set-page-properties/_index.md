---
title: Obter e Definir Propriedades da Página
linktitle: Obter e Definir Propriedades da Página
type: docs
url: /pt/rust-cpp/get-and-set-page-properties/
description: Aprenda como obter e definir propriedades de página para documentos PDF usando Aspose.PDF for Rust, permitindo a formatação personalizada de documentos.
lastmod: "2026-07-20"
TechArticle: true
AlternativeHeadline: Obter e Definir Propriedades da Página com Aspose.PDF for Rust
Abstract: Aspose.PDF for Rust via C\u002B\u002B fornece recursos abrangentes para obter e definir propriedades de página em documentos PDF, permitindo que os desenvolvedores acessem e modifiquem diversos atributos da página, como tamanho, rotação, margens e metadados. Esses recursos possibilitam controle preciso sobre o layout e a aparência do documento para atender a requisitos específicos da aplicação. A biblioteca garante personalização e otimização contínuas das páginas PDF. A documentação oferece orientações detalhadas e exemplos de código para ajudar os desenvolvedores a recuperar e atualizar eficientemente as propriedades de página em suas aplicações.
SoftwareApplication: rust-cpp
---


Aspose.PDF for Rust permite ler e definir propriedades das páginas em um arquivo PDF. Esta seção mostra como obter o número de páginas de um arquivo PDF, obter informações sobre as propriedades da página PDF, como cor, e definir propriedades de página.

## Obter Número de Páginas em um Arquivo PDF

Ao trabalhar com documentos, você costuma querer saber quantas páginas eles contêm. Com Aspose.PDF isso leva no máximo duas linhas de código.

**Aspose.PDF for Rust via C\u002B\u002B** permite que você conte Pages com [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) função.

O próximo trecho de código foi projetado para abrir um documento PDF, recuperar sua contagem de páginas e, em seguida, imprimir o resultado.

O [page_count](https://reference.aspose.com/pdf/rust-cpp/core/page_count/) O método é chamado para obter o número total de páginas no documento PDF. Isso é útil para tarefas que precisam saber o comprimento do documento, como ao extrair páginas específicas ou realizar operações em todas as páginas. Este método é uma maneira direta de consultar a estrutura do documento.

Para obter o número de páginas em um arquivo PDF:

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document from file
      let pdf = Document::open("sample.pdf")?;

      // Return page count in PDF-document
      let count = pdf.page_count()?;

      // Print the page count
      println!("Count: {}", count);

      Ok(())
  }
```

## Definir Tamanho da Página

Neste exemplo, o método `page_set_size` altera o tamanho da primeira página do documento PDF. A constante `PageSize::A1` garante que a primeira página seja definida para o tamanho de papel A1. Isso é útil ao converter documentos para um formato padronizado ou ao garantir que conteúdo específico se ajuste corretamente nas páginas.

1. Abrindo o Documento PDF com [open](https://reference.aspose.com/pdf/rust-cpp/core/open/) método.
1. Definindo o Tamanho da Página com [page_set_size](https://reference.aspose.com/pdf/rust-cpp/organize/page_set_size/) função.
1. Salvando o documento usando [save_as](https://reference.aspose.com/pdf/rust-cpp/core/save_as/) método.

```rs

    use asposepdf::{Document, PageSize};

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set the size of a page in the PDF-document
        pdf.page_set_size(1, PageSize::A1)?;

        // Save the previously opened PDF-document with new filename
        pdf.save_as("sample_page1_set_size_A1.pdf")?;

        Ok(())
    }
```