---
title: Sécurisation et signature de PDF en Python
linktitle: Sécurisation et signature en PDF
type: docs
weight: 210
url: /fr/python-net/securing-and-signing/
description: Cette section décrit les fonctionnalités d’utilisation d’une signature et de sécurisation de votre document PDF avec Python
lastmod: "2025-06-23"
sitemap: 
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Signer des documents PDF avec Python
Abstract: Cette section de la documentation Aspose.PDF pour Python via .NET fournit des instructions complètes sur la sécurisation et la signature des documents PDF de manière programmatique. Elle couvre des sujets essentiels tels que la protection par mot de passe, les algorithmes de chiffrement, l’application et la vérification des signatures numériques, la gestion des certificats et les autorisations de document. Les développeurs apprendront à mettre en œuvre différents niveaux de sécurité pour protéger les contenus sensibles, garantir l’intégrité des documents et se conformer aux normes réglementaires. Les exemples et références API permettent une intégration rapide des fonctionnalités de sécurité dans les applications Python, facilitant la protection des flux de travail PDF en toute confiance.
---

Cette section explique comment appliquer en toute sécurité des signatures numériques aux documents PDF à l’aide de la bibliothèque Python. Bien que les termes signature électronique et signature numérique soient parfois utilisés de manière interchangeable, ils ne désignent pas la même chose. Une signature numérique est soutenue par une [autorité de certification](https://en.wikipedia.org/wiki/Certificate_authority), offrant un sceau de confiance qui protège le document contre la falsification. En revanche, une signature électronique est généralement utilisée pour indiquer l’intention d’une personne de signer un document, sans le même niveau de validation de sécurité.

Aspose.PDF prend en charge les signatures numériques :

- PKCS1 avec l’algorithme de signature RSA et le condensat SHA-1.
- PKCS7 avec l’algorithme de signature RSA et le condensat SHA-1.
- PKCS7 détaché avec les algorithmes de signature DSA, RSA et ECDSA. Les algorithmes de condensat pris en charge dépendent de l’algorithme de signature.
- Signature horodatée.

Algorithmes de condensat pour PKCS7 détaché :

- DSA - SHA-1.
- RSA - SHA-1, SHA-256, SHA-384, SHA-512.
- ECDSA - SHA-256, SHA-384, SHA-512, SHA3-256, SHA3-384, SHA3-512.

Il est recommandé d’éviter les signatures numériques avec l’algorithme de condensat SHA-1 en raison de son manque de sécurité.

- [Signer numériquement un fichier PDF](/pdf/python-net/digitally-sign-pdf-file/)
- [Définir les privilèges, chiffrer et déchiffrer le fichier PDF](/pdf/python-net/set-privileges-encrypt-and-decrypt-pdf-file/)
- [Extraire les images et les informations de signature](/pdf/python-net/extract-image-and-signature-information/)
- [Signer le document PDF depuis une carte à puce](/pdf/python-net/sign-pdf-document-from-smart-card/)
