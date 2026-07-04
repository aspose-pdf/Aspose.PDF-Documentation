---
title: Sécurisation et signature de PDF en Go
linktitle: Sécurisation et signature de PDF
type: docs
weight: 50
url: /fr/go-cpp/securing-and-signing/
description: Cette section décrit les fonctionnalités d’utilisation d’une signature et de sécurisation de votre document PDF avec Go
lastmod: "2026-07-04"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

Cette section fournit un guide complet pour travailler avec des documents PDF sécurisés en utilisant Aspose.PDF for Go via C++. Elle explique comment protéger les fichiers PDF avec des mots de passe, gérer les autorisations d’accès et ouvrir ou déverrouiller en toute sécurité les documents chiffrés dans les applications Go.

L'article passe en revue les tâches PDF courantes liées à la sécurité, notamment le chiffrement des PDF avec des algorithmes cryptographiques modernes, le déchiffrement des fichiers protégés par mot de passe et le contrôle de l'accès des utilisateurs via les drapeaux d'autorisation. Vous apprendrez également à inspecter les paramètres d'autorisation existants et à ouvrir les documents sécurisés en utilisant les informations d'identification du propriétaire pour un traitement ultérieur.

Vous apprendrez comment créer des documents PDF, appliquer une protection cryptographique moderne en utilisant le chiffrement basé sur AES, et contrôler les capacités des utilisateurs telles que l’impression, la modification du contenu et le remplissage des formulaires. L'article montre également comment ouvrir des PDF protégés par mot de passe en utilisant les informations d'identification du propriétaire et les déchiffrer afin de produire des documents sans restriction, adaptés à un traitement ultérieur.

- [Chiffrer un fichier PDF](/pdf/fr/go-cpp/encrypt-pdf/)
- [Déchiffrer le fichier PDF](/pdf/fr/go-cpp/decrypt-pdf/)
- [Obtenir les autorisations](/pdf/fr/go-cpp/get-permissions/)
- [Définir les autorisations](/pdf/fr/go-cpp/set_permissions/)
- [Ouvrir un PDF protégé par mot de passe](/pdf/fr/go-cpp/open-password-protected-pdf/)

Pour travailler avec Set Permissions et Get Permissions, veuillez vous référer au tableau de référence des autorisations PDF.  Celui-ci répertorie les indicateurs d’autorisation disponibles qui peuvent être appliqués à un document PDF pour contrôler la façon dont les utilisateurs finaux interagissent avec lui.

## Référence des autorisations PDF

| **Autorisation** | **Description** |
| :- | :- |
| PrintDocument | Autoriser l'impression |
| ModifyContent | Autoriser la modification du contenu (à l'exception des formulaires/annotations) |
| ExtractContent | Autoriser la copie/l'extraction du texte et des graphiques |
| ModifyTextAnnotations | Autoriser l'ajout/la modification des annotations de texte |
| FillForm | Autoriser le remplissage de formulaires interactifs |
| ExtraireContenuAvecHandicaps | Autoriser l'extraction de contenu pour l'accessibilité |
| AssemblerDocument | Autoriser l'insertion/la rotation/la suppression de pages ou la modification de la structure |
| QualitéImpression | Autoriser une impression de haute qualité / fidèle |


