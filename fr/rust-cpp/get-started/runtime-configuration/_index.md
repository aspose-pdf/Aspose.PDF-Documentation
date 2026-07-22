---
title: Configuration d'exécution Aspose.PDF pour Rust via C++
linktitle: Configuration d'exécution
type: docs
weight: 100
url: /fr/rust-cpp/runtime-configuration/
description: Les applications Rust qui dépendent de bibliothèques dynamiques natives—telles qu'Aspose.PDF—nécessitent une configuration correcte du chemin d'exécution pour fonctionner correctement sur les systèmes Linux et macOS
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Configuration du RPATH pour le natif Aspose.PDF pour Rust
Abstract: Lorsqu’on travaille avec des bibliothèques dynamiques natives en Rust, un lien d’exécution correct est essentiel pour garantir que votre application puisse localiser les dépendances requises. Sous Linux et macOS, le chargeur dynamique du système ne recherche pas automatiquement le répertoire de l’exécutable à moins que le RPATH ne soit explicitement configuré. Cet article explique comment configurer le RPATH afin que votre application Rust puisse localiser correctement la bibliothèque native Aspose.PDF lors de l’exécution. Il couvre la configuration au niveau du projet à l’aide de Cargo, la configuration basée sur l’environnement avec RUSTFLAGS, ainsi que les options d’installation système, avec des notes sur le comportement sous Windows.
SoftwareApplication: rust-cpp
---

> Il s’agit d’une exigence standard lors de l’utilisation de bibliothèques dynamiques natives en Rust.

Sous Linux et macOS, le chargeur dynamique du système ne recherche pas automatiquement le répertoire de l’exécutable à moins que RPATH ne soit configuré. Pour garantir que votre application puisse trouver la bibliothèque native Aspose.PDF à l’exécution, vous devez configurer le **RPATH** (Run-time Search Path).

Notre script de génération extrait la bibliothèque et tente de créer un lien symbolique vers celle-ci dans votre répertoire de sortie (par exemple, `target/debug/`). Pour permettre à l'exécutable de le trouver, choisissez l'une des options suivantes :

## Option 1 : Configuration au niveau du projet (recommandée)

Créer un dossier nommé `.cargo` dans le répertoire racine de votre projet (s'il n'existe pas) et créez un fichier nommé `config.toml` à l'intérieur :

```toml
[target.'cfg(target_os = "linux")']
rustflags = ["-C", "link-arg=-Wl,-rpath,$ORIGIN"]

[target.'cfg(target_os = "macos")']
rustflags = ["-C", "link-arg=-Wl,-rpath,@loader_path"]
```

## Option 2 : variable d’environnement RUSTFLAGS

Construisez votre projet avec le drapeau suivant :

```bash
# Linux
RUSTFLAGS="-C link-arg=-Wl,-rpath,\$ORIGIN" cargo build

# macOS
RUSTFLAGS="-C link-arg=-Wl,-rpath,@loader_path" cargo build
```

## Option 3 : Installation système (non recommandée pour le développement)

Si vous préférez installer la bibliothèque globalement :

* **Linux:** Copier le `.so` fichier à `/usr/local/lib` et exécuter `sudo ldconfig`.
* **macOS:** Copier le `.dylib` fichier à `/usr/local/lib`.

> **Windows**
> Aucune action n’est généralement requise parce que la bibliothèque se trouve dans le même dossier que le `.exe`. Alternativement, vous pouvez ajouter le répertoire contenant le `.dll` à votre système `PATH` variable d'environnement.