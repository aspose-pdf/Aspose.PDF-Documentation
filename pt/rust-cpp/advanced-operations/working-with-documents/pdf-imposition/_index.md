---
title: Imposição de PDF usando Aspose.PDF for Rust via C++
linktitle: Imposição de PDF
type: docs
weight: 30
url: /pt/rust-cpp/pdf-imposition/
description: Este artigo explica como reorganizar páginas de PDF para layouts otimizados para impressão usando Aspose.PDF for Rust via C++.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Como criar um livreto ou N-Up de arquivos PDF
Abstract: Aspose.PDF for Rust via C++ fornece ferramentas poderosas para reestruturar documentos PDF a fim de atender aos requisitos de impressão e layout. Este artigo demonstra como converter um PDF padrão em um livreto, garantindo a ordem correta das páginas para dobragem, e como criar um PDF N-Up que combina várias páginas em uma única folha. Usando exemplos concisos de código Rust, os desenvolvedores podem implementar rapidamente transformações de PDF prontas para impressão em fluxos de trabalho de documentação, publicação e arquivamento.
SoftwareApplication: rust-cpp
---

## Criar N-Up de PDF

Um PDF N-Up coloca várias páginas de origem em uma única página de saída. Neste exemplo, é usado um layout de 2 × 2, portanto quatro páginas originais são combinadas em cada página do documento de saída.

1. Abra o documento PDF de origem.
1. Salve o documento usando um layout N-Up com o número especificado de linhas e colunas.

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Convert and save the previously opened PDF-document as N-Up PDF-document
        pdf.save_n_up("sample_n_up.pdf", 2, 2)?;

        Ok(())
    }
```

## Criar livreto de PDF

Aspose.PDF for Rust via C++ explica como converter um documento PDF padrão em um PDF no estilo de livreto.
O formato de livreto reorganiza as páginas de modo que, quando impressas e dobradas, o documento forma um livreto adequado com as páginas na ordem correta.

1. Abra o documento PDF de origem.
1. Salve o documento como um PDF de livreto.

```rs

  use asposepdf::Document;

  fn main() -> Result<(), Box<dyn std::error::Error>> {
      // Open a PDF-document with filename
      let pdf = Document::open("sample.pdf")?;

      // Convert and save the previously opened PDF-document as booklet PDF-document
      pdf.save_booklet("sample_booklet.pdf")?;

      Ok(())
  }
```

**Observe que uma Licença de Avaliação Gratuita é necessária para funcionalidade completa.**

Explore o resultado da criação de um livreto de 4 páginas.

![Exemplo de um livreto de 4 páginas](sample_4.png)

Explore o resultado da criação de um livreto de 3 páginas.

![Exemplo de um livreto de 3 páginas](sample_3.png)