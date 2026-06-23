---
title: Installer avec l'outil de configuration
linktitle: Installer avec l'outil de configuration
type: docs
weight: 30
url: /fr/reportingservices/install-with-configuring-tool/
description: Guide étape par étape pour installer Aspose.PDF pour Reporting Services à l'aide de l'outil de configuration pour une intégration transparente.
lastmod: "2026-06-19"
---

L'outil de configuration Aspose.Pdf for Reporting Services peut vous aider à configurer l'extension Aspose.Pdf for Reporting Services pour n'importe quelle version prise en charge de Report Server (RS). Actuellement, il prend en charge RS2016, RS2017, RS2019, RS2022 et Power BI Report Server. L'outil de configuration nécessite le .NET Framework 4.8.

Si vous souhaitez installer l'extension et l'enregistrer auprès du Report Server, sélectionnez le type d'action « Register ». Pour désenregistrer et désinstaller l'extension, sélectionnez le type d'action « Unregister ».

![todo:image_alt_text](install-with-configuring-tool_1.png)

**Les étapes suivantes décrivent comment l'utiliser en détail :**

1. Saisissez ou parcourez le chemin du fichier DLL pour l'extension Aspose.Pdf for Reporting Services ;
1. Sélectionnez le type d'action correspondant : Register ou Unregister ;
1. Sélectionnez l'onglet correspondant à la version du Report Server que vous souhaitez configurer. Veuillez vous assurer d'avoir sélectionné le fichier DLL destiné à votre version de RS. Si la version demandée du produit n'est pas installée sur la machine, l'outil de configuration vous en informera avec des conseils. Si vous configurez l'extension pour l'instance nommée RS2016 (et non celle par défaut 'MSSQLSERVER'), veuillez saisir le nom d'instance personnalisé, puis appuyer sur le bouton 'Refresh'.
1. Assurez-vous que les chemins et les noms des fichiers de configuration affichés dans les zones de texte du bas sont corrects. S'ils ne le sont pas, vous pouvez appuyer sur le bouton 'Refresh' pour tenter de retrouver à nouveau l'instance RS, ou les rechercher manuellement.
1. Appuyez sur le bouton 'Config'. L'outil va maintenant essayer d'effectuer la configuration demandée et vous indiquera si la configuration a réussi ou non.
 

