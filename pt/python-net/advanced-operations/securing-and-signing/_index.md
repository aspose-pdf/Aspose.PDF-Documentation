---
title: Protegendo e assinando PDF em Python
linktitle: Protegendo e assinando em PDF
type: docs
weight: 210
url: /pt/python-net/securing-and-signing/
description: Esta seção descreve os recursos de uso de assinatura e proteção do seu documento PDF usando Python
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Assine documentos PDF com Python
Abstract: Esta seção da documentação Aspose.PDF para Python via .NET fornece orientações abrangentes sobre como proteger e assinar documentos PDF programaticamente. Ela aborda tópicos essenciais, incluindo proteção por senha, algoritmos de criptografia, aplicação e verificação de assinaturas digitais, manipulação de certificados e permissões de documentos. Os desenvolvedores aprenderão a implementar vários níveis de segurança para proteger conteúdo sensível, garantir a integridade do documento e atender aos padrões regulatórios. Os exemplos e referências de API permitem uma rápida integração de recursos de segurança em aplicações Python, facilitando a proteção dos fluxos de trabalho de PDF com confiança.
---

Esta seção explica como aplicar assinaturas digitais de forma segura a documentos PDF usando a Biblioteca Python. Embora os termos assinatura eletrônica e assinatura digital sejam às vezes usados de forma intercambiável, eles não são iguais. Uma assinatura digital é respaldada por uma [autoridade certificadora](https://en.wikipedia.org/wiki/Certificate_authority), fornecendo um selo confiável que protege o documento contra adulteração. Em contraste, uma assinatura eletrônica é tipicamente usada para indicar a intenção de uma pessoa de assinar um documento, sem o mesmo nível de validação de segurança.

Aspose.PDF suporta assinaturas digitais:

- PKCS1 com algoritmo de assinatura RSA e digestão SHA-1.
- PKCS7 com algoritmo de assinatura RSA e digestão SHA-1.
- PKCS7 destacado com algoritmos de assinatura DSA, RSA e ECDSA. Os algoritmos de digestão suportados dependem do algoritmo de assinatura.
- Assinatura de carimbo de tempo.

Algoritmos de digestão para PKCS7 destacado:

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

É recomendado evitar assinaturas digitais com o algoritmo de digestão SHA-1 devido à sua insegurança.

- [Assinar digitalmente arquivo PDF](/pdf/python-net/digitally-sign-pdf-file/)
- [Definir privilégios, criptografar e descriptografar arquivo PDF](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extrair imagem e informações de assinatura](/pdf/python-net/extract-image-and-signature-information/)
- [Assinar documento PDF a partir de cartão inteligente](/pdf/python-net/sign-pdf-document-from-smart-card/)
