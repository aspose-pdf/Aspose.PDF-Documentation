---
title: Sécurisation et signature de PDF en Rust
linktitle: Sécurisation et signature de PDF
type: docs
weight: 50
url: /fr/rust-cpp/securing-and-signing/
description: Cette section décrit les fonctionnalités d'utilisation d'une signature et de sécurisation de votre document PDF avec Rust
lastmod: "2026-07-20"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cette section fournit un guide complet pour travailler avec des documents PDF sécurisés en utilisant Aspose.PDF for Rust via C++. Elle explique comment protéger les fichiers PDF avec des mots de passe, gérer les autorisations d'accès et ouvrir ou déverrouiller en toute sécurité les documents chiffrés en Rust.

L'article passe en revue les tâches courantes liées à la sécurité des PDF, y compris le chiffrement des PDF avec des algorithmes cryptographiques modernes, le déchiffrement des fichiers protégés par mot de passe, et le contrôle de l'accès des utilisateurs via des indicateurs d'autorisations. Vous apprendrez également comment inspecter les paramètres d'autorisation existants et ouvrir les documents sécurisés en utilisant les identifiants du propriétaire pour un traitement ultérieur.

Vous apprendrez comment créer des documents PDF, appliquer une protection cryptographique moderne utilisant un chiffrement basé sur AES, et contrôler les capacités des utilisateurs telles que l'impression, la modification du contenu et le remplissage des formulaires. L'article montre également comment ouvrir des PDF protégés par mot de passe en utilisant les identifiants du propriétaire et les déchiffrer afin de produire des documents non restreints adaptés à un traitement ultérieur.

- [Crypter un fichier PDF](/pdf/fr/rust-cpp/encrypt-pdf/)
- [Décrypter le fichier PDF](/pdf/fr/rust-cpp/decrypt-pdf/)
- [Obtenir les autorisations](/pdf/fr/rust-cpp/get-permissions/)
- [Définir les autorisations](/pdf/fr/rust-cpp/set_permissions/)
- [Ouvrir un PDF protégé par mot de passe](/pdf/fr/rust-cpp/open-password-protected-pdf/)

Pour travailler sur les fonctions Définir les autorisations et Obtenir les autorisations, veuillez vous référer au tableau de référence des autorisations PDF.  Celui-ci répertorie les indicateurs d'autorisation disponibles pouvant être appliqués à un document PDF afin de contrôler la manière dont les utilisateurs finaux interagissent avec celui-ci.

## Référence des autorisations PDF

| **Permission** | **Description** |
| :- | :- |
| Permissions::PRINT_DOCUMENT | Autoriser l'impression |
| Permissions::MODIFY_CONTENT | Autoriser la modification du contenu (sauf les formulaires/annotations) |
| Permissions::EXTRACT_CONTENT | Autoriser la copie/l'extraction du texte et des graphiques |
| Permissions::MODIFY_TEXT_ANNOTATIONS | Autoriser l'ajout/modification des annotations de texte |
| Permissions::FILL_FORM | Autoriser le remplissage des formulaires interactifs |
| Permissions::EXTRACT_CONTENT_WITH_DISABILITIES | Autoriser l'extraction de contenu pour l'accessibilité |
| Permissions::ASSEMBLE_DOCUMENT | Autoriser l'insertion/la rotation/la suppression de pages ou la modification de la structure |
| Permissions::PRINTING_QUALITY | Autoriser une impression de haute qualité / fidèle |
