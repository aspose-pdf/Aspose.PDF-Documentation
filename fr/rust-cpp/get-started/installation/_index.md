---
title: Comment installer Aspose.PDF pour Rust via C++
linktitle: Installation
type: docs
weight: 20
url: /fr/rust-cpp/installation/
description: Cette section présente une description du produit et des instructions pour installer Aspose.PDF pour Rust vous-même.
lastmod: "2026-07-20"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Guide d'installation d'Aspose.PDF pour Rust
Abstract: Le guide d'installation d'Aspose.PDF for Rust via C++ fournit des instructions étape par étape pour installer et configurer la bibliothèque afin de l'utiliser dans des projets Rust avec intégration C++. Il couvre différentes méthodes d'installation, y compris la configuration manuelle et l'utilisation de gestionnaires de packages comme NuGet. Le guide décrit également les exigences système, les dépendances et les étapes de configuration nécessaires pour assurer une intégration transparente dans les environnements de développement. Cette documentation aide les développeurs à démarrer la création, la lecture et la manipulation de documents PDF en Rust via C++ de manière efficace.
SoftwareApplication: rust-cpp
---

## Installation

### Installation depuis le site Web d'Aspose

Ce paquet inclut un fichier volumineux qui est stocké sous forme d'archive bzip2.

1. **Télécharger** l'archive **Aspose.PDF for Rust via C++** sur le site officiel d'Aspose.
   La version la plus récente (la plus à jour) est affichée en haut et est téléchargée par défaut lorsque vous cliquez sur le bouton **Télécharger**.
   Il est recommandé d'utiliser cette dernière version. Téléchargez une version précédente uniquement si nécessaire.
   Exemple : `Aspose.PDF-for-Rust-via-CPP-25.6.zip`

   Le format du nom de fichier d'archive est : `Aspose.PDF-for-Rust-via-CPP-YY.M.zip`, où:
   - `YY` = les deux derniers chiffres de l'année (p. ex., `25` pour 2025)
   - `M` = numéro du mois à partir de `1` à `12`

2. **Extraire** l'archive dans le répertoire de votre choix `{path}` en utilisant un outil approprié :

   - Sur Linux/macOS :

     ```bash
     unzip Aspose.PDF-for-Rust-via-CPP-YY.M.zip -d {path}
     ```

   - Sur Windows, utilisez l'extraction intégrée de l'Explorateur ou tout outil de décompression (7‑Zip, WinRAR).

3. **Ajouter** la bibliothèque en tant que dépendance dans votre projet Rust. Vous pouvez le faire de deux manières :

   - **Utilisation de la ligne de commande :**

     ```bash
     cargo add asposepdf --path {path}/asposepdf
     ```

   - **Modification manuelle** `Cargo.toml`:**
     Ouvrez le projet de votre `Cargo.toml` et ajoutez ce qui suit sous `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { path = "{path}/asposepdf" }
     ```

4. **Construisez votre projet** (`cargo build`). Lors de la première construction, la bibliothèque dynamique appropriée pour votre plateforme sera automatiquement extraite du `.bz2` archiver dans le `lib` dossier et lié à votre projet.

**Notes**

- Le script de compilation tente de créer un **lien symbolique** vers la bibliothèque dans votre répertoire de sortie (par ex., `target/debug/`).
- Pour **Linux et macOS**, vous devez également suivre le [Configuration d'exécution](#runtime-configuration) section ci-dessous pour garantir que l'exécutable puisse trouver la bibliothèque au moment de l'exécution.
- Tout `.bz2` les archives ont correspondantes `.sha256` fichiers de somme de contrôle. Si une somme de contrôle est manquante ou invalide, la construction échouera.

### Installation depuis GitHub

Ce package comprend des bibliothèques natives précompilées ("`.dll`, `.so`, `.dylib`) qui sont stockés sous forme compressée `.bz2` archives dans le dépôt GitHub.

1. **Ajouter** la bibliothèque en tant que dépendance dans votre projet Rust. Vous pouvez le faire de deux manières :

   - **Utilisation de la ligne de commande :**

     ```bash
     cargo add asposepdf --git https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git
     ```

   - **Modification manuelle** `Cargo.toml`:**

     Ouvrez le projet de votre `Cargo.toml` et ajoutez ce qui suit sous `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = { git = "https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git" }
     ```

    > **Note :** Pour utiliser une version de publication spécifique, vous pouvez spécifier une balise :
    >
    > ```toml
    > asposepdf = { git = \"https://github.com/aspose-pdf/aspose-pdf-rust-cpp.git", tag = "v1.26.1" }
    > ```

2. **Construisez votre projet** (`cargo build`). Lors de la première construction, la bibliothèque dynamique appropriée pour votre plateforme sera automatiquement extraite du `.bz2` archiver dans le `lib` dossier et lié à votre projet.

**Notes**

- Vous n'avez pas besoin de télécharger ou d'extraire manuellement des fichiers - tout est inclus dans le dépôt GitHub.
- Le script de compilation tente de créer un **lien symbolique** vers la bibliothèque dans votre répertoire de sortie (par ex., `target/debug/`).
- Pour **Linux et macOS**, vous devez également suivre le [Configuration d'exécution](#runtime-configuration) section ci-dessous pour garantir que l'exécutable puisse trouver la bibliothèque au moment de l'exécution.
- Tout `.bz2` les archives correspondent `.sha256` fichiers de somme de contrôle. La somme de contrôle est vérifiée avant le déballage.
- Si la vérification du checksum échoue ou si l'archive est manquante, la construction échouera avec une erreur détaillée.

### Installation depuis crates.io

Ce paquet est disponible sur [crates.io](https://crates.io/crates/asposepdf). 
En raison des limites de taille, le crate publié n’inclut pas les bibliothèques binaires natives (`.dll`, `.so`, ou `.dylib`).
Vous pouvez obtenir les bibliothèques natives requises soit à partir de l'archive de distribution officielle (voir [Installation depuis le site Web d'Aspose](#installation-from-aspose-website)) ou depuis le dépôt GitHub (voir [Installation depuis GitHub](#installation-from-github)).
Le script de construction localisera, vérifiera et extraira la bibliothèque native appropriée d'une archive compressée au format .bz2 pendant le processus de construction.

1. **Ajouter** la bibliothèque en tant que dépendance dans votre projet Rust. Vous pouvez le faire de deux manières :

   - **Utilisation de la ligne de commande :**

     ```bash
     cargo add asposepdf
     ```

   - **Modification manuelle** `Cargo.toml`:**

     Ouvrez le projet de votre `Cargo.toml` et ajoutez ce qui suit sous `[dependencies]`:

     ```toml
     [dependencies]
     asposepdf = "1.26.1"
     ```

2. **Définir le chemin** vers le répertoire contenant les bibliothèques natives et télécharger les fichiers requis :

   - **Définir la variable d'environnement** `ASPOSE_PDF_LIB_DIR`** pour pointer vers le dossier où vous placerez le natif `.bz2` archives, leurs `.sha256` fichiers de somme de contrôle, et les bibliothèques natives extraites (`.dll`, `.so`, `.dylib`, et pour Windows aussi `.lib`):

     - Sur Linux/macOS :

       ```bash
       export ASPOSE_PDF_LIB_DIR=/path/to/lib
       ```

     - Sous Windows (Invite de commandes):

       ```cmd
       set ASPOSE_PDF_LIB_DIR=C:\path\to\lib
       ```

     - Sur Windows (PowerShell) :
     
       ```powershell
       $env:ASPOSE_PDF_LIB_DIR = "C:\path\to\lib"
       ```

**Note sur ASPOSE_PDF_LIB_DIR**

Le `ASPOSE_PDF_LIB_DIR` la variable d'environnement définit le répertoire de travail pour le script de construction. Elle est utilisée **uniquement pendant la compilation** pour localiser, vérifier et extraire les archives de bibliothèques natives. La définition de cette variable **n'ajoute pas** automatiquement le répertoire au chemin de recherche des bibliothèques d'exécution de votre système (voir [Configuration d'exécution](#runtime-configuration)).

  - **Téléchargez le requis** `.bz2` archives** et fichiers de somme de contrôle du référentiel GitHub [`lib/` dossier](https://github.com/aspose-pdf/aspose-pdf-rust-cpp/tree/main/lib) et **placez-les** dans le dossier défini dans `ASPOSE_PDF_LIB_DIR`:

  - Pour **Linux x64**, téléchargez :
    - `libAsposePDFforRust_linux_amd64.so.bz2`
    - `libAsposePDFforRust_linux_amd64.so.bz2.sha256`

  - Pour **macOS x86_64**, télécharger :
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2`
    - `libAsposePDFforRust_darwin_amd64.dylib.bz2.sha256`

  - Pour **macOS arm64**, télécharger :
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2`
    - `libAsposePDFforRust_darwin_arm64.dylib.bz2.sha256`

  - Pour **Windows x64**, téléchargez :
    - `AsposePDFforRust_windows_amd64.dll.bz2`
    - `AsposePDFforRust_windows_amd64.dll.bz2.sha256`
    - `AsposePDFforRust_windows_amd64.lib` (bibliothèque d'importation native, non compressée)

**Note:** Vous devez télécharger manuellement ces fichiers depuis GitHub et les placer dans le répertoire indiqué par `ASPOSE_PDF_LIB_DIR`.  
Le script de construction décompressera automatiquement les bibliothèques natives depuis le `.bz2` archives lors du premier build.

3. **Construire** votre projet (`cargo build`). Lors de la première compilation, la bibliothèque native correspondant à votre plateforme sera automatiquement extraite de la `.bz2` archiver et lier à votre projet.

**Important :** Pour **Linux et macOS**, vous devez également suivre le [Configuration d'exécution](#runtime-configuration) section ci-dessous pour garantir que l'exécutable puisse trouver la bibliothèque au moment de l'exécution.

**Notes**

- Le `ASPOSE_PDF_LIB_DIR` la variable est utilisée **uniquement pendant le processus de construction** pour localiser et extraire les archives.
- Le script de construction tente de créer un **lien symbolique** vers la bibliothèque extraite dans votre répertoire de sortie (par exemple, `target/debug/`).
- Vous devez fournir le dossier contenant le `.bz2` et `.sha256` fichiers séparément, car ces archives binaires ne sont pas distribuées via crates.io.
- Si l'archive requise est manquante ou que la somme de contrôle échoue, le processus de construction échouera avec une erreur détaillée.
- Les mêmes fichiers binaires utilisés pour l'installation via GitHub ou le site Web d'Aspose peuvent être réutilisés ici.

## Démarrage rapide

Tous les extraits de code sont contenus dans le [extrait](https://onedrive.live.com/examples).