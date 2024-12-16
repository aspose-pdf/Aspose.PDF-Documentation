---
title: Comment - Mettre à jour les démos JasperReports existantes pour utiliser Aspose.Pdf pour JasperReports
type: docs
weight: 20
url: /fr/jasperreports/how-to-update-existing-jasperreports-demos-to-use-aspose-pdf-for-jasperreports/
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.PDF pour JasperReports comprend un certain nombre de projets de démonstration pour vous aider à commencer à exporter des rapports au format PDF. Ces démos sont basées sur les démos standard de JasperReports qui ont été modifiées pour démontrer comment utiliser les nouveaux exportateurs. Ce tutoriel passe en revue les étapes nécessaires pour mettre à jour les démos JasperReports existantes afin d'utiliser Aspose.PDF pour JasperReports.

{{% /alert %}}
### **Mise à jour des démos pour utiliser Aspose.PDF**

{{% alert color="primary" %}}

Les étapes suivantes expliquent comment mettre à jour les démos existantes pour utiliser l'extension d'exportation Aspose.PDF pour JasperReports plutôt que d'utiliser la fonctionnalité d'exportation PDF standard de JasperReport.

1. Téléchargez JasperReports depuis <http://sourceforge.net/project/showfiles.php?group_id=36382&package_id=28579>.
   Assurez-vous de télécharger l'ensemble du projet archivé avec le code source et les démos, et non pas seulement un seul JAR. Ce didacticiel a été préparé en utilisant JasperReports-3.5.2.  
2. Décompressez le projet archivé à un emplacement sur votre disque dur, par exemple C:\.  
3. Copiez **aspose.pdf.jasperreports.jar** du dossier \lib dans **Aspose.PDF.JasperReports.zip** vers ```<InstallDir>```\jasperreports\lib.  
4. Ouvrez ```<InstallDir>```\jasperreports\demo\samples, (où ```<InstallDir>``` est l'emplacement où vous avez décompressé JasperReports) pour mettre à jour une démo existante. Si vous avez sélectionné la démo des polices, par exemple, pour l'utiliser avec Aspose.PDF pour JasperReports, créez-en une copie afin que la démo originale reste la même. Aux fins de cet exemple, nous avons nommé le nouveau dossier **fonts.ap**.  
Note: les démos fonctionneront à partir de ```<InstallDir>``` \jasperreports\demo\samples car les scripts de construction de la démo dépendent de la structure des dossiers de JasperReports. Si vous changez le dossier d'exemple, vous devez modifier les scripts de construction.  
5. Ouvrez le fichier **FontsApp.java** du dossier src et ajoutez une référence à Aspose.PDF pour JasperReports:  

   import com.aspose.pdf.jr3_7_0.jasperreports.*;  ```
(Nous utilisons jr3_7_0 car ce tutoriel a été préparé avec JasperReports 3.5.2.)
6. Ajouter une nouvelle chaîne :
   private static final String TASK_ASPOSE_PDF = "aspose_pdf"; avec les variables existantes comme une option d'exportation via Aspose.PDF pour JasperReports.
7. Localisez le segment de code else if (TASK_PDF.equals(taskName)) et copiez tout le segment.
8. Collez le snippet de code sous le même segment.

```
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
```
```java
exporter.setParameter(JRExporterParameter.FONT_MAP, fontMap);
exporter.exportReport();
System.err.println("Temps de création du PDF : " + (System.currentTimeMillis() - start));
}
```

```
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
10. Faites une copie du segment suivant et placez-le à l'intérieur du même fichier :

```
<target name="pdf" description="Générer un PDF via Aspose.PDF pour JasperReports.">
    <java classname="${class.name}">
        <arg value="pdf"/>
        <arg value="${file.name}.jrprint"/>
        <classpath refid="classpath"/>
    </java>
</target>
```

```
update  name="pdf"  as   name="aspose_pdf"
update  <arg value="pdf"/>  as   <arg value="aspose_pdf"/>
```

11. Pour exécuter la démo :

   - Téléchargez l'outil ANT depuis <http://ant.apache.org/bindownload.cgi>.
- Décompressez l'outil ANT et configurez les variables d'environnement comme décrit dans le manuel de l'outil.
- Changez le répertoire courant en <InstallDir>\demo\hsqldb et exécutez la ligne de commande suivante :
  ant runServer
12. Ouvrez une nouvelle instance de l'invite de commande et changez le répertoire courant en <InstallDir>\demo\samples\fonts.ap et exécutez les commandes suivantes dans la ligne de commande :
13. ant javac – pour compiler les fichiers source Java de l'application de test
14. ant compile – pour compiler le design de rapport XML et produire le fichier .jasper
15. ant fill – pour remplir le design de rapport compilé avec des données et produire le fichier .jrprint
16. ant aspose_pdf – pour produire un fichier PDF en utilisant Aspose.PDF pour JasperReports.
17. Ouvrez le PDF résultant (**FontsReport.pdf**) depuis le dossier <InstallDir>\demo\samples\fonts.ap\build\reports\.

{{% /alert %}}