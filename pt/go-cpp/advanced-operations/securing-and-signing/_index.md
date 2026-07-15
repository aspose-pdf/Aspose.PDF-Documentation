---
title: Protegendo e assinando PDF em Go
linktitle: Protegendo e assinando PDF
type: docs
weight: 50
url: /pt/go-cpp/securing-and-signing/
description: Esta seção descreve os recursos de uso de uma assinatura e de proteção do seu documento PDF usando Go
lastmod: "2026-07-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Esta seção fornece um guia abrangente para trabalhar com documentos PDF seguros usando Aspose.PDF for Go via C++. Ela explica como proteger arquivos PDF com senhas, gerenciar permissões de acesso e abrir ou desbloquear com segurança documentos criptografados em aplicações Go.

O artigo aborda tarefas comuns relacionadas à segurança de PDFs, incluindo criptografar PDFs com algoritmos criptográficos modernos, descriptografar arquivos protegidos por senha e controlar o acesso do usuário por meio de flags de permissão. Você também aprenderá como inspecionar as configurações de permissão existentes e abrir documentos seguros usando as credenciais do proprietário para processamento adicional.

Você aprenderá como criar documentos PDF, aplicar proteção criptográfica moderna usando criptografia baseada em AES e controlar as capacidades do usuário, como impressão, edição de conteúdo e preenchimento de formulários. O artigo também demonstra como abrir PDFs protegidos por senha usando credenciais do proprietário e descriptografá-los para produzir documentos sem restrições adequados para processamento adicional.

- [Criptografar e Arquivo PDF](/pdf/pt/go-cpp/encrypt-pdf/)
- [Descriptografar Arquivo PDF](/pdf/pt/go-cpp/decrypt-pdf/)
- [Obter Permissões](/pdf/pt/go-cpp/get-permissions/)
- [Definir permissões](/pdf/pt/go-cpp/set_permissions/)
- [Abrir um PDF protegido por senha](/pdf/pt/go-cpp/open-password-protected-pdf/)

Para trabalhar com Definir Permissões e Obter Permissões, consulte a tabela de Referência de Permissões de PDF.  Que lista os sinalizadores de permissão disponíveis que podem ser aplicados a um documento PDF para controlar como os usuários finais interagem com ele.

## Referência de Permissões de PDF

| **Permissão** | **Descrição** |
| :- | :- |
| PrintDocument | Permitir impressão |
| ModifyContent | Permitir modificar o conteúdo (exceto formulários/anotações) |
| ExtractContent | Permitir copiar/extrair texto e gráficos |
| ModifyTextAnnotations | Permitir adicionar/modificar anotações de texto |
| FillForm | Permitir preenchimento de formulários interativos |
| ExtractContentWithDisabilities | Permitir extração de conteúdo para acessibilidade |
| AssembleDocument | Permitir inserir/rotacionar/excluir páginas ou alterar a estrutura |
| PrintingQuality | Permitir impressão de alta qualidade / fidedigna |


