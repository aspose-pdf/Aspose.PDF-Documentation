---
title: Operações avançadas usando JavaScript via C++
linktitle: Operações avançadas
type: docs
weight: 60
url: /javascript-cpp/advanced-operations/
description: Aspose.PDF para JavaScript via C++ pode realizar não apenas tarefas simples e fáceis, mas também lidar com objetivos mais complexos. Confira a próxima seção para usuários avançados e desenvolvedores.
lastmod: "2023-02-17"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

**Operações Avançadas** é uma seção sobre como lidar com arquivos PDF existentes programaticamente, sejam eles documentos criados com Aspose.PDF, como discutido em [Operações Básicas](/pdf/javascript-cpp/basic-operations/), ou PDFs criados com Adobe Acrobat, Google Docs, Microsoft Office, Open Office ou qualquer outro produtor de PDF.

## Usando Web Workers

A versão 23.6 adicionou a capacidade de usar Web Workers:

```js
const AsposePDFWebWorker = new Worker("AsposePDFforJS.js");
```

O uso de Web Workers do JavaScript via C++ permite que você realize operações sem bloquear a interface, em uma thread de trabalhador separada.

Web Workers é uma ferramenta simples para executar scripts em segundo plano, o que permite realizar tarefas sem interferir na interface do usuário, em uma thread de trabalho separada.

Você aprenderá diferentes maneiras de:

- [Trabalhando com Documentos](/pdf/javascript-cpp/working-with-documents/) - comprimir, dividir e mesclar documentos e fazer outras operações com o documento inteiro.
- [Trabalhando com Páginas](/pdf/javascript-cpp/working-with-pages/) - adicionar, mover ou remover, cortar páginas, carimbos.
- [Metadados em PDFs](/pdf/javascript-cpp/pdf-file-metadata/) - obter ou definir metadados em documentos.
- [Trabalhando com Imagens](/pdf/javascript-cpp/working-with-images/) - inserir, remover, extrair imagem no documento
- [Navegação e Interação](/pdf/javascript-cpp/navigation-and-interaction/) - lidar com ações, favoritos, navegar pelas páginas
- [Anotações](/pdf/javascript-cpp/annotations/) - As anotações permitem que os usuários adicionem conteúdo personalizado nas páginas de PDF. Você pode adicionar, excluir e modificar a anotação nos documentos PDF.

- [Protegendo e Assinando](/pdf/javascript-cpp/securing-and-signing/) - proteger e assinar seu documento PDF programaticamente
- [Anexos](/pdf/javascript-cpp/attachments/) - Documentos PDF podem conter anexos de arquivos. Esses anexos podem ser outros documentos PDF ou qualquer tipo de arquivo, como arquivos de áudio, documentos do Microsoft Office, etc. Você aprenderá como adicionar anexos ao PDF, obter informações de um anexo e salvá-lo em um arquivo, excluir o anexo do PDF programaticamente com JavaScript.