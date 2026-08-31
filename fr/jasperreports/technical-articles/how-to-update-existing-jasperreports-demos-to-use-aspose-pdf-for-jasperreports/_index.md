---
title: Comment - Mettre à jour les démos JasperReports existantes pour utiliser Aspose.PDF for JasperReports
linktitle: Comment - Mettre à jour les démos JasperReports existantes pour utiliser Aspose.PDF for JasperReports
type: docs
weight: 20
url: /fr/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
description: Découvrez comment mettre à jour les démos JasperReports existantes pour tirer parti des fonctionnalités d'Aspose.PDF for JasperReports.
lastmod: "2026-08-31"
---

{{% alert color="primary" %}}

Aspose.PDF for JasperReports comprend un certain nombre de projets de démonstration pour vous aider à commencer à exporter des rapports au format PDF. Ces démos sont basées sur des démos JasperReports standard qui ont été modifiées pour montrer comment utiliser de nouveaux exportateurs. Ce didacticiel passe en revue les étapes nécessaires pour mettre à jour les démos JasperReports existantes afin d'utiliser Aspose.PDF for JasperReports.

{{% /alert %}}

## Mise à jour des démos pour utiliser Aspose.PDF

{{% alert color="primary" %}}

Les étapes suivantes expliquent comment mettre à jour les démos existantes pour utiliser l'extension d'exportation Aspose.PDF for JasperReports plutôt que d'utiliser la fonctionnalité d'exportation PDF standard de JasperReport.

1. Téléchargez JasperReports depuis <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Assurez-vous de télécharger l'intégralité du projet archivé avec le code source et les démos, pas seulement un seul JAR. Ce didacticiel a été préparé à l'aide de JasperReports-3.5.2.
2. Décompressez le projet archivé à un emplacement de votre disque dur, par exemple C:\.
3. Copiez **aspose.pdf.jasperreports.jar** du dossier \lib dans **Aspose.PDF.JasperReports.zip** vers ```<InstallDir>```\jasperreports\lib.
4. Ouvrez ```<InstallDir>```\jasperreports\demo\samples, (where ```<InstallDir>``` est l'emplacement dans lequel vous avez décompressé JasperReports) pour mettre à jour une démo existante. Si vous avez sélectionné la démo de polices, par exemple, à utiliser avec Aspose.PDF for JasperReports, créez-en une copie afin que la démo originale reste la même. Pour les besoins de cet exemple, nous avons nommé le nouveau dossier **fonts.ap**.
Remarque : les démos seront exécutées à partir de ```<InstallDir>``` \jasperreports\demo\samples car les scripts de construction de démonstration s'appuient sur la structure de dossiers de JasperReports. Si vous modifiez le dossier d'exemples, vous devez modifier les scripts de build.
5. Ouvrez le fichier **FontsApp.java** à partir du dossier src et ajoutez une référence à Aspose.PDF for JasperReports :
   importer com.aspose.pdf.jr3_7_0.jasperreports.* ;
   (Nous utilisons jr3_7_0 car ce tutoriel a été préparé avec JasperReports 3.5.2.)
6. Add a new string:
   chaîne finale statique privée TASK_ASPOSE_PDF = "aspose_pdf"; avec les variables existantes comme option d'exportation via Aspose.PDF for JasperReports.
7. Localisez le segment de code for else if (TASK_PDF.equals(taskName)) et copiez l'intégralité du segment.
8. Collez l'extrait de code sous le même segment.

```java
 else if (TASK_PDF.equals(taskName))
{
  File sourceFile = new File(fileName);
  JasperPrint jasperPrint = (JasperPrint)JRLoader.loadObject(sourceFile);
  File destFile = new File(sourceFile.getParent(), jasperPrint.getName() + ".pdf");
  JRPdfExporter exporter = new JRPdfExporter();
  HashMap fontMap = new HashMap();
  FontKey key = new FontKey("DejaVu Serif", true, false);
  PdfFont font = new PdfFont("DejaVuSerif-Bold.ttf", "Cp1252", true);
  fontMap.put(key, font);
  exporter.setParameter(JRExporterParameter.JASPER_PRINT, jasperPrint);
  exporter.setParameter(JRExporterParameter.OUTPUT_FILE_NAME, destFile.toString());
  exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
  exporter.exportReport();
  System.err.println("PDF creation time : " + (System.currentTimeMillis() - start));
}
```

```text
update
else if (TASK_PDF.equals(taskName))
as
else if (TASK_ASPOSE_PDF.equals(taskName))
replace
JRPdfExporter exporter = new JRPdfExporter();
with
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new
com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
```

9. Ouvrez le fichier **build.xml**.
10. Faites une copie du segment suivant et placez-la dans le même fichier :

```xml
 <target name="pdf" description="Generat PDF via Aspose.PDF for JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```diff
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Pour exécuter la démo :
   -  Téléchargez l'outil ANT depuis <http://ant.apache.org/bindownload.cgi>.
   - Décompressez l'outil ANT et configurez les variables d'environnement comme décrit dans le manuel de l'outil.
   -  Remplacez le répertoire actuel par <InstallDir>\demo\hsqldb et exécutez la ligne de commande suivante :
      fourmi runServer
12. Ouvrez une nouvelle instance d'invite de commande et modifiez le répertoire actuel en <InstallDir>\demo\samples\fonts.ap et exécutez les commandes suivantes dans la ligne de commande :
13. ant javac – pour compiler les fichiers sources Java de l'application de test
14. ant compile – pour compiler la conception du rapport XML et produire le fichier .jasper
15. ant fill – pour remplir la conception du rapport compilé avec des données et produire le fichier .jrprint
16. ant aspose_pdf – pour produire un fichier PDF en utilisant Aspose.PDF for JasperReports.
17. Ouvrez le PDF obtenu (**FontsReport.pdf**) à partir du dossier <InstallDir>\demo\samples\ fonts.ap\build\reports\.

{{% /alert %}}

