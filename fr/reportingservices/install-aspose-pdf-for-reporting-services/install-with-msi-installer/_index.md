---
title: Installer avec l'installateur MSI
type: docs
weight: 10
url: fr/reportingservices/install-with-msi-installer/
lastmod: "2021-06-05"
---

Vous pouvez installer Aspose.Pdf pour Reporting Services en utilisant un installateur MSI. Exécutez Aspose.Pdf.ReportingServices.msi et suivez les étapes proposées par l'installateur. L'installateur copiera l'assembly et d'autres fichiers dans le répertoire spécifié et installera le produit sur l'instance par défaut des Reporting Services. Vous n'avez pas besoin de copier ou modifier des fichiers manuellement à moins que vous ne souhaitiez ajouter des paramètres de configuration spéciaux comme décrit dans la section 'Configurer Aspose.Pdf pour Reporting Services'.

L'installation automatique est la meilleure option qui fonctionne dans la plupart des cas. Cependant, vous pourriez avoir besoin d'installer le produit manuellement dans certaines situations comme :

- L'installation automatique échoue en raison de problèmes de sécurité I/O.
- Vous devez installer le produit sur une instance nommée (non par défaut) de Reporting Services 2016 ou sur plusieurs instances.

- Vous mettez à niveau vers la dernière version et souhaitez simplement remplacer l'assembly au lieu de désinstaller l'ancienne version et d'installer la nouvelle en utilisant l'installateur MSI.
{{% alert color="primary" %}}

Note : Prenez note que dans ce dernier cas, vous pourriez vous retrouver avec d'autres composants (tels que la documentation hors ligne) qui ne sont pas mis à niveau vers la version correspondante.

{{% /alert %}}