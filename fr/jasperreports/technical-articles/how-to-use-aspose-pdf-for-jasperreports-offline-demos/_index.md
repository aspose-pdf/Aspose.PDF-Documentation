---
title: Comment - utiliser Aspose.PDF pour les démos hors ligne JasperReports
linktitle: Comment - utiliser Aspose.PDF pour les démos hors ligne JasperReports
type: docs
weight: 10
url: /fr/jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
description: Explorez les démos hors ligne d'Aspose.PDF for JasperReports. Apprenez les implémentations et les fonctionnalités pratiques de manière pratique.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports comprend un certain nombre de projets de démonstration pour vous aider à commencer à exporter des rapports au format PDF à partir de votre application. Les démos sont des démos JasperReports standard qui ont été modifiées pour montrer comment utiliser de nouveaux exportateurs.

{{% /alert %}}

## Exécution d'Aspose.PDF pour les démos JasperReports

Pour exécuter Aspose.PDF pour les démos JasperReports :

{{% alert color="primary" %}}

1. Téléchargez JasperReports depuis <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Assurez-vous de télécharger l'intégralité du projet archivé avec le code source et les démos, pas seulement un seul JAR.
2. Décompressez le projet archivé à un emplacement de votre disque dur, par exemple C:\.
3. Copiez tous les dossiers de démonstration du dossier \demo dans **Aspose.PDF.JasperReports.zip** vers ```<InstallDir>```\jasperreports\demo\samples, where ```<InstallDir>``` est l'emplacement dans lequel vous avez décompressé JasperReports. Cette étape est requise car les scripts de build de démonstration reposent sur la structure de dossiers JasperReports, sinon vous devez modifier les scripts de build.
4. Copiez le fichier **aspose.pdf.jasperreports.jar** du dossier \lib dans **Aspose.PDF.JasperReports.zip** vers ```<InstallDir>```\jasperreports\lib.
5. Téléchargez l'outil ANT depuis <http://ant.apache.org/bindownload.cgi>.
6. Décompressez l'outil ANT et configurez les variables d'environnement comme décrit dans le manuel de l'outil.
7. Remplacez le répertoire actuel par ```<InstallDir>```\demo\hsqldb et exécutez la ligne de commande suivante :
   ant runServer
8. Ouvrez une nouvelle instance d'invite de commande et remplacez le répertoire actuel par l'une des démos Aspose.PDF for JasperReports, par exemple ```<InstallDir>```\demo\samples\charts.ap.
9. Exécutez les commandes suivantes sur la ligne de commande :
10. ant javac – to compile the Java source files of the test application.
11. ant compile – to compile the XML report design and produce the .jasper file
12. ant fill – pour remplir la conception du rapport compilé avec des données et produire le fichier .jrprint
13. Exécutez la commande suivante sur la ligne de commande :
   ant pdf – pour produire un fichier PDF à partir du rapport de démonstration.
14. Ouvrez l'un des documents résultants pour afficher, par exemple ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf dans Adobe Reader ou une autre application.

{{% /alert %}}

