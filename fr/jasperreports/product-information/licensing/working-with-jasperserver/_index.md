---

title: Travailler avec JasperServer

type: docs

weight: 20

url: /fr/jasperreports/working-with-jasperserver/

lastmod: "2021-06-05"

---



#### <ins>**Définir le paramètre licenseFile Exporter dans applicationContext.xml**

{{% alert color="primary" %}}



Cette méthode est utilisée avec JasperServer.



{{% /alert %}}



1. Téléchargez la licence sur votre ordinateur et copiez-la dans le dossier ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF```, où ```<InstallDir>``` représente le répertoire d'installation de JasperServer.

2. Localisez le fichier ```<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml``` et ajoutez les lignes suivantes :



```

 <bean id="AsposeExportParameters" class="comcom.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

    <property name="licenseFile" value="C:/jasperserver-pro-3.7.1/apache-tomcat/webapps/jasperserver-pro/WEB-  

    INF/Aspose.Total.JasperReports.lic"/>

</bean>

```

{{% alert color="primary" %}}


Remarque : Veuillez noter que le chemin d'installation ne doit pas contenir d'espaces, par exemple C:/Program Files/JasperServer… car cela cause des problèmes lors de l'accès au fichier de licence.

{{% /alert %}}



#### **Vérifiez que la licence fonctionne**

Exportez n'importe quel rapport au format PDF et vérifiez si le rapport contient un message d'évaluation. S'il n'y a pas de message d'évaluation, alors la licence fonctionne correctement.



**Aspose.PDF pour JasperReports injecte un filigrane lorsqu'il fonctionne en mode évaluation**



![todo:image_alt_text](working-with-jasperserver_1.png)







**Aspose.PDF pour JasperReports injecte un filigrane lorsqu'il fonctionne en mode évaluation**



![todo:image_alt_text](working-with-jasperserver_2.png)