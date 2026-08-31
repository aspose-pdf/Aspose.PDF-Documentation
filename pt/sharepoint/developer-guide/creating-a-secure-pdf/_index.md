---
title: Criar um PDF Seguro no SharePoint
linktitle: Criando um PDF Seguro
type: docs
weight: 60
url: /pt/sharepoint/creating-a-secure-pdf/
lastmod: "2026-08-31"
description: Usando a API PDF do SharePoint, você pode produzir PDFs seguros e criptografados e especificar suas senhas no SharePoint.
---

{{% alert color="primary" %}}

Aspose.PDF for SharePoint suporta a criação de PDFs seguros. Instalar Aspose.PDF for SharePoint adiciona uma opção **PDF Secure Settings** nas Configurações do Site. Aqui, você pode definir a senha do usuário, a senha do proprietário e qualquer valor da lista de algoritmos para criptografar o PDF de saída. A lista de algoritmos oferece diferentes combinações de algoritmos de criptografia e tamanhos de chave. Passe o valor de sua escolha.

Este artigo demonstra como usar Aspose.PDF for SharePoint para gerar um PDF criptografado.

{{% /alert %}}

## Criando um PDF Seguro

Para demonstrar o recurso, primeiro configuramos a opção **PDF Secure Setting** para a senha do proprietário e do usuário e o algoritmo de criptografia. O exemplo então mescla dois documentos de uma biblioteca de documentos.

### Configurando opções de PDF Secure Setting

Abra a opção **PDF Secure Settings** em Configurações do Site e defina o algoritmo, a senha do proprietário e a senha do usuário.

Especifique senhas diferentes para usuário e proprietário ao criptografar o arquivo PDF.

- A senha do usuário, se definida, é o que você precisa fornecer para abrir um PDF. O Acrobat Reader solicita que o usuário insira a senha do usuário. Se estiver errada, o documento não será aberto.
- A senha do proprietário, se definida, controla permissões como impressão, edição, extração, comentários, etc. O Acrobat Reader desabilita esses recursos com base nas configurações de permissão. O Acrobat requer essa senha se você quiser definir/alterar permissões.

![Configurações Seguras de PDF](creating-a-secure-pdf_1.png)

### Mesclar Documentos

Mescle dois documentos usando a opção **Convert to PDF**. Esse recurso mescla vários arquivos que não são PDF (HTML, texto ou imagem) em um arquivo PDF.

1. Abra uma biblioteca de documentos e selecione os documentos desejados na lista.

![Mesclar Documentos](creating-a-secure-pdf_2.png)

1. Use a opção **Merge to PDF** nas Library Tools para salvar o arquivo de saída. Você será solicitado a salvar o arquivo de saída no disco.

![Mesclar para PDF](creating-a-secure-pdf_3.png)

### Saída

O arquivo de saída está criptografado.

![Saída](creating-a-secure-pdf_4.png)

