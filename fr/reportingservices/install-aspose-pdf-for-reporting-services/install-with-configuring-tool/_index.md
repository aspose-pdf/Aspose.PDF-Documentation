---
title: Installer avec l'outil de configuration
type: docs
weight: 30
url: fr/reportingservices/install-with-configuring-tool/
lastmod: "2021-06-05"
---

L'outil de configuration Aspose.Pdf pour Reporting Services peut vous aider à configurer l'extension Aspose.Pdf pour Reporting Services pour n'importe quelle version du serveur de rapports (RS) prise en charge. Actuellement, il prend en charge RS2016, RS2017, RS2019, RS2022 et Power BI Report Server. L'outil de configuration nécessite .NET Framework 4.8.

Si vous souhaitez installer l'extension et l'enregistrer avec le serveur de rapports, sélectionnez le type d'action 'Register'. Pour désenregistrer et désinstaller l'extension, sélectionnez le type d'action 'Unregister'.

![todo:image_alt_text](install-with-configuring-tool_1.png)

**Les étapes suivantes décrivent comment l'utiliser en détail :**

1. Saisissez ou parcourez le chemin du fichier DLL pour l'extension Aspose.Pdf pour Reporting Services ;
1. Sélectionnez le type d'action correspondant : Register ou Unregister ;
1. Sélectionnez l'onglet correspondant à la version du Report Server que vous souhaitez configurer. Veuillez vous assurer que vous avez sélectionné le fichier DLL destiné à votre version RS. Si la version demandée du produit n'est pas installée sur la machine, l'outil de configuration vous informera avec des conseils. Si vous configurez l'extension pour l'instance nommée RS2016 (pas celle par défaut 'MSSQLSERVER'), veuillez entrer le nom de l'instance personnalisée, puis appuyez sur le bouton 'Actualiser'.
1. Assurez-vous que les chemins et les noms des fichiers de configuration affichés dans les zones de texte inférieures sont corrects. S'ils ne le sont pas, vous pouvez appuyer sur le bouton 'Actualiser' pour essayer de retrouver l'instance RS, ou vous pouvez les rechercher manuellement.
1. Appuyez sur le bouton 'Config'. L'outil va maintenant tenter de faire la configuration demandée et vous informera si la configuration a réussi ou non.