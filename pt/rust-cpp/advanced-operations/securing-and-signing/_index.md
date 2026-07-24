---
title: Protegendo e assinando PDF em Rust
linktitle: Protegendo e assinando PDF
type: docs
weight: 50
url: /pt/rust-cpp/securing-and-signing/
description: Esta seção descreve os recursos de uso de uma assinatura e proteção do seu documento PDF usando Rust
lastmod: "2026-07-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Esta seção fornece um guia abrangente para trabalhar com documentos PDF seguros usando Aspose.PDF for Rust via C++. Ela explica como proteger arquivos PDF com senhas, gerenciar permissões de acesso e abrir ou desbloquear documentos criptografados com segurança em Rust.

O artigo percorre tarefas comuns relacionadas à segurança de PDFs, incluindo criptografar PDFs com algoritmos criptográficos modernos, descriptografar arquivos protegidos por senha e controlar o acesso do usuário por meio de flags de permissão. Você também aprenderá como inspecionar as configurações de permissão existentes e abrir documentos seguros usando as credenciais do proprietário para processamento adicional.

Você aprenderá como criar documentos PDF, aplicar proteção criptográfica moderna usando criptografia baseada em AES e controlar as capacidades do usuário, como impressão, edição de conteúdo e preenchimento de formulários. O artigo também demonstra como abrir PDFs protegidos por senha usando credenciais de proprietário e descriptografá-los para gerar documentos sem restrições adequados para processamento adicional.

- [Encriptar e Arquivo PDF](/pdf/pt/rust-cpp/encrypt-pdf/)
- [Descriptografar Arquivo PDF](/pdf/pt/rust-cpp/decrypt-pdf/)
- [Obter Permissões](/pdf/pt/rust-cpp/get-permissions/)
- [Definir permissões](/pdf/pt/rust-cpp/set_permissions/)
- [Abrir um PDF protegido por senha](/pdf/pt/rust-cpp/open-password-protected-pdf/)

Para trabalhar com Definir Permissões e Obter Permissões, consulte a tabela de Referência de Permissões de PDF, que lista as flags de permissão disponíveis que podem ser aplicadas a um documento PDF para controlar como os usuários finais interagem com ele.

## Referência de Permissões PDF

| **Permissão** | **Descrição** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | Permitir impressão |
| Permissions::MODIFY_CONTENT | Permitir modificar conteúdo (exceto formulários/anotações) |
| Permissions::EXTRACT_CONTENT | Permitir copiar/extrair texto e gráficos |
| Permissions::MODIFY_TEXT_ANNOTATIONS | Permitir adicionar/modificar anotações de texto |
| Permissions::FILL_FORM | Permitir o preenchimento de formulários interativos |
| Permissions::EXTRACT_CONTENT_WITH_DISABILITIES | Permitir extração de conteúdo para acessibilidade |
| Permissions::ASSEMBLE_DOCUMENT | Permitir inserção/rotação/exclusão de páginas ou alteração da estrutura |
| Permissions::PRINTING_QUALITY | Permitir impressão de alta qualidade / fiel |
