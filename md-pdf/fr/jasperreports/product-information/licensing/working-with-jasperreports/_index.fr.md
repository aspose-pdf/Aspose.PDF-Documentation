---

title: Travailler avec JasperReports

type: docs

weight: 10

url: /jasperreports/working-with-jasperreports/

lastmod: "2021-06-05"

---



{{% alert color="primary" %}}



Aspose.Words pour JasperReports est disponible gratuitement, pour une évaluation illimitée dans le temps depuis la page de téléchargement. Les versions d'évaluation et sous licence du produit sont le même téléchargement.



Lorsque vous êtes satisfait de la version d'évaluation, [achetez une licence](http://www.aspose.com/purchase/default.aspx). Assurez-vous de comprendre et d'accepter les termes de la licence.



{{% /alert %}}



La licence est disponible en téléchargement depuis la page de commande après le paiement de la commande. La licence est un fichier XML signé numériquement et en texte clair. La licence contient des informations telles que le nom du client, le produit acheté et le type de licence. Ne modifiez pas le contenu du fichier de licence : cela invalide la licence.



Il existe plusieurs façons d'activer une licence :



- [Appelez setLicense](/pdf/jasperreports/working-with-jasperreports/#call-setlicense).


- [Définir un paramètre d'exportation dans le code](/pdf/jasperreports/working-with-jasperreports/#set-the-licensefile-exporter-parameter-in-the-code).

- [Définir un paramètre d'exportateur dans **applicationContext.xml**](/pdf/jasperreports/working-with-jasperserver/).

Les deux premiers sont utilisés avec JasperReports, le dernier avec JasperServer.

#### **Appeler setLicense**

<ins> **Cette méthode est utilisée avec JasperReports.**

1. Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier approprié (par exemple, le dossier de votre application ou JasperReports\lib).

2. Ajoutez le code suivant à votre projet :

```
import com.aspose.pdf.jr3_7_0.jasperreports.*;

try

{ 

    // créer un objet stream contenant le fichier de licence

   FileInputStream fstream = new FileInputStream("C:\\Aspose.PDF.JasperReports.lic");  



    // Définir la licence via l'objet stream

 

   License license = new License();

   license.setLicense(fstream);

}

catch(Exception ex)

{

   System.out.println(ex.toString());

}

```

#### **Définir le paramètre Exporter licenseFile dans le Code**

<ins> **Cette méthode est utilisée avec JasperReports.** Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier approprié (par exemple, le dossier de votre application ou JasperReports\lib).

2. Ajoutez le code suivant à votre projet :



```



import com.aspose.pdf.jr3_7_0.jasperreports.*;



com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter exporter = new com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExporter();

exporter.setParameter(PdfExporterParameter.LICENSE, "Aspose.PDF.JasperReports.lic");

exporter.exportReport();



```