```
   <property name="contentType" value="application/pdf"/>

</bean>
```

{{% alert color="primary" %}}

2. Redémarrez JasperServer pour que les modifications prennent effet.

{{% /alert %}}

3. Après avoir redémarré, ouvrez JasperServer dans un navigateur Web.

4. Accédez à un rapport que vous souhaitez exporter au format PDF.

5. Cliquez sur le bouton d'exportation et sélectionnez "Pdf - PDF via Aspose.PDF for JasperReports".

{{% alert color="primary" %}}

La configuration est maintenant terminée et JasperServer est prêt à exporter des rapports au format PDF en utilisant Aspose.PDF pour JasperReports.

{{% /alert %}}


<property name="iconSrc" value="/images/pdf.gif"/>

<property name="parameterDialogName" value="dlg"/>

<property name="exportParameters" ref="AsposeExportParameters"/>

<property name="currentExporter" ref="AsposePdfExporter"/>

</bean>
```

{{% alert color="primary" %}}

2. Localisez l'élément <util:map id=”exporterConfigMap> dans le fichier **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\flows\viewReportBeans.xml** et ajoutez les lignes suivantes :

{{% /alert %}}


<util:map id="exporterConfigMap">

<entry key="pdf" value-ref="pdfExporterConfiguration"/>

<entry key="xls" value-ref="xlsExporterConfiguration"/>

<entry key="rtf" value-ref="rtfExporterConfiguration"/>

<entry key="csv" value-ref="csvExporterConfiguration"/>

<entry key="swf" value-ref="swfExporterConfiguration"/>

<!-- DÉBUT des LIGNES AJOUTÉES -->

<entry key="Aspose_pdf" value-ref="AsposePdfExporterConfiguration"/>

<!-- FIN des NOUVELLES LIGNES -->

</util:map>
```

{{% alert color="primary" %}}

3. Copiez toutes les images GIF du dossier \lib de **Aspose-pdf-jasperreports.zip** vers <InstallDir>\apache-tomcat\webapps\jasperserver\images\.

4. Copiez **Aspose-pdf-jasperreports.jar** du dossier \lib dans **Aspose.PDF.JasperReports.zip** vers <InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\lib\.

5. Ajoutez les lignes suivantes au fichier **<InstallDir>\apache-tomcat\webapps\jasperserver\WEB-INF\applicationContext.xml**.



   Ce bean peut contenir divers paramètres de configuration destinés à configurer l'exportation. Par exemple, vous pouvez utiliser la fonction de mappage de polices de JasperReports ou spécifier l'emplacement du fichier de licence Aspose.Cells pour JasperReports.

  

{{% /alert %}}



```

<bean id="AsposeExportParameters" class="com.aspose.pdf.jr3_7_0.jasperreports.JrPdfExportParametersBean">

<property name="localizedFontMap" ref="localePdfFontMap"/>



<!-- Décommentez pour appliquer une licence. Vérifiez le chemin de la licence.

<property name="licenseFile" value="C:/jasperserver-3.0/apache-tomcat/webapps/


jasperserver/WEB-INF/Aspose.PDF.JasperReports.lic"/>

```

{{% alert color="primary" %}}



6. Exécutez JasperServer et ouvrez n'importe quel rapport pour le visualiser. Si les étapes précédentes ont été effectuées correctement, vous verrez une icône pour l'exportation via Aspose.PDF pour JasperReports dans la liste des formats disponibles.



   **Aspose.PDF pour JasperReports est intégré**



![todo:image_alt_text](integration-with-jasperserver_1.png)



{{% /alert %}}

```