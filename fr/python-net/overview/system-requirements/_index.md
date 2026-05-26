---
title: Exigences système
linktitle: Exigences système
type: docs
weight: 30
url: /fr/python-net/system-requirements/
description: Cette section répertorie les systèmes d’exploitation pris en charge dont un développeur a besoin pour travailler avec succès avec Aspose.PDF for Python.
lastmod: "2026-05-22"
sitemap:
    changefreq: "monthly"
    priority: 0.7
TechArticle: true
AlternativeHeadline: Systèmes d’exploitation pris en charge par Aspose.PDF for Python via .NET
Abstract: Aspose.PDF for Python via .NET est une API de traitement PDF conçue pour les développeurs afin de gérer des documents PDF sans avoir besoin de Microsoft Office ou d’Adobe Acrobat Automation. Elle prend en charge le développement d’applications Python 32 bits et 64 bits sur divers systèmes d’exploitation, notamment Windows et Linux, où Python 3.5 ou une version ultérieure est installé. L’API est compatible avec plusieurs versions de Windows, de Windows XP à Windows 11, ainsi qu’avec les principales distributions Linux telles qu’Ubuntu, OpenSUSE et CentOS. Pour les systèmes Linux, les exigences spécifiques incluent les bibliothèques d’exécution GCC‑6, les dépendances du .NET Core Runtime (sans nécessiter le runtime lui‑même), et la version pymalloc de Python pour les versions 3.5‑3.7. De plus, une bibliothèque partagée libpython est nécessaire, ce qui peut nécessiter des ajustements de configuration pour la reconnaissance correcte du chemin de la bibliothèque.
---

## Vue d’ensemble

Aspose.PDF for Python via .NET, API de traitement PDF qui permet aux développeurs de travailler avec des documents PDF sans avoir besoin de Microsoft Office® ou d'automatisation Adobe Acrobat. Aspose.PDF for Python peut être utilisé pour développer des applications Python 32 bits et 64 bits pour différents systèmes d'exploitation (tels que Windows et Linux) où Python 3.5 ou version ultérieure est installé.

## Système d'exploitation pris en charge

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Serveur
- Windows 2016 Serveur
- Windows 2019 Serveur
- Windows XP
- Windows Vista
- Windows 7
- Windows 8, 8.1
- Windows 10
- Windows 11

### Linux

- Ubuntu
- OpenSUSE
- CentOS
- et d'autres

## Exigences système pour Linux cible

- Bibliothèques d'exécution GCC-6 (ou ultérieures).

- Dépendances du runtime .NET Core. L'installation du runtime .NET Core lui‑même n'est PAS requise.

- Pour Python 3.5-3.7 : la version pymalloc de Python est nécessaire. L'option de compilation --with-pymalloc de Python est activée par défaut. En général, la version pymalloc de Python est indiquée par le suffixe m dans le nom de fichier.

- Bibliothèque partagée libpython pour Python. L'option de construction --enable-shared de Python est désactivée par défaut, certaines distributions Python ne contiennent pas la bibliothèque partagée libpython. Sur certaines plateformes Linux, la bibliothèque partagée libpython peut être installée à l'aide du gestionnaire de paquets, par exemple : sudo apt-get install libpython3.7. Le problème habituel est que la bibliothèque libpython est installée dans un emplacement différent de l'emplacement standard du système pour les bibliothèques partagées. Le problème peut être résolu en utilisant les options de construction de Python pour définir des chemins de bibliothèque alternatifs lors de la compilation de Python, ou en créant un lien symbolique vers le fichier de bibliothèque libpython dans l'emplacement standard du système pour les bibliothèques partagées. Typiquement, le nom du fichier de la bibliothèque partagée libpython est libpythonX.Ym.so.1.0 pour Python 3.5-3.7, ou libpythonX.Y.so.1.0 pour Python 3.8 ou ultérieur (par exemple : libpython3.7m.so.1.0, libpython3.9.so.1.0).


