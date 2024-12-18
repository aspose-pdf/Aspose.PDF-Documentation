---
title: Como Criar Portfólio PDF
type: docs
weight: 10
url: /pt/java/how-to-create-pdf-portfolio/
lastmod: "2022-01-27"
---

{{% alert color="primary" %}}

Os portfólios PDF permitem reunir conteúdo de diversas fontes (por exemplo, arquivos PDF, Word, Excel, JPEG) em um único contêiner unificado. Os arquivos originais mantêm suas identidades individuais, mas são montados em um arquivo de portfólio PDF. Os usuários podem abrir, ler, editar e formatar cada arquivo componente independentemente dos outros arquivos componentes.

Aspose.PDF para Java permite a criação de documentos de Portfólio PDF usando a classe Document. Carregue o arquivo individual em um objeto FileSpecification e adicione-os ao objeto Document.Collection usando o método add(...). Uma vez que os arquivos tenham sido adicionados, use o método save(..) da classe Document para gerar o documento do portfólio.

{{% /alert %}}

## Exemplo de Código

O exemplo a seguir usa um arquivo Microsoft XPS, um documento Word, PDF e um arquivo de imagem para criar um Portfólio PDF.

**Um portfólio PDF criado com Aspose.PDF**

![todo:image_alt_text](how-to-create-pdf-portfolio_1.png)

{{< gist "aspose-pdf" "474c352a71ac9477aa0d604fd32e1c6a" "CreatePDFPortfolio.java" >}}