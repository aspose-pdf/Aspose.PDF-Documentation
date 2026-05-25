---
title: Proteger e Assinar Arquivos PDF em Python
linktitle: Proteção e assinatura em PDF
type: docs
weight: 210
url: /pt/python-net/securing-and-signing/
description: Aprenda como assinar, criptografar, descriptografar e proteger arquivos PDF em Python, incluindo assinaturas digitais, cartões inteligentes e permissões de documento.
lastmod: "2026-05-18"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine, criptografe, descriptografar e proteja documentos PDF em Python
Abstract: Esta seção explica como proteger e assinar documentos PDF usando Aspose.PDF for Python via .NET. Aprenda como aplicar assinaturas digitais, usar cartões inteligentes e certificados, extrair informações de assinatura e gerenciar a criptografia de PDF, senhas e privilégios de acesso em Python.
---

Esta seção explica como aplicar assinaturas digitais de forma segura a documentos PDF usando Python Library. Enquanto os termos assinatura eletrônica e assinatura digital são às vezes usados de forma intercambiável, eles não são iguais. Uma assinatura digital é respaldada por um [autoridade certificadora](https://en.wikipedia.org/wiki/Certificate_authority), fornecendo um selo confiável que protege o documento contra adulteração. Em contraste, uma assinatura eletrônica é normalmente usada para indicar a intenção de uma pessoa de assinar um documento, sem o mesmo nível de validação de segurança.

Use estes guias quando precisar proteger o conteúdo PDF, controlar as permissões do documento, verificar a confiança ou aplicar assinaturas baseadas em certificado em fluxos de trabalho Python.

## Tarefas de Segurança e Assinatura Abrangidas

Aspose.PDF oferece suporte a assinaturas digitais:

- PKCS1 com algoritmo de assinatura RSA e digestão SHA-1.
- PKCS7 com algoritmo de assinatura RSA e digestão SHA-1.
- PKCS7 destacado com algoritmos de assinatura DSA, RSA e ECDSA. Os algoritmos de digestão suportados dependem do algoritmo de assinatura.
- Assinatura de timestamp.

Algoritmos de digestão para PKCS7 destacado:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Recomenda-se evitar assinaturas digitais com o algoritmo de resumo SHA-1 devido à sua insegurança.

- [Assinar digitalmente arquivo PDF](/pdf/pt/python-net/digitally-sign-pdf-file/)
- [Definir privilégios, criptografar e descriptografar arquivo PDF](/pdf/pt/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extrair informações de imagem e assinatura](/pdf/pt/python-net/extract-image-and-signature-information/)
- [Assinar documento PDF a partir de cartão inteligente](/pdf/pt/python-net/sign-pdf-document-from-smart-card/)
