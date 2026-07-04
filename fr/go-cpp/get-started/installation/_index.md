---
title: Comment installer Aspose.PDF pour Go via C++
linktitle: Installation
type: docs
weight: 20
url: /fr/go-cpp/installation/
description: Cette section présente une description du produit et des instructions pour installer Aspose.PDF for Go par vous-même.
lastmod: "2026-07-04"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide d\'installation d\'Aspose.PDF for Go
Abstract: Le guide d'installation Aspose.PDF for Go via C++ fournit des instructions étape par étape pour installer et configurer la bibliothèque en vue d'une utilisation dans des projets Go avec intégration C++. Il couvre diverses méthodes d'installation, y compris la configuration manuelle et l'utilisation de gestionnaires de paquets tels que NuGet. Le guide décrit également les exigences système, les dépendances et les étapes de configuration nécessaires pour garantir une intégration transparente dans les environnements de développement. Cette documentation aide les développeurs à démarrer la création, la lecture et la manipulation de documents PDF en Go via C++ de manière efficace.
SoftwareApplication: go-cpp
---

## Installation

Ce paquet comprend un fichier volumineux qui est stocké sous forme d'archive bzip2.

1. Ajoutez le package asposepdf à votre projet :

```sh
go get github.com/aspose-pdf/aspose-pdf-go-cpp@latest
```

2. Générez le fichier volumineux :

- **macOS et linux**

1. Ouvrir le terminal

2. Répertoriez les dossiers de github.com/aspose-pdf dans le cache des modules Go :

```sh
ls $(go env GOMODCACHE)/github.com/aspose-pdf/
```

3. Modifiez le dossier curent vers le dossier de version spécifique du package obtenu à l'étape précédente :

```sh
cd $(go env GOMODCACHE)/github.com/aspose-pdf/aspose-pdf-go-cpp@vx.x.x
```

Remplacez `@vx.x.x` par la version réelle du package.

4. Exécutez go generate avec des privilèges superutilisateur :

```sh
sudo go generate
```

- **Windows**

1. Ouvrir l'invite de commandes

2. Répertoriez les dossiers de github.com/aspose-pdf dans le cache des modules Go :

```cmd
for /f "delims=" %G in ('go env GOMODCACHE') do for /d %a in ("%G\github.com\aspose-pdf\*") do echo %~fa
```

3. Modifiez le dossier curent vers le dossier de version spécifique du package obtenu à l'étape précédente :

```cmd
cd <specific version folder of the package>
```

4. Exécuter go generate:

```cmd
go generate
```

5. Ajoutez le dossier de version spécifique du package à la variable d’environnement %PATH% :

```cmd
setx PATH "%PATH%;<specific version folder of the package>\lib\"
```

Remplacer `<specific version folder of the package>` avec le chemin réel obtenu à partir de l'étape 2.

## Test

Le test s'exécute depuis le dossier racine du package :

```sh
go test -v
```

## Démarrage rapide

Tous les extraits de code sont contenus dans le [extrait](https://github.com/aspose-pdf/aspose-pdf-go-cpp).