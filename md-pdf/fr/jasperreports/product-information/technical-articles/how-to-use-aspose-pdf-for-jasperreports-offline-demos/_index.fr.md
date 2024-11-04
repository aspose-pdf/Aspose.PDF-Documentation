---
title: Comment - utiliser Aspose.Pdf pour les démos hors ligne de JasperReports
type: docs
weight: 10
url: /jasperreports/how-to-use-aspose-pdf-for-jasperreports-offline-demos/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF pour JasperReports inclut un certain nombre de projets de démonstration pour vous aider à commencer à exporter des rapports aux formats PDF depuis votre application. Les démos sont des démos standard de JasperReports qui ont été modifiées pour démontrer comment utiliser les nouveaux exportateurs.

{{% /alert %}}
### **Exécution des Démos Aspose.PDF pour JasperReports**
Pour exécuter les démos Aspose.PDF pour JasperReports :

{{% alert color="primary" %}}

1. Téléchargez JasperReports depuis <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>. Assurez-vous de télécharger l'ensemble du projet archivé avec le code source et les démos, pas seulement un seul JAR.
2. Décompressez le projet archivé à un endroit de votre disque dur, par exemple C:\.
3. Copy all demo folders from the \demo folder in **Aspose.PDF.JasperReports.zip** to ```<InstallDir>```\jasperreports\demo\samples, où ```<InstallDir>``` est l'emplacement où vous avez décompressé JasperReports. Cette étape est nécessaire car les scripts de construction de démonstration dépendent de la structure de dossiers de JasperReports, sinon vous devez modifier les scripts de construction.  
4. Copiez le fichier **aspose.pdf.jasperreports.jar** depuis le dossier \lib dans **Aspose.PDF.JasperReports.zip** vers ```<InstallDir>```\jasperreports\lib.  
5. Téléchargez l'outil ANT depuis <http://ant.apache.org/bindownload.cgi>.  
6. Décompressez l'outil ANT et configurez les variables d'environnement comme décrit dans le manuel de l'outil.  
7. Changez le répertoire courant vers ```<InstallDir>```\demo\hsqldb et exécutez la ligne de commande suivante :  
   ant runServer  
8. Ouvrez une nouvelle instance d'invite de commande et changez le répertoire courant vers l'un des démos Aspose.PDF pour JasperReports, par exemple ```<InstallDir>```\demo\samples\charts.ap.  
9. Exécutez les commandes suivantes sur la ligne de commande :  
10. ant javac – pour compiler les fichiers source Java de l'application de test.
11. ant compile – pour compiler le design du rapport XML et produire le fichier .jasper
12. ant fill – pour remplir le design de rapport compilé avec des données et produire le fichier .jrprint
13. Exécutez la commande suivante dans la ligne de commande :
   ant pdf – pour produire un fichier PDF à partir du rapport de démonstration.
14. Ouvrez l'un des documents résultants pour visualiser, par exemple ```<InstallDir>```\demo\samples\charts.ap\AreaChartReport.pdf dans Adobe Reader ou une autre application.
{{% /alert %}}
