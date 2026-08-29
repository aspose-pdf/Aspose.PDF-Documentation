---
title: Travailler avec JasperReports
linktitle: Travailler avec JasperReports
type: docs
weight: 10
url: /fr/jasperreports/working-with-jasperreports/
description: Maîtrisez l'utilisation de JasperReports à l'aide d'Aspose.PDF. Créez et exportez des rapports détaillés au format PDF avec des fonctionnalités avancées.
lastmod: "2021-06-05"
---

{{% alert color="primary" %}}

Aspose.Words pour JasperReports est disponible pour une évaluation gratuite et illimitée dans le temps à partir de la page de téléchargement. Les versions d'évaluation et sous licence du produit sont le même téléchargement.

Lorsque vous êtes satisfait de la version d'évaluation, [acheter une licence](https://purchase.aspose.com/buy?ppId=98899). Assurez-vous de comprendre et d'accepter les termes de la licence.

{{% /alert %}}

La licence est disponible en téléchargement depuis la page de commande après le paiement de la commande. La licence est un fichier XML en texte clair, signé numériquement. La licence contient des informations telles que le nom du client, le produit acheté et le type de licence. Ne modifiez pas le contenu du fichier de licence : cela invalide la licence.

Il existe plusieurs manières d'activer une licence :

- [Appeler setLicense](/pdf/fr/jasperreports/working-with-jasperreports/#call-setlicense).
- [Définir un paramètre d'exportateur dans le code](/pdf/fr/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).
- [Définir un paramètre d'exportateur dans **applicationContext.xml**](/pdf/fr/jasperreports/working-with-jasperserver/).

Les deux premiers sont utilisés avec JasperReports, le dernier avec JasperServer.

## Appeler setLicense

Cette méthode est utilisée avec JasperReports.

1. Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier approprié (par exemple le dossier de votre application ou JasperReports\lib).
2. Ajoutez le code suivant à votre projet :

```java
import com.aspose.pdf.jr3_7_0.jasperreports.*;
try
{ 
    // create a stream object containing the license file
   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  

    // Set the license through the stream object
 
   License license = new License();
   license.setLicense(fstream);
}
catch(Exception ex)
{
   System.out.println(ex.toString());
}

```

## Définissez le paramètre LicenseFile Exporter dans le code

Cette méthode est utilisée avec JasperReports.

1. Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier approprié (par exemple le dossier de votre application ou JasperReports\lib).
2. Ajoutez le code suivant à votre projet :

```java

import com.aspose.pdf.jr3_7_0.jasperreports.*;

com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();
exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");
exporter.exportReport();

```


