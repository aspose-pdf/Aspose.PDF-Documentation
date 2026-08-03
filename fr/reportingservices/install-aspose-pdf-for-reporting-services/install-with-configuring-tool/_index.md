---
title: Installer avec l'outil de configuration
linktitle: Installer avec l'outil de configuration
type: docs
weight: 30
url: /reportingservices/install-with-configuring-tool/
description: Guide étape par étape pour installer Aspose.PDF pour Reporting Services à l’aide de l’outil de configuration pour une intégration transparente.
lastmod: "2021-06-05"
---

L'outil de configuration Aspose.PDF for Reporting Services peut vous aider à configurer l'extension Aspose.PDF for Reporting Services pour l'une des versions de Report Server (RS) prises en charge. Actuellement, il prend en charge RS2016, RS2017, RS2019, RS2022 et Power BI Report Server. L'outil de configuration nécessite .NET Framework 4.8.

Si vous souhaitez installer l'extension et l'enregistrer auprès du Report Server, sélectionnez le type d'action `Register`. Pour désenregistrer et désinstaller l'extension, sélectionnez le type d'action `Unregister`.

![Install with configuring tool](install-with-configuring-tool_1.png)

**Les étapes suivantes décrivent comment l'utiliser en détail :**

1. Saisissez ou parcourez le chemin du fichier DLL pour l’extension Aspose.PDF pour Reporting Services ;
1. Sélectionnez le type d'action correspondant : S'inscrire ou Se désinscrire ;
1. Sélectionnez l'onglet correspondant à la version du Report Server que vous souhaitez configurer. Veuillez vous assurer que vous avez sélectionné le fichier DLL destiné à votre version RS. Si la version demandée du produit n'est pas installée sur la machine, l'outil de configuration vous en informera avec des astuces. Si vous configurez l'extension pour l'instance RS2016 nommée (et non celle par défaut « MSSQLSERVER »), veuillez saisir le nom de l'instance personnalisée, puis appuyez sur le bouton « Actualiser ».
1. Assurez-vous que les chemins et les noms des fichiers de configuration affichés dans les zones de texte du bas sont corrects. Si ce n'est pas le cas, vous pouvez appuyer sur le bouton « Actualiser » pour essayer de retrouver l'instance RS, ou vous pouvez la rechercher manuellement.
1. Appuyez sur le bouton « Config ». L'outil va maintenant tenter d'effectuer la configuration demandée et vous informera si la configuration réussit ou non.
