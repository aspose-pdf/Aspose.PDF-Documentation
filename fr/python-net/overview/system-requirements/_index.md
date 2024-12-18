---
title: Exigences du système
linktitle: Exigences du système
type: docs
weight: 30
url: /fr/python-net/system-requirements/
description: Cette section liste les systèmes d'exploitation pris en charge dont un développeur a besoin pour travailler avec succès avec Aspose.PDF pour Python.
lastmod: "2022-12-22"
sitemap:
    changefreq: "weekly"
    priority: 0.7
---

## Aperçu

Aspose.PDF pour Python via .NET, une API de traitement PDF qui permet aux développeurs de travailler avec des documents PDF sans avoir besoin de Microsoft Office® ou d'Adobe Acrobat Automation. Aspose.PDF pour Python peut être utilisé pour développer des applications Python 32 bits et 64 bits pour différents systèmes d'exploitation (tels que Windows et Linux) où Python 3.5 ou ultérieur est installé.

## Système d'exploitation pris en charge

### Windows

- Windows 2003 Server
- Windows 2008 Server
- Windows 2012 Server
- Windows 2012 R2 Server
- Windows 2016 Server
- Windows 2019 Server
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


## Exigences système pour le Linux cible

- Bibliothèques d'exécution GCC-6 (ou ultérieures).

- Dépendances de l'environnement d'exécution .NET Core. L'installation de l'environnement d'exécution .NET Core lui-même n'est PAS requise.

- Pour Python 3.5-3.7 : La version pymalloc de Python est nécessaire. L'option de construction --with-pymalloc de Python est activée par défaut. Typiquement, la version pymalloc de Python est marquée avec le suffixe m dans le nom de fichier.

- Bibliothèque partagée libpython de Python.
 L'option de construction --enable-shared de Python est désactivée par défaut, certaines distributions de Python ne contiennent pas la bibliothèque partagée libpython. Pour certaines plateformes Linux, la bibliothèque partagée libpython peut être installée à l'aide du gestionnaire de paquets, par exemple : sudo apt-get install libpython3.7. Le problème courant est que la bibliothèque libpython est installée à un emplacement différent de l'emplacement système standard pour les bibliothèques partagées. Le problème peut être résolu en utilisant les options de construction de Python pour définir des chemins de bibliothèque alternatifs lors de la compilation de Python, ou en créant un lien symbolique vers le fichier de la bibliothèque libpython dans l'emplacement système standard pour les bibliothèques partagées. Typiquement, le nom de fichier de la bibliothèque partagée libpython est libpythonX.Ym.so.1.0 pour Python 3.5-3.7, ou libpythonX.Y.so.1.0 pour Python 3.8 ou ultérieur (par exemple : libpython3.7m.so.1.0, libpython3.9.so.1.0).