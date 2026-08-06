---
title: Crie um PDF seguro no SharePoint
linktitle: Criando um PDF Seguro
type: docs
weight: 60
url: /pt/sharepoint/creating-a-secure-pdf/
lastmod: "2020-12-16"
description: Usando a API PDF SharePoint, você pode produzir PDFs criptografados e seguros e especificar suas senhas no SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF para SharePoint oferece suporte à criação de PDFs seguros. A instalação do Aspose.PDF para SharePoint adiciona uma opção **Configurações seguras de PDF** na configuração do site. Aqui, você pode definir a senha do usuário, a senha do proprietário e qualquer valor da lista de algoritmos para criptografar o PDF de saída. A lista de algoritmos fornece diferentes combinações de algoritmos de criptografia e tamanhos de chave. Passe o valor de sua preferência.

Este artigo demonstra como usar Aspose.PDF for SharePoint para gerar um PDF criptografado.

{{% /alert %}}

## Criando um PDF Seguro

Para demonstrar o recurso, primeiro configuramos a opção **PDF Secure Setting** para senha de proprietário e usuário e algoritmo de criptografia. O exemplo então mescla dois documentos de uma biblioteca de documentos.

### Configurando opções de configuração segura de PDF

Abra a opção **Configurações seguras de PDF** em Configurações do site e defina o algoritmo, a senha do proprietário e a senha do usuário.

Especifique diferentes senhas de usuário e proprietário ao criptografar o arquivo PDF.

- A senha do usuário, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat Reader solicita que o usuário insira a senha do usuário. Se estiver errado, o documento não abre.
- A senha do proprietário, se definida, controla permissões como impressão, edição, extração, comentários, etc. O Acrobat Reader não permite esses recursos com base nas configurações de permissão. O Acrobat exige essa senha se você deseja definir/alterar permissões.

![Configurações seguras de PDF](creating-a-secure-pdf_1.png)

### Mesclar documentos

Mescle dois documentos usando a opção **Converter para PDF**. Este recurso mescla vários arquivos não PDF (HTML, texto ou imagem) em um arquivo PDF.

1. Abra uma biblioteca de documentos e selecione os documentos desejados na lista.

![Mesclar documentos](creating-a-secure-pdf_2.png)

1. Use a opção **Mesclar em PDF** em Ferramentas de biblioteca para salvar o arquivo de saída. Você será solicitado a salvar o arquivo de saída no disco.

![Mesclar em PDF](creating-a-secure-pdf_3.png)

### Saída

O arquivo de saída está criptografado.

![Saída](creating-a-secure-pdf_4.png)


