---
title: Sécuriser et signer des fichiers PDF en Python
linktitle: Sécurisation et signature de PDF
type: docs
weight: 210
url: /fr/python-net/securing-and-signing/
description: Apprenez comment signer, chiffrer, déchiffrer et sécuriser des fichiers PDF en Python, y compris les signatures numériques, les cartes à puce et les autorisations de documents.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signez, chiffrez, déchiffrez et protégez des documents PDF en Python
Abstract: Cette section explique comment sécuriser et signer des documents PDF en utilisant Aspose.PDF pour Python via .NET. Apprenez à appliquer des signatures numériques, à utiliser des cartes à puce et des certificats, à extraire les informations de signature et à gérer le chiffrement PDF, les mots de passe et les privilèges d'accès en Python.
---

Cette section explique comment appliquer en toute sécurité des signatures numériques aux documents PDF en utilisant Python Library. Bien que les termes signature électronique et signature numérique soient parfois utilisés de manière interchangeable, ils ne sont pas équivalents. Une signature numérique est soutenue par un [autorité de certification](https://en.wikipedia.org/wiki/Certificate_authority), fournissant un sceau de confiance qui protège le document contre la falsification. En revanche, une signature électronique est généralement utilisée pour indiquer l'intention d'une personne de signer un document, sans le même niveau de validation de sécurité.

Utilisez ces guides lorsque vous devez protéger le contenu PDF, contrôler les autorisations du document, vérifier la confiance ou appliquer des signatures basées sur des certificats dans les flux de travail Python.

## Tâches de sécurité et de signature couvertes

Aspose.PDF prend en charge les signatures numériques :

- PKCS1 avec l'algorithme de signature RSA et le hachage SHA-1.
- PKCS7 avec algorithme de signature RSA et empreinte SHA-1.
- PKCS7 détaché avec les algorithmes de signature DSA, RSA et ECDSA. Les algorithmes d'empreinte pris en charge dépendent de l'algorithme de signature.
- Signature d'horodatage.

Algorithmes d'empreinte pour PKCS7 détaché :

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Il est recommandé d'éviter les signatures numériques avec l'algorithme de hachage SHA-1 en raison de son manque de sécurité.

- [Signer numériquement le fichier PDF](/pdf/fr/python-net/digitally-sign-pdf-file/)
- [Définir les privilèges, chiffrer et déchiffrer le fichier PDF](/pdf/fr/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extraire les informations d'image et de signature](/pdf/fr/python-net/extract-image-and-signature-information/)
- [Signer le document PDF depuis une carte à puce](/pdf/fr/python-net/sign-pdf-document-from-smart-card/)
