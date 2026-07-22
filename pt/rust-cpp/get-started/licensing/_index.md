---
title: Licença Aspose PDF
linktitle: Licenciamento e limitações
type: docs
weight: 90
url: /pt/rust-cpp/licensing/
description: Aspose. PDF for Rust convida seus clientes a obter uma Licença Classic. Também permite usar uma licença limitada para explorar melhor o produto.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Licenciamento do Aspose.PDF para Rust via C++
Abstract: A página de Licenciamento para Aspose.PDF for Rust via C++ explica as opções de licenciamento disponíveis para o produto. Os clientes podem escolher entre uma Licença Classic, uma Licença por Medição ou uma licença limitada para fins de avaliação. A página também destaca os benefícios de obter uma licença adequada, como desbloquear a funcionalidade completa e remover as limitações de avaliação.
SoftwareApplication: rust-cpp
---

## Licença

- O **código-fonte Rust** está licenciado sob a Licença MIT.
- A **biblioteca compartilhada** (AsposePDFforRust_windows_amd64.dll, libAsposePDFforRust_linux_amd64.so, libAsposePDFforRust_darwin_amd64.dylib, libAsposePDFforRust_darwin_arm64.dylib) é proprietária e requer uma licença comercial. Para usar a funcionalidade completa, você deve obter uma licença.

## Versão de avaliação

Você pode usar **Aspose.PDF for Rust via C++** gratuitamente para avaliação. A versão de avaliação fornece quase toda a funcionalidade do produto com certas limitações. A mesma versão de avaliação torna-se licenciada quando você compra uma licença e adiciona algumas linhas de código para aplicar a licença.

- Se você quiser testar Aspose.PDF for Rust sem as limitações da versão de avaliação, também pode solicitar uma Licença Temporária de 30 dias. Por favor, consulte [Como obter uma Licença Temporária?](https://purchase.aspose.com/temporary-license)?

### Limitação de uma versão de avaliação

Queremos que nossos clientes testem nossos componentes de forma completa antes de comprar, por isso a versão de avaliação permite que você a use como faria normalmente.

- **Documentos criados com uma marca d'água de avaliação**. A versão de avaliação do Aspose.PDF for Rust fornece funcionalidade completa do produto, mas todas as páginas nos arquivos gerados são marcadas com a marca d'água contendo o texto "Evaluation Only. Created with Aspose.PDF. Copyright 2002-2025 Aspose Pty Ltd." no topo.
- **Limitar o número de páginas que podem ser processadas**. Na versão de avaliação, você só pode processar as quatro primeiras páginas de um documento.

### Uso em produção

Uma chave de licença comercial é necessária em um ambiente de produção. Por favor, entre em contato conosco para adquirir uma licença comercial.

### Aplicar licença

Aplicando uma licença para habilitar a funcionalidade completa do Aspose.PDF for Rust usando um arquivo de licença (Aspose.PDF.RustViaCPP.lic).

```rs

    use asposepdf::Document;

    fn main() -> Result<(), Box<dyn std::error::Error>> {
        // Open a PDF-document with filename
        let pdf = Document::open("sample.pdf")?;

        // Set license with filename
        pdf.set_license("Aspose.PDF.RustViaCPP.lic")?;

        // Now you can work with the licensed PDF document
        // ...

        Ok(())
    }
```