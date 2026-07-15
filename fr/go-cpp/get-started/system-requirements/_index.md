---
title: Exigences système
linktitle: Exigences système
type: docs
weight: 30
url: /fr/go-cpp/system-requirements/
description: Cette section répertorie les systèmes d'exploitation pris en charge dont un développeur a besoin pour travailler avec succès avec Aspose.PDF for Go.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Page des exigences système pour Aspose.PDF for Go
Abstract: La page des exigences système pour Aspose.PDF for Go fournit les détails nécessaires à l'installation de la bibliothèque sur diverses plateformes. Elle décrit les paramètres d'environnement requis, tels que les systèmes d'exploitation pris en charge, les dépendances système et les configurations matérielles, afin d'assurer une installation réussie de la bibliothèque et des performances optimales. Elle inclut également des informations sur les prérequis logiciels, comme les versions prises en charge de Go, ainsi que toute configuration supplémentaire nécessaire pour exécuter efficacement la bibliothèque sur différents systèmes. Ces informations aident les développeurs à configurer correctement leur environnement de développement.
SoftwareApplication: go-cpp
---

## Plateformes prises en charge d'Aspose.PDF for Go via C++

Le package asposepdf est une boîte à outils puissante qui permet aux développeurs de manipuler directement les fichiers PDF et d'effectuer diverses tâches liées aux PDF.
Contient des fonctionnalités uniques pour convertir le PDF en d’autres formats.

Support implémenté pour les plateformes Linux x64, macOS x86_64, macOS arm64 et Windows x64. Utilisé [cgo](https://go.dev/wiki/cgo).

La version spécifique à la plateforme de la bibliothèque dynamique du dossier ‘lib’ dans le répertoire racine du package est requise pour distribuer l’application résultante :

- **libAsposePDFforGo_linux_amd64.so** pour la plateforme Linux x64.
- **libAsposePDFforGo_darwin_arm64.dylib** pour la plateforme macOS arm64.
- **libAsposePDFforGo_darwin_amd64.dylib** pour la plateforme macOS x86_64.
- **AsposePDFforGo_windows_amd64.dll** pour la plateforme Windows x64.

La plateforme Windows x64 requiert [MinGW-W64](https://www.mingw-w64.org/) installé.